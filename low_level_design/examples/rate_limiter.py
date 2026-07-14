"""Rate limiter: a thread-safe token bucket behind a small interface.

The design choices worth noticing:

  - RateLimiter is an interface, so token bucket, leaky bucket, and sliding window are
    interchangeable and a caller depends only on allow().
  - The bucket refills lazily on each call from a clock, rather than a background thread topping it
    up. Fewer moving parts, and the clock is injected so a test can advance time deterministically
    instead of sleeping.
  - The lock guards the read-modify-write of the token count. Without it, two threads can both read
    the same count and both spend the last token. This is the concurrency point the round is
    looking for; see the concurrency track.

The exercise: swap in a leaky-bucket or sliding-window implementation without touching callers, or
make the buckets per-user with eviction of idle keys.
"""

from abc import ABC, abstractmethod
from threading import Lock
from typing import Callable


class RateLimiter(ABC):
    @abstractmethod
    def allow(self, key: str) -> bool:
        """Return True if the request for `key` is within the limit, else False."""
        ...


class _Bucket:
    def __init__(self, capacity: float, tokens: float, last_refill: float):
        self.capacity = capacity
        self.tokens = tokens
        self.last_refill = last_refill


class TokenBucketRateLimiter(RateLimiter):
    def __init__(
        self,
        capacity: float,
        refill_per_second: float,
        now: Callable[[], float],
    ):
        self.capacity = capacity
        self.refill_per_second = refill_per_second
        self.now = now  # injected clock, e.g. time.monotonic
        self._buckets: dict[str, _Bucket] = {}
        self._lock = Lock()

    def allow(self, key: str) -> bool:
        with self._lock:
            now = self.now()
            bucket = self._buckets.get(key)
            if bucket is None:
                bucket = _Bucket(self.capacity, self.capacity, now)
                self._buckets[key] = bucket

            # Lazy refill: add the tokens that would have accrued since last seen.
            elapsed = now - bucket.last_refill
            bucket.tokens = min(
                bucket.capacity, bucket.tokens + elapsed * self.refill_per_second
            )
            bucket.last_refill = now

            if bucket.tokens >= 1:
                bucket.tokens -= 1
                return True
            return False
