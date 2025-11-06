# 4-Month Senior System Design Deep Reasoning Companion  
### Month 1 — Core Foundations + DDIA

**Goal:** Build first-principles understanding of distributed systems, storage, replication, and trade-offs.  
Use these questions to deepen conceptual reasoning and validate your reading insights.

---

## Section 1 — Data Models & Storage Engines (DDIA Ch. 1–3, CMU 15-445 L1-5)

### Core Questions

1. What fundamental design trade-offs exist between **LSM-trees** and **B-trees**?  
2. Why do modern systems often prefer **append-only logs** even when random writes are possible?  
3. How does **storage layout** (row vs column) influence compression, query efficiency, and update cost?  
4. When should **in-memory indexes** (e.g., skip lists, hash maps) supplement on-disk structures?  
5. Why do write-ahead logs remain the foundation of durability, and what are their scaling limits?

<details>
<summary>Answers</summary>

1. **LSM-trees vs B-trees:**  
   LSM-trees optimize write throughput via sequential appends and background merges (compaction), trading off read amplification and higher write-path latency during compactions. B-trees favor read efficiency and predictable latency but suffer under heavy random writes. LSMs dominate in high-ingest NoSQL systems (Cassandra, RocksDB), while B-trees remain standard in OLTP RDBMS due to stable read latency.

2. **Append-only logs:**  
   They simplify concurrency, avoid in-place mutation, and provide clear recovery semantics. Sequential I/O is faster on both HDDs and SSDs, and logs double as replication and recovery mechanisms. Their drawback is compaction/garbage collection overhead and unbounded growth without maintenance.

3. **Row vs Column:**  
   Row stores group complete tuples—best for OLTP workloads with frequent small writes and point queries. Column stores cluster values per column, enabling aggressive compression and vectorized scans, ideal for analytics. The choice dictates cache locality, compression ratio, and update cost.

4. **In-memory indexes:**  
   Used when access patterns exhibit strong temporal locality (hot keys). They act as read caches or skip levels for cold data, reducing disk seeks. However, they require coherence with persistent state and impose memory pressure in high-cardinality workloads.

5. **Write-ahead logs:**  
   WAL ensures atomicity and durability: every change is persisted before data pages update. Scaling limits appear when the log becomes contention bottleneck or when sync latency dominates throughput; sharded or per-partition logs mitigate this.

</details>

**Reflection → Add your own notes here.**

---

## Section 2 — Replication & Consistency (DDIA Ch. 5, Understanding Distributed Systems Ch. 6–7)

### Core Questions

1. Explain **leader-based** vs **leaderless** replication and when to prefer each.  
2. What are the key roles of **quorums** in read/write coordination?  
3. How does **replication lag** manifest and why is it critical for client-visible correctness?  
4. When does **eventual consistency** become unacceptable?  
5. Compare **strong**, **causal**, and **eventual** consistency models in practice.

<details>
<summary>Answers</summary>

1. **Leader-based:** one replica accepts writes and propagates to followers—simple conflict resolution but potential single-point bottleneck. **Leaderless:** clients write to multiple replicas; conflicts resolved via version vectors or last-write-wins, improving availability but increasing reconciliation complexity.

2. **Quorums:** ensure overlapping read/write sets so at least one replica always has the latest write. Common choice N=3, W=2, R=2. Adjusting R/W tunes latency vs consistency.

3. **Replication lag:** occurs when async followers trail the leader, leading to stale reads or read-after-write anomalies. Monitoring replica lag and using read-your-writes consistency per session mitigate it.

4. **Eventual consistency unacceptable:** in financial, security, or metadata systems where invariants (e.g., “only one active session”) must hold immediately. Acceptable in social feeds or counters.

5. **Consistency spectrum:**  
   - *Strong:* all reads reflect latest write (Spanner, linearizable).  
   - *Causal:* respects cause-before-effect ordering, lighter coordination (Cassandra + client-side tracking).  
   - *Eventual:* only guarantees convergence, cheapest coordination.

</details>

**Reflection:** *Write about a case from your work where replication lag caused subtle bugs.*

---

## Section 3 — Partitioning & Scalability (DDIA Ch. 6, System Design Primer)

### Core Questions

1. What motivates **data partitioning**, and what new problems does it introduce?  
2. How does **consistent hashing** mitigate rebalancing overhead?  
3. What is a **hot partition**, and how can you detect and mitigate it?  
4. Compare **range**, **hash**, and **composite** partitioning.  
5. How do global services manage **cross-region replication** without high tail latency?

<details>
<summary>Answers</summary>

1. Partitioning spreads data and load across machines for scalability and fault isolation. It introduces data locality issues, skew, and coordination complexity for multi-partition operations.

2. Consistent hashing minimizes remapping when nodes join/leave by mapping both data and nodes to a hash ring. Only adjacent key ranges move, avoiding full rebalancing.

3. Hot partition: a small subset receives disproportionate traffic (e.g., celebrity ID). Detected via uneven metrics; mitigated by key randomization, caching, or hierarchical partitioning.

4. Range partitioning preserves ordering—great for range scans but prone to skew. Hash partitioning balances load but breaks order. Composite (hash + range) blends both.

