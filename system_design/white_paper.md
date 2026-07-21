# White Papers

Two groups in one list: a required **core set** of roughly eight papers, then an **optional deep
dive** for targeted use. Do the core set; pull from the deep dive only when a specific team or a
mock-interview gap calls for it.

## Reading for Interview Value

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

## Core Set (Required)

Chosen because they cover the concepts that recur most often across senior-level system design
interviews, rather than the full list the field has produced. Between these eight you get the core
lineage of distributed storage (GFS to Bigtable to Spanner), the two dominant approaches to
replication (leader-based and consistency-favoring versus leaderless and availability-favoring), the
standard reference for consensus, and the standard references for batch and streaming computation.

Two ideas from the optional tier are worth carrying as concepts even though their papers stay
optional, because they come up in reasoning at the upper-Senior and Staff range. The **FLP
impossibility** result explains why consensus protocols rely on timeouts and cannot promise both
safety and liveness under fully asynchronous conditions; understand the claim and its practical
consequence rather than the proof (see the building blocks consensus section). **Clock uncertainty**
and Spanner's TrueTime explain why globally strong consistency needs bounded-error time and a commit
wait. You do not need to read the FLP paper to use the result.

**Consensus**

- [ ] [Raft](https://raft.github.io/raft.pdf). The one to be able to explain end to end: leader
  election, log replication, and safety. For the underlying idea, keep
  [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) as a short companion
  read so you can say how Raft relates to Paxos. This is the "Raft/Paxos" pairing senior-level
  interviews expect.

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

## Optional Deep Dive

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
- [ ] [The Part-Time Parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) (Lamport's original Paxos paper; Paxos Made Simple in the core set is the accessible companion)
- [ ] [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [ ] [Unreliable Failure Detectors for Reliable Distributed Systems](https://dl.acm.org/doi/pdf/10.1145/226643.226647)
- [ ] [Implementing Fault-Tolerant Services Using the State Machine Approach](https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf)
- [ ] [Mencius](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/mao/mao.pdf)

**Coordination**

- [ ] [ZooKeeper](https://www.usenix.org/legacy/event/atc10/tech/full_papers/Hunt.pdf)
- [ ] [Chubby](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf)

**Database**

- [ ] [F1](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41344.pdf)
- [ ] [Mesa](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42851.pdf)
- [ ] [PNUTS](https://people.mpi-sws.org/~druschel/courses/ds/papers/cooper-pnuts.pdf)
- [ ] [TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)
- [ ] [Amazon Aurora](https://web.stanford.edu/class/cs245/readings/aurora.pdf)
- [ ] [Megastore](https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf)

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
- [ ] [SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf)
- [ ] [Pastry](https://www.cs.cornell.edu/courses/cs6452/2012sp/papers/pastry.pdf)

**Search**

- [ ] [Top-m Passages](https://plg.uwaterloo.ca/~claclark/top.pdf)
- [ ] [Earlybird](https://cs.uwaterloo.ca/~jimmylin/publications/Busch_etal_ICDE2012.pdf)
- [ ] [Unicorn](https://www.vldb.org/pvldb/vol6/p1150-curtiss.pdf)
- [ ] [Google Cluster Architecture](https://static.googleusercontent.com/media/research.google.com/en//archive/googlecluster-ieee.pdf)

**Storage**

- [ ] [Erasure Coding](https://www.usenix.org/system/files/conference/atc12/atc12-final181_0.pdf)
- [ ] [Facebook's Photo Storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf)
- [ ] [GFS: Evolution on Fast-forward](https://web.archive.org/web/2018/https://queue.acm.org/detail.cfm?id=1594206)
- [ ] [RCFile](https://web.archive.org/web/2018/http://www.cse.ohio-state.edu/hpcs/WWW/HTML/publications/papers/TR-11-4.pdf)
- [ ] [XORing Elephants](https://arxiv.org/pdf/1301.3791)

**Streaming**

- [ ] [MillWheel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41378.pdf)
- [ ] [Photon](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41318.pdf)

**Systems Theory**

- [ ] [Harvest, Yield, and Scalable Tolerant Systems](https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf)
- [ ] [On Designing and Deploying Internet-Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf)
- [ ] [The Tail at Scale](https://dl.acm.org/doi/pdf/10.1145/2408776.2408794)
- [ ] [Data on the Outside versus Data on the Inside](https://www.cidrdb.org/cidr2005/papers/P12.pdf)
- [ ] [CAP Twelve Years Later: How the "Rules" Have Changed](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [ ] [Why Distributed Computing?](https://www.artima.com/weblogs/viewpost.jsp?thread=4247)
- [ ] [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
- [ ] [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
- [ ] [Consistency, Availability, and Convergence](https://www.cs.cornell.edu/lorenzo/papers/cac-tr.pdf)
- [ ] [Life Beyond Distributed Transactions](https://queue.acm.org/detail.cfm?id=3025012)
- [ ] [Eventually Consistent - Revisited](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
- [ ] [Avoiding Two-Phase Commit](https://web.archive.org/web/20180821165044/http://www.addsimplicity.com/adding_simplicity_an_engi/2006/12/avoiding_two_ph.html)
- [ ] [The Log: What Every Software Engineer Should Know About Real-time Data's Unifying Abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)
- [ ] [Principles of Robust Timing over the Internet](https://dl.acm.org/doi/pdf/10.1145/1735223.1735241)
- [ ] [Building on Quicksand](https://arxiv.org/pdf/0909.1788)
- [ ] [Distributed Computing Economics](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2003-24.pdf)
