# 4-Month Senior System Design Deep Reasoning Companion  
### Month 2 — Deep Internals + Database Systems

**Goal:** Understand internal mechanics - storage, replication, consensus, and distributed database design. Focus on detailed trade-offs and comparative reasoning.

---

## Section 1 — Storage Engines Deep Dive (Database Internals Ch.1–5, CMU 15-445 L3–5, Bigtable)

### Core Questions

1. Compare **B-tree vs LSM-tree storage** for high-ingest, read-heavy, and mixed workloads.  
2. How does **Bigtable** use SSTables and memtables to manage write amplification?  
3. What are the advantages and limitations of **columnar storage** in distributed databases?  
4. Why is **compression** crucial in storage engines, and how do you balance CPU vs I/O trade-offs?  
5. How does **tablet splitting** in Bigtable affect load balancing and latency?

<details>
<summary>Answers</summary>

1. **B-tree vs LSM-tree:**  
   - B-tree: balanced tree, good for random reads, moderate writes, predictable latency.  
   - LSM-tree: append-only memtables, periodic compaction; optimized for high write throughput but increased read amplification and compaction overhead.  
   Mixed workloads may require hybrid approaches or read-optimized LSM variants.

2. **Bigtable SSTables & Memtables:**  
   Memtables accumulate writes in memory, flushed to immutable SSTables on disk. Compaction merges SSTables, reducing read amplification and disk fragmentation. This design balances write throughput, read latency, and storage efficiency.

3. **Columnar storage:**  
   - Advantages: compresses repeated column values, enables vectorized scans, reduces I/O for analytics queries.  
   - Limitations: poor random write performance; full-row reconstruction may be expensive. Suitable for OLAP rather than OLTP.

4. **Compression trade-offs:**  
   - CPU-intensive compression reduces I/O but increases CPU load.  
   - Lighter compression favors low-latency reads but may increase disk usage. Optimal balance depends on workload, disk speed, and CPU availability.

5. **Tablet splitting:**  
   - Tablets (Bigtable partitions) split when size thresholds exceeded.  
   - Pros: avoids hotspots, improves parallelism.  
   - Cons: introduces metadata overhead and transient imbalances; careful monitoring needed to prevent cascading splits.

</details>

**Reflection → Add personal observations about LSM/B-tree trade-offs.**

---

## Section 2 — Replication & Consensus (Understanding Distributed Systems Ch.6–10, Raft, Paxos)

### Core Questions

1. Compare **primary-backup**, **leaderless**, and **quorum-based replication** models.  
2. What are the fundamental challenges in achieving **consensus** in unreliable networks?  
3. How does **Raft** simplify understanding compared to **Paxos**?  
4. Describe how **leader election** and **log replication** ensure safety.  
5. When is **synchronous replication** necessary despite latency costs?

<details>
<summary>Answers</summary>

1. **Replication models:**  
   - Primary-backup: leader coordinates writes; simple but single-leader bottleneck.  
   - Leaderless: clients write to multiple replicas; higher availability but complex reconciliation.  
   - Quorum-based: requires a majority of replicas for read/write; balances availability and consistency.

2. **Consensus challenges:**  
   - Network partitions, message reordering, node crashes, and asynchrony make reaching agreement nontrivial.  
   - Fundamental impossibility: FLP theorem; solutions rely on timeouts, retries, and leader election.

3. **Raft vs Paxos:**  
   - Raft introduces explicit leader, terms, and log index tracking, making state transitions easier to understand and reason about.  
   - Paxos is minimal and mathematically elegant but harder to implement and explain in real systems.

4. **Leader election & log replication:**  
   - Leader elected per term; only leader appends to log.  
   - Followers replicate entries; commit only after majority acknowledgment ensures safety.  
   - Ensures that all committed entries are durable even if leader crashes.

5. **Synchronous replication:**  
   - Necessary when correctness is critical (e.g., financial transactions, metadata).  
   - Guarantees that writes are acknowledged only after durable replication to majority, preventing data loss at the cost of increased latency.

</details>

---

## Section 3 — Real System Comparisons (Bigtable, Dynamo, Cassandra, Spanner, F1)

### Comparative Questions

1. How do **Bigtable** and **Dynamo** differ in storage and consistency models?  
2. Compare **Cassandra** and **Dynamo** quorum strategies; how does each handle failures?  
3. How does **Spanner** achieve global consistency using TrueTime?  
4. In which scenarios would you prefer **Dynamo/Cassandra** over **Spanner**?  
5. Discuss the trade-offs between **external consistency** and **latency/cost** at scale.

<details>
<summary>Answers</summary>

1. **Bigtable vs Dynamo:**  
   - Bigtable: structured column-family store, master-coordinated tablets, strong consistency per tablet, optimized for read-heavy analytical workloads.  
   - Dynamo: key-value store, leaderless quorum replication, eventual consistency, designed for high availability under partitions.

2. **Cassandra vs Dynamo:**  
   - Both implement quorum reads/writes; Cassandra allows tunable R/W quorum sizes, while Dynamo often relies on configurable consistency levels and hinted handoff.  
   - Failure handling: Dynamo uses vector clocks and reconciliation; Cassandra uses anti-entropy repair and hinted handoff to maintain eventual convergence.

