# System Design Building Blocks

The [framework](./framework.md) tells you the *steps* of a design interview.
This file is the *components* you reach for while walking those steps: the reusable toolkit that
turns "I'd add a cache here" into a crisp statement of which caching strategy, why, and what it costs
you. During the deep-dive step, the difference between a hire and a strong hire is often exactly
this: naming the right building block, justifying it against a named alternative, and stating its
failure mode without being asked.

Use this as a reference, not a linear read. Work through a few practice designs first; when one
surfaces a component you can't reason about crisply, come here and close that gap. For each block
below, the goal is to be able to answer three things from memory: **when do I reach for it, what is
the main alternative and the trade-off between them, and how does it fail?**

---

## 1. Load Balancing

- **L4 vs L7.** L4 balances on TCP/UDP (fast, protocol-agnostic, no visibility into the request);
  L7 balances on HTTP/gRPC (can route by path, header, or cookie, terminate TLS, and retry, at some
  CPU cost). Reach for L7 when routing decisions depend on request content.
- **Algorithms.** Round-robin, least-connections, least-response-time, and hashing (consistent
  hashing when backends are stateful or cache-warm). Weighted variants for heterogeneous hardware.
- **Health checks and circuit breaking.** Active vs passive health checks; ejecting an unhealthy
  backend; a circuit breaker to stop hammering a failing dependency and shed load fast.
- **Session affinity** (sticky sessions) when a backend holds per-session state, and why stateless
  services that externalize session state are usually the better answer.
- **Placement.** DNS-based (coarse, geographic), a dedicated LB tier, or client-side load balancing
  (common with service mesh / gRPC).

## 2. Caching

- **Strategies.** Cache-aside (lazy, app manages the cache: the common default), read-through,
  write-through (consistent, higher write latency), write-behind / write-back (fast writes, risk of
  loss on crash), and refresh-ahead (proactively reload hot keys before they expire, which hides the
  refill latency but wastes work when the prediction is wrong).
- **Eviction.** LRU (the usual default), LFU (favors long-term popularity over recency), and FIFO
  or random (cheap, for when access has no useful locality). The eviction policy and the TTL are
  separate levers: TTL bounds staleness, eviction bounds size.
- **Redis vs Memcached.** Memcached is a plain in-memory LRU key-value store, multithreaded and
  simple. Redis is single-threaded per node but adds data structures (sorted sets, lists, hashes),
  persistence, replication, and pub/sub. Reach for Memcached when you only need a fast look-aside
  cache, and for Redis when you need those structures (rate-limiter counters, leaderboards, a queue)
  or durability.
- **Layers.** Client / browser -> CDN -> edge cache -> application-level (in-process or shared, e.g.
  Redis/Memcached) -> database buffer cache. Say which layer you mean.
- **Invalidation.** TTL, event-driven / pub-sub invalidation, and versioned keys. Invalidation is
  the hard part of caching, so be explicit about how stale the data is allowed to get and why that
  staleness is acceptable for this data.
- **Failure modes to name unprompted.** Cache stampede / thundering herd on a cold or expired hot
  key (mitigate with request coalescing, staggered TTLs, or a lock-and-refresh); and the caching of
  negative results to absorb lookups for keys that don't exist.
- **When *not* to cache.** Write-heavy data with low read reuse, or data whose staleness is
  unacceptable. Knowing when a cache adds complexity without payoff is itself a senior signal.

## 3. Content Delivery (CDN)

- Edge caching of static and cacheable dynamic content close to users; origin shielding to protect
  the origin from cache-miss stampedes; cache-control headers and purge/invalidation.
- Pull (lazy, origin-fetched on first miss) vs push (pre-populated) CDNs.
- The core justification is the latency arithmetic in the framework: a cross-region round trip
  dwarfs everything else, so serving from the edge is the single biggest user-facing latency win.

## 4. Partitioning and Sharding

- **Strategies.** Range partitioning (good for range scans, prone to skew), hash partitioning
  (even load, breaks ordering), and composite / hash-then-range (blends both).
- **Consistent hashing.** Map both keys and nodes onto a ring so adding or removing a node moves
  only a small slice of keys; use **virtual nodes** to smooth load across heterogeneous or few nodes.
  This is the standard answer to "how do you rebalance without reshuffling everything?"
