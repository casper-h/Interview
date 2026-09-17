# System Design Curriculum

This is the canonical system design learning path. Follow the stages in order. Supporting documents exist to make this path easier to execute, not to create alternate curricula.

## How to Work Through a Stage

1. Answer the linked [companion](./companion.md) questions before reading.
2. Read one bounded topic or closely related group in order.
3. Revise the matching answers in your own words and apply the topic to a listed exercise.
4. Continue alternating reading and practice. Attempt each assigned prompt before opening a breakdown or reference solution.
5. Compare requirements and decisions, not diagrams.
6. Change one constraint and reattempt from a blank page.
7. Move on only when the observable exit criteria are reliable.

The path assumes roughly four to seven system design hours per week and commonly takes five to seven months. “Required” means complete an item before the stage exit. “Choose N” means select that many items. “Optional” and “targeted” material addresses a diagnosed gap or role. *Designing Data-Intensive Applications* (DDIA) is the conceptual spine. Hello Interview supplies interview execution, current technology framing, common patterns, “In the Wild” examples, and breakdowns. The System Design Primer supplies an early breadth pass and reference index. Papers, books, and primary engineering sources add distributed-systems and production depth.

## Stage 0: Cold Diagnostic and Format Baseline

### Learn

- Establish what you can do before learning a framework.
- Separate missing systems knowledge from interview execution problems.
- Learn the actual format of each target company without treating community reports as policy.

### Read

