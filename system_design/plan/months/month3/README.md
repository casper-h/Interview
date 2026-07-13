# 4-Month Senior System Design Deep Reasoning Companion  
### Month 3 — Distributed Computation + Reliability

**Goal:** Understand computation frameworks, fault tolerance, and operational reliability in large-scale systems. Focus on batch/stream processing, monitoring, and fault-tolerant design.

---

## Section 1 — Batch vs Stream Processing (DDIA Ch.7–9, MIT 6.824 L7–10)

### Core Questions

1. What are the key differences between **batch** and **stream processing** in terms of latency, throughput, and fault tolerance?  
2. How do **checkpointing** and **replay** mechanisms differ between the two models?  
3. How do frameworks like **MapReduce, FlumeJava, Dremel** handle large-scale parallel computation?  
4. How do you design for **exactly-once semantics** in streaming pipelines?  
5. How do **stateful operators** manage recovery in distributed streams?

<details>
<summary>Answers</summary>

1. **Batch vs Stream:**  
   - Batch: high throughput, higher latency, deterministic, good for full dataset analysis.  
   - Stream: low latency, incremental updates, complex state management, requires checkpointing and replay.  

2. **Checkpointing & Replay:**  
   - Batch: failure recovery involves re-running the job; stateless transformations make replay simple.  
   - Stream: requires periodic snapshots (checkpointing) and event replay to recover stateful operators.

3. **Framework handling:**  
   - MapReduce: splits tasks into map/reduce jobs, relies on distributed file system (HDFS) for inputs/outputs.  
   - FlumeJava: abstracts batch jobs with pipelines, optimizes execution graph.  
   - Dremel: columnar storage + tree aggregation for interactive queries; trades high parallelism for low-latency analytics.

4. **Exactly-once semantics:**  
   - Use idempotent operations, transactional writes, or unique message IDs.  
   - Checkpoint offsets and use replay to ensure no message processed twice or missed.

5. **Stateful recovery:**  
   - Operators checkpoint state regularly; after failure, replay events from last checkpoint to reconstruct state.  
   - Requires deterministic computation to guarantee correctness.

</details>

---

## Section 2 — Fault Tolerance & Reliability (Understanding Distributed Systems Ch.11–13, SRE Ch.3–5)

### Core Questions

1. What are the key concepts of **SLIs, SLOs, and SLAs**, and how do they guide system reliability?  
2. How do **redundancy, replication, and failover** reduce downtime?  
3. What is the role of **backpressure** in preventing cascading failures?  
4. How do large-scale systems implement **graceful degradation** under load or partial failure?  
5. How should monitoring and alerting be designed to prevent **alert fatigue** yet detect critical issues?

<details>
<summary>Answers</summary>

1. **SLIs/SLOs/SLAs:**  
   - SLI: measured indicator of service health (e.g., latency, error rate).  
   - SLO: target value for SLI over time (e.g., 99.9% success).  
   - SLA: contractual obligation to clients; violations incur penalties.  
   - Together they prioritize reliability engineering and incident response.

2. **Redundancy & failover:**  
   - Replicate data/services across nodes or regions; automatic failover maintains availability.  
   - Must consider split-brain, leader election, and consistency impacts.

3. **Backpressure:**  
   - Prevents downstream services from being overwhelmed.  
   - Achieved via throttling, bounded queues, or producer coordination to stabilize system throughput.

4. **Graceful degradation:**  
   - Partial service continues under failure: cached reads, restricted writes, reduced functionality.  
   - Improves user experience compared to full service outage.

5. **Monitoring design:**  
   - Use tiered alerts (critical, warning, info).  
   - Combine automated anomaly detection with human review to avoid alert fatigue while catching failures.

</details>

---

## Section 3 — Real-World System Comparisons (Megastore, Percolator, Tenzing)

### Core Questions

1. How do **Megastore** and **Percolator** provide transactional guarantees at scale?  
2. How does **Tenzing** optimize interactive SQL queries on large distributed datasets?  
3. Compare **batch vs incremental updates** for analytical systems.  
4. How do these systems balance **latency, consistency, and throughput**?  
5. What design principles can be applied to modern data pipelines from these case studies?

<details>
<summary>Answers</summary>

1. **Megastore/Percolator:**  
   - Megastore: hierarchical two-phase commit + Paxos for global transactions.  
   - Percolator: transactional updates on top of Bigtable using distributed locks and timestamps for consistency.

2. **Tenzing:**  
   - Distributed SQL query engine; uses columnar scans and tree aggregation for low-latency analytics.  
   - Optimizes for large-scale joins and minimal data shuffling.