- **Hot partitions / the celebrity problem.** Detection (per-partition metrics) and mitigation:
  key salting, splitting the hot key across sub-partitions, or fronting it with a cache.
- **Choosing a partition key.** High cardinality, even access distribution, and alignment with your
  dominant query so you avoid scatter-gather across all partitions.

## 5. Replication

- **Models.** Single-leader (simple, one write path, read replicas for scale), multi-leader (writes
  in multiple regions, needs conflict resolution), and leaderless / quorum (Dynamo-style, highly
  available).
- **Sync vs async.** Synchronous replication protects against data loss but adds write latency and
  couples availability to the slowest replica; asynchronous is fast but risks losing recent writes
  on failover and exposes replication lag.
- **Quorums.** With N replicas, `R + W > N` guarantees a read overlaps the latest write. Tune R and
  W to trade read vs write latency against freshness (e.g. W=N for read-heavy, W=1 for write-heavy).
- **Failure modes.** Replication lag (stale reads, read-your-writes anomalies), split-brain on
  partition, and failover correctness (fencing tokens to stop a demoted leader from accepting
  writes).

## 6. Consensus and Coordination

- **What it's for.** Leader election, distributed locks, membership, and configuration/metadata that
  must be linearizable. Reach for it sparingly: it is a correctness tool, not a throughput tool.
- **Algorithms.** Raft (leader + replicated log; the one to be able to explain), Paxos (mention as
  the foundation), ZAB (ZooKeeper). Off-the-shelf: ZooKeeper, etcd, Consul.
- **Cost.** A majority round trip per decision, and reduced availability during elections, which is
  why you keep the consensus-managed state small and layer high-throughput data outside it.
- **Distributed locks.** A lease (a lock with a TTL) so a crashed holder does not block the system
  forever, plus a **fencing token**: a monotonically increasing number handed out with the lock that
  the protected resource checks, so a paused-then-resumed holder whose lease already expired cannot
  still act on stale authority. Redis Redlock is the contested single-store option; a lease on
  ZooKeeper or etcd is the safer answer when correctness matters. The strong-hire point is that a
  lock without fencing is not safe under process pauses.
- **The FLP result, stated plainly.** In an asynchronous system where a single process may fail,
  no deterministic protocol can guarantee that consensus always terminates. Real systems live with
  this by relaxing the "always" rather than the safety: Raft and Paxos never return a wrong result,
  but they can stall (repeated elections) while messages are delayed, and they make progress once
  the network is well-behaved for long enough. Cite FLP to explain why consensus protocols depend on
  timeouts and cannot promise both safety and liveness under fully asynchronous conditions; do not
  cite it as a reason consensus is impossible in practice.

### Time, Clocks, and Their Limits

- **Physical clocks drift and are not monotonic.** Wall-clock time across machines disagrees by
  milliseconds even under NTP, and it can jump backward on correction, so a timestamp comparison is
  not a safe way to order events on different hosts. This is the reason "just use the timestamp" is
  the wrong answer to most ordering questions.
- **Logical clocks order events without physical time.** A Lamport clock gives a total order
  consistent with causality but cannot tell whether two events are concurrent; a vector clock can
  distinguish concurrent from causally-ordered events at the cost of storing one counter per node.
  Reach for these when the requirement is "establish an ordering," not "know the real time."
- **Bounded clock uncertainty as a design tool.** Spanner's TrueTime exposes the clock's error bound
  as an interval rather than a point, and a transaction waits out that interval before committing so
  that commit timestamps respect real-time order across regions. The cost is a deliberate wait tied
  to the uncertainty bound, which is why globally strong consistency at that scale needs specialized
  time infrastructure. Name this trade-off when a design asks for external consistency across
  regions (see geo-distribution, block 13).

## 7. Rate Limiting

- **Algorithms.** Token bucket (allows bursts up to bucket size: the usual default), leaky bucket
  (smooths to a fixed rate), fixed window (simple, but allows 2x bursts at the boundary), sliding
  window log / counter (accurate, more state).
- **Distributed enforcement.** A shared counter (Redis) vs per-node local limits; the coordination
  vs accuracy trade-off. Where to enforce: API gateway, per-service, per-user, or per-IP.
