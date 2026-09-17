# Primary Paper Path

Read papers in prerequisite order. For each paper, write the workload, failure model, central mechanism, guarantees, non-goals, and one interview decision it changes. **Required** papers are assigned by a curriculum stage. **Targeted** papers are optional unless a role or prompt calls for them.

## 1. Foundations of Data and Computation

### The Google File System

- **Link:** [The Google File System](https://storage.googleapis.com/gweb-research2023-media/pubtools/4446.pdf)
- **Status:** Required, Stage 2.
- **Problem:** Large distributed files on failure-prone commodity machines for Google's workloads.
- **Prerequisites:** Files, replication, checksums, and remote procedure calls (RPCs).
- **Understand:** Large chunks, centralized metadata, leases, replication, record append, and recovery assumptions.
- **Does not claim:** General Portable Operating System Interface (POSIX) filesystem semantics or that one metadata server is a universal architecture.
- **Interview use:** Object storage, metadata versus data planes, large-file ingestion, and append workloads.

### MapReduce: Simplified Data Processing on Large Clusters

- **Link:** [MapReduce](https://storage.googleapis.com/gweb-research2023-media/pubtools/4449.pdf)
- **Status:** Required, Stage 3.
- **Problem:** Reliable parallel batch computation across large clusters.
- **Prerequisites:** GFS, partitioning, and sorting.
- **Understand:** Map and reduce contracts, shuffle, locality, scheduling, retries, backup tasks, and deterministic recomputation.
- **Does not claim:** Low-latency stream processing, arbitrary iterative efficiency, or inherent exactness for external effects.
- **Interview use:** Backfills, aggregation, indexing, batch recovery, and stragglers.

### Bigtable: A Distributed Storage System for Structured Data

- **Link:** [Bigtable](https://storage.googleapis.com/gweb-research2023-media/pubtools/4443.pdf)
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

- **Link:** [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
- **Status:** Targeted, Stage 2.
- **Problem:** Agreement despite crash failures and delayed or lost messages.
- **Prerequisites:** Quorums and state-machine replication.
- **Understand:** Proposers, acceptors, learners, ballot numbers, quorum intersection, and safety.
- **Does not claim:** A complete production protocol for persistence, reconfiguration, snapshots, or clients.
- **Interview use:** Consensus comparisons and careful discussion of quorum safety.

### The Chubby Lock Service for Loosely-Coupled Distributed Systems

- **Link:** [Chubby](https://storage.googleapis.com/gweb-research2023-media/pubtools/4444.pdf)
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

- **Link:** [Kafka](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf); then [current Kafka documentation](https://kafka.apache.org/documentation/)
- **Status:** Required, Stage 3.
- **Problem:** High-throughput distributed log ingestion and consumption at LinkedIn.
- **Prerequisites:** Logs, partitioning, replication, and batching.
- **Understand:** Partitions, sequential I/O, batching, offsets, consumer groups, retention, and replay.
- **Does not claim:** Current Kafka behavior. Modern Kafka Raft (KRaft) metadata, producer idempotence, transactions, consumer protocols, and replication must be checked against current versioned documentation.
- **Interview use:** Event backbones, change-data capture, queue versus log choices, replay, and ordering scope.

### MillWheel: Fault-Tolerant Stream Processing at Internet Scale

- **Link:** [MillWheel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41378.pdf)
- **Status:** Required, Stage 3.
- **Problem:** Low-latency stateful processing of unbounded data with fault tolerance.
- **Prerequisites:** Kafka-like logs, checkpoints, event time, and distributed state.
- **Understand:** Per-key computation, persistent state, low watermarks, timers, checkpointing, and duplicate handling.
- **Does not claim:** Exactly one arbitrary external business effect or that event time is necessary for every pipeline.
- **Interview use:** Windowed aggregation, late data, state recovery, and stream guarantees.

## 4. Serving, Caching, and Observability

### Scaling Memcache at Facebook

- **Link:** [Scaling Memcache at Facebook](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf)
- **Status:** Required when P3 is selected; otherwise targeted, Stages 2 and 3.
- **Problem:** A distributed cache for extremely read-heavy, globally operated Facebook workloads.
- **Prerequisites:** Cache-aside, sharding, replication, and invalidation.
- **Understand:** Client routing, leases, stampede protection, invalidation, regional pools, cold clusters, and failure behavior.
- **Does not claim:** Strong consistency or that its topology fits low-scale services.
- **Interview use:** Distributed cache, news feed, hot keys, invalidation races, and cache failure.

### Dapper, a Large-Scale Distributed Systems Tracing Infrastructure

- **Link:** [Dapper](https://research.google.com/archive/papers/dapper-2010-1.pdf)
- **Status:** Required, Stage 3.
- **Problem:** Low-overhead tracing across Google's large, multilingual service graph.
- **Prerequisites:** Remote procedure calls (RPCs), context propagation, and sampling.
- **Understand:** Trace and span identifiers, common-library instrumentation, sampling, collection, and analysis tools.
- **Does not claim:** Complete unsampled auditing or replacement of metrics, logs, and profiling.
- **Interview use:** Observability, fanout debugging, latency attribution, and platform adoption.

### Monarch: Google's Planet-Scale In-Memory Time Series Database

- **Link:** [Monarch](https://storage.googleapis.com/gweb-research2023-media/pubtools/6348.pdf)
- **Status:** Targeted, Stage 3 or observability roles.
- **Problem:** Regional ingestion and global querying for high-scale monitoring data.
- **Prerequisites:** Time-series models, replication, aggregation, and multi-tenancy.
- **Understand:** Regional zones, ingestion, in-memory storage, query federation, configuration, and availability.
- **Does not claim:** General transactional storage or unlimited cardinality at no cost.
- **Interview use:** Metrics platforms, regionalization, control planes, retention, and query fanout.

### The Tail at Scale

- **Link:** [The Tail at Scale publication page](https://research.google/pubs/the-tail-at-scale/)
- **Status:** Required, Stage 3.
- **Problem:** Rare component delays become common at large fanout.
- **Prerequisites:** Latency distributions, parallel requests, and overload.
- **Understand:** Tail amplification, hedged requests, tied requests, micro-partitioning, and cancellation.
- **Does not claim:** Hedging is free or safe under saturation and non-idempotent effects.
- **Interview use:** Search, feeds, scatter-gather, replicas, and latency SLOs.

## 5. Targeted Production Systems

### Finding a Needle in Haystack: Facebook's Photo Storage

- **Link:** [Haystack](https://www.usenix.org/legacy/events/osdi10/tech/full_papers/Beaver.pdf)
- **Status:** Targeted, Stage 2.
- **Problem:** Efficient serving of billions of photos while reducing filesystem metadata operations.
- **Prerequisites:** Object storage, indexes, caching, and replication.
- **Understand:** Append-only stores, compact indexes, CDN interaction, replication, and recovery.
- **Does not claim:** A general object-store API or optimality for large mutable objects.
- **Interview use:** Photo storage, small blobs, metadata amplification, and immutable media.

### TAO: Facebook's Distributed Data Store for the Social Graph

- **Link:** [TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)
- **Status:** Targeted, Stage 2.
- **Problem:** High-volume object and association reads for the social graph.
- **Prerequisites:** MySQL sharding, caching, graph access patterns, and eventual consistency.
- **Understand:** Workload-specific API, leaders and followers, caching tiers, invalidation, and geographic operation.
- **Does not claim:** General graph traversal, pattern matching, or strong consistency for every read.
- **Interview use:** Feeds, social graphs, workload-shaped APIs, and selective consistency.

### Large-Scale Cluster Management at Google with Borg

- **Link:** [Borg](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf)
- **Status:** Targeted, Stage 4.
- **Problem:** Scheduling and operating mixed production and batch workloads across large clusters.
- **Prerequisites:** Containers, scheduling, quotas, and failure domains.
- **Understand:** Declarative jobs, admission, placement, overcommitment, isolation, rescheduling, and operational lessons.
- **Does not claim:** The Kubernetes API or that maximum utilization is the only objective.
- **Interview use:** Schedulers, compute platforms, multi-tenancy, capacity, and control loops.

### Zanzibar: Google's Consistent, Global Authorization System

- **Link:** [Zanzibar](https://storage.googleapis.com/gweb-research2023-media/pubtools/5068.pdf)
- **Status:** Targeted, Stage 4.
- **Problem:** Global relationship-based authorization with consistent decisions at high scale.
- **Prerequisites:** Graph relations, caching, snapshots, causality, and global storage.
- **Understand:** Relation tuples, namespaces, checks, expansion, zookies, consistency, and caching.
- **Does not claim:** Authentication, identity proofing, policy governance, or a complete security program.
- **Interview use:** Sharing, authorization, stale-permission prevention, and globally consistent metadata.

## 6. Targeted Data and Processing Branches

These papers from the broader roadmap are valuable for particular roles. They are not additional
required stages.

### Dremel: Interactive Analysis of Web-Scale Datasets

- **Link:** [Dremel](https://storage.googleapis.com/gweb-research2023-media/pubtools/3293.pdf)
- **Status:** Targeted, Stage 3 for analytics and data-platform roles.
- **Problem:** Interactive aggregation over nested, web-scale datasets.
- **Prerequisites:** MapReduce, columnar storage, query planning, and trees.
- **Understand:** Nested columnar representation, repetition and definition levels, column pruning,
  multilevel serving trees, and aggregation.
- **Does not claim:** To describe all current BigQuery behavior or general online transaction
  processing.
- **Interview use:** Data warehouses, OLTP versus OLAP, scan cost, nested schemas, and distributed
  query execution.

BigQuery is a current product descended from Dremel ideas, not the title of a single foundational
paper. Pair Dremel with the [current BigQuery documentation](https://cloud.google.com/bigquery/docs/introduction)
when product behavior matters.

### Resilient Distributed Datasets

- **Link:** [Resilient Distributed Datasets](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)
- **Status:** Targeted, Stage 3 for data-platform roles.
- **Problem:** Efficient reuse and fault recovery for iterative and interactive cluster computation.
- **Prerequisites:** MapReduce, partitions, directed acyclic graphs, and deterministic transformations.
- **Understand:** Lineage, narrow and wide dependencies, recomputation, persistence, and shuffle
  boundaries.
- **Does not claim:** To describe current Spark SQL, Structured Streaming, or every modern Spark
  execution detail.
- **Interview use:** Iterative computation, lineage versus replication, caching intermediate state,
  and recovery cost.

### ZooKeeper: Wait-Free Coordination for Internet-Scale Systems

- **Link:** [ZooKeeper](https://www.usenix.org/legacy/events/atc10/tech/full_papers/Hunt.pdf)
- **Status:** Targeted comparison after Chubby, Stage 2.
- **Problem:** A replicated coordination service with an API suitable for higher-level recipes.
- **Prerequisites:** Consensus, sessions, linearizability, and watches.
- **Understand:** Ordered updates, sessions, ephemeral nodes, watches, client caching, and the gap
  between primitives and correct recipes.
- **Does not claim:** That every operation is wait-free for every client or that a coordination
  primitive makes a distributed lock safe without correct client behavior.
- **Interview use:** Discovery, membership, election, configuration, and coordination API design.

### Large-Scale Incremental Processing Using Distributed Transactions and Notifications

- **Link:** [Percolator](https://research.google.com/pubs/archive/36726.pdf)
- **Status:** Targeted, Stage 3 for storage, search, and incremental-processing roles.
- **Problem:** Incrementally update a large search index without rerunning full batch jobs.
- **Prerequisites:** Bigtable, multiversion concurrency control, snapshot isolation, and MapReduce.
- **Understand:** Distributed transactions over Bigtable, locks, timestamps, notifications,
  observers, and incremental recomputation.
- **Does not claim:** Serializable isolation for arbitrary workloads or a general stream processor.
- **Interview use:** Incremental indexing, materialized views, change propagation, and transaction
  recovery.

### Apache Flink: Stream and Batch Processing in a Single Engine

- **Link:** [Flink](https://asterios.katsifodimos.com/assets/publications/flink-deb.pdf)
- **Status:** Targeted, Stage 3 for streaming roles.
- **Problem:** Execute batch and low-latency stateful stream processing through one dataflow engine.
- **Prerequisites:** Kafka, MillWheel, distributed snapshots, and event time.
- **Understand:** Dataflow execution, state, checkpoints, watermarks, backpressure, and rescaling.
- **Does not claim:** Current Flink product semantics. Pair it with the
  [current Flink documentation](https://nightlies.apache.org/flink/flink-docs-stable/).
- **Interview use:** Stateful streams, recovery, savepoints, rescaling, and batch-stream unification.

## 7. Deliberate Roadmap Omissions

The source roadmap also lists HDFS, Pregel, Photon, Mesa, and Earlybird. They remain optional because
the required path already establishes their prerequisite design families:

- HDFS largely extends the GFS branch for Hadoop-specific roles.
- Pregel is useful for offline graph-processing roles after MapReduce.
- Photon adds geographically distributed continuous joins after MillWheel.
- Mesa adds geo-replicated analytical aggregation after Dremel.
- Earlybird adds mutable inverted indexes and real-time search after indexing and fanout basics.

Use [Stephen Holiday's notes](https://stephenholiday.com/notes/) to discover these branches, then
follow the primary paper rather than relying on the note or its historical outbound link.
