# 4-Month Senior System Design Plan (Nov → Feb)

---

## Month 1 — November: Core Foundations + DDIA

**Goal:** Build strong mental models of distributed system fundamentals. Focus on architecture patterns, storage, replication, and trade-offs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 1–6: Data Models, Storage Engines, Encoding, Replication, Partitioning
  - Focus on trade-offs (e.g., LSM vs B-Trees, Consistency vs Availability)
- **Understanding Distributed Systems**
  - Ch. 1–5: Core Distributed Concepts, Nodes, Networks, Failure Models
- **System Design Interview (Vol. 1)**
  - Ch. 1–3: Scale from Zero to Millions, Estimation, Design Frameworks
  - Ch. 4–8: Rate Limiter, Consistent Hashing, Key-Value Store, Unique ID Generator, URL Shortener
- **System Design Interview (Vol. 2)**
  - Ch. 4: Distributed Message Queue
  - Ch. 9: S3-like Object Storage
- **System Design Primer**
  - Sections: System Design Topics: Start Here, Performance vs Scalability, Latency vs Throughput, CAP Theorem and Consistency, Availability Patterns, DNS, CDN, Load Balancing
  - Use as reference for conceptual overviews and trade-off visualization


**Supplement / Lectures**
- MIT 6.824 Lectures 1-3: Introductions, RPC and Threads, GFS
- CMU 15-445 Lectures 1-5: Relational Model, Storage I & II, Compression
- [System Design Primer](https://github.com/donnemartin/system-design-primer) - Caching, Load Balancing, Consistency
- ByteByteGo - URL Shortener, News Feed, Rate Limiter
- [Harvest, Yield, and Scalable Tolerant Systems](https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf)
- [On Designing and Deploying Internet-Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf)
- [The Tail at Scale](https://dl.acm.org/doi/pdf/10.1145/2408776.2408794)
- [Data on the Outside versus Data on the Inside](https://www.cidrdb.org/cidr2005/papers/P12.pdf)
- Optional: [SRE Networking Chapter](https://sre.google/sre-book/monitoring-distributed-systems/)

**Practice**
1. URL Shortener - Hashing, Storage Model, Replication
2. News Feed - Fan-Out
3. Distributed Cache - Consistency, Eviction, TTL

**White Papers**
- [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [CAP Twelve Years Later: How the "Rules" Have Changed ](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [Why Distributed Computing?](https://www.artima.com/weblogs/viewpost.jsp?thread=4247)
- [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
- [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)

**Tip:** Create a System Design Concept Log (one page per topic: replication, partitioning, CAP) and update weekly.

---

## Month 2 — December: Deep Internals + Database Systems

**Goal:** Move from architecture reasoning to internal design: storage, consensus, replication, and consistency models.

**Primary Reading**
- **Database Internals**
  - Part I (Ch. 1–5): Storage Engines
  - Part II (Ch. 6–9): Distributed Systems
- **Understanding Distributed Systems**
  - Ch. 6–10: Replication, Partitioning, Consensus, Consistency
- **System Design Interview (Vol. 1)**
  - Ch. 6–15: Key-Value Store, Notification, News Feed, Chat, Search, YouTube, Google Drive
- **System Design Interview (Vol. 2)**
  - Ch. 1–4, 9: Proximity Service, Nearby Friends, Google Maps, Distributed Message Queue, S3-like Object Storage
- **Database System Concepts**
  - Ch. 12–16: Storage, Indexing, Concurrency Control
- **System Design Primer**
  - Sections: Databases, SQL vs NoSQL, RDBMS, Sharding, Master-Slave Replication, Denormalization, Caching (cache-aside, write-through, write-behind)
  - Use for database scaling patterns and caching strategy reviews


**Supplement / Lectures**
- CMU 15-445 Lectures 3-10: Storage, Compression, Memory Management, Indexes & Filters
- MIT 6.824 Lectures 4-6: Primary-Backup, Fault Tolerance, Raft
- [Consistency, Availability, and Convergence](https://www.cs.cornell.edu/lorenzo/papers/cac-tr.pdf)
- [Life Beyond Distributed Transactions](https://queue.acm.org/detail.cfm?id=3025012)
- [Eventually Consistent - Revisited](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
- [Avoiding Two-Phase Commit](https://web.archive.org/web/20180821165044/http://www.addsimplicity.com/adding_simplicity_an_engi/2006/12/avoiding_two_ph.html)
- [The Log: What Every Software Engineer Should Know About Real-time Data’s Unifying Abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)

**Practice**
1. Kafka-like Message Queue - Log Segmentation, Offsets
2. Dropbox / Google Drive - Metadata vs Blob Storage
3. Slack / WhatsApp - Real-Time Messaging

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

**Tip:** Create a Replication Trade-offs Matrix (synchronous vs async, leader-based vs quorum) with real-world examples.

---

## Month 3 — January: Distributed Computation + Reliability

**Goal:** Understand large-scale computation, streaming, and reliability practices.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 7–9: Batch and Stream Processing
- **Site Reliability Engineering (SRE)**
  - Ch. 3–5: SLIs, SLOs, Monitoring, Incident Response
- **Understanding Distributed Systems**
  - Ch. 11–13: Fault Tolerance, Backpressure, Orchestration
- **System Design Interview (Vol. 1)**
  - Ch. 10–12: Notification System, News Feed, Chat System
- **System Design Interview (Vol. 2)**
  - Ch. 5–10: Metrics Monitoring, Ad Click Aggregation, Hotel Reservation, Email Service, S3-like Object Storage, Real-Time Gaming Leaderboard
- **System Design Primer**
  - Sections: Asynchronism, Message Queues, Task Queues, Communication (TCP, UDP, RPC, REST), Application Layer, Microservices, Service Discovery, Reverse Proxy, Load Balancer Scaling
  - Reinforce distributed computation and reliability mechanisms


**Supplement / Lectures**
- MIT 6.824 Lectures 7-10: MapReduce, Fault-Tolerant Services, Transactions, Dremel
- CMU 15-445 Lectures 11-16: Sorting, Joins, Execution, Concurrency
- [Megastore](https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf)
- [Principles of Robust timing over the internet](https://dl.acm.org/doi/pdf/10.1145/1735223.1735241)

**Practice**
1. Real-Time Analytics / Metrics Platform - Stream Processing, Monitoring
2. Recommendation Engine - Batch + Stream Pipelines
3. Large-Scale Messaging System - SLA, Replication, Recovery

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

**Tip:** Simulate failure modes (node failure, duplication, network partition) and document recovery approaches.

---

## Month 4 — February: Advanced Systems + Senior Hiring Readiness

**Goal:** Integrate knowledge and reason through full-stack distributed design with production-scale trade-offs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 10–12: Dataflow, Derived Data, Real-Time Systems
- **Database Internals**
  - Ch. 10–12: Distributed Transactions, Coordination, Recovery
- **Understanding Distributed Systems**
  - Ch. 14–15: Complex Systems, Performance Tuning
- **System Design Interview (Vol. 1)**
  - Ch. 13–15: Search Autocomplete, YouTube, Google Drive
- **System Design Interview (Vol. 2)**
  - Ch. 10–13: Real-Time Gaming Leaderboard, Payment System, Digital Wallet, Stock Exchange
- **Site Reliability Engineering (SRE)**
  - Ch. 6–10: Production Practices and Architecture Reliability
- **System Design Primer**
  - Sections: Security, Monitoring, Scalability, Failover Strategies, Real-World Architectures (Netflix, Twitter, YouTube), Engineering Blogs, Latency Numbers, Powers of Two Table
  - Use for synthesis of large-scale production systems and final interview readiness


**Supplement / Case Studies**
- MIT 6.824 Lectures 11-12: Fault-Tolerant Key-Value Stores
- CMU 15-445 Lectures 20-24: Logging, Recovery, Distributed Databases
- Meta TAO, Uber Michelangelo, Pinterest Real-Time Systems
- Netflix TechBlog - Resilience and Chaos Engineering
- [Building on Quicksand](https://arxiv.org/pdf/0909.1788)
- [Distributed Computing Economics](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2003-24.pdf)

**Practice**
1. YouTube / Netflix - Content Delivery
2. Uber / Lyft - Distributed Coordination
3. Twitter Timeline - Fan-Out, Caching, DB Scaling
4. Graph Analytics / Metrics - Large-Scale Pipelines
5. Optional: Multi-Tenant Analytics Platform (Uber-style Michelangelo)

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

## More Reading

- [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [Unreliable Failure Detectors for Reliable Distributed Systems](https://dl.acm.org/doi/pdf/10.1145/226643.226647)
- [Implementing Fault-Tolerant Services Using the State Machine Approach](https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf)
- [Mencius](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/mao/mao.pdf)
- [SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf)
- [Pastry](https://www.cs.cornell.edu/courses/cs6452/2012sp/papers/pastry.pdf)

## Weekly Cadence

| Day | Focus | Duration |
|-----|--------|-----------|
| Mon–Wed | Core Reading & Concept Mapping | 1.5–2 hrs/day |
| Thu | Lecture or White Paper Deep Dive | 1–1.5 hrs |
| Fri | Reflection & Teach-Back Review | 1 hr |
| Sat | System Design Practice & Failure Simulation | 1.5–2 hrs |
| Sun | Integration Review & Case Study Synthesis | 1.5 hrs |

### Weekly Process

**Reading Comprehension**
- Read actively rather than sequentially; aim for conceptual clarity, not completion
- Summarize every core idea in your own words before moving forward
- Track recurring trade-offs such as latency vs consistency or throughput vs correctness
- When concepts feel unclear, return to first principles (e.g., Lamport clocks, Raft replication, CAP models)
- Highlight not just what a system does but why the design choices exist

**Paper Annotation**
- Use a consistent template for every paper:
  - **Problem → Design → Trade-offs → Takeaways**
- Capture 1–2 central insights and tie them to a real-world system (Spanner, Kafka, Dynamo)
- Identify failure modes and recovery mechanisms for every paper reviewed

**System Design Practice**
- Each week, pick one system and walk through a complete structured design
  - Clarify the goal and constraints
  - Estimate load and capacity with back-of-envelope calculations
  - Define the data model, critical paths, and scalability levers
  - Identify one deep bottleneck and explore trade-offs
  - Consider one failure mode and outline a recovery path
  - Reflect on how the design changes under 10× growth
- Focus on reasoning through decisions rather than naming technologies

**Teach-Back Summary**
- End each week with a concise 3–5 bullet summary of key takeaways
- Explain each idea aloud or in writing as if teaching another engineer
- Capture one example of a design trade-off you now understand more intuitively

**Cross-Linking**
- Relate ideas across readings and systems
  - Paxos ↔ Raft → Consensus lineage
  - Lamport clocks ↔ Vector clocks ↔ Dynamo causality
  - State machine replication ↔ Fault tolerance ↔ Recovery
- Maintain a linked note index so ideas reinforce one another over time

**Reflection**
- Maintain a short log titled *“What changed in understanding this week?”*
- Capture shifts in mental models, new intuitions, or persisting gaps
- Focus on how design reasoning and trade-off intuition evolve

---

## Study Principles

**1. Foundational Stage (November–December)**
- Build mental models for replication, partitioning, caching, and CAP
- Prioritize conceptual accuracy over breadth of coverage
- Validate understanding by explaining ideas without referring to notes

**2. Architectural Stage (December–January)**
- Combine components to design end-to-end systems
- Reason about scaling paths, bottlenecks, and trade-offs between throughput, latency, and consistency
- Apply patterns such as leader-follower replication, quorum writes, and async queues

**3. Operational Stage (January–February)**
- Add production constraints to designs: failure handling, SLOs, and backpressure
- Focus on trade-offs between durability, fault tolerance, and latency
- Simulate failure and recovery paths to understand real-world system behavior

**4. Articulation Stage (February onward)**
- Practice structured communication under time limits
- Present designs with clarity of reasoning and justification of choices
- Strengthen explanation precision and calm, top-down articulation

---

## Evaluation and Progress Tracking

**Consistency**
- Study regularly; small, sustained sessions yield deeper understanding than sporadic bursts
- Repetition and revisiting complex ideas improves long-term retention
- Missing a session occasionally is acceptable if overall consistency is maintained

**Depth Over Breadth**
- Aim for deep comprehension of core distributed systems before expanding
- Focus on Raft, Paxos, Dynamo, Spanner, and Kafka as anchor systems
- Evaluate mastery by whether you can analyze trade-offs under failure conditions

**Iterative Progress**
- Expect nonlinear growth; understanding deepens with multiple passes over key topics
- Each cycle should refine your ability to reason precisely about correctness, latency, and availability
- Accept conceptual rework as progress rather than regression

**Retrospectives**
- At the end of each month, write a reflection
  *“What can I design now that I could not reason about before?”*
- Summarize improved intuitions, design instincts, and remaining blind spots
- Use this feedback to adjust focus areas for the next month

---

## Practice Framework

**System Design Drills**
- Practice one design per week using a consistent 6-step format
  1. Clarify goals and assumptions
  2. Estimate scale and constraints
  3. Define major components and data flow
  4. Deep dive into one critical subsystem
  5. Analyze trade-offs and potential bottlenecks
  6. Identify failure scenarios and recovery mechanisms

**Failure Mode Exercises**
- For each system, simulate one type of fault (node crash, network partition, duplicate message)
- Describe how the system behaves and how recovery would proceed
- Record the trade-offs in durability, latency, and availability

**Mock Interviews**
- Starting in January, schedule one mock interview every two weeks
- In February, increase to two or more per week with peers or mentors
- Record and review sessions to identify clarity and pacing issues
- Focus on explaining reasoning rather than listing technologies

---

## Integration and Application

**Connecting Theory to Practice**
- Lamport → Paxos → Raft → State Machine Replication
- DDIA → Real-world architectures such as Spanner, DynamoDB, Kafka
- White papers → Design frameworks and decision heuristics

**Trade-off Framework**
- Replication → Latency vs Durability
- Partitioning → Data locality vs Rebalance complexity
- Consistency → Availability vs Correctness
- Caching → Freshness vs Performance
- Queueing → Throughput vs Ordering guarantees
- Batch vs Stream → Latency vs Accuracy
- Observability → Cost vs Coverage

**Outcome**
- Target architectural fluency: reasoning clearly through trade-offs, articulating design constraints, and evaluating correctness under fault conditions
- Measure progress by clarity of reasoning and depth of understanding rather than number of systems studied
