# Core White Papers

A trimmed set of roughly eight papers, chosen because they cover the concepts that recur most
often across Senior and Senior Plus system design interviews, rather than the full list that
system design as a field has produced. Treat this as the required set. Everything else lives in
`optional_deep_dive.md`, available when a specific topic needs more depth than this set provides,
particularly if you are targeting an infrastructure or platform team.

Between the eight of these, you get the core lineage of distributed storage
(GFS leading to Bigtable leading to Spanner), the two dominant approaches to replication
(leader-based and consistency-favoring versus leaderless and availability-favoring), the standard
reference for consensus, and the standard references for batch and streaming computation.

## Consensus

- [ ] [Raft](https://raft.github.io/raft.pdf)

## Database

- [ ] [Bigtable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [ ] [Cassandra](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf)
- [ ] [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [ ] [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)

## Distributed Computation

- [ ] [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)

## Storage

- [ ] [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)

## Streaming

- [ ] [Kafka](https://cs.uwaterloo.ca/~ssalihog/courses/papers/netdb11-final12.pdf)

## How to read these for interview value, not just completion

For each paper, you should be able to answer, without rereading it, the following three
questions: what problem was this system solving that existing systems at the time did not solve,
what is the one core design decision that defines the system, and what would you reach for this
system for versus reach for one of the others in this list instead. If you cannot answer those
three questions from memory, the paper has not yet become usable interview knowledge, regardless
of whether you have technically read it.