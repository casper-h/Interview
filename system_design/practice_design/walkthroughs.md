# Worked design walkthroughs

Four designs worked end to end against the [framework](../framework.md), chosen because each
anchors a different core skill: read-heavy caching, key generation, and a metadata-versus-blob
storage split (Pastebin), in-memory structures and cluster sharding (distributed cache), the fanout
trade-off (news feed), and correctness under failure (payment). Read one, then close the file and rebuild it out loud against a
clock. These are reasoning references, not canned answers to memorize; the value is in seeing where
the trade-off lives and being able to reconstruct it when the interviewer perturbs the prompt.

Each walkthrough cites the matching [system-design-primer](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics)
solution as further reading, and reaches into the [building blocks](../building_blocks.md) by
name where a component is used.

## Pastebin

This design exercises read-heavy caching, key generation at scale, and a metadata-versus-blob storage
split. It is the Pastebin variant of the shortlink family: unlike a bare URL shortener, whose record
is a short key mapping to a target URL of about a hundred bytes, a paste stores real user content, so
the sizing and the storage split are the point. A pure URL shortener would carry a much smaller
per-record size and would not need a separate object store, which is exactly the distinction worth
naming out loud if the interviewer frames the prompt as one rather than the other.

Begin with requirements. The system must support 10M users creating 10M pastes per month and reading
100M pastes per month, which gives a 10-to-1 read-to-write ratio. State the non-functional
constraints: reads must be low latency (cache-first), writes can be slower, and shortlinks must not
collide. The back-of-envelope numbers show 4 writes per second average and 40 reads per second
average. Assume an average paste of roughly 1.27 KB (content plus metadata), so 12.7 GB of new
content arrives monthly and 360M pastes accumulate over 3 years. Treat that per-paste size as an
example value, not a fixed figure; it is the input the storage split depends on, so state your
assumption explicitly. That sizing drives both the key-generation choice and the decision to store
content outside the mapping table.

Design the API as two REST endpoints. POST `/api/v1/paste` accepts paste content and optional
expiration, returns a 7-character shortlink. GET `/api/v1/paste?shortlink=<key>` returns the paste
content and metadata. The shortlink generation uses base62 encoding of a hash (built from IP address
plus timestamp, or from random data). Take the first 7 characters. Base62 produces 62^7 possible
values (roughly 3.5 trillion), which is far more than sufficient for 360M shortlinks over 3 years.
Base62 avoids the `+` and `/` characters that base64 includes, so the result is URL-safe without
escaping. Collisions are rare but possible; on a collision, regenerate and retry. Support custom
shortlinks by accepting a user-supplied key and checking the database for uniqueness before
insertion.

The high-level architecture splits storage by access pattern. Use a
[relational database](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)
with the shortlink as a unique primary key to map shortlinks to paste metadata (expiration, creation
time, and a path to the content blob). Store the paste content itself in an object store (S3 or
equivalent) rather than embedding it in the row. This keeps the mapping table small and
cache-friendly, while the object store handles large content without schema constraints. See the
[SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql) discussion in the
building blocks for when to reach for each.

