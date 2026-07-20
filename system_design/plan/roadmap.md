# System Design Interview Roadmap

This document transcribes the durable content of the roadmap image at the repository root. It is oriented toward the upper-end Senior and lower-end Staff hiring band. The roadmap organizes resources by priority tier and maps concepts to hiring bands as a progression from Mid to Staff level.

---

## Resource Tier List

The following tier list prioritizes learning resources for system design interviews. The user prioritizes S and A tiers and de-emphasizes C as a primary study path.

### Applied Problems Books

- **A Tier:** System Design Interview Volumes 1 and 2 (Alex Xu)
- **B Tier:** Hacking the System Design Interview (Stanley Chiang)
- **C Tier:** Grokking the System Design Interview (Design Gurus), System Design Interview (Alex Xu, other edition), general System Design introduction books

### Concepts Books

- **S Tier:** Designing Data-Intensive Applications (DDIA) by Martin Kleppmann
- **A Tier:** jepsen.io, Database Internals by Alex Petrov
- **B Tier:** Understanding Distributed Systems, Donne Martin's System Design Primer

### Secondary and Tangential Books

- **S Tier:** Specifying Systems by Leslie Lamport
- **A Tier:** Building Microservices, Distributed Systems by van Steen and Tanenbaum
- **B Tier:** Site Reliability Engineering, Software Architecture: The Hard Parts, Designing Distributed Systems
- **C Tier:** Fundamentals of Software Architecture

### YouTube Channels

- **S Tier:** Martin Kleppmann, CMU Database Group, MIT 6.824 Distributed Systems
- **A Tier:** InfoQ, USENIX, System Design Interview channel, DistSys Reading Group, TLA+ Video Course
- **B Tier:** A Life Engineered, ByteByteGo, Fireship
- **C Tier:** System Design Fight Club, Exponent, NeetCode, Tushar Roy, interviewing.io, Tech Dummies Narendra L, Jordan Has No Life, Gaurav Sen

---

## Whitepapers Reference

The following papers and systems are named on the roadmap image. Most have entries, with URLs and pedagogy, in the [white paper catalog](../white_paper.md); a few (BigQuery, Spark, HDFS, Flink) are named as systems on the roadmap without a corresponding paper entry in the catalog, and are listed here for completeness.

**Named on the roadmap:** Dynamo, Kafka, Cassandra, Bigtable, BigQuery, Spanner, GFS, Dremel, Raft, Paxos, MapReduce, Spark, Chubby, ZooKeeper, HDFS, Flink, TAO, Pregel, Photon, Percolator, MillWheel, Mesa, Earlybird.

**Annotated paper list:** Stephen Holiday's annotated Level 7 paper list at https://stephenholiday.com/notes/ provides additional context for many distributed systems papers.

---

## Engineering Blogs Reference

**Company engineering blogs:** Uber, Pinterest, Snapchat, Netflix, Dropbox, Google, Facebook, Twitter, Jane Street. Also highscalability.com and allthingsdistributed.com.

**Aggregator lists:** The company-engineering-blogs list in donnemartin/system-design-primer on GitHub, and github.com/kilimchoi/engineering-blogs.

---

## Communities Reference

**Active communities for system design preparation:** System Design Fight Club, Alex Xu's channel, Facebook E6 mock interview group, NeetCode's channel, A Life Engineered's channel.

Invite links to Discord and Slack channels expire and are not listed here. Refer to the respective YouTube channels or community websites for current access.

---

## Hiring Band Concept Matrix

This is the most important section of the roadmap. It shows what concepts and skills are expected at each hiring band. The progression is cumulative: each band assumes mastery of everything above it.

### Lower Mid (LLD focus)

**Concepts expected:**
- CAP theorem
- Replication
- Partitioning
- Horizontal scaling
- NoSQL fundamentals
- Denormalization

### Upper Mid

**Interview focus:** High-level design fluency with trade-offs; competency in scaling; problems tend to feature eventual consistency plus high availability.

**Concepts expected:**
- Load balancers
- CAP theorem application
- Replication strategies
- Partitioning strategies
- Leader-follower pattern
- Eventual consistency
- Familiarity with the hot-partition issue

### Lower Senior

**Interview focus:** High-level design fluency with partial failures; high-level design fluency with partition keys and secondary indices; high-level design fluency with machine-count estimates (Non-Abstract Large System Design, or NALSD, from the Google SRE Workbook).

**Concepts expected:**
- Familiarity with consensus algorithms
- Streaming analytics such as Flink
- Familiarity with some component internals: B-trees, LSM-trees, R-trees, quad-trees, inverted index

### Upper Senior

**Interview focus:** Problems are likely to require stronger consistency levels.

**Concepts expected:**
- FLP impossibility result
- Clock drift
- Fluency with isolation levels
- Fluency with intermediary consistency levels such as causal consistency
- Fluency with a large variety of component internals

### Lower Staff

**Interview focus:** High-level design fluency with latency estimates (NALSD); some cost awareness in designs; problems taken from the real world that do not have clean or happy endings.

**Concepts expected:**
- CRDT implementations and algorithms such as the Count-Min sketch
- Consensus-algorithm trade-offs (Database Internals describes several distinct consensus algorithms and their trade-offs)

**Note on study resources at this band:** Alex Xu's books alone are insufficient at the upper-Senior and Staff band. They underweight partitioning-key selection, in-depth secondary-index design including the global-versus-local choice, trade-off fluency, and causal consistency. Templated Grokking-style low-level design is a poor model for real-world problems that lack clean solutions.

---

## Your Target Band: Upper Senior and Lower Staff

For the upper-Senior and lower-Staff band, the concepts that matter most are:

- Stronger consistency levels beyond eventual consistency
- The FLP impossibility result and its practical consequences for consensus protocols
- Clock drift and bounded-time reasoning (as in Spanner's TrueTime)
- Isolation levels in databases
- Causal and other intermediary consistency models
- A broad command of component internals (storage engines, indexing structures, network protocols)
- CRDT implementations and probabilistic data structures such as Count-Min sketch
- Consensus-algorithm trade-offs (Raft versus Paxos versus other algorithms)
- Cost awareness in design decisions
- Latency estimation (NALSD)
- Real-world problems without clean answers

**Where these are covered:**

- **Building blocks:** [../building_blocks.md](../building_blocks.md) covers component internals, consensus, CRDTs, and partitioning strategies.
- **Reading plan:** [./README.md](./README.md) stages the primary reading (DDIA, Database Internals, Understanding Distributed Systems, lectures) and marks optional depth appropriately.
- **White paper catalog:** [../white_paper.md](../white_paper.md) provides the core set and optional deep-dive papers, with pedagogy for which papers address which gaps.

---

## NALSD Definition

NALSD stands for Non-Abstract Large System Design. The term originates from the Google SRE Workbook. It refers to system design reasoning that includes concrete capacity estimates, latency calculations, machine counts, bandwidth requirements, and cost considerations, rather than abstract architectural diagrams alone.
