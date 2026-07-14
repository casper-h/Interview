# White Papers

Two tiers in one list: a required **core set** of roughly eight papers, then an **optional deep
dive** for targeted use. Do the core set; pull from the deep dive only when a specific team or a
mock-interview gap calls for it.

## How to read these for interview value, not just completion

For each paper, you should be able to answer, without rereading it, three questions: what problem
was this system solving that existing systems at the time did not, what is the one core design
decision that defines the system, and what would you reach for this system for versus one of the
others in this list instead. If you cannot answer those three from memory, the paper has not yet
become usable interview knowledge, regardless of whether you have technically read it.

A word on scope: the core set below, plus the interview-relevant chapters of DDIA, is enough reading
to walk into any senior-level loop. The optional list is genuinely optional. It rewards a specific
team, real interest, or a longer Staff and Principal horizon, and it is also the easiest place in
this whole repo to mistake reading for progress. If the choice on a given week is one more paper from
the optional tier versus another mock or another design worked end to end, take the mock or the
design; the optional papers have the lowest interview return per hour of anything here.

---

## Core set (required)

Chosen because they cover the concepts that recur most often across senior-level system design
interviews, rather than the full list the field has produced. Between these eight you get the core
lineage of distributed storage (GFS to Bigtable to Spanner), the two dominant approaches to
replication (leader-based and consistency-favoring versus leaderless and availability-favoring), the
standard reference for consensus, and the standard references for batch and streaming computation.

**Consensus**

- [ ] [Raft](https://raft.github.io/raft.pdf)

**Database**

- [ ] [Bigtable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [ ] [Cassandra](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf)
- [ ] [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [ ] [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)

**Distributed Computation**

- [ ] [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)

**Storage**

- [ ] [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)

**Streaming**

- [ ] [Kafka](https://cs.uwaterloo.ca/~ssalihog/courses/papers/netdb11-final12.pdf)

---

## Optional deep dive

Everything below was kept out of the required core set because, for a generalist senior-level loop,
the direct interview return is lower relative to the time to read it well. None of it is low
quality. It is better suited to targeted use: a specific infrastructure or platform team, genuine
interest, or building toward Staff or Principal over a longer horizon.

Because the timeline is flexible rather than fixed, it is reasonable to work through more of this
list during Phase 2 or Phase 3 of the schedule, particularly if a mock interview surfaces a specific
gap one of these papers would directly address. The recommendation is only to keep this list
optional and pull from it deliberately, rather than treating it as required reading alongside coding,
low-level design, and behavioural prep from the start.

**Consensus**

- [ ] [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)

**Coordination**

- [ ] [ZooKeeper](https://www.usenix.org/legacy/event/atc10/tech/full_papers/Hunt.pdf)
- [ ] [Chubby](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf)

**Database**

- [ ] [F1](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41344.pdf)
- [ ] [Mesa](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42851.pdf)
- [ ] [PNUTS](https://people.mpi-sws.org/~druschel/courses/ds/papers/cooper-pnuts.pdf)
- [ ] [TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)
- [ ] [Amazon Aurora](https://web.stanford.edu/class/cs245/readings/aurora.pdf)

**Distributed Computation**

- [ ] [Dremel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36632.pdf)
- [ ] [FlumeJava](https://pages.cs.wisc.edu/~akella/CS838/F12/838-CloudPapers/FlumeJava.pdf)
- [ ] [Hive](https://www.vldb.org/pvldb/vol2/vldb09-938.pdf)
- [ ] [Percolator](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Peng.pdf)
- [ ] [Tenzing](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37200.pdf)

**Caching**

- [ ] [Scaling Memcache at Facebook](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf)

**Experimentation**

- [ ] [Online Controlled Experiments](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf)

**Observability**

- [ ] [Dapper](https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf)

**Graph**

- [ ] [GraphChi](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-126.pdf)
- [ ] [PowerGraph](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf)
- [ ] [Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf)

**Peer-to-Peer**

- [ ] [Chord](https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf)

**Search**

- [ ] [Top-m Passages](https://plg.uwaterloo.ca/~claclark/top.pdf)
- [ ] [Earlybird](https://cs.uwaterloo.ca/~jimmylin/publications/Busch_etal_ICDE2012.pdf)
- [ ] [Unicorn](https://www.vldb.org/pvldb/vol6/p1150-curtiss.pdf)
- [ ] [Google Cluster Architecture](https://static.googleusercontent.com/media/research.google.com/en//archive/googlecluster-ieee.pdf)

**Storage**

- [ ] [Erasure Coding](https://www.usenix.org/system/files/conference/atc12/atc12-final181_0.pdf)
- [ ] [Facebook's Photo Storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf)
- [ ] [GFS: Evolution on Fast-forward](https://queue.acm.org/detail.cfm?id=1594206)
- [ ] [RCFile](https://scispace.com/pdf/rcfile-a-fast-and-space-efficient-data-placement-structure-2kq37wcjl0.pdf)
- [ ] [XORing Elephants](https://arxiv.org/pdf/1301.3791)

**Streaming**

- [ ] [MillWheel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41378.pdf)
- [ ] [Photon](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41318.pdf)