- **Two distinct goals.** Abuse prevention (per-user/per-IP, a security concern) vs load shedding
  (protecting the system under overload): they call for different limits and placement.

## 8. Message Queues and Event Streaming

- **Delivery semantics.** At-most-once (may drop), at-least-once (may duplicate: the common
  default, pair with idempotent consumers), exactly-once (expensive; usually at-least-once +
  dedup/transactional writes rather than true exactly-once delivery).
- **Ordering.** Global ordering is expensive; per-partition / per-key ordering (Kafka) is the
  pragmatic answer. Partition by the key whose order you actually need to preserve.
- **Queue vs log.** A traditional queue (SQS, RabbitMQ) deletes on ack; a log (Kafka) retains and
  lets consumers replay from an offset. The latter doubles as an event source and recovery tool.
- **Backpressure.** Bounded queues, consumer-lag monitoring, and producer throttling so a slow
  consumer can't exhaust memory upstream. This connects to the concurrency track's producer-consumer
  pattern.
- **Use cases.** Decoupling services, smoothing spiky load, async/background work, and event-driven
  fan-out.

## 9. Idempotency and Reliability

- **Idempotency keys.** A client-generated key plus a server-side dedup table so a retried write
  (after a timeout or network blip) doesn't double-charge. The canonical example is a payment.
- **Retries done safely.** Exponential backoff with jitter (to avoid synchronized retry storms) and
  a circuit breaker to stop retrying a dead dependency.
- **Deduplication at scale.** A dedup table, or a bloom filter as a cheap first-pass "have I seen
  this?" check in front of it.
- **Distributed transactions.** Two-phase commit (blocking, coordinator is a single point of
  failure) vs the **saga pattern** (a sequence of local transactions with compensating actions).
  Sagas are the modern default for cross-service consistency and a strong thing to raise unprompted.

## 10. Consistency Models

- **Strong** (linearizable / serializable): every read sees the latest write; needed for balances,
  inventory, unique-constraint invariants.
- **Causal / read-your-writes / monotonic reads:** cheaper session guarantees that cover most
  "the user should see their own action reflected" cases.
- **Eventual:** replicas converge; fine for feeds, counts, and caches.
- **The frameworks to cite.** CAP (during a partition, choose consistency or availability) and its
  refinement **PACELC** (Else, even with no partition, choose Latency or Consistency). Map real
  systems: Spanner is roughly PC/EC, Dynamo is roughly PA/EL.
- **Replication consistency versus transaction isolation.** The models above describe what a single
  replicated object guarantees across replicas. Isolation levels (below) describe what concurrent
  multi-object transactions guarantee against each other. They are separate axes: a store can be
  linearizable per key and still expose weak isolation across a transaction that touches many keys.
  Keeping the two apart is a common point where a strong answer separates from a hand-waved one.

### Transaction Isolation Levels

Order from weakest to strongest by the anomaly each one prevents. Naming the specific anomaly, not
just the level, is the signal an interviewer is looking for.

- **Read uncommitted:** no protection; a transaction can read another's uncommitted writes (a **dirty
  read**). Rarely a deliberate choice.
- **Read committed:** reads see only committed data, which removes dirty reads. It still allows a
  **non-repeatable read**: reading the same row twice in one transaction can return two values because
  another transaction committed in between.
- **Repeatable read and snapshot isolation:** repeated reads of the same row are stable, so
  non-repeatable reads are gone. Snapshot isolation is the common implementation, where the
  transaction reads from a consistent snapshot taken at its start. The two are often named together,
  but they differ on phantoms: textbook repeatable read still allows a **phantom** (a range query
  returning a different set of rows when repeated), while snapshot isolation does not for its own
  reads. Snapshot isolation still permits **write skew**, where two transactions read an overlapping
  set, make disjoint writes that each preserve an invariant alone, and together violate it (the
  canonical example is two on-call doctors each checking that at least one other is on duty and both
  going off call).
- **Serializable:** the outcome is equivalent to some serial order of the transactions, which
  eliminates write skew and phantoms. It is the strongest and the most expensive, implemented through
  two-phase locking, serializable snapshot isolation (SSI), or actual serial execution.