5. Cross-region replication uses async pipelines with eventual consistency or geo-distributed consensus (Spanner’s TrueTime). Latency is mitigated through locality-aware reads and multi-tier caches (CDNs, edge stores).

</details>

---

## Section 4 — Trade-Off Frameworks & CAP Theorem

### Core Questions

1. Interpret the **CAP theorem** in modern systems: is it binary or continuous?  
2. Provide real examples of **CP** and **AP** systems and their implications.  
3. How do systems actually recover after **network partitions**?  
4. What does **PACELC** add to CAP’s reasoning?  
5. Why is partition tolerance non-negotiable in real networks?

<details>
<summary>Answers</summary>

1. CAP is not binary—systems operate along a spectrum. During partition, one must trade off between immediate consistency and availability, but outside partitions both can coexist.

2. **CP:** Spanner, Zookeeper—favor correctness; writes may block under partition. **AP:** Dynamo, Cassandra—remain available but allow temporary divergence.

3. Recovery: nodes reconcile via anti-entropy protocols, vector-clock conflict resolution, or leader re-election. Data convergence may lag behind network restoration.

4. **PACELC:** extends CAP—if no partition (Else), choose between Latency and Consistency. E.g., Dynamo = PA/EL; Spanner = PC/EC.

5. Partition tolerance mandatory because network failures are inevitable at scale (fiber cuts, routing blackholes). Systems must assume partitions occur.

</details>

---

## Section 5 — Distributed Systems in Practice (GFS, Brewer, Tail at Scale, Data on Outside)

### Core Questions

1. Summarize the key **architectural insight of GFS** and how it shaped Bigtable.  
2. Why does **“The Tail at Scale”** matter for user-facing systems?  
3. Explain **data on the outside vs inside** and its impact on microservice design.  
4. What did **Brewer’s Harvest & Yield** paper propose beyond CAP?  
5. How does **network unreliability** manifest at scale, and how do large systems hide it?

<details>
<summary>Answers</summary>

1. **GFS:** simplified distributed file system with large immutable files, master metadata, and chunkserver replication. Inspired Bigtable’s tablet abstraction (GFS → Bigtable → Spanner lineage).

2. **Tail at Scale:** small latency outliers across thousands of RPCs compound to large tail latencies. Mitigation: hedged requests, load balancing, replication, and latency-aware scheduling.

3. **Data on the Outside vs Inside:** argues for explicit contracts between services (APIs, schemas) and separation of persistent data boundaries. Encourages “bounded contexts” and prevents accidental coupling.

4. **Harvest & Yield:** formalized the idea that partial results (yield) are better than full outage (harvest loss). Motivated graceful degradation and partial availability patterns.

5. **Network unreliability:** packet loss, reordering, transient failures. Large systems use retries with exponential backoff, idempotent operations, quorum reads/writes, and health-based routing.

</details>

---

## Section 6 — Practice Designs (URL Shortener, News Feed, Distributed Cache)

### Core Questions

#### URL Shortener
1. What storage design ensures unique, short IDs without collisions at scale?  
2. How would you replicate short link metadata globally?  
3. Discuss consistency vs latency in redirect serving.

<details>
<summary>Answers</summary>

1. Use base-62 encoding of incremental or Snowflake-style IDs; ensure atomicity via DB auto-increment or ID service. Collision avoidance via centralized allocator or sharded ID ranges.  
2. Replicate via leader-follower or eventually consistent KV store; DNS or CDN caches absorb read load.  
3. Prioritize availability and latency; eventual consistency is fine since stale redirect metadata rarely critical.

</details>

#### News Feed
1. Compare **fan-out-on-write** vs **fan-out-on-read**.  
2. How to ensure ordering guarantees under high fan-out?

<details>
<summary>Answers</summary>

1. Fan-out-on-write pushes updates to followers—low read latency, high write cost. Fan-out-on-read pulls on demand—cheap writes, expensive reads. Hybrid models combine both.  
2. Maintain per-user sequence numbers or vector timestamps; use message queues with ordering keys.

</details>

#### Distributed Cache
1. Discuss cache invalidation and consistency challenges.  
2. When would you choose write-through vs write-back?  
3. How does TTL affect correctness and cost?

<details>
<summary>Answers</summary>

1. Invalidation hard because source of truth may change before TTL expiry; strategies include versioning or pub/sub invalidation.  
2. Write-through keeps cache consistent but adds latency; write-back improves write latency but risks data loss on crash.  
3. TTL balances freshness and resource cost—short TTLs improve correctness but increase load.

</details>

---

## Section 7 — Integration & Reasoning Prompts

- When would you sacrifice **availability** for **correctness**?  
- Which failure mode dominates each design?  
- What latency sources dominate end-to-end response time?  
- How would your system behave under a **partial network failure**?  
- Identify three recurring patterns between **cache, KV-store, and rate-limiter** architectures.

<details>
<summary>Sample Answers</summary>

- **Consistency over availability:** payments, authorization, metadata synchronization.  
- **Dominant failure:** network partitions, leader election stalls, or hot partitions.  
- **Latency sources:** serialization, disk sync, cross-region hops, dependent RPCs.  
- **Partial failure:** fallback to degraded mode, retries with idempotency keys.  
- **Recurring patterns:** replication for reliability, hashing for partitioning, caching for latency mitigation.

</details>

---
