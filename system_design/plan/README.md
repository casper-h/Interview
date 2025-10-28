# 4-Month Senior System Design Plan (Nov → Feb)

---

## Month 1 — November: Core Foundations + DDIA

**Goal:** Build strong mental models of distributed system fundamentals. Focus on architecture patterns, storage, replication, and tradeoffs.

**Primary Reading**
- **Designing Data-Intensive Applications (DDIA)**
  - Ch. 1–6: Data Models, Storage Engines, Encoding, Replication, Partitioning
  - Focus on tradeoffs (e.g., LSM vs. B-trees, consistency vs. availability)
- **Understanding Distributed Systems**
  - Ch. 1–5: Basic distributed system concepts, nodes, networks, failures
- **System Design Interview (Volume 1 & 2)**
  - High-level system patterns and case studies  

**Supplement / Lectures**
- [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) – caching, load balancing, consistency
- ByteByteGo videos – URL shortener, news feed, rate limiter  

**Practice**
1. **URL Shortener** – hashing, storage model, replication  
2. **News Feed** – fan-out tradeoffs  
3. **Distributed Cache** – consistency, eviction, TTL  

> Explain tradeoffs using DDIA and Understanding Distributed Systems concepts.

**Whitepapers / Intro**
- Google File System (GFS)  
- “Notes on Distributed Systems for Young Bloods” – Jeff Hodges  

---

## Month 2 — December: Deep Internals + Database Systems

**Goal:** Move from architectural reasoning to component-level understanding of storage, consensus, and replication.

**Primary Reading**
- **Database Internals**
  - Part I: Storage Engines (Ch. 1–5)  
  - Part II: Distributed Systems (Ch. 6–9)  
- **Understanding Distributed Systems**
  - Ch. 6–10: Replication, consensus, partitioning, failures, consistency  
- **System Design Interview (Volume 1 & 2)** – revisit chapters related to messaging, caching, DB scaling  

**Supplement / Lectures**
- CMU 15-445: Logging, indexing, MVCC  
- MIT 6.824 lectures 1–3: consensus, replication, sharding  

**Practice**
1. **Kafka-like Message Queue** – log segmentation, offsets  
2. **Dropbox / Google Drive** – metadata vs. blob storage  
3. **Slack / WhatsApp** – real-time messaging, delivery guarantees  

**Whitepapers**
- **Consensus:** Raft, Impossibility of Distributed Consensus with One Faulty Process  
- **Database:** BigTable, Cassandra, Dynamo, F1, Mesa, PNUTS, Spanner, TAO  

---

## Month 3 — January: Distributed Computation + Reliability

**Goal:** Understand large-scale computation, experimentation, streaming, and reliability patterns.

**Primary Reading**
- **Site Reliability Engineering (SRE)** – reliability, monitoring, production best practices  
- **DDIA Ch. 7–9** – Batch & stream processing  

**Supplement / Lectures**
- MapReduce, FlumeJava, Dremel lectures (MIT 6.824 / online resources)  
- Online controlled experiments – A/B testing and metrics  
- **Understanding Distributed Systems** – as reference for architecture tradeoffs and fault-tolerance  

**Practice**
1. **Real-Time Analytics / Metrics Platform** – stream processing, monitoring  
2. **Recommendation / Personalization Engine** – batch + streaming pipelines  
3. **Large-Scale Messaging System** – SLA guarantees, replication  

**Whitepapers**
- **Distributed Computation:** Dremel, FlumeJava, Hive, MapReduce, Percolator, Tenzing  
- **Experimentation:** Online Controlled Experiments  
- **Storage & Streaming:** Kafka, MillWheel, Photon  

---

## Month 4 — February: Advanced Systems + Senior Hiring Readiness

**Goal:** Integrate knowledge; design end-to-end systems with performance, scaling, and tradeoff reasoning at senior/staff level.

**Primary Reading**
- **DDIA Ch. 10–12** – Batch, Stream, Dataflow  
- **Database Internals (advanced chapters)** – distributed transactions, consistency  
- **Understanding Distributed Systems** – as reference for complex systems and decision-making  
- **System Design Interview (Volume 1 & 2)** – optional revisit for mock interview prep  

**Supplement / Case Studies**
- Meta TAO, Uber Michelangelo – large-scale service patterns  
- Netflix TechBlog – resilience, chaos engineering  

**Practice**
1. **YouTube / Netflix** – large-scale content delivery  
2. **Uber / Lyft** – distributed coordination  
3. **Twitter Timeline** – fan-out, caching, DB scaling  
4. **Graph Analytics / Metrics** – large-scale pipelines  

> Include capacity planning: QPS, throughput, memory footprint, replication lag.

**Whitepapers**
- **Graph:** GraphChi, PowerGraph, Pregel  
- **Peer-to-Peer:** Chord  
- **Search:** Top-m Passages, Earlybird, Unicorn, Google Cluster Architecture  
- **Storage:** Erasure Coding, Facebook Photo Storage, GFS Evolution, RCFile, XORing Elephants  

---

## Recommended Weekly Cadence

| Day | Focus |
|-----|-------|
| Mon–Wed | Read (1–1.5h/day) – DDIA, Database Internals, or SRE |
| Thu–Fri | Light review, notes, or whitepaper summary |
| Sat–Sun | System design session (1–2h) + summarize designs in your repo / optional mock interviews |

---

## Notes on Timeline
- **4 months** is aggressive but feasible with ~8–12h/week  
- Month 1–2: Core concepts, architecture, database internals, distributed system fundamentals  
- Month 3: Large-scale computation, reliability, streaming  
- Month 4: Advanced synthesis, staff-level design, mock interviews  
- Optional extension: add 1–2 weeks if mock interviews or rare cases (graph, search, P2P) need more focus