- **Phantom reads** sit alongside these: a query over a range returns a different set of rows when
  repeated because another transaction inserted or deleted a matching row. Snapshot isolation handles
  the read-side phantom for its own snapshot; preventing a write that depends on the absence of such
  rows requires serializable isolation.

## 11. Data Modeling and Storage Selection

- **Access-pattern-first.** Choose storage from the query, not the other way around. OLTP point
  reads/writes vs OLAP scans and aggregations pull toward very different stores.
- **Store types.** Relational (joins, transactions, secondary indexes), key-value (fast point
  access), document (flexible schema), wide-column (Bigtable/Cassandra: huge write throughput,
  query-driven schema), blob/object (large immutable files + metadata elsewhere), search index,
  time-series, graph.
- **Normalization vs denormalization.** Normalize for write integrity; denormalize (and precompute /
  materialize) for read-heavy paths, and be explicit about the write-amplification and
  consistency cost of doing so.
- **Indexing.** Secondary indexes speed reads at the cost of write throughput and storage; composite
  keys to serve range queries and to spread hot keys.
- **Storage engine internals worth a sentence.** LSM-tree (high write throughput, read/space
  amplification, compaction) vs B-tree (predictable read latency): reach for LSM for write-heavy
  ingest, B-tree for balanced OLTP.

## 12. API and Communication Patterns

- **Protocols.** REST (simple, cacheable, great for public APIs), gRPC (efficient binary, strong
  typing, ideal for internal service-to-service), GraphQL (flexible client-shaped queries, at the
  cost of HTTP caching and added query-complexity concerns).
- **Real-time transports.** Long-polling (simple, works everywhere), Server-Sent Events (one-way
  server->client push), and WebSockets (full-duplex). Pick by whether you need bidirectional, and
  reach for WebSockets for chat/collab, SSE for live feeds/notifications.
- **Pagination.** Cursor/keyset (stable under concurrent writes: the default at scale) vs offset
  (simple but drifts as data changes).
- **Versioning and idempotency.** URL vs header versioning with backward compatibility as a
  constraint; idempotency keys on mutating endpoints (cross-reference block 9).

## 13. Geo-Distribution and Multi-Region

- **Why.** Latency (serve from the nearest region) and disaster recovery (survive a regional
  outage).
- **Topologies.** Active-passive (a standby region, simpler, slower failover) vs active-active
  (all regions serve, needs conflict resolution and careful data ownership).
- **Consistency at distance.** Globally strong (Spanner/TrueTime: pay latency and clock
  infrastructure) vs regional-primary with async cross-region replication (fast local, eventual
  global) vs leaderless per-region.
- **Routing and failover.** Latency-based / geo DNS, anycast, and health-based failover; and the
  data-residency constraints that sometimes pin data to a region regardless of latency.

## 14. Cell-Based Architecture

- Partition the whole system into independent **cells** (each a full stack serving a slice of
  users/tenants) to bound blast radius: a failure or poison request is contained to one cell rather
  than taking down the fleet. A router maps each request to its cell.
- Worth raising for high-availability, multi-tenant systems (it is how DynamoDB, Slack, and others
  limit the reach of failures): a good "how would you make this more resilient?" answer.

## 15. Observability

- **The three signals.** Metrics (aggregate, cheap, for dashboards and alerts), logs (structured,
  detailed, sampled at volume), traces (per-request spans across services, for latency debugging).
- **What to measure.** The **RED** method for services (Rate, Errors, Duration) and **USE** for
  resources (Utilization, Saturation, Errors); always report latency as percentiles (p50/p95/p99),
  never a mean, because tail latency is what users feel.
- **SLIs, SLOs, error budgets.** An SLI is the measured signal, an SLO the target, and the error
  budget the allowed shortfall that governs how aggressively you ship vs stabilize. Alert on
  symptoms (SLO burn) rather than causes to avoid alert fatigue.

## 16. Security and Trust

- **AuthN / AuthZ.** How users and services authenticate (tokens, OAuth/OIDC, mTLS between services)
  and how authorization is scoped (RBAC/ABAC, resource-level checks).
- **Encryption.** In transit (TLS everywhere) and at rest (storage- or field-level for sensitive
  data); key management as the real hard part.