Scale reads with a tiered approach that reflects the 10-to-1 read bias. Put a
[memory cache](https://github.com/donnemartin/system-design-primer#cache) (Redis or Memcached) in
front of the read path; the 40 reads per second average (higher at peak) benefits from
sub-millisecond cache hits. On a miss, fall through to a SQL read replica. Add read replicas behind a
load balancer as read load grows, which defers
[sharding](https://github.com/donnemartin/system-design-primer#sharding) until write volume saturates
a single master. For writes, a single master handles 4 writes per second comfortably. If write spikes
push past that, reach for [federation](https://github.com/donnemartin/system-design-primer#federation)
(split by region or user shard) or sharding by hash of the shortlink.

Deep-dive on key generation. The base62-of-hash approach is stateless and fast, but collisions exist,
so the write path retries with a new hash on collision. An alternative is a centralized counter with
range pre-allocation to each writer, which guarantees uniqueness but introduces coordination
overhead. The trade-off: hashing is faster and scales horizontally at the cost of rare retries;
counters are deterministic but harder to partition. Custom aliases behave differently from generated
keys: a custom-alias collision returns an error to the client (the user chose the collision), while a
generated-key collision retries silently (the system owns the choice). Naming that distinction is a
senior signal.

The read failure mode is cache staleness: an updated or deleted paste can stay cached until TTL
expiry. Mitigate with a short TTL (5 to 10 minutes) and synchronous invalidation on write or delete.
The write failure mode is a collision after exhausting retries, which returns an error. For
observability, track cache hit rate, replica lag, and collision-retry count. At 10x scale, shard the
writes by hash of the shortlink and front popular content with a
[CDN](https://github.com/donnemartin/system-design-primer#content-delivery-network). See the
[pastebin primer solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/pastebin)
for further reading.

A strong hire explains why base62-of-hash produces enough entropy for the sizing, names the SQL vs
object-store split by access pattern unprompted, and deep-dives on collision handling plus
custom-alias semantics; a lean hire stops at "we hash the input and store it."

## Distributed cache

This design exercises in-memory data structures for O(1) operations, eviction, and cluster-wide
sharding. Begin with requirements. The system must cache query results for 10B queries per month
(roughly 4,000 requests per second) with low latency. Each cached entry is 270 bytes (query key plus
title and snippet). If all queries were unique, the system would need 2.7 TB of memory per month, so
eviction is mandatory. State the non-functional constraints: lookups and insertions must be O(1), and
the cache must survive partial cluster failure. A single-machine cache is too small, so the design
must shard across machines.

Design the API as two operations: `get(query)` returns cached results or null on miss; `set(query,
results)` stores a result and evicts the least recently used entry if the cache is at capacity. The
cache is a hash map (query to linked-list node) plus a doubly linked list (head is most recently
used, tail is least recently used). On `get`, look up the node in O(1) via the hash map, move it to
the head in O(1) with pointer updates, and return the result. On `set`, look up the node; if it
exists, update and move to head; if not and the cache is full, remove the tail node from both the
list and the hash map, then insert the new node at the head. Each operation is O(1) because hash-map
access is O(1) and doubly-linked-list splicing is O(1) with direct node references. This is the same
structure as the LRU cache coding problem, which is worth noticing out loud.

Use [cache-aside](https://github.com/donnemartin/system-design-primer#cache-aside) as the update
policy. On a miss, the query service calls the reverse-index and document services, assembles the
result, writes it to the cache, and returns it. Set a TTL (commonly 10 to 30 minutes) to expire stale
results when page content or ranking changes. The trade-off is a stale window until expiry or manual
invalidation. The failure mode is a thundering herd when a hot key expires and every request misses
at once, all flooding the backend. Mitigate with request coalescing (a single request fetches and
populates while concurrent requests wait for it) or staggered TTL (add randomness to expiry so hot
keys do not expire together). A second failure mode is a hot key that saturates a single node;
mitigate by replicating the hot entry or adding a small in-process cache tier in front of the
cluster.

Scale across machines with sharding. Three options: each machine runs its own independent cache
(simple, but low hit rate because the same query can land on different machines); replicate the full
cache to every machine (simple, but wastes memory); or shard across the cluster with `machine =
hash(query)` (best). Reach for the third. Use consistent hashing to map queries to machines so that a
node joining or leaving moves only a fraction of keys rather than rehashing the entire keyspace,
which limits invalidation on membership changes. A node failure removes a slice of the keyspace;
those queries miss and fetch from the backend until the cache repopulates. The failure is graceful,
but a sudden spike of misses can overwhelm the backend if the failed node held popular keys; mitigate
with backend read replicas or a standby that takes over the hash range.

Deep-dive on the thundering herd. A hot query with many concurrent requests expires, all miss, all
call the backend at once, and the backend saturates. The canonical fix is request coalescing (also
called request collapsing or stampede protection): the first request to miss acquires a lock or sets
a sentinel in the cache, fetches, and populates; concurrent requests see the sentinel and wait, or
serve stale data if it is available. An alternative is probabilistic early expiration: before TTL
expires, a request has a small probability of proactively refreshing the entry, so hot keys rarely
expire under load. The trade-off is added complexity versus the cost of backend overload. State it
explicitly.

For observability, track hit rate (by query), eviction rate, and backend latency on miss. At 10x
scale, add an edge cache tier for geographic distribution and partition the backend to absorb miss
load. See the
[query_cache primer solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/query_cache)
for further reading.

A strong hire explains why the hash map plus doubly linked list is O(1) per operation, names the
thundering-herd failure mode unprompted, and states request coalescing with its trade-offs; a lean
hire stops at "we use an LRU cache and shard by hashing."

## News feed and timeline

This design exercises the read-heavy fanout problem and the hybrid push-pull model. Start with
requirements. Establish that this is read-heavy (250B reads versus 15B writes per month, roughly 100K
reads per second versus 6K tweets per second), that posting must be fast (under 500ms), and that
home-timeline reads must stay under 200ms at p99. State the consistency trade-off explicitly:
eventual consistency is acceptable for the timeline, but a user's own tweets must appear immediately
in their user timeline. Bound the scale: 100M active users, 500M tweets per day, average fanout of 10
followers, which yields 150B fanout deliveries per month. The estimation step reveals the real
bottleneck: 60K fanout deliveries per second is the write-path constraint, not the 6K tweets per
second.

For API design, name three endpoints: POST `/tweet` (user_id, auth_token, status, media_ids), GET
`/home_timeline` (recent tweets from followed users), and GET `/user_timeline` (the user's own
tweets). The high-level architecture has a Write API that stores tweets in SQL and triggers a Fan Out
Service, which queries the User Graph Service (who follows whom, stored in a
[key-value store](https://github.com/donnemartin/system-design-primer#key-value-store) for O(1)
lookup) and writes to per-follower Redis lists. The Read API fetches from the memory cache with O(1)
access, then hydrates via multiget to a Tweet Info Service and a User Info Service.

The data model step is where the Redis list structure matters. Each follower gets a list of
(tweet_id, user_id, meta) tuples, roughly 25 bytes per entry. Keep only the most recent few hundred
tweets per timeline in cache (covering the common case of scrolling back a day or two) and only
active users (logged in within 30 days); rebuild an inactive user's timeline on demand from SQL, which
holds the full history. Use
[master-slave replication](https://github.com/donnemartin/system-design-primer#master-slave-replication)
for SQL reads and [sharding](https://github.com/donnemartin/system-design-primer#sharding) on user_id
for writes once write load exceeds a single master.

The deep dive is the hybrid fanout model, the highest-value trade-off to state by name. Pure
fan-out-on-write breaks for celebrity accounts: a user with 10M followers triggers 10M writes per
tweet, saturating the 60K-deliveries-per-second budget. The failure mode is that celebrity tweets take
minutes to propagate, and a race emerges with @replies (a reply can appear in a follower's timeline
before the original if fanout order is not preserved). The hybrid solution skips fanout for accounts
above a follower threshold (commonly 1M), pulls their tweets at read time from a separate index,
merges with the pre-fanned-out timeline, then re-orders by timestamp at serve time. That re-order also
fixes the @reply race, because the read path sees the full set and orders it correctly. The trade-off
is that reads for users following many celebrities become more expensive (extra queries plus a merge),
which is acceptable because those readers are a small fraction of traffic.

For bottlenecks and failure modes, cover the thundering herd when a hot Redis key expires (staggered
TTLs, and a write path that also logs to a durable queue for replay), the SQL write bottleneck (shard
by user_id, or move tweets to a
[document store](https://github.com/donnemartin/system-design-primer#document-store)), and the User
Graph Service as a single point of failure (replicate it, shard the follower graph). The wrap-up names
observability (fanout latency per tweet, cache hit rate, p99 read latency by endpoint) and cost (Redis
memory is the largest line item; compressing timeline entries or moving cold timelines to SSD-backed
storage is the lever). At 10x scale the hybrid threshold drops and you add an async fanout tier for
mid-sized accounts, where the post returns immediately and fanout completes within seconds. See the
[twitter primer solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter)
for further reading.

A strong hire names the hybrid model unprompted, quantifies the celebrity fanout bottleneck, and
explains the re-order-at-serve-time fix for the race; a lean hire stops at pure fan-out-on-write.

## Payment and digital wallet

This design exercises correctness under failure and the exactly-once-effect pattern. Start with
requirements. Functional: users fund a wallet from a bank account, send money to other users, and
query their balance. Non-functional: strong consistency for balances (a stale read that says you have
$100 when you have $50 is wrong), durability (no money lost on crash), auditability (every state
change is traceable), and idempotency (a retry after timeout does not double-charge). State the scale:
10M users, 30M linked accounts, 5B transactions per month (roughly 2K writes per second), 500M reads
per month (roughly 200 reads per second), so this is write-heavy at 10-to-1. Estimation shows 250 GB
of new transaction data per month at 50 bytes per transaction, which fits a single database for the
first year.

For API design, name POST `/fund` (user_id, account_id, amount, idempotency_key), POST `/transfer`
(from_user_id, to_user_id, amount, idempotency_key), and GET `/balance` (user_id). Every mutating
endpoint requires an idempotency key. The high-level architecture has a Write API that checks an
idempotency table (keyed on idempotency_key with the request hash and result), appends to a ledger,
updates balances, and writes to a transactional outbox for downstream consumers (notifications, fraud
detection, analytics). The Read API serves balances from a read replica or a short-TTL
[cache-aside](https://github.com/donnemartin/system-design-primer#cache-aside) cache (5 seconds is an
acceptable balance-freshness window).

The data model is a double-entry ledger. Each transaction creates two entries, a debit from one
account and a credit to another. The ledger table is append-only (no UPDATE or DELETE) with columns
for entry_id, transaction_id, account_id, debit_amount, credit_amount, balance_after, and created_at;
exactly one of debit_amount and credit_amount is non-zero per row, and the rows for a given
transaction_id sum to zero, which is the invariant reconciliation checks. Balances are denormalized
into a separate table for fast reads, but the ledger is the source of truth.
The idempotency table carries idempotency_key, request_hash (to detect a replay that reuses a key with
different parameters, which is an error), result, and created_at, with a unique index on the key. For
linked accounts, store credentials encrypted at rest and pull transactions daily through an async
queue, which is the pipeline shape the
[mint primer solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/mint)
covers; the correctness depth below is the payment-specific part that mint does not address.

The deep dive is correctness under failure, in four parts. First, idempotency. A client sends POST
`/transfer` with a key. The server checks the idempotency table: if the key exists and the request
hash matches, return the cached result (a retry of a completed request); if the key exists but the
hash differs, return 400 (the client reused a key); if the key is absent, proceed. The server then
runs one database transaction that inserts the idempotency record as in-progress, appends the two
ledger entries, updates the two balances, writes the outbox row, marks the idempotency record success,
and commits. If the commit fails, everything rolls back and the client's retry looks fresh; if the
commit succeeds but the response is lost, the retry returns the cached result. This is what prevents a
double-charge.

Second, strong consistency where it counts, which is the write path, not the read. Overdraft
prevention is a property of the debit, not of what balance the user last saw: the transfer runs a
conditional write that re-checks `balance >= amount` at commit under a linearizable guarantee
(synchronous replication, or a distributed database like Spanner or CockroachDB), so a stale read can
never authorize an overdraw because the write re-validates. That is why the displayed balance can
tolerate the short-TTL cache above: reads may lag by a few seconds without being wrong, while the
authorization write must be strongly consistent. Be precise about this split under probing; claiming
"the whole system must be strongly consistent" is weaker than naming that only the balance-mutating
write needs it. The trade-off is higher write latency (a synchronous round-trip) and reduced
availability if the master is down; mitigate availability with automatic
[failover](https://github.com/donnemartin/system-design-primer#fail-over) and latency by keeping
replicas in-region.

Third, exactly-once effect via the transactional outbox. Downstream consumers must act on each
transaction once. True exactly-once delivery does not exist; you get at-least-once delivery plus
idempotency. The Write API writes the outbox row in the same transaction as the ledger append. A
separate processor polls the outbox (or uses change-data-capture), publishes each row to a
[message queue](https://github.com/donnemartin/system-design-primer#message-queues), and marks it
sent. Consumers dedupe on transaction_id and discard duplicates. Publishing inside the transaction but
delivering through an at-least-once queue is what prevents both a lost message (crash after commit,
before publish) and an acted-on duplicate.

Fourth, cross-service money movement via a saga. To add "cash out to a bank," you cannot run a
distributed transaction because the bank does not support two-phase commit. Use a saga: debit the
wallet, call the bank API, and if the bank call fails, credit the wallet back (the compensating
transaction). Log each step in a saga-state table so you can resume after a crash. The failure mode is
that the compensation itself can fail; handle it with retries plus a daily manual-reconciliation queue.

For bottlenecks, shard the ledger and balances by user_id or
[federate](https://github.com/donnemartin/system-design-primer#federation) by geography, run a nightly
reconciliation that sums ledger entries per account against the balances table and alerts on drift,
and feed the outbox into a real-time fraud service that can block or reverse within seconds. The
wrap-up names observability (transaction latency, idempotency hit rate, saga success rate,
reconciliation drift) and cost (storage dominates; archive ledger entries past the retention window to
cold storage). At 10x scale, move to a distributed database, split the Write API per transaction type,
and add a materialized view for balance history.

A strong hire covers all four correctness mechanisms unprompted, quantifies the double-charge failure
mode, and explains the outbox plus downstream dedupe; a lean hire describes idempotency but misses the
outbox or the saga.