3. **Batch vs incremental:**  
   - Batch: high throughput, deterministic, slow to react.  
   - Incremental/stream: low-latency updates, can tolerate partial failures but requires careful state management.

4. **Balancing LCT (Latency, Consistency, Throughput):**  
   - Trade-offs depend on SLA targets and workload type; partial replication or async updates improve throughput but affect freshness.

5. **Design principles:**  
   - Leverage logs for durability, decouple storage and computation, use timestamp-based coordination, and prioritize idempotency and deterministic operations.

</details>

---

## Section 4 — Messaging & Stream Systems (Kafka, MillWheel, Photon)

### Core Questions

1. How do **stream processing frameworks** differ in their fault tolerance models?  
2. What is **exactly-once processing**, and why is it challenging?  
3. How does **windowing** affect streaming computation and state recovery?  
4. How do large systems handle **out-of-order messages**?  
5. How can **backpressure** be applied in multi-stage pipelines?

<details>
<summary>Answers</summary>

1. **Fault tolerance models:**  
   - Kafka: persistent logs, replayable offsets, consumer-managed progress.  
   - MillWheel: checkpointed operator state with deterministic replay.  
   - Photon: continuous state streaming with deterministic recovery.

2. **Exactly-once:**  
   - Challenging due to distributed failures and retries.  
   - Requires atomic writes, idempotent transformations, and careful checkpointing.

3. **Windowing:**  
   - Defines computation intervals; affects timing of aggregation and output.  
   - Impacts checkpoint frequency and state size, influencing recovery speed.

4. **Out-of-order messages:**  
   - Use event-time ordering with buffering and watermarks to emit results in logical sequence.  
   - Delayed events may be late but can be corrected with window updates.

5. **Backpressure in pipelines:**  
   - Throttle upstream producers when downstream operators lag.  
   - Dynamic buffering and flow-control ensure system stability under variable load.

</details>

---

## Section 5 — Practice Designs

### Real-Time Analytics Pipeline
1. How would you combine **batch and streaming layers** for near-real-time analytics?  
2. How do you handle **state consistency** between batch and stream layers?  
3. What are potential bottlenecks and mitigation strategies?

<details>
<summary>Answers</summary>

1. Use Lambda architecture: batch layer for complete view, speed layer for incremental updates, serving layer to merge results.  
2. Synchronize using timestamps, materialized views, or event ordering; replay streams to reconcile discrepancies.  
3. Bottlenecks: network shuffle, skewed partitions, disk I/O, serialization. Mitigate with partitioning, parallelism, compression, and caching.

</details>

### Recommendation System
1. How do you integrate **real-time events** with precomputed models?  
2. How would you handle **cold-start users or items**?  
3. What trade-offs exist between freshness and computation cost?

<details>
<summary>Answers</summary>

1. Stream updates (clicks, interactions) feed feature stores; batch-trained models provide baseline recommendations.  
2. Cold-start: use content-based or demographic heuristics; gradually refine with user activity.  
3. Freshness: frequent updates reduce staleness but increase resource usage; balance depends on SLA.

</details>

### Messaging System
1. How do you guarantee **at-least-once vs exactly-once delivery**?  
2. How do you mitigate **cascading failures** under peak load?  
3. How would you scale partitions and consumers dynamically?

<details>
<summary>Answers</summary>

1. At-least-once: retry messages; idempotent consumers handle duplicates.  
   Exactly-once: transactional writes or deduplication logic.  
2. Cascading failures mitigated via backpressure, circuit breakers, throttling, and isolation.  
3. Repartition logs/topics, rebalance consumers, and shard load dynamically with minimal downtime.

</details>

---

## Section 6 — Integration & Reflection Prompts

- How do batch and stream pipelines **complement each other** in modern systems?  
- Which **failure modes dominate latency vs throughput trade-offs**?  
- How can **SLIs/SLOs** be operationalized in real-time pipelines?  
- Identify patterns across **messaging, analytics, and batch systems** that recur in fault-tolerant design.

<details>
<summary>Sample Answers</summary>

- Batch: complete, slower; stream: incremental, fast. Integration allows freshness without losing durability.  
- Latency failures: network, disk, skewed partitions; throughput: backpressure, serialization.  
- SLIs/SLOs: measure processing latency, throughput, error rates; alert on deviations.  
- Patterns: logs as backbone, partitioning for parallelism, idempotent operations, checkpointing for state recovery, bounded queues for flow control.

</details>

---
