# 4-Month Senior System Design Plan (Nov → Feb)

---

## Month 1 — November: Core Foundations + DDIA

**Goal:** Build strong mental models of distributed system fundamentals. Focus on architecture patterns, storage, replication, and trade-offs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 1-6: Data Models, Storage Engines, Encoding, Replication, Partitioning
  - Focus on trade-offs (e.g., LSM vs B-trees, consistency vs availability)
- **Understanding Distributed Systems**
  - Ch. 1-5: Core Distributed Concepts, Nodes, Networks, Failure Models
- **System Design Interview (Vol. 1 & 2)**
  - Foundational patterns and high-level system overviews
- **System Design Primer**
  - Checklists and reference during practice

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
  - Part I: Storage Engines (Ch. 1-5)
  - Part II: Distributed Systems (Ch. 6-9)
- **Understanding Distributed Systems**
  - Ch. 6-10: Replication, Partitioning, Consensus, Consistency
- **System Design Interview (Vol. 1 & 2)**
  - Messaging, Caching, DB Scaling
- **Database System Concepts**
  - Ch. 12-16: Storage, Indexing, Concurrency Control

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
  - Ch. 7-9: Batch and Stream Processing
- **Site Reliability Engineering (SRE)**
  - SLIs, SLOs, Monitoring, Incident Response
- **Understanding Distributed Systems**
  - Fault Tolerance, Backpressure, Orchestration
- **System Design Interview (Vol. 1 & 2)**
  - Stream and analytics case studies

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
  - Ch. 10-12: Batch, Stream, Dataflow
- **Database Internals**
  - Distributed Transactions, Coordination, Recovery
- **Understanding Distributed Systems**
  - Complex Systems, Performance Tuning
- **System Design Interview (Vol. 1 & 2)**
  - Mock interviews and articulation practice
- **Site Reliability Engineering (SRE)**
  - Production SRE practices that tie into architecture

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
| Mon–Wed | Core Reading | 1.5–2 hrs/day |
| Thu | Lecture / White Paper Deep Dive | 1–1.5 hrs |
| Fri | Weekly Reflection | 1 hr |
| Sat | System Design Practice | 1.5–2 hrs |
| Sun | Concept Synthesis / Case Study Review | 1.5 hrs |

### Weekly Process

**Reading Comprehension**
- Break readings into small conceptual chunks; aim for understanding, not completion
- Track recurring trade-offs (latency vs consistency, throughput vs correctness)
- When concepts feel unclear, trace them back to fundamental models (Lamport’s happens-before, Raft’s log replication, CAP trade-offs)

**Paper Annotation**
- Use a structured template for every paper:
  - **Problem → Design → Trade-offs → Takeaways**  
- Capture 1–2 core insights and relate them to a real-world system (e.g., Spanner, Kafka, Dynamo)

**Teach-Back Summary**
- End each week with 3–5 concise bullets summarizing key insights
- Write as if explaining the concept aloud; clarity reveals depth of understanding

**Cross-Linking**
- Connect ideas across systems and theories:  
  - Paxos ↔ Raft — Consensus Lineage
  - Lamport clocks ↔ Vector clocks ↔ Dynamo Causality
  - State Machine Replication ↔ Fault Tolerance and Recovery Mechanisms

**Reflection**
- Maintain a short log titled *“What changed in understanding this week?”*
- Capture insights, confusions, and moments of conceptual clarity. These form the intuition base for design reasoning

---

## Notes on Timeline

**Consistency**
- Maintain steady daily progress rather than bursts of effort
- Distributed reasoning compounds through repetition
- Missing sessions occasionally is not a setback; long-term consistency builds lasting understanding

**Depth Over Breadth**
- Deep comprehension of a few systems outweighs shallow familiarity with many
- Core focus: Raft, Paxos, Dynamo, Spanner, Kafka

**Nonlinear Progress**
- Expect to revisit Consensus, Replication, and CAP multiple times
- Each pass should strengthen intuition and improve reasoning precision

**Retrospectives**
- End each month with a short reflection:  
  *“What can be designed now that couldn’t be reasoned about before?”*
- Capture new trade-offs understood, design instincts gained, and unresolved questions

**Integration**
- Relate theoretical insights to practical systems design:
  - Lamport → Paxos → Raft
  - DDIA → Real-World Architectures (Spanner, DynamoDB)
  - White Papers → Decision Frameworks/Trade-Off Reasonings

**Outcome**
- The goal is architectural fluency: reasoning in trade-offs, articulating design constraints, and evaluating correctness under failure
- Progress is measured by clarity of thought and design precision, not by volume of materials completed.
