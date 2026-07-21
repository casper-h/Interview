# System Design Concepts by Hiring Level

This document maps system design concepts to hiring bands and collects the supporting reference
lists (papers, engineering blogs, and communities). It is oriented toward the upper-end Senior and
lower-end Staff band. The concept matrix is cumulative: each band assumes command of everything below
it.

---

## White Papers Reference

The systems below recur across senior-level distributed-systems interviews. Most have entries, with
URLs and pedagogy, in the [white paper catalog](../white_paper.md); a few (BigQuery, Spark, HDFS,
Flink) are named here as systems worth recognizing without a corresponding paper entry in the catalog.

**Systems worth recognizing:** Dynamo, Kafka, Cassandra, Bigtable, BigQuery, Spanner, GFS, Dremel,
Raft, Paxos, MapReduce, Spark, Chubby, ZooKeeper, HDFS, Flink, TAO, Pregel, Photon, Percolator,
MillWheel, Mesa, Earlybird.

**Annotated paper list:** Stephen Holiday's annotated Level 7 paper list at
https://stephenholiday.com/notes/ provides additional context for many distributed systems papers.

---

## Engineering Blogs Reference

**Company engineering blogs:** Uber, Pinterest, Snapchat, Netflix, Dropbox, Google, Facebook, Twitter,
Jane Street. Also highscalability.com and allthingsdistributed.com.

**Aggregator lists:** the company-engineering-blogs list in donnemartin/system-design-primer on
GitHub, and github.com/kilimchoi/engineering-blogs.

---

## Communities Reference

**Active communities for system design preparation:** System Design Fight Club, Alex Xu's channel,
the Facebook E6 mock interview group, NeetCode's channel, A Life Engineered's channel.

Invite links to Discord and Slack channels expire and are not listed here. Refer to the respective
YouTube channels or community websites for current access.

---

## Hiring Band Concept Matrix

This matrix shows what concepts and skills are expected at each hiring band. The progression is
cumulative: each band assumes mastery of everything above it.

### Lower Mid (LLD Focus)

**Concepts expected:**
- CAP theorem
- Replication
- Partitioning
- Horizontal scaling
- NoSQL fundamentals
- Denormalization

### Upper Mid

**Interview focus:** high-level design fluency with trade-offs; competency in scaling; problems tend
to feature eventual consistency plus high availability.

**Concepts expected:**
- Load balancers
- CAP theorem application
- Replication strategies
- Partitioning strategies
- Leader-follower pattern
- Eventual consistency
- Familiarity with the hot-partition issue

### Lower Senior

**Interview focus:** high-level design fluency with partial failures; with partition keys and
secondary indices; and with machine-count estimates (Non-Abstract Large System Design, or NALSD, from
the Google SRE Workbook).

**Concepts expected:**
- Familiarity with consensus algorithms
- Streaming analytics such as Flink
- Familiarity with some component internals: B-trees, LSM-trees, R-trees, quad-trees, inverted index

### Upper Senior

**Interview focus:** problems are likely to require stronger consistency levels.

**Concepts expected:**
- FLP impossibility result
- Clock drift
- Fluency with isolation levels
- Fluency with intermediary consistency levels such as causal consistency
- Fluency with a large variety of component internals

### Lower Staff

**Interview focus:** high-level design fluency with latency estimates (NALSD); some cost awareness in
designs; problems taken from the real world that do not have clean or happy endings.

**Concepts expected:**
- CRDT implementations and algorithms such as the Count-Min sketch
- Consensus-algorithm trade-offs (Database Internals describes several distinct consensus algorithms
  and their trade-offs)

**Note on study resources at this band:** Alex Xu's books alone are insufficient at the upper-Senior
and Staff band. They underweight partitioning-key selection, in-depth secondary-index design including
the global-versus-local choice, trade-off fluency, and causal consistency. Templated Grokking-style
low-level design is a poor model for real-world problems that lack clean solutions.

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

- **Building blocks:** the [building blocks library](../building_blocks.md) covers component
  internals, consensus, CRDTs, and partitioning strategies.
- **Reading plan:** the [reading plan](./README.md) stages the primary reading (DDIA, Database
  Internals, Understanding Distributed Systems, lectures) and marks optional depth appropriately.
- **White paper catalog:** the [white paper catalog](../white_paper.md) provides the required core set
  and optional deep-dive papers, with pedagogy for which papers address which gaps.

---

## NALSD Definition

NALSD stands for Non-Abstract Large System Design. The term originates from the Google SRE Workbook.
It refers to system design reasoning that includes concrete capacity estimates, latency calculations,
machine counts, bandwidth requirements, and cost considerations, rather than abstract architectural
diagrams alone.
