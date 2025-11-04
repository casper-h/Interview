# 4-Month Senior System Design Plan (Nov → Feb)

---

## Month 1 — November: Core Foundations + DDIA

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

**Supplement / Lectures**
- MIT 6.824 Lectures 1-3: Introductions, RPC and Threads, GFS
- CMU 15-445 Lectures 1-5: Relational Model, Storage I & II, Compression
- [Harvest, Yield, and Scalable Tolerant Systems](https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf)
- [On Designing and Deploying Internet-Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf)
- [The Tail at Scale](https://dl.acm.org/doi/pdf/10.1145/2408776.2408794)
- [Data on the Outside versus Data on the Inside](https://www.cidrdb.org/cidr2005/papers/P12.pdf)

**Practice**
1. URL Shortener: Hashing, Storage Model, Replication
2. News Feed: Fan-Out, Read vs Write Optimization
3. Distributed Cache: Consistency, Eviction, TTL

**White Papers**
- [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [CAP Twelve Years Later: How the "Rules" Have Changed ](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [Why Distributed Computing?](https://www.artima.com/weblogs/viewpost.jsp?thread=4247)
- [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
- [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)

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

## Month 2 — December: Deep Internals + Database Systems

**Goal:** Move from architecture reasoning to internal design: storage, consensus, replication, and consistency models.

**Primary Reading**
- **Database Internals**
  - Part I (Ch. 1-5): Storage Engines
  - Part II (Ch. 6-9): Distributed Systems
- **Understanding Distributed Systems**
  - Ch. 6-10: Replication, Partitioning, Consensus, Consistency
- **System Design Interview (Vol. 1)**
  - Ch. 6-9: Key-Value Store, Unique ID Generator, URL Shortener, Web Crawler
- **System Design Interview (Vol. 2)**
  - Ch. 1-3: Proximity Service, Nearby Friends, Google Maps
  - Ch. 9: S3-like Object Storage
- **Database System Concepts**
  - Ch. 12-16: Storage, Indexing, Concurrency Control
- **System Design Primer**
  - Sections: SQL vs NoSQL, RDBMS, Sharding, Replication, Caching (cache-aside, write-through, write-behind)
  - Use for practical scaling and storage trade-off summaries

**Supplement / Lectures**
- CMU 15-445 Lectures 3-10: Storage, Compression, Memory Management, Indexes & Filters
- MIT 6.824 Lectures 4-6: Primary-Backup, Fault Tolerance, Raft
- [Consistency, Availability, and Convergence](https://www.cs.cornell.edu/lorenzo/papers/cac-tr.pdf)
- [Life Beyond Distributed Transactions](https://queue.acm.org/detail.cfm?id=3025012)
- [Eventually Consistent - Revisited](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
- [Avoiding Two-Phase Commit](https://web.archive.org/web/20180821165044/http://www.addsimplicity.com/adding_simplicity_an_engi/2006/12/avoiding_two_ph.html)
- [The Log: What Every Software Engineer Should Know About Real-time Data’s Unifying Abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)

**Practice**
1. Kafka-like Queue: Log Segmentation, Offsets, Consumer Groups
2. Dropbox / Google Drive: Metadata vs Blob Storage
3. Slack / WhatsApp: Message Ordering, Delivery Guarantees

**White Papers**
- **Consensus**
  - [Raft](https://raft.github.io/raft.pdf)
  - [The Part-Time Parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)
  - [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
  - [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)
- **Database**
  - [Bigtable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
  - [Cassandra](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf)
  - [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
  - [F1](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41344.pdf)
  - [Mesa](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42851.pdf)
  - [PNUTS](https://people.mpi-sws.org/~druschel/courses/ds/papers/cooper-pnuts.pdf)
  - [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
  - [TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)

### Knowledge Integration Questions
1. Why do distributed logs unify both messaging and database design?
2. How do replication strategies differ between Cassandra, Dynamo, and Spanner?
3. When is synchronous replication necessary despite performance costs?
4. How does Raft simplify reasoning about consensus compared to Paxos?
5. Why is the “log as a system backbone” a recurring idea?

<details>
<summary>Expand for Sample Reasoning</summary>

1. Logs unify both messaging and database systems by preserving event ordering and enabling deterministic replay for recovery and replication, making them the backbone for durability and consistency.

2. Replication strategies differ by emphasis. Cassandra uses quorum-based eventual consistency, Dynamo allows tunable quorum models, and Spanner enforces external consistency through synchronized clocks and true-time guarantees.

3. Synchronous replication is required for correctness-critical data such as financial transactions or configuration metadata, where data loss is unacceptable even if latency increases.

4. Raft simplifies consensus reasoning compared to Paxos by using a single elected leader and an explicit log replication model that makes system state transitions easier to reason about.

5. The log abstraction recurs because it represents ordered, append-only data that can support messaging, recovery, replication, and state reconstruction through a single model of event sequencing.
</details>

---

## Month 3 — January: Distributed Computation + Reliability

**Goal:** Understand computation frameworks, fault tolerance, and how systems maintain reliability at scale.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 7-9: Batch and Stream Processing
- **Site Reliability Engineering (SRE)**
  - Ch. 3-5: SLIs, SLOs, Monitoring, Incident Response
- **Understanding Distributed Systems**
  - Ch. 11-13: Fault Tolerance, Backpressure, Orchestration
- **System Design Interview (Vol. 1)**
  - Ch. 10-12: Notification, News Feed, Chat
- **System Design Interview (Vol. 2)**
  - Ch. 5-8: Metrics Monitoring, Ad Aggregation, Hotel Reservation, Distributed Email Service
- **System Design Primer**
  - Sections: Asynchronism, Message Queues, Microservices, Service Discovery, Reverse Proxy

**Supplement / Lectures**
- MIT 6.824 Lectures 7-10: MapReduce, Fault-Tolerant Services, Transactions, Dremel
- CMU 15-445 Lectures 11-16: Sorting, Joins, Execution, Concurrency
- [Megastore](https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf)
- [Principles of Robust Timing over the Internet](https://dl.acm.org/doi/pdf/10.1145/1735223.1735241)

**Practice**
1. Real-Time Analytics: Stream Processing
2. Recommendation System: Batch + Stream Integration
3. Messaging System: SLA, Fault Recovery

**White Papers**
- **Distributed Computation**
  - [Dremel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36632.pdf)
  - [FlumeJava](https://pages.cs.wisc.edu/~akella/CS838/F12/838-CloudPapers/FlumeJava.pdf)
  - [Hive](https://www.vldb.org/pvldb/vol2/vldb09-938.pdf)
  - [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
  - [Percolator](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Peng.pdf)
  - [Tenzing](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37200.pdf)
- **Streaming**
  - [Kafka](https://cs.uwaterloo.ca/~ssalihog/courses/papers/netdb11-final12.pdf)
  - [MillWheel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41378.pdf)
  - [Photon](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41318.pdf)
- **Experimentation**
  - [Online Controlled Experiments](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf)

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

## Month 4 — February: Advanced Systems + Senior Hiring Readiness

**Goal:** Integrate theoretical knowledge and develop reasoning clarity under interview conditions.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 10-12: Dataflow, Real-Time Systems
- **Database Internals**
  - Ch. 10-12: Distributed Transactions, Coordination, Recovery
- **Understanding Distributed Systems**
  - Ch. 14-15: Complex Systems, Performance Tuning
- **System Design Interview (Vol. 1)**
  - Ch. 13-15: Search Autocomplete, YouTube, Google Drive
- **System Design Interview (Vol. 2)**
  - Ch. 10-13: Real-Time Leaderboard, Payment System, Digital Wallet, Stock Exchange
- **Site Reliability Engineering (SRE)**
  - Ch. 6-10: Production Practices, Scalability, and Architecture Reliability

**Supplement / Case Studies**
- MIT 6.824 Lectures 11-12: Fault-Tolerant Key-Value Stores
- CMU 15-445 Lectures 20-24: Logging, Recovery, Distributed Databases
- Meta TAO, Uber Michelangelo, Netflix TechBlog
- [Building on Quicksand](https://arxiv.org/pdf/0909.1788)
- [Distributed Computing Economics](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2003-24.pdf)

**Practice**
1. YouTube / Netflix: Content Delivery
2. Uber / Lyft: Distributed Coordination
3. Twitter Timeline: Fan-Out, Caching
4. Graph Analytics: Large-Scale Data Pipelines

**White Papers**
- **Graph**
  - [GraphChi](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-126.pdf)
  - [PowerGraph](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf)
  - [Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf)
- **Peer-to-Peer**
  - [Chord](https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf)
- **Search**
  - [Earlybird](https://cs.uwaterloo.ca/~jimmylin/publications/Busch_etal_ICDE2012.pdf)
  - [Unicorn](https://www.vldb.org/pvldb/vol6/p1150-curtiss.pdf)
  - [Google Cluster Architecture](https://static.googleusercontent.com/media/research.google.com/en//archive/googlecluster-ieee.pdf)
- **Storage**
  - [Erasure Coding](https://www.usenix.org/system/files/conference/atc12/atc12-final181_0.pdf)
  - [Facebook Photo Storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf)
  - [RCFile](https://scispace.com/pdf/rcfile-a-fast-and-space-efficient-data-placement-structure-2kq37wcjl0.pdf)
  - [XORing Elephants](https://arxiv.org/pdf/1301.3791)

### Knowledge Integration Questions
1. How do real-world systems trade off latency, durability, and cost at scale?
2. What operational principles separate “good designs” from production-ready systems?
3. How do graph or analytics workloads shift storage and partitioning strategies?
4. How can chaos engineering validate distributed resilience?
5. What does “graceful degradation” look like in global architectures?

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

- [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [Unreliable Failure Detectors for Reliable Distributed Systems](https://dl.acm.org/doi/pdf/10.1145/226643.226647)
- [Implementing Fault-Tolerant Services Using the State Machine Approach](https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf)
- [Mencius](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/mao/mao.pdf)
- [SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf)
- [Pastry](https://www.cs.cornell.edu/courses/cs6452/2012sp/papers/pastry.pdf)

---

## Integration Projects (Optional)

Each month, select one synthesis project to consolidate reading and reasoning.

| Month | Project | Focus |
|-------|----------|-------|
| **November** | Distributed Cache | Consistency, replication, read/write trade-offs |
| **December** | Distributed Message Queue | Log segmentation, offset management, backpressure |
| **January** | Real-Time Analytics Pipeline | Stream vs batch unification, latency management |
| **February** | Global Content Platform | Geo-replication, failure isolation, scalability |

Each project should include one page outlining assumptions, design, trade-offs, and one major bottleneck analysis.

---

## Production Realism Exercises

Integrate “real-world failure” thought experiments weekly:
- Node crash during leader election
- Network partition between regions
- Message duplication in async queues
- Database hot partition from uneven key distribution
- Backpressure in streaming ingestion
- Cross-region replication lag under heavy writes

Record how each failure propagates and how the system design can mitigate or recover from it.

---

## Final Phase: Interview Refinement

The final phase should train clarity, composure, and structured articulation.

### Structure
- **Week 1:** 60-min design mocks &rarr; focus on structure and completenes
- **Week 2:** Add peer “pushback” &rarr; justify trade-offs and assumptions
- **Week 3:** Timed rounds &rarr; 30-min designs emphasizing concise reasoning
- **Week 4:** Simulated panel with back-to-back design + follow-up questions

### Refinement Goals
- Speak through reasoning transitions clearly (“Because we need consistency, we’ll...”)
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