3. **Spanner TrueTime:**  
   - Uses globally synchronized clocks with bounded uncertainty to order transactions externally.  
   - Guarantees linearizability across data centers without sacrificing high availability.

4. **Preference scenarios:**  
   - Dynamo/Cassandra: high availability, geographically distributed workloads, flexible consistency.  
   - Spanner: strict correctness required (banking, critical metadata), willing to pay latency and cost for global consistency.

5. **Trade-offs:**  
   - External consistency (Spanner) → higher latency, clock infrastructure cost, and operational complexity.  
   - Eventual consistency → lower latency, simpler infrastructure, but client must handle anomalies.

</details>

---

## Section 4 — Logs & Messaging (Kafka, Dropbox, Slack, LinkedIn “Log” paper)

### Core Questions

1. Why are **logs** a unifying abstraction across messaging and storage?  
2. How does Kafka manage **offsets, partitions, and consumer groups** to scale?  
3. What is **backpressure**, and how do distributed queues handle it?  
4. How does a **log-based design** aid recovery and replication in Dropbox/Google Drive?  
5. Discuss the trade-offs between **batch** vs **streaming consumption** of logs.

<details>
<summary>Answers</summary>

1. **Logs as unifying abstraction:**  
   - Serialize all updates in an append-only, ordered stream.  
   - Supports replay, replication, recovery, and deterministic reconstruction.

2. **Kafka internals:**  
   - Topics partitioned; each partition is ordered log.  
   - Consumers track offsets; consumer groups allow parallel processing with load balancing.  
   - Guarantees ordering per partition; scaling achieved by partition count.

3. **Backpressure:**  
   - Occurs when consumers lag producers.  
   - Mitigated via rate limiting, bounded queues, flow-control, or dynamic scaling.

4. **Dropbox/Drive recovery:**  
   - Metadata log allows deterministic reconstruction of state after crash or partition.  
   - Enables delta sync, incremental updates, and eventual consistency.

5. **Batch vs streaming:**  
   - Batch: higher throughput, easier error recovery, higher latency.  
   - Streaming: low latency, incremental processing, complex checkpointing and fault-tolerance.

</details>

---

## Section 5 — Practice Designs

### Kafka-like Queue
1. How would you design **log segmentation and offset management** for millions of messages/sec?  
2. How does **consumer group rebalancing** affect message ordering and delivery guarantees?  
3. How would you handle **message duplication** and exactly-once semantics?

<details>
<summary>Answers</summary>

1. Partition logs into segments; maintain per-partition indexes for offsets. Segment size balanced to avoid excessive disk seeks but allow compaction and retention policies.  
2. Consumer rebalancing pauses consumption temporarily; use stable hashing to preserve partition ownership; ordering maintained per partition.  
3. Deduplication via unique message IDs, idempotent producers, or transactional writes ensures exactly-once delivery.

</details>

### Dropbox/Google Drive Metadata + Blob
1. How would you separate **metadata** and **blob storage**?  
2. How does replication differ between small metadata and large blob data?  
3. What consistency guarantees are necessary for collaborative edits?

<details>
<summary>Answers</summary>

1. Metadata: key-value store with strong consistency; blobs: distributed object store with eventual consistency and chunked storage.  
2. Metadata replicated synchronously to prevent conflicts; blobs replicated asynchronously due to size.  
3. Collaborative edits require causal or optimistic concurrency; conflict resolution handled by versioning or CRDTs.

</details>

### Slack/WhatsApp Messaging
1. How do you maintain **message ordering** across distributed partitions?  
2. How do you provide **delivery guarantees** under network partitions?  
3. What are trade-offs between **fan-out-on-write vs fan-out-on-read** in messaging?

<details>
<summary>Answers</summary>

1. Sequence numbers per conversation; partitions can be mapped by conversation ID to maintain local order.  
2. Asynchronous replication with ack tracking; retries with idempotency; eventual consistency acceptable for chat.  
3. Fan-out-on-write: low read latency, high write cost. Fan-out-on-read: low write cost, higher read latency. Hybrid strategies balance performance and freshness.

</details>

---

## Section 6 — Integration & Reflection Prompts

- Why are **logs central to both database internals and distributed messaging**?  
- How do replication strategies differ for high-availability vs strongly consistent systems?  
- How does **consensus algorithm choice** impact latency, throughput, and recovery complexity?  
- Identify recurring design patterns across **queue, KV store, and metadata services**.  
- How would you handle **global hotspots** in partitioned systems?

<details>
<summary>Sample Answers</summary>

- Logs unify persistence, replication, and recovery across messaging and storage.  
- CP systems: synchronous replication, leader coordination; AP systems: asynchronous, eventual convergence.  
- Consensus: Raft favors clarity and implementation simplicity; Paxos minimizes assumptions but harder to reason about.  
- Recurring patterns: partitioning via hashing, replication for durability, log-based recovery, idempotency for safe retries.  
- Global hotspots: partition splitting, sharding, caching, geo-partitioned load balancing, or key salting.

</details>

---