1. Read only the [URL shortener prompt](./practice.md#p1-url-shortener-or-paste-service). Do not read the references, framework, or a solution.

### Understand

- Your current approach to requirements, interfaces, data, scale, and failure.
- Whether time management, communication, or technical depth is the dominant gap.

### Practice

1. Design P1 aloud for 45 minutes from a blank page.
2. Record or obtain peer notes.
3. Write the three largest observable gaps and one example of each.
4. For a target interview, ask the recruiter about duration, medium, expected scope, and interview types.

### Companion Questions

[Stage 0 questions](./companion.md#stage-0-cold-diagnostic-and-format-baseline)

### Move On When

- You have a concrete review of one complete attempt.
- You can distinguish knowledge gaps from delivery gaps.
- You have not contaminated the baseline by reading a solution.

## Stage 1: Interview Process and Foundational Components

### Learn

- Lead a scoped design conversation and reach a simple end-to-end system.
- Derive APIs, data models, indexes, caches, queues, and partition keys from access patterns.
- Estimate only when the result can change a decision.

### Read

1. [System Design Framework](./framework.md).
2. Hello Interview: [Introduction](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction), [How to Prepare](https://www.hellointerview.com/learn/system-design/in-a-hurry/how-to-prepare), and [Delivery Framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery).
3. Hello Interview Core Concepts, in this order: [Networking Essentials](https://www.hellointerview.com/learn/system-design/core-concepts/networking-essentials), [API Design](https://www.hellointerview.com/learn/system-design/core-concepts/api-design), [Data Modeling](https://www.hellointerview.com/learn/system-design/core-concepts/data-modeling), [Database Indexing](https://www.hellointerview.com/learn/system-design/core-concepts/db-indexing), [Caching](https://www.hellointerview.com/learn/system-design/core-concepts/caching), [Sharding](https://www.hellointerview.com/learn/system-design/core-concepts/sharding), [Consistent Hashing](https://www.hellointerview.com/learn/system-design/core-concepts/consistent-hashing), [CAP Theorem](https://www.hellointerview.com/learn/system-design/core-concepts/cap-theorem), and [Numbers to Know](https://www.hellointerview.com/learn/system-design/core-concepts/numbers-to-know).
4. Hello Interview [Key Technologies overview](https://www.hellointerview.com/learn/system-design/in-a-hurry/key-technologies). Learn the capability of each category before product details.
5. System Design Primer: [Study Guide](https://github.com/donnemartin/system-design-primer#study-guide), [How to Approach a System Design Interview Question](https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question), [Back-of-the-Envelope Calculations](https://github.com/donnemartin/system-design-primer#back-of-the-envelope-calculations), and the topic index sections from Performance versus Scalability through Communication.
6. DDIA Chapter 1, “Reliable, Scalable, and Maintainable Applications”; Chapter 2, “Data Models and Query Languages”; Chapter 3, “Storage and Retrieval”; and Chapter 4, “Encoding and Evolution.”
7. Optional applied practice: *System Design Interview*, Volume 1, Chapters 1 to 3.

### Understand

- Functional requirements, nonfunctional requirements, invariants, and explicit non-goals.
- Acknowledged write paths, read paths, sources of truth, and derived state.
- Latency versus throughput; availability versus durability; vertical versus horizontal scaling.
- API idempotency, pagination boundaries, data modeling, indexes, caching, asynchronous work, and compatibility.
- Why an API gateway or load-balancing tier is a replicated logical role, not one unavoidable machine.

### Practice

1. Reattempt P1 and compare it with the diagnostic.
2. Design [P2 rate limiter](./practice.md#p2-rate-limiter).
3. Design [P3 distributed cache](./practice.md#p3-distributed-cache) as a diagnostic. Revisit it after Stage 2.
4. For each Hello Interview question, attempt the prompt first, identify the concepts exercised, compare decisions after the attempt, then repeat under the cataloged mutation. Start with Bitly and Rate Limiter.
5. Use one Primer solution, such as [Pastebin](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/pastebin), only after your attempt. The Primer's OOD questions and Anki decks are optional parallel recall material, not part of this HLD path.

### Companion Questions

[Stage 1 questions](./companion.md#stage-1-interview-foundations)

### Move On When

- You can produce requirements, entities, interfaces, a source of truth, and complete read and write paths in 45 minutes.
- Every component answers a requirement or measured bottleneck.
- You can explain one useful estimate and how it changed the design.
- You can answer the Stage 1 companion questions without notes and apply them to P1 or P2.

## Stage 2: Storage, Distribution, and Correctness

### Learn

- Reason from storage internals through replication, partitioning, consistency, transactions, and consensus.
- Protect application invariants without conflating distinct guarantees.
- Select data models and coordination mechanisms from workload and failure assumptions.

### Read

1. DDIA Chapters 5 to 9: “Replication,” “Partitioning,” “Transactions,” “The Trouble with Distributed Systems,” and “Consistency and Consensus.”
2. *Database Internals*, Chapters 1 to 7 for storage engines, then Chapters 8 to 14 for distributed systems. Chapters 1 to 7 are required. Chapters 8 to 14 are required for storage or infrastructure roles and optional reinforcement for generalists.
3. [The Google File System](https://research.google/pubs/the-google-file-system/), [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf), [Bigtable](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/), [Raft](https://raft.github.io/raft.pdf), [Chubby](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/), and the direct official PDF of [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf), using the assigned entries in the [paper path](./papers.md).
4. Read the historical [Cassandra paper](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf), then current Apache Cassandra documentation for [architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html), [guarantees](https://cassandra.apache.org/doc/latest/cassandra/architecture/guarantees.html), [storage engine](https://cassandra.apache.org/doc/latest/cassandra/architecture/storage-engine.html), and [repair](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/repair.html). Product semantics belong to official documentation, not the historical paper or an interview summary.
5. Hello Interview: [Cassandra](https://www.hellointerview.com/learn/system-design/deep-dives/cassandra), [DynamoDB](https://www.hellointerview.com/learn/system-design/deep-dives/dynamodb), [PostgreSQL](https://www.hellointerview.com/learn/system-design/deep-dives/postgres), [Scaling Reads](https://www.hellointerview.com/learn/system-design/patterns/scaling-reads), [Scaling Writes](https://www.hellointerview.com/learn/system-design/patterns/scaling-writes), and [Dealing with Contention](https://www.hellointerview.com/learn/system-design/patterns/dealing-with-contention).
6. [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).
7. Optional theory: [Paxos Made Simple](https://www.microsoft.com/en-us/research/publication/paxos-made-simple/).

### Understand

- B-trees, write-ahead logs, LSM trees, SSTables, compaction, recovery, and amplification.
- Single-leader, multi-leader, and leaderless replication; anti-entropy and repair.
- Partition-key locality, hot partitions, online resharding, and local versus global secondary indexes.
- Linearizability, serializability, strict serializability, snapshot isolation, causal consistency, and session guarantees.
- Consensus versus atomic commit; leases, fencing tokens, failure detection, and authority transfer.
- Why `R + W > N` gives overlap only under stated assumptions and is not a universal proof of strong consistency.
- Why synchronous replication alone does not establish linearizability.
- Dynamo, modern Cassandra, Bigtable, and Spanner as different workload and guarantee choices, not CAP labels.
- The guarantee boundaries of conflict-free replicated data types (CRDTs), including merge assumptions, metadata, deletion, and invariants they cannot preserve without coordination.

### Practice

1. Design [P4 key-value store](./practice.md#p4-key-value-store), [P5 news feed](./practice.md#p5-news-feed), and [P6 chat](./practice.md#p6-chat).
2. Design either [P11 ticket reservation](./practice.md#p11-ticket-reservation) or [P12 payments or ledger](./practice.md#p12-payments-or-ledger). Place each invariant on shards explicitly and trace an in-flight transaction through coordinator failure and resharding.
3. Revisit P3 and explain routing, replication, consistency, stampedes, failover, and online node changes.
4. Inject a hot partition, stale replica, coordinator failure, clock skew, and concurrent write into separate designs.
5. Attempt the relevant Hello Interview breakdown before viewing it. State which published decisions depend on different assumptions from yours.

### Companion Questions

[Stage 2 questions](./companion.md#stage-2-data-distribution-and-correctness)

### Move On When

- You can compare the assigned systems by data model, write path, partitioning, replication, guarantees, and recovery.
- Every coordination choice names the invariant and failure it protects.
- Migration and resharding answers include mixed routing, validation, cutover, and cleanup.
- You can answer the Stage 2 companion questions and apply them to an unfamiliar datastore prompt.

## Stage 3: Messaging, Processing, and Reliability

### Learn

- Define guarantees across producers, brokers, processors, sinks, and business effects.
- Recover batch and stream processing after partial failure.
- Design for overload, retries, tail latency, and user-relevant reliability.

### Read

1. DDIA Chapters 10 and 11: “Batch Processing” and “Stream Processing.” Chapter 12, “The Future of Data Systems,” is optional synthesis.
2. [Kafka paper and open references](https://kafka.apache.org/books-and-papers), followed by the current [Apache Kafka documentation](https://kafka.apache.org/documentation/). Product semantics belong to the versioned official documentation, not the historical paper or an interview summary.
3. [MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) and [MillWheel](https://research.google/pubs/millwheel-fault-tolerant-stream-processing-at-internet-scale/) from the [paper path](./papers.md).
4. Hello Interview: [Kafka](https://www.hellointerview.com/learn/system-design/deep-dives/kafka), [Flink](https://www.hellointerview.com/learn/system-design/deep-dives/flink), [Real-time Updates](https://www.hellointerview.com/learn/system-design/patterns/realtime-updates), [Managing Long Running Tasks](https://www.hellointerview.com/learn/system-design/patterns/long-running-tasks), and [Multi-Step Processes](https://www.hellointerview.com/learn/system-design/patterns/multi-step-processes).
5. Google SRE: [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/), [Handling Overload](https://sre.google/sre-book/handling-overload/), and [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/).
6. Site Reliability Workbook: [Implementing SLOs](https://sre.google/workbook/implementing-slos/), [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/), and [Data Processing Pipelines](https://sre.google/workbook/data-processing/).
7. *Release It!* sections “Stability Antipatterns” and “Stability Patterns.”
8. [Stripe on idempotency](https://stripe.com/blog/idempotency), [AWS on timeouts and retries](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), and [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/).

### Understand

- Work queues versus retained logs; acknowledgment, visibility, retention, ordering, replay, and consumer ownership.
- At-least-once effects, deduplication, idempotency, outbox duplicate publication, poison records, and reconciliation.
- Why “exactly once” must name a boundary and does not automatically include an external side effect.
- Batch task retry and shuffle recovery; stateful stream checkpoints and source positions.
- Event time, processing time, watermarks, allowed lateness, corrections, and cases where event time is not required.
- Lambda versus kappa architecture as different operational choices, not synonyms.
- SLIs, SLOs, error budgets, multi-window burn alerts, bounded resources, retry budgets, shedding, and degradation.

### Practice

1. Design [P7 message queue](./practice.md#p7-distributed-message-queue), [P8 notifications](./practice.md#p8-notification-system), [P9 metrics](./practice.md#p9-metrics-or-observability-platform), and [P10 job scheduler](./practice.md#p10-job-scheduler).
2. Inject duplicate publication, a poison record, replay from retention, a slow sink, retry amplification, and broker loss.
3. For one streaming design, state the checkpoint contents and the guarantee boundary for every external write. For one batch design, define attempt-isolated output and how one completed generation becomes authoritative.
4. Read Hello Interview's “In the Wild” [Slack job queue](https://www.hellointerview.com/learn/system-design/in-the-wild/slack-job-queue) only after attempting P7 or P10. Extract why the original queue failed and why the added log helped.

### Companion Questions

[Stage 3 questions](./companion.md#stage-3-messaging-processing-and-reliability)

### Move On When

- You never use an exactly-once claim without defining its scope.
- You can trace recovery after failure at each pipeline boundary.
- Your overload answer defines a trigger, rejected work, protected traffic, retry behavior, and recovery.
- You can answer the Stage 3 companion questions and mutate one design without notes.

## Stage 4: Production Architecture and Evolution

### Learn

- Design multi-region systems, capacity, cost, security, tenancy, migrations, incidents, and control planes as one operating system.
- Make failure domains and degraded behavior explicit.
- Evolve a running system without assuming an atomic cutover.

### Read

1. Site Reliability Workbook: [Non-Abstract Large System Design](https://sre.google/workbook/non-abstract-design/), [Managing Load](https://sre.google/workbook/managing-load/), [Configuration Design and Best Practices](https://sre.google/workbook/configuration-design/), and [Canarying Releases](https://sre.google/workbook/canarying-releases/).
2. Google SRE: [Managing Incidents](https://sre.google/sre-book/managing-incidents/), [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/), [Data Integrity](https://sre.google/sre-book/data-integrity/), and [Reliable Product Launches at Scale](https://sre.google/sre-book/reliable-product-launches/).
3. *Release It!* sections “Control Plane,” “Security,” “Design for Deployment,” “Handling Versions,” “Adaptation,” and “Chaos Engineering.”
4. *Building Secure and Reliable Systems*: Chapters 2, “Understanding Adversaries”; 4, “Design Tradeoffs”; 5, “Design for Least Privilege”; 8, “Design for Resilience”; 9, “Design for Recovery”; 12, “Writing Code”; and 18, “Recovery and Aftermath.”
5. [Stripe: Online Migrations at Scale](https://stripe.com/blog/online-migrations), [AWS: Static Stability Using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), and the [Cloudflare control-plane outage](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/).
6. Choose two Stage 4 sources from [Engineering Case Studies](./engineering_case_studies.md), including one migration or incident.
7. Optional by prompt: Hello Interview [Change Data Capture](https://www.hellointerview.com/learn/system-design/deep-dives/change-data-capture), [Time Series Databases](https://www.hellointerview.com/learn/system-design/deep-dives/time-series-databases), [Proximity Search](https://www.hellointerview.com/learn/system-design/deep-dives/proximity-search), and other [In the Wild](https://www.hellointerview.com/learn/system-design/in-the-wild) articles.

### Understand

- Peak capacity, headroom, failover reserve, machine count, storage, bandwidth, and dominant cost.
- Data plane versus control plane; last-known-good behavior when control operations fail.
- Regional write ownership, active-active conflict semantics, fencing, recovery objectives, residency, and reconciliation.
- Quotas, fair scheduling, cells, noisy-neighbor isolation, tenant movement, and shared dependencies outside a cell.
- Expand, migrate, and contract phases; snapshot plus change-data-capture handoff; dual-write failures; shadow reads; rollback after new-only writes.
- Threat models, authentication, authorization, least privilege, audit, key handling, abuse controls, and safe automation.
- Why keyset pagination improves continuation efficiency but is not automatically a stable snapshot.

### Practice

1. Mutate an earlier design from one region to active-active.
2. Replace its primary datastore online while old and new versions serve traffic.
3. Operate it at one-tenth the budget and then at ten times the peak.
4. Add multi-tenancy with one very large tenant, then survive a regional outage.
5. Recover from silent corruption and define detection, authority, repair, and user communication.
6. Write a short postmortem critique that separates trigger, contributing conditions, detection, response, and preventive actions.

### Companion Questions

[Stage 4 questions](./companion.md#stage-4-production-architecture-and-evolution)

### Move On When

- A capacity or cost calculation changes a design decision.
- Migration plans include mixed-version operation, validation, rollback, reconciliation, and cleanup.
- Multi-region plans identify authority and degraded behavior before traffic movement.
- Security, tenancy, and automation controls have failure and recovery behavior.
- You can answer the Stage 4 companion questions and apply them to an earlier prompt.

## Stage 5: Staff-Depth Judgment and Interview Conversion

### Learn

- Find the crux, make decisions under ambiguity, and remove unjustified complexity.
- Connect architecture to technical strategy, ownership, adoption, and organizational boundaries.
- Convert deep preparation into concise, collaborative interview performance without claiming experience you do not have.

### Read

1. Hello Interview: [5 Keys to Staff-Level System Design Interviews](https://www.hellointerview.com/blog/staff-level-system-design).
2. *Software Architecture: The Hard Parts*: Chapters 7, “Service Granularity”; 9, “Data Ownership and Distributed Transactions”; 11, “Managing Distributed Workflows”; 12, “Transactional Sagas”; 13, “Contracts”; and 15, “Build Your Own Trade-Off Analysis.”
3. *Designing Distributed Systems*: “Replicated Load-Balanced Services,” “Sharded Services,” “Ownership Election,” “Work Queue Systems,” and “Coordinated Batch Processing.”
4. [Staff Engineer Archetypes](https://staffeng.com/guides/staff-archetypes/), [What Do Staff Engineers Actually Do?](https://staffeng.com/guides/what-do-staff-engineers-actually-do/), and [Being Glue](https://noidea.dog/glue).
5. Revisit only the papers, case studies, and Hello Interview advanced topics connected to weak mock dimensions or the target role.
6. Optional applied prompts: *System Design Interview*, Volume 2, selected by gap. Do not use it as a second curriculum.

### Understand

- The difference between discussing trade-offs and making a justified decision.
- Reversible versus irreversible decisions and evidence that should reverse a choice.
- Architecture as ownership, on-call, API evolution, capacity, adoption, and deprecation boundaries.
- Sagas as one family of workflow techniques, not automatic rollback of arbitrary external effects.
- Unknown outcomes: an external timeout requires status resolution or reconciliation before compensation is assumed safe.
- Strategy as sequencing, stakeholder alignment, success measures, and explicit non-goals.
- Why interview preparation can demonstrate depth but cannot manufacture a record of Staff-level organizational impact.

### Practice

1. Apply every Staff variant in [Practice Designs](./practice.md#staff-depth-variants) across at least four different core prompts.
2. Divide one system across four teams and define APIs, ownership, on-call, migration coordination, and decision rights.
3. Present a two-stage technical strategy for a real system you know, including adoption risks and what not to build.
4. Complete at least four externally evaluated system design mocks. Reattempt weak prompts from a blank page.
5. For Hello Interview breakdowns, compare the Mid-level, Senior, and Staff expectations only after your attempt. Use them to identify missing dimensions, not wording to imitate.

### Companion Questions

[Stage 5 questions](./companion.md#stage-5-staff-depth-and-interview-conversion)

### Move On When

- Three recent, relevant mocks show consistent completion, technical correctness, prioritization, and adaptation.
- You lead without monopolizing the discussion and handle pushback without a memorized architecture.
- You can connect reliability, evolution, security, cost, and ownership to the prompt when relevant.
- You can answer Stage 5 questions and defend one strategy to a skeptical reviewer.
