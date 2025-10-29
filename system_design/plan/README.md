# 4-Month Senior System Design Plan (Nov → Feb)

---

## Month 1 — November: Core Foundations + DDIA

**Goal:** Build strong mental models of distributed system fundamentals. Focus on architecture patterns, storage, replication, and tradeoffs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 1–6: Data Models, Storage Engines, Encoding, Replication, Partitioning
  - Focus on tradeoffs (e.g., LSM vs. B-trees, consistency vs. availability)
- **Understanding Distributed Systems**
  - Ch. 1–5: Core Distributed Concepts, Nodes, Networks, and Failure Models
- **System Design Interview (Vol. 1 & 2)**
  - Foundational Patterns and High-Level System Overviews

**Supplement / Lectures**
- [System Design Primer](https://github.com/donnemartin/system-design-primer) – caching, load balancing, consistency
- ByteByteGo videos – URL shortener, news feed, rate limiter
- [Harvest, Yield, and Scalable Tolerant Systems](https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf) – CAP tradeoffs and fault-tolerance
- [On Designing and Deploying Internet Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf) – service-oriented architecture
- [The Tail at Scale](https://dl.acm.org/doi/pdf/10.1145/2408776.2408794) – latency and tail amplification
- [Data on the Outside versus Data on the Inside](https://www.cidrdb.org/cidr2005/papers/P12.pdf) – data boundaries and architectural implications

**Practice**
1. **URL Shortener** – hashing, storage model, replication
2. **News Feed** – fan-out tradeoffs
3. **Distributed Cache** – consistency, eviction, TTL

**Whitepapers**
- [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [CAP Twelve Years Later: How the "Rules" Have Changed](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [Why Distributed Computing?](https://www.artima.com/weblogs/viewpost.jsp?thread=4247)
- “Notes on Distributed Systems for Young Bloods” – Jeff Hodges

---

## Month 2 — December: Deep Internals + Database Systems

**Goal:** Move from architecture reasoning to internal design: storage, consensus, replication, and consistency models.

**Primary Reading**
- **Database Internals**
  - Part I: Storage Engines (Ch. 1–5)
  - Part II: Distributed Systems (Ch. 6–9)
  - Topics: Replication, Partitioning, Consensus, Consistency Models
- **Understanding Distributed Systems**
  - Ch. 6–10: Replication, Partitioning, Consensus, Consistency Models
- **System Design Interview (Vol. 1 & 2)**
  - Messaging, Caching, Database Scaling

**Supplement / Lectures**
- CMU 15-445: Logging, Indexing, MVCC
- MIT 6.824 lectures 1–3: Consensus, Replication, Sharding
- [Consistency, Availability, and Convergence](https://www.cs.cornell.edu/lorenzo/papers/cac-tr.pdf) – modern framing of CAP
- [Life Beyond Distributed Transactions](https://queue.acm.org/detail.cfm?id=3025012) – async, idempotent systems
- [Eventual Consistency](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html) – Amazon’s consistency principles
- [Avoiding Two-Phase Commit](https://web.archive.org/web/20180821165044/http://www.addsimplicity.com/adding_simplicity_an_engi/2006/12/avoiding_two_ph.html) – reducing coordination bottlenecks

**Practice**
1. **Kafka-like Message Queue** – log segmentation, offsets
2. **Dropbox / Google Drive** – metadata vs. blob storage
3. **Slack / WhatsApp** – real-time messaging and delivery guarantees

**Whitepapers**
- **Consensus**
  - [Raft](https://raft.github.io/raft.pdf)
  - [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)
- **Database**
  - [BigTable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
  - [Cassandra](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf)
  - [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
  - [F1](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41344.pdf)
  - [Mesa](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42851.pdf)
  - [PNUTS](https://people.mpi-sws.org/~druschel/courses/ds/papers/cooper-pnuts.pdf)
  - [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
  - [TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)

---

## Month 3 — January: Distributed Computation + Reliability

**Goal:** Understand large-scale computation, streaming, and reliability practices.

**Primary Reading**
- **Site Reliability Engineering (SRE)**
  - SLIs, SLOs, Monitoring, Incident Response
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 7–9: Batch and Stream Processing Models
- **Understanding Distributed Systems**
  - Fault-Tolerance, Backpressure, Orchestration

**Supplement / Lectures**
- MIT 6.824: MapReduce, Dremel, Distributed Transactions
- [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
- [Dremel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36632.pdf)
- [Photon](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41318.pdf)
- [Megastore](https://research.google/pubs/pub36971/)
- [Principles of Robust Timing over the Internet](https://www.hpl.hp.com/techreports/2004/HPL-2004-83.pdf)
- [The Tail at Scale](https://research.google/pubs/pub40801/) – revisit for reliability under load

**Practice**
1. **Real-Time Analytics / Metrics Platform** – stream processing, monitoring
2. **Recommendation Engine** – batch + streaming pipelines
3. **Large-Scale Messaging System** – SLA guarantees, replication, recovery

**Whitepapers**
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

---

## Month 4 — February: Advanced Systems + Senior Hiring Readiness

**Goal:** Integrate knowledge and reason through full-stack distributed design with production-scale tradeoffs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 10–12: Batch, Stream, and Dataflow
- **Database Internals**
  - Distributed Transactions, Coordination, Recovery
- **Understanding Distributed Systems**
  - Complex Systems, Performance Tuning
- **System Design Interview (Vol. 1 & 2)**
  - Mock Interviews and Articulation Practice

**Supplement / Case Studies**
- Meta TAO, Uber Michelangelo, Pinterest Real-Time Systems
- Netflix TechBlog – resilience and chaos engineering
- [Building on Quicksand](https://s3.amazonaws.com/systemsandpapers/papers/HellandBuildingOnQuicksand.pdf)
- [SOA Creates Order Out of Chaos at Amazon](https://queue.acm.org/detail.cfm?id=945137)
- [Distributed Computing Economics](https://www.microsoft.com/en-us/research/publication/distributed-computing-economics/)

**Practice**
1. **YouTube / Netflix** – large-scale content delivery
2. **Uber / Lyft** – distributed coordination
3. **Twitter Timeline** – fan-out, caching, DB scaling
4. **Graph Analytics / Metrics** – large-scale pipelines

**Whitepapers**
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
  - [Facebook's Photo Storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf)
  - [RCFile](https://scispace.com/pdf/rcfile-a-fast-and-space-efficient-data-placement-structure-2kq37wcjl0.pdf)
  - [XORing Elephants](https://arxiv.org/pdf/1301.3791)

---

## Supplemental Reference Library

These papers don’t map neatly into a single month but are highly recommended to read throughout the plan:

- [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [Unreliable Failure Detectors for Reliable Distributed Systems](https://s3.amazonaws.com/systemsandpapers/papers/ChandraToueg.pdf)
- [Implementing Fault-Tolerant Services Using the State Machine Approach](https://lamport.azurewebsites.net/pubs/state-machine.pdf)
- [Mencius](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/mencius.pdf)
- [SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf)
- [Pastry](https://www.cs.rice.edu/Conferences/IPTPS02/109.pdf)

---

## Revised Weekly Cadence

| Day | Focus | Duration |
|-----|--------|-----------|
| Mon–Wed | **Core Reading** – DDIA, Database Internals, or Understanding Distributed Systems | 1.5–2 hrs/day |
| Thu | **Lecture or Whitepaper Deep Dive** – MIT/CMU lecture or one key paper | 1–1.5 hrs |
| Fri | **Light Review / Notes** – summarize readings or prepare flashcards | 1 hr |
| Sat | **System Design Practice** – one scenario (e.g., “Design Dropbox”) | 1.5–2 hrs |
| Sun | **Reflection / Case Study Review** – re-explain or diagram a paper or real-world system | 1.5 hrs |

---

## Notes on Timeline

- **Pacing:** With ~10–12 hrs/week (≈2 hrs/day), this plan is **intensive but sustainable**.  
- **Depth over breadth:** If one paper or concept (e.g., Raft, consistency models) requires a week, take it — mastery compounds over time.  
- **Flexibility:** Extend by 2–3 weeks if complex topics (like consensus or stream processing) need additional reinforcement.  
- **Outcome:** By February, you’ll have strong mental models for distributed systems, database internals, and clear articulation of system design tradeoffs suitable for **upper-senior** interviews.
