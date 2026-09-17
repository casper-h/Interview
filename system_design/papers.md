# Primary Paper Path

Read papers in prerequisite order. For each paper, write the workload, failure model, central mechanism, guarantees, non-goals, and one interview decision it changes. **Required** papers are assigned by a curriculum stage. **Targeted** papers are optional unless a role or prompt calls for them.

## 1. Foundations of Data and Computation

### The Google File System

- **Link:** [The Google File System](https://research.google/pubs/the-google-file-system/)
- **Status:** Required, Stage 2.
- **Problem:** Large distributed files on failure-prone commodity machines for Google's workloads.
- **Prerequisites:** Files, replication, checksums, and remote procedure calls (RPCs).
- **Understand:** Large chunks, centralized metadata, leases, replication, record append, and recovery assumptions.
- **Does not claim:** General Portable Operating System Interface (POSIX) filesystem semantics or that one metadata server is a universal architecture.
- **Interview use:** Object storage, metadata versus data planes, large-file ingestion, and append workloads.

### MapReduce: Simplified Data Processing on Large Clusters

- **Link:** [MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
- **Status:** Required, Stage 3.
- **Problem:** Reliable parallel batch computation across large clusters.
- **Prerequisites:** GFS, partitioning, and sorting.
- **Understand:** Map and reduce contracts, shuffle, locality, scheduling, retries, backup tasks, and deterministic recomputation.
- **Does not claim:** Low-latency stream processing, arbitrary iterative efficiency, or inherent exactness for external effects.
- **Interview use:** Backfills, aggregation, indexing, batch recovery, and stragglers.

### Bigtable: A Distributed Storage System for Structured Data

- **Link:** [Bigtable](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/)
- **Status:** Required, Stage 2.
- **Problem:** A scalable sorted data model for varied Google workloads.
- **Prerequisites:** GFS, logs, SSTables, and partitioning.
- **Understand:** Sparse multidimensional map, row-key locality, tablets, memtables, sorted-string tables (SSTables), compaction, metadata, and Chubby dependency.
- **Does not claim:** A relational model, unrestricted secondary indexes, or general multi-row atomicity, consistency, isolation, and durability (ACID) transactions.
- **Interview use:** Wide-column stores, time-series keys, range scans, hot partitions, and LSM trade-offs.

## 2. Replication, Ordering, and Coordination

### Time, Clocks, and the Ordering of Events in a Distributed System

- **Link:** [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
- **Status:** Required, Stage 2.
- **Problem:** Reasoning about causality and ordering without a global clock.
- **Prerequisites:** Processes, messages, and partial orders.
- **Understand:** Happened-before, logical clocks, and extending a partial order to a total order.
- **Does not claim:** Lamport timestamps detect concurrency, measure elapsed time, or replace consensus.
- **Interview use:** Message ordering, causality, versioning, and why wall-clock timestamps are unsafe authority.

### Dynamo: Amazon's Highly Available Key-value Store

- **Link:** [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- **Status:** Required, Stage 2.
- **Problem:** Highly available, always-writable key-value storage for selected Amazon services.
- **Prerequisites:** Replication, hashing, quorums, and versioning.
- **Understand:** Consistent hashing, preference lists, sloppy quorums, hinted handoff, vector clocks, read repair, and Merkle trees.
- **Does not claim:** Strong consistency, universal suitability, or describe DynamoDB.
- **Interview use:** Shopping carts, available writes, conflict reconciliation, repair, and quorum caveats.

### Cassandra: A Decentralized Structured Storage System

- **Link:** [Cassandra paper](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf); then [current Cassandra documentation](https://cassandra.apache.org/doc/latest/)
- **Status:** Required comparison, Stage 2.
- **Problem:** Facebook-era decentralized storage combining Dynamo distribution with a Bigtable-like model.
- **Prerequisites:** Dynamo, Bigtable, and LSM trees.
- **Understand:** Historical partitioning, replication, failure detection, storage path, and tunable operations.
- **Does not claim:** Current Apache Cassandra behavior. Modern conflict resolution, CQL, repair, lightweight transactions, and implementation details require current documentation.
- **Interview use:** Wide-column modeling, tunable consistency, repair, compaction, and historical versus current product semantics.

### In Search of an Understandable Consensus Algorithm (Extended Version)

- **Link:** [Raft](https://raft.github.io/raft.pdf)
- **Status:** Required, Stage 2.
- **Problem:** Understandable replicated-log consensus under crash failures.
- **Prerequisites:** Quorums, replicated state machines, and partial failure.
- **Understand:** Terms, leader election, log matching, commitment, safety, membership changes, and snapshots.
- **Does not claim:** Byzantine fault tolerance or provide every production detail, such as client deduplication and storage engineering.
- **Interview use:** Metadata, leader election, configuration, linearizable state, and authority transfer.

### Paxos Made Simple

- **Link:** [Paxos Made Simple](https://www.microsoft.com/en-us/research/publication/paxos-made-simple/)
- **Status:** Targeted, Stage 2.
- **Problem:** Agreement despite crash failures and delayed or lost messages.
- **Prerequisites:** Quorums and state-machine replication.
- **Understand:** Proposers, acceptors, learners, ballot numbers, quorum intersection, and safety.
- **Does not claim:** A complete production protocol for persistence, reconfiguration, snapshots, or clients.
- **Interview use:** Consensus comparisons and careful discussion of quorum safety.

### The Chubby Lock Service for Loosely-Coupled Distributed Systems

- **Link:** [Chubby](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/)
- **Status:** Required, Stage 2.
- **Problem:** Reliable coarse-grained coordination and small metadata storage.
- **Prerequisites:** Consensus, leases, and sessions.
- **Understand:** Lock service API, sessions, caching, events, sequencers, availability choices, and client behavior.
- **Does not claim:** High-throughput data storage or that a lease alone prevents stale actions.
- **Interview use:** Service discovery, configuration, leader election, locks, leases, and fencing.

### Spanner: Google's Globally-Distributed Database

- **Link:** [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
- **Status:** Required, late Stage 2 and revisit in Stage 4.
- **Problem:** Global, synchronously replicated SQL transactions with externally consistent commits.
- **Prerequisites:** Consensus, two-phase commit, MVCC, transactions, and clock uncertainty.
- **Understand:** Paxos groups, directory placement, distributed transactions, TrueTime, commit timestamps, commit wait, and historical reads.
- **Does not claim:** Ordinary clocks make transactions safe, zero latency, or synchronous replication alone provides external consistency.
- **Interview use:** Global SQL, multi-region transactions, read freshness, clocks, and data placement.

## 3. Logs and Stream Processing

### Kafka: A Distributed Messaging System for Log Processing

- **Link:** [Kafka books and papers](https://kafka.apache.org/books-and-papers); then [current Kafka documentation](https://kafka.apache.org/documentation/)
- **Status:** Required, Stage 3.
- **Problem:** High-throughput distributed log ingestion and consumption at LinkedIn.
- **Prerequisites:** Logs, partitioning, replication, and batching.
- **Understand:** Partitions, sequential I/O, batching, offsets, consumer groups, retention, and replay.
- **Does not claim:** Current Kafka behavior. Modern Kafka Raft (KRaft) metadata, producer idempotence, transactions, consumer protocols, and replication must be checked against current versioned documentation.
- **Interview use:** Event backbones, change-data capture, queue versus log choices, replay, and ordering scope.

### MillWheel: Fault-Tolerant Stream Processing at Internet Scale

- **Link:** [MillWheel](https://research.google/pubs/millwheel-fault-tolerant-stream-processing-at-internet-scale/)
- **Status:** Required, Stage 3.
- **Problem:** Low-latency stateful processing of unbounded data with fault tolerance.
- **Prerequisites:** Kafka-like logs, checkpoints, event time, and distributed state.
- **Understand:** Per-key computation, persistent state, low watermarks, timers, checkpointing, and duplicate handling.
- **Does not claim:** Exactly one arbitrary external business effect or that event time is necessary for every pipeline.
- **Interview use:** Windowed aggregation, late data, state recovery, and stream guarantees.

## 4. Serving, Caching, and Observability

### Scaling Memcache at Facebook

- **Link:** [Scaling Memcache at Facebook](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala)
- **Status:** Required when P3 is selected; otherwise targeted, Stages 2 and 3.
- **Problem:** A distributed cache for extremely read-heavy, globally operated Facebook workloads.
- **Prerequisites:** Cache-aside, sharding, replication, and invalidation.
- **Understand:** Client routing, leases, stampede protection, invalidation, regional pools, cold clusters, and failure behavior.
- **Does not claim:** Strong consistency or that its topology fits low-scale services.
- **Interview use:** Distributed cache, news feed, hot keys, invalidation races, and cache failure.

### Dapper, a Large-Scale Distributed Systems Tracing Infrastructure

- **Link:** [Dapper](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)
- **Status:** Required, Stage 3.
- **Problem:** Low-overhead tracing across Google's large, multilingual service graph.
- **Prerequisites:** Remote procedure calls (RPCs), context propagation, and sampling.
- **Understand:** Trace and span identifiers, common-library instrumentation, sampling, collection, and analysis tools.
- **Does not claim:** Complete unsampled auditing or replacement of metrics, logs, and profiling.
- **Interview use:** Observability, fanout debugging, latency attribution, and platform adoption.

### Monarch: Google's Planet-Scale In-Memory Time Series Database

- **Link:** [Monarch](https://research.google/pubs/monarch-googles-planet-scale-in-memory-time-series-database/)
- **Status:** Targeted, Stage 3 or observability roles.
- **Problem:** Regional ingestion and global querying for high-scale monitoring data.
- **Prerequisites:** Time-series models, replication, aggregation, and multi-tenancy.
- **Understand:** Regional zones, ingestion, in-memory storage, query federation, configuration, and availability.
- **Does not claim:** General transactional storage or unlimited cardinality at no cost.
- **Interview use:** Metrics platforms, regionalization, control planes, retention, and query fanout.

### The Tail at Scale

- **Link:** [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/)
- **Status:** Required, Stage 3.
- **Problem:** Rare component delays become common at large fanout.
- **Prerequisites:** Latency distributions, parallel requests, and overload.
- **Understand:** Tail amplification, hedged requests, tied requests, micro-partitioning, and cancellation.
- **Does not claim:** Hedging is free or safe under saturation and non-idempotent effects.
- **Interview use:** Search, feeds, scatter-gather, replicas, and latency SLOs.

## 5. Targeted Production Systems

### Finding a Needle in Haystack: Facebook's Photo Storage

- **Link:** [Haystack](https://www.usenix.org/conference/osdi10/finding-needle-haystack-facebooks-photo-storage)
- **Status:** Targeted, Stage 2.
- **Problem:** Efficient serving of billions of photos while reducing filesystem metadata operations.
- **Prerequisites:** Object storage, indexes, caching, and replication.
- **Understand:** Append-only stores, compact indexes, CDN interaction, replication, and recovery.
- **Does not claim:** A general object-store API or optimality for large mutable objects.
- **Interview use:** Photo storage, small blobs, metadata amplification, and immutable media.

### TAO: Facebook's Distributed Data Store for the Social Graph

- **Link:** [TAO](https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson)
- **Status:** Targeted, Stage 2.
- **Problem:** High-volume object and association reads for the social graph.
- **Prerequisites:** MySQL sharding, caching, graph access patterns, and eventual consistency.
- **Understand:** Workload-specific API, leaders and followers, caching tiers, invalidation, and geographic operation.
- **Does not claim:** General graph traversal, pattern matching, or strong consistency for every read.
- **Interview use:** Feeds, social graphs, workload-shaped APIs, and selective consistency.

### Large-Scale Cluster Management at Google with Borg

- **Link:** [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)
- **Status:** Targeted, Stage 4.
- **Problem:** Scheduling and operating mixed production and batch workloads across large clusters.
- **Prerequisites:** Containers, scheduling, quotas, and failure domains.
- **Understand:** Declarative jobs, admission, placement, overcommitment, isolation, rescheduling, and operational lessons.
- **Does not claim:** The Kubernetes API or that maximum utilization is the only objective.
- **Interview use:** Schedulers, compute platforms, multi-tenancy, capacity, and control loops.

### Zanzibar: Google's Consistent, Global Authorization System

- **Link:** [Zanzibar](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/)
- **Status:** Targeted, Stage 4.
- **Problem:** Global relationship-based authorization with consistent decisions at high scale.
- **Prerequisites:** Graph relations, caching, snapshots, causality, and global storage.
- **Understand:** Relation tuples, namespaces, checks, expansion, zookies, consistency, and caching.
- **Does not claim:** Authentication, identity proofing, policy governance, or a complete security program.
- **Interview use:** Sharing, authorization, stale-permission prevention, and globally consistent metadata.
