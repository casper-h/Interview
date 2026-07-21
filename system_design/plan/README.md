# System Design Reading Plan

This is a staged reading plan, not a calendar. The four parts below are a sensible ordering of the
material, not a four-month deadline: roughly three to four months of focused, interleaved effort is
a reasonable target for most people, but let a part run longer if it needs to and don't treat any
date as a gate. Progress through the parts using the exit conditions in the [schedule](../../schedule/README.md), not a
calendar.

Each part pairs **required** interview-relevant reading with a **deep reasoning companion**
(the matching part of the [deep reasoning companion](./companion.md)) of integration questions and worked answers:
that companion is the highest-value part of this track, so treat the Q&A as active practice rather
than skimming it.
The **supplement** material below (the long white-paper tail and the optional textbooks) is
**optional depth**: valuable if you lack production distributed-systems experience, but not something
to grind through by default.

## Reading Priority

Time is the binding constraint, so the order below puts the highest-return material first. The
[concepts-by-level reference](./concepts_by_level.md) maps system design concepts to hiring bands and
informs this priority.

- **The concepts spine (read for depth).** *Designing Data-Intensive Applications* (DDIA) is the
  center of gravity. *Database Internals* by Alex Petrov is core, not optional, at this band: it is
  where the storage-engine and distributed-transaction internals live. The MIT 6.824 and CMU 15-445
  lecture series are primary sources, watched alongside the reading rather than deferred.
- **Depth for the Staff edge.** *Specifying Systems* and the TLA+ material for reasoning about
  correctness formally, and jepsen.io for how consistency claims fail under real partitions. These
  separate a strong answer from a competent one when a deep dive turns to correctness.
- **Applied warm-up, not the spine.** *System Design Interview* Volumes 1 and 2 (Alex Xu) are useful
  for problem shape and vocabulary early on, and Volume 2 has a few worthwhile worked designs. Treat
  them as a warm-up for the practice designs, not as core reading. The chapter pointers to them below
  are optional and can be skipped once you are fluent in the framework.
- **Supporting material.** *Understanding Distributed Systems* gives the concept scaffolding, and
  Donne Martin's System Design Primer is a useful applied reference. Both are supporting material,
  not the primary spine.

**A note on the chapter and lecture references.** The paper links and the CMU 15-445 lecture topics
below are verified. The DDIA and Site Reliability Engineering chapter numbers were corrected against
the published tables of contents. The MIT 6.824 lecture topics follow the current published schedule
at https://pdos.csail.mit.edu/6.824/schedule.html, whose numbering shifts year to year, so confirm
the numbers against the live schedule. The *Database Internals* and *Understanding Distributed
Systems* chapter mappings could not be confirmed against a public table of contents; verify them
against your copy.