- **Abuse and edge protection.** Rate limiting (block 7), WAF, and DDoS mitigation at the edge.
- **PII and data lifecycle.** Retention, deletion/right-to-be-forgotten, and audit logging,
  increasingly expected unprompted, especially for fintech and anything storing user data.

## 17. Probabilistic and Specialized Structures

- **Bloom filter.** Space-efficient set-membership with no false negatives: front a store to avoid
  disk lookups for absent keys (LSM engines use it internally). Reach for it whenever the question
  is "is this key *definitely not* present?"
- **Count-min sketch / HyperLogLog.** Approximate frequency and approximate distinct-count in small,
  fixed memory: the standard answer for "top-K" and "unique visitors" at massive scale where exact
  counts are too expensive.
- **Inverted index.** The core structure behind search: term -> posting list of documents, plus
  ranking and sharding across the corpus. Enough to reason about a search or typeahead design.

## 18. API Gateway and Service Mesh

- **API gateway.** A single ingress in front of many backend services: it handles routing, request
  aggregation, authentication/authorization, TLS termination, and rate limiting (block 7) in one
  place, so individual services don't each re-implement them. Reach for it whenever many clients hit
  many services and you want a consistent edge for auth, quotas, and versioning.
- **Service mesh.** Moves service-to-service concerns (mTLS, retries, timeouts, load balancing,
  circuit breaking, and per-hop observability) into a sidecar proxy next to each service, configured
  centrally. Reach for it when the pain is *east-west* traffic between many internal services, not
  *north-south* traffic from external clients.
- **Gateway vs mesh vs plain reverse proxy.** A reverse proxy (block 1) is the primitive; a gateway
  is a reverse proxy specialized for client-facing API concerns; a mesh is the internal, per-service
  version of the same ideas. They compose: a gateway at the edge, a mesh inside. The strong-hire
  answer to "how do you enforce auth and rate limiting across a hundred services?" names the gateway
  for the edge and the mesh (or a shared library) for internal calls, rather than reaching for one
  tool for both.
- **Cost and failure modes.** Both add a network hop and become a shared dependency: an overloaded
  or misconfigured gateway is a system-wide single point of failure, and a mesh's sidecars add
  latency and operational complexity that a small service count rarely justifies.

## 19. Batch Processing

- **What it's for.** Reprocessing a large, bounded dataset for throughput rather than latency:
  nightly aggregations, building a search index or recommendation model, backfills, and ETL. The
  input is complete before the job runs, so results are correct rather than approximate.
- **The model.** MapReduce and its descendants (Spark): partition the input, map in parallel,
  shuffle by key, reduce. The shuffle is usually the bottleneck and the thing worth reasoning about.
- **Trade-off.** High latency (minutes to hours) for high throughput and simple fault recovery: a
  failed task just re-runs on another node because the input partition is immutable and replayable.
- **When to reach for it.** Whenever the question involves "compute X over all historical data" and
  a delay of minutes is acceptable. Pair it with stream processing (block 20) in a lambda or kappa
  architecture when you need both a fast approximate path and a slow exact one.

## 20. Stream Processing

- **What it's for.** Continuous computation over an unbounded event stream with low latency:
  real-time analytics, fraud detection, live leaderboards, and materialized views kept fresh from a
  change stream. Tools: Kafka Streams, Flink, Spark Structured Streaming.
- **Windowing.** Tumbling (fixed, non-overlapping), sliding (fixed, overlapping), and session
  (gap-defined) windows. State the window type explicitly, because it decides what "the last five
  minutes" actually means.
- **Event time vs processing time.** Aggregate on event time (when it happened) not processing time
  (when it arrived), and use a **watermark** to decide how long to wait for late events before
  closing a window. This is the single hardest part and a strong-hire distinction.
- **Exactly-once.** Harder than in a plain queue because operators carry state: it needs
  checkpointed state plus idempotent or transactional sinks. Say "effectively-once via checkpointing
  and idempotent writes" rather than claiming true exactly-once.
- **Failure modes.** Late and out-of-order data, state that grows without bound (needs TTL or
  compaction), and reprocessing after a code change (replay from an offset, block 8).

## 21. Geospatial Indexing

