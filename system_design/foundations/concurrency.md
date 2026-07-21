# Concurrency and Multithreading

A smaller track than Low-Level Design or System Design, but worth deliberate coverage: it appears
both as a standalone topic and embedded inside system design deep dives, and it is commonly
underprepared relative to how often it comes up.

## Core Concepts

- **Race conditions.** What they are, a concrete example of one, and why they are hard to catch
  through testing alone.
- **Mutexes, semaphores, and monitors.** A mutex is mutual exclusion for one holder; a semaphore is
  a counter that admits up to N holders, for bounding access to a resource pool; a monitor bundles a
  lock with one or more condition variables so a thread can wait for a predicate and be signaled when
  it changes (Java's `synchronized` plus `wait`/`notify` is a monitor). Know which one each problem
  actually needs.
- **Deadlock, livelock, and starvation.** The four conditions required for deadlock (mutual
  exclusion, hold and wait, no preemption, circular wait), and at least one avoidance strategy such
  as consistent lock ordering. Livelock is threads actively responding to each other but making no
  progress; starvation is one thread perpetually denied a resource it needs. Be able to tell the
  three apart with an example of each.
- **Locks versus lock-free structures.** When a simple mutex is the right tool, and when
  contention makes a lock-free or compare-and-swap-based structure worth the added complexity.
- **Thread pools.** Why they exist, how they bound resource usage compared to spawning a thread
  per task, and the basic trade-off in choosing pool size.
- **Producer-consumer.** The pattern itself, and how a bounded queue between producer and
  consumer relates to backpressure, which also shows up in the system design track.

## The Memory Model, and Why Correct-Looking Code Is Still Wrong

The concepts above assume threads see each other's writes; on real hardware and compilers they do
not, unless you make them. This is the layer a standalone concurrency round probes once the basics
are solid, and it is where a lot of plausible code is quietly broken.

- **Happens-before.** A partial ordering that guarantees one thread's write is visible to another.
  It is established by synchronization actions: releasing a lock, a write to a volatile or atomic
  variable, or starting and joining a thread. Without a happens-before edge, there is no guarantee
  the reader ever sees the write, no matter how much wall-clock time passes.
- **Visibility versus atomicity.** `volatile` (Java) or `std::atomic` gives visibility and ordering,
  but a `count++` on a volatile is still three operations and still races. Visibility and atomicity
  are separate guarantees, and most bugs come from assuming one gives the other.
- **The thread-safe singleton.** A common error: double-checked locking is broken without a
  volatile instance field, because another thread can observe a partially constructed object through
  a reordered write. Being able to explain why is a fast signal that you understand the memory model,
  not just the syntax.
- **False sharing.** Two threads updating independent variables that happen to sit on the same cache
  line contend on the hardware cache anyway, so throughput collapses for no logical reason. The fix
  is padding to push them onto separate lines. Relevant for performance-sensitive and low-latency
  teams.

## Language-Specific Idioms

Prepare this section for whichever language you expect to interview in.

- **Java**: `synchronized`, the `java.util.concurrent` package, `ExecutorService`, and
  `CompletableFuture`.
- **Python**: the Global Interpreter Lock and what it does and does not protect you from,
  `threading` versus `multiprocessing`, and `asyncio` for I/O-bound concurrency.
- **Go**: goroutines and channels, and the idiom of communicating by sharing memory versus sharing
  memory by communicating.

## How Concurrency Shows Up Inside System Design Answers

This is where the standalone concepts above connect back to the System Design track, and is worth
being ready to raise unprompted during a deep dive.

- **Idempotency keys** to handle retried requests safely, which is really a concurrency-adjacent
  correctness problem at the API layer.
- **Optimistic versus pessimistic concurrency control** when multiple writers might update the same
  record, and the trade-off between retry-on-conflict and locking up front.
- **Distributed locks**, for example built on Redis or ZooKeeper, when coordination is needed across
  processes or machines rather than threads within one process.
- **Compare-and-swap** as the building block behind both lock-free data structures and optimistic
  concurrency control.

## Practice Problems

Concurrency shows up two ways, and you should practice for both. It appears embedded in system
design (the integration points above) and low-level design (a parking lot or rate limiter with
shared state), and it also appears as a *standalone* round at infrastructure- and systems-leaning
companies. The integration reasoning is covered by folding it into other tracks, but the standalone
round needs reps at actually implementing the primitives: so keep a short, concrete problem list:

- [ ] Print in Order: the simplest ordering-with-signaling problem
- [ ] Print FooBar Alternately: two threads coordinating turns
- [ ] Building H2O / Print Zero Even Odd: barrier and turn-based coordination
- [ ] Bounded blocking queue: the producer-consumer core, and the gateway to backpressure
- [ ] Thread-safe LRU cache with a time-to-live: connects the LeetCode LRU problem to real locking
- [ ] Token-bucket rate limiter, thread-safe: the concurrent version of the low-level design problem
- [ ] A read-write lock from scratch: classic, and forces you to reason about writer starvation
- [ ] Dining philosophers: the canonical deadlock demonstration, and lock-ordering as the fix
- [ ] Readers-writers: many readers or one writer, and the choice of which side you let starve
- [ ] Thread-safe singleton: double-checked locking done correctly, and why the volatile matters

For each, be ready to discuss where the lock boundaries are, whether a lock-free approach is
warranted, and how the design would behave under high contention.

## Practice Approach

Beyond the list above, fold this in naturally: when working through the System Design track's
replication and consensus material, pause and ask how the same correctness problem would be solved
at the thread level within a single process, and vice versa. The two tracks reinforce each other
more than either does alone. Concretely, start the standalone problems above in the second half of
Phase 2, alongside the System Design replication and distributed-locks topics, so the thread-level
and cross-process versions of the same idea land together.