**Minimum viable pass.** If you are short on time, the following is enough to be ready for a Senior
loop at most product companies: DDIA's interview-relevant chapters, the eight core white papers in
the [white paper core set](../white_paper.md#core-set-required), the
[building blocks](../building_blocks.md) component library, and roughly a dozen practice
designs done out loud against the clock. Beyond that, *Database Internals* and the lecture series are
the first things to add for the upper-Senior and Staff range; the optional white papers are the last.
Read them when a mock surfaces a specific gap, not as a prerequisite.

---

## Part 1: Core Foundations + DDIA

**Goal:** Build strong mental models of distributed system fundamentals. Focus on architecture patterns, storage, replication, and trade-offs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 1-6: Data Models, Storage Engines, Encoding, Replication, Partitioning
  - Focus on trade-offs (e.g., LSM vs B-Trees, Consistency vs Availability)
- **Understanding Distributed Systems**
  - Ch. 1-5: Core Distributed Concepts, Nodes, Networks, Failure Models
- **System Design Interview (Vol. 1)**
  - Ch. 1-3: Scale from Zero to Millions, Estimation, Design Frameworks
  - Ch. 4-5: Rate Limiter, Consistent Hashing
- **System Design Interview (Vol. 2)**
  - Ch. 4: Distributed Message Queue
  - Ch. 9: S3-like Object Storage
- **System Design Primer**
  - Sections: Performance vs Scalability, Latency vs Throughput, CAP Theorem, Availability Patterns, DNS, CDN, Load Balancing
  - Use as conceptual reference for foundational trade-offs

**Lectures (primary spine)** and **supplementary papers (optional depth)**
- MIT 6.824 Lectures 1-3: Introductions, RPC and Threads, GFS. Primary source, watch alongside the reading.
- CMU 15-445 Lectures 1-5: Relational Model, Storage I & II, Compression. Primary source, watch alongside the reading.
- Optional systems theory papers: Harvest and Yield, On Designing and Deploying Internet-Scale Services, The Tail at Scale, Data on the Outside versus Data on the Inside. See the [white paper catalog](../white_paper.md) optional tier under Systems Theory.

**Practice**
1. URL Shortener: Hashing, Storage Model, Replication
2. News Feed: Fan-Out, Read vs Write Optimization
3. Distributed Cache: Consistency, Eviction, TTL

**White Papers**
- GFS from the [core set](../white_paper.md#core-set-required)
- Optional systems theory papers: CAP Twelve Years Later, Why Distributed Computing, Notes on Distributed Systems for Young Bloods, Time Clocks and the Ordering of Events in a Distributed System. See the [white paper catalog](../white_paper.md) optional tier under Systems Theory.

### Knowledge Integration Questions
1. When would I prefer consistency over availability in a design?
2. How does partition tolerance change system architecture when scaling globally?
3. What patterns recur across distributed cache, rate limiter, and key-value store designs?
4. How does latency amplification occur in layered systems, and how can it be mitigated?
5. How does the CAP theorem shape replication strategies in practice?

<details>
<summary>Expand for Sample Reasoning</summary>

1. Consistency is prioritized when correctness of state outweighs latency, such as in payment systems or metadata updates that require accuracy even at higher response times.
2. Partition tolerance changes system architecture when scaling globally by forcing asynchronous replication, leader election, or eventual consistency to maintain operation under network splits.
3. Distributed cache, rate limiter, and key-value store designs all share the same fundamental distributed storage abstractions such as hashing, replication, and consistency mechanisms, differing mainly in their performance focus and operational guarantees.
4. Latency amplification occurs when dependent RPC chains or sequential service calls propagate small delays across the system; it can be mitigated through parallelization, batching, and caching.
5. The CAP theorem defines the balance between consistency and availability. CP systems such as Spanner favor consistency under partition, while AP systems such as Dynamo favor availability with eventual consistency.
</details>

---

## Part 2: Deep Internals + Database Systems

**Goal:** Move from architecture reasoning to internal design: storage, consensus, replication, and consistency models.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 7-9: Transactions, The Trouble with Distributed Systems, Consistency and Consensus
- **Understanding Distributed Systems**
  - Ch. 6-10: Replication, Partitioning, Consensus, Consistency
- **System Design Interview (Vol. 1)**
  - Ch. 6-9: Key-Value Store, Unique ID Generator, URL Shortener, Web Crawler
- **System Design Interview (Vol. 2)**
  - Ch. 1-3: Proximity Service, Nearby Friends, Google Maps
  - Ch. 9: S3-like Object Storage
- **System Design Primer**
  - Sections: SQL vs NoSQL, RDBMS, Sharding, Replication, Caching (cache-aside, write-through, write-behind)
  - Use as a reference for practical scaling and storage trade-off summaries, not a linear read

**Primary spine (this part), plus optional textbooks**
- **Database Internals**: Part I (Ch. 1-5, Storage Engines); Part II (Ch. 6-9, Distributed Systems).
  Core at the upper-Senior and Staff band, not optional: this is the storage-engine and
  distributed-systems internals reading DDIA only summarizes.
- CMU 15-445 Lectures 3-10: Storage, Compression, Memory Management, Indexes & Filters. Primary source.
- MIT 6.824 Lectures 4 and 6-7: Paxos, then Fault Tolerance with Raft. Primary source. Lecture numbering shifts year to year; confirm against the live schedule.
- **Database System Concepts** (Ch. 12-16: Storage, Indexing, Concurrency Control): a university
  textbook that largely overlaps DDIA and Database Internals; optional, for the academic treatment.
- Optional systems theory papers: Consistency Availability and Convergence, Life Beyond Distributed Transactions, Eventually Consistent - Revisited, Avoiding Two-Phase Commit, The Log. See the [white paper catalog](../white_paper.md) optional tier under Systems Theory.

**Practice**
1. Kafka-like Queue: Log Segmentation, Offsets, Consumer Groups
2. Dropbox / Google Drive: Metadata vs Blob Storage
3. Slack / WhatsApp: Message Ordering, Delivery Guarantees

**White Papers**
- **Consensus papers** (Raft, Paxos Made Simple, Part-Time Parliament, FLP impossibility) from the [core and optional sets](../white_paper.md). Read Raft and Paxos Made Simple alongside this part; the others are optional depth.
- **Database papers** (Bigtable, Cassandra, Dynamo, Spanner from the [core set](../white_paper.md#core-set-required); F1, Mesa, PNUTS, TAO from the [optional tier](../white_paper.md#optional-deep-dive)). Read the core four alongside this part; the optional papers are for targeted use.

### Knowledge Integration Questions
1. Why do distributed logs unify both messaging and database design?
2. How do replication strategies differ between Cassandra, Dynamo, and Spanner?
3. When is synchronous replication necessary despite performance costs?
4. How does Raft simplify reasoning about consensus compared to Paxos?
5. Why is the "log as a system backbone" a recurring idea?

<details>
<summary>Expand for Sample Reasoning</summary>

1. Logs unify both messaging and database systems by preserving event ordering and enabling deterministic replay for recovery and replication, making them the backbone for durability and consistency.
2. Replication strategies differ by emphasis. Cassandra uses quorum-based eventual consistency, Dynamo allows tunable quorum models, and Spanner enforces external consistency through synchronized clocks and true-time guarantees.
3. Synchronous replication is required for correctness-critical data such as financial transactions or configuration metadata, where data loss is unacceptable even if latency increases.
4. Raft simplifies consensus reasoning compared to Paxos by using a single elected leader and an explicit log replication model that makes system state transitions easier to reason about.
5. The log abstraction recurs because it represents ordered, append-only data that can support messaging, recovery, replication, and state reconstruction through a single model of event sequencing.
</details>

---

## Part 3: Distributed Computation + Reliability

**Goal:** Understand computation frameworks, fault tolerance, and how systems maintain reliability at scale.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 10-11: Batch and Stream Processing
- **Site Reliability Engineering (SRE)**
  - Ch. 3-4: Embracing Risk, Service Level Objectives; Ch. 6: Monitoring Distributed Systems; Ch. 13-15: Emergency Response, Managing Incidents, Postmortem Culture
- **Understanding Distributed Systems**
  - Ch. 11-13: Fault Tolerance, Backpressure, Orchestration
- **System Design Interview (Vol. 1)**
  - Ch. 10-12: Notification, News Feed, Chat
- **System Design Interview (Vol. 2)**
  - Ch. 5-8: Metrics Monitoring, Ad Aggregation, Hotel Reservation, Distributed Email Service
- **System Design Primer**
  - Sections: Asynchronism, Message Queues, Microservices, Service Discovery, Reverse Proxy

**Lectures (primary spine)** and **supplementary papers (optional depth)**
- MIT 6.824: MapReduce (Lab 1) and the fault-tolerance and distributed-transaction lectures. Primary source.
- CMU 15-445 Lectures 11-16: Sorting, Joins, Execution, Concurrency. Primary source.
- Optional papers: Megastore, Principles of Robust Timing over the Internet. See the [white paper catalog](../white_paper.md) optional tier under Database and Systems Theory.

**Practice**
1. Real-Time Analytics: Stream Processing
2. Recommendation System: Batch + Stream Integration
3. Messaging System: SLA, Fault Recovery

**White Papers**
- **Distributed Computation papers** (MapReduce from the [core set](../white_paper.md#core-set-required); Dremel, FlumeJava, Hive, Percolator, Tenzing from the [optional tier](../white_paper.md#optional-deep-dive)). Read MapReduce alongside this part; the others are optional depth.
- **Streaming papers** (Kafka from the [core set](../white_paper.md#core-set-required); MillWheel, Photon from the [optional tier](../white_paper.md#optional-deep-dive)). Read Kafka alongside this part; the others are optional depth.
- **Experimentation paper** (Online Controlled Experiments from the [optional tier](../white_paper.md#optional-deep-dive)).

### Knowledge Integration Questions
1. How do batch and stream processing models differ in their fault tolerance mechanisms?
2. What are common bottlenecks in large-scale data pipelines?
3. How do you measure and manage backpressure in distributed stream systems?
4. What trade-offs exist between throughput, latency, and accuracy in analytics systems?
5. How do you integrate batch, real-time, and serving layers coherently?

<details>
<summary>Expand for Sample Reasoning</summary>

1. Batch systems like MapReduce favor completeness and fault tolerance, while streaming systems like MillWheel prioritize low latency through checkpointing and replay-based recovery mechanisms.
2. Common bottlenecks in distributed pipelines include network shuffles, disk I/O, skewed data partitions, and serialization overhead that limits parallel throughput.
3. Backpressure arises when downstream operators process data slower than producers. Techniques such as dynamic scaling, rate limiting, and adaptive buffering help maintain throughput without overload.
4. Throughput, latency, and accuracy trade-offs vary by workload. Monitoring favors low latency and approximate correctness, while financial computation emphasizes durability and accuracy.
5. Integration of batch, real-time, and serving layers requires consistent data freshness guarantees and alignment of replay boundaries, often achieved through unified stream processing or materialized view updates.
</details>

---

## Part 4: Advanced Systems + Hiring Readiness

**Goal:** Integrate theoretical knowledge and develop reasoning clarity under interview conditions.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 12: The Future of Data Systems (dataflow, integration, and derived data)
- **Understanding Distributed Systems**
  - Ch. 14-15: Complex Systems, Performance Tuning
- **System Design Interview (Vol. 1)**
  - Ch. 13-15: Search Autocomplete, YouTube, Google Drive
- **System Design Interview (Vol. 2)**
  - Ch. 10-13: Real-Time Leaderboard, Payment System, Digital Wallet, Stock Exchange
- **Site Reliability Engineering (SRE)**
  - Ch. 7-9: Automation, Release Engineering, Simplicity; and the Part III production-practices chapters (Ch. 10 onward)

**Primary spine (this part), plus optional case studies**
- **Database Internals** Ch. 10-12: Distributed Transactions, Coordination, Recovery. Core at this
  band for reasoning about commit protocols and recovery.
- MIT 6.824 Lectures 11-12: Distributed Transactions and Spanner. Primary source.
- CMU 15-445 Lectures 20-24: Logging, Recovery, Distributed Databases. Primary source.
- Meta TAO, Uber Michelangelo, Netflix TechBlog
- Optional papers: Building on Quicksand, Distributed Computing Economics. See the [white paper catalog](../white_paper.md) optional tier under Systems Theory.

**Practice**
1. YouTube / Netflix: Content Delivery
2. Uber / Lyft: Distributed Coordination
3. Twitter Timeline: Fan-Out, Caching
4. Graph Analytics: Large-Scale Data Pipelines

**White Papers**

All papers below are from the [optional deep-dive tier](../white_paper.md#optional-deep-dive). Read them when a specific team or mock feedback calls for one of these topics.

- **Graph papers:** GraphChi, PowerGraph, Pregel
- **Peer-to-Peer papers:** Chord
- **Search papers:** Earlybird, Unicorn, Google Cluster Architecture
- **Storage papers:** Erasure Coding, Facebook Photo Storage, RCFile, XORing Elephants

### Knowledge Integration Questions
1. How do real-world systems trade off latency, durability, and cost at scale?
2. What operational principles separate "good designs" from production-ready systems?
3. How do graph or analytics workloads shift storage and partitioning strategies?
4. How can chaos engineering validate distributed resilience?
5. What does "graceful degradation" look like in global architectures?

<details>
<summary>Expand for Sample Reasoning</summary>

1. Large-scale systems balance latency, durability, and cost through multi-tiered storage, asynchronous replication, and caching hierarchies that optimize access frequency and reliability.
2. Production-grade systems distinguish themselves through observability, failure isolation, and controlled degradation of services rather than complete shutdowns.
3. Graph and analytics workloads affect partitioning and storage differently. Graphs require minimizing cross-partition edges, while analytics systems prioritize balanced distribution and predictable query parallelism.
4. Chaos engineering validates resilience by injecting controlled failures such as node termination or network latency and measuring recovery speed against defined service objectives.
5. Graceful degradation allows partial functionality to continue during failure, such as serving cached data when the database is unavailable or restricting writes while allowing reads.
</details>

---

## More Reading

Additional consensus and peer-to-peer papers (The Byzantine Generals Problem, Unreliable Failure Detectors for Reliable Distributed Systems, Implementing Fault-Tolerant Services Using the State Machine Approach, Mencius, SWIM, Pastry) are available in the [white paper catalog](../white_paper.md) optional tier under Consensus and Peer-to-Peer. These are for targeted use when a specific team or interest calls for them.

---

## Integration Projects (Optional)

These are optional synthesis projects: deeper learning exercises, not interview prep, so prioritize
practice designs first and reach for one of these only if you want to consolidate a part's reading
before moving on. Pair each with the part whose material it exercises.

| Alongside | Project | Focus |
|-------|----------|-------|
| **Part 1** | Distributed Cache | Consistency, replication, read/write trade-offs |
| **Part 2** | Distributed Message Queue | Log segmentation, offset management, backpressure |
| **Part 3** | Real-Time Analytics Pipeline | Stream vs batch unification, latency management |
| **Part 4** | Global Content Platform | Geo-replication, failure isolation, scalability |

Each project should include one page outlining assumptions, design, trade-offs, and one major bottleneck analysis.

---

## Production Realism Exercises

Integrate "real-world failure" thought experiments weekly:
- Node crash during leader election
- Network partition between regions
- Message duplication in async queues
- Database hot partition from uneven key distribution
- Backpressure in streaming ingestion
- Cross-region replication lag under heavy writes

Record how each failure propagates and how the system design can mitigate or recover from it.

---

## Final Phase: Interview Refinement

The final phase should train clarity, composure, and structured articulation. This corresponds to
Phases 3 and 4 of the [schedule](../../schedule/README.md) and the cadence in [mocks](../../schedule/mocks.md); the progression below
is the system-design-specific view of that same sprint, not a separate schedule.

### Progression
- **First:** 60-min design mocks, focused on structure and completeness.
- **Then:** add peer pushback and justify trade-offs and assumptions.
- **Then:** timed 30-min rounds emphasizing concise reasoning.
- **Finally:** a simulated panel with back-to-back design plus follow-up questions.

### Refinement Goals
- Speak through reasoning transitions clearly ("Because we need consistency, we'll...")
- Lead the discussion top-down - define requirements before architecture
- Quantify design decisions (latency, QPS, replication factors)
- Close with operational and monitoring considerations

Recording each session is critical for pacing, clarity, and confidence calibration.

---

## Outcome

The goal is architectural fluency. Your architectural reasoning should be fluent, quantitative, and production-aware. You should be able to:
- Analyze trade-offs confidently under ambiguity
- Design end-to-end distributed systems coherently
- Explain failure handling and scalability with operational insight
- Communicate with precision, composure, and structured depth

Progress is measured by clarity of thought and design precision, not by volume of materials completed.