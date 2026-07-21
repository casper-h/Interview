# Fundamentals: Networking, OS, and Database Internals

This track covers the layer beneath distributed systems design: networking, operating systems, and
database internals. For most product and feature-team loops, the coding, system-design, and
behavioural tracks are what is tested, and time spent here is better spent there. But
infrastructure, platform, systems, and trading-adjacent teams probe below the distributed-systems
layer, and a candidate who can design Spanner at a high level but cannot explain a TCP handshake or
the difference between a process and a thread reads as having memorized system design rather than
earned it.

The database-internals portion (storage engines, indexing, isolation levels, MVCC, write-ahead log)
is expected knowledge at the upper-Senior and lower-Staff band, where component internals like
B-trees, LSM-trees, and inverted index are expected (see the
[concepts-by-level reference](../plan/concepts_by_level.md)). That portion is largely
review once you have done the DDIA and Database Internals reading in the
[reading plan](../plan/README.md). The networking and operating-systems portion scales with team type:
heavy for infrastructure, platform, systems, and trading teams, light for product teams.

Use the "Adapting depth by company or team type" guidance in the [system design framework](../framework.md)
to decide how much of this you need: product companies, database internals plus light networking;
infrastructure and platform teams, most of it.

## Networking

Be able to explain, and reason about the performance implications of:

- **The TCP/IP model and a TCP connection:** the three-way handshake, why connection setup costs a
  round trip (and why connection reuse and pooling matter), flow control, and congestion control at
  a conceptual level.
- **TCP vs UDP** and when each is the right choice (reliability and ordering vs latency and
  overhead).
- **HTTP/1.1 vs HTTP/2 vs HTTP/3:** head-of-line blocking, multiplexing, and why HTTP/3 moved to
  QUIC/UDP.
- **TLS:** what the handshake establishes, the round-trip cost, and session resumption.
- **DNS resolution:** the lookup path, caching and TTLs, and its role in load balancing and failover.
- **Load balancing at the network level:** L4 vs L7 (cross-reference the building-blocks library),
  and anycast.

## Operating Systems

- **Processes vs threads:** address-space isolation vs shared memory, the cost of context switches,
  and when you'd reach for multiple processes vs multiple threads (connects directly to the
  concurrency track).
- **Concurrency primitives at the OS level:** mutexes, semaphores, condition variables, and how they
  map to the language idioms in the [concurrency track](./concurrency.md).
- **Virtual memory:** paging, the page cache, and why memory-mapped I/O and the page cache matter for
  storage-engine performance.
- **I/O models:** blocking vs non-blocking, synchronous vs asynchronous, and the event-loop model
  (epoll/kqueue) behind high-concurrency servers.
- **Scheduling:** preemptive versus cooperative scheduling, the role of time slices and priorities,
  and why CPU-bound and I/O-bound workloads behave differently under the same scheduler (an I/O-bound
  task yields often and stays responsive; a CPU-bound task must be preempted). Be able to connect
  this to thread-pool sizing, where the right pool size depends on whether the work blocks on I/O.
- **Clocks and time:** why the wall clock is unreliable for ordering or measuring durations. System
  time can jump backward when NTP corrects drift, so a monotonic clock is the right source for
  elapsed-time measurements, and cross-machine timestamp comparison is unsafe without bounded-error
  time. This is the operating-system-level foundation for the clock-skew and TrueTime material in the
  system-design [building blocks](../building_blocks.md); a design that orders events by raw
  wall-clock timestamps is a common and avoidable error.

## Database Internals

- **Storage engines:** B-tree vs LSM-tree in depth (write/read/space amplification, compaction):
  the same trade-off the system-design track uses, but here you should be able to explain the
  mechanism, not just cite the conclusion.
- **Indexing:** clustered vs secondary indexes, covering indexes, and the write-vs-read cost of
  adding one.
- **Transactions and isolation levels:** read-committed, repeatable-read, snapshot isolation, and
  serializable: what anomaly each prevents (dirty read, non-repeatable read, phantom, write skew).
- **MVCC:** how multi-version concurrency control gives readers a consistent snapshot without
  blocking writers.
- **The write-ahead log:** why it's the foundation of durability and crash recovery, and how it
  doubles as the basis for replication.
- **Query execution basics:** how a join is executed (nested loop, hash, merge), and what a query
  planner is choosing between.

## How to Study This

This is reference material, not a problem set. The DDIA and Database Internals reading in the
[reading plan](../plan/README.md) already covers the database-internals portion in depth. If you have
done that reading, most of this section is review. For networking and OS, the goal is being able to
answer a pointed question crisply and reason about the performance consequence, not to recite RFCs.
Treat a blank on any bullet above the same way you treat a blank in the coding pattern-recall
checklist: a specific signal of where to read, not a reason to read everything.