- **What it's for.** "Find the nearest N" and "what is within this region" queries: ride-hailing,
  store locators, nearby-friends, geofencing. A plain B-tree on latitude and longitude cannot answer
  these efficiently because proximity is two-dimensional.
- **The techniques.** Geohash (interleave lat/long bits into a single sortable string, so a prefix
  is a bounding box and the problem reduces to a range scan), quadtree (recursively subdivide space,
  splitting dense cells further), and S2 or H3 (map the sphere to cells, the production choice at
  Google and Uber). Reach for geohash when you want to reuse an existing key-value or SQL store; a
  quadtree when density is very uneven.
- **The boundary problem.** The nearest point can sit in an adjacent cell, so query the target cell
  plus its neighbors, then rank the merged candidates by true distance. Name this unprompted, because
  the naive single-cell answer is subtly wrong.
- **Moving objects.** For drivers or players that move constantly, the index is write-heavy: bucket
  updates, accept a short staleness window, and keep the hot index in memory (Redis geospatial
  commands are the quick answer).

## 22. Change Data Capture and the Outbox Pattern

- **What it's for.** Reliably turning committed database writes into an event stream, so a search
  index, cache, or downstream service stays in sync without dual-writes. The core problem is that
  writing to the database and publishing to a queue in two steps can partially fail and diverge.
- **CDC.** Tail the database's replication log (binlog, WAL) with a tool like Debezium and emit an
  event per row change. No application change, and it captures every write including ones outside
  your service, at the cost of coupling to the storage engine's log format.
- **Transactional outbox.** Write the business row and an "outbox" event row in the same local
  transaction, then a relay reads the outbox and publishes. This keeps the write and the intent to
  publish atomic, and is the answer when you control the writing service.
- **When to reach for it.** Any time a design says "keep the index in sync with the database" or
  "publish an event when an order is created": dual-writing directly to a queue is the trap this
  block exists to avoid.

## 23. Event Sourcing and CQRS

- **Event sourcing.** Store the append-only log of state-changing events as the source of truth and
  derive current state by replaying them, rather than storing only the latest snapshot. You get a
  full audit trail, the ability to rebuild state or reconstruct any past point, and a natural fit for
  ledgers and order systems. The costs are replay time (mitigated with periodic snapshots), schema
  evolution of old events, and that "delete" becomes a compensating event, not a row removal.
- **CQRS.** Separate the write model from one or more read models: commands append events, and
  denormalized read views are projected from those events for fast queries. Reach for it when read
  and write shapes diverge sharply, and be explicit that the read side is eventually consistent with
  the write side.
- **When *not* to reach for it.** For simple CRUD, event sourcing and CQRS add real complexity for
  little payoff. Naming that boundary is itself a senior signal, the same way "when not to cache" is.

## 24. Dead-Letter Queues

- **What it's for.** A separate queue that captures messages a consumer cannot process after a set
  number of retries (a poison message, a schema it can't parse, a permanent downstream failure), so
  one bad message does not block the partition behind it or retry forever.
- **How it fits.** Pair it with bounded retries and exponential backoff (block 9): retry a few times
  for transient faults, then route to the dead-letter queue and move on. Alert on dead-letter depth
  and give someone a way to inspect, fix, and replay.
- **When to raise it.** Any async or queue-based design should have an answer for "what happens to a
  message that keeps failing?" A DLQ is that answer, and leaving it out is a common gap in otherwise
  complete designs.

---

## How This Maps to the Framework

During a design, this library feeds mainly two steps:

- **High-level architecture:** blocks 1-3, 8, 12, 14, 18-24 (the boxes and arrows: load balancers,
  caches, CDN, queues, gateways, meshes, cells, batch and stream pipelines, change-capture,
  event-sourced stores, dead-letter queues).
- **Deep dive:** blocks 4-6, 9-11, 13, 15-17, 20-23 (the internals: partitioning, replication,
  consensus, consistency, storage, geo, observability, specialized structures, windowing and
  watermarks, geospatial indexing, outbox reliability, event-sourced read models).

You will never use all of these in one interview. The skill is reaching for the two or three the
problem actually needs, naming the alternative you rejected and why, and stating how the block fails,
which is exactly the three-question test at the top of this file.
