# System Design Stage Companion

This companion tests whether the reading in each curriculum stage became usable reasoning. Answer
each question aloud or in writing before opening the sample answer. The answers are calibration, not
scripts. A sufficient answer states assumptions, gives the main mechanism, names a consequential
trade-off or failure, and explains when the decision would change.

## Stage 0: Cold Diagnostic and Format Baseline

This section tests [Stage 0](./README.md#stage-0-cold-diagnostic-and-format-baseline). It has no sample architecture because the purpose is to preserve an uncontaminated baseline.

### 1. What evidence will distinguish a knowledge gap from a delivery gap?

<details>
<summary>Sample answer</summary>

Assume a recorded 45-minute attempt. A knowledge gap appears when I cannot explain a required mechanism or make a technically sound choice even with time. A delivery gap appears when I know the mechanism afterward but failed to scope, prioritize, communicate, or finish under interview conditions. The boundary is imperfect because time pressure affects recall. I would use a transcript, timestamps, and a second untimed explanation to classify the gap, then change the classification if the untimed explanation is also weak.

</details>

## Stage 1: Interview Foundations

These questions correspond to [Stage 1](./README.md#stage-1-interview-process-and-foundational-components): the framework,
Hello Interview core concepts, the System Design Primer breadth pass, and DDIA Chapters 1 to 4.

### 1. When should an estimate appear in a design interview?

<details>
<summary>Sample answer</summary>

Estimate when the result can change a decision. Peak request rate can determine whether one database
or service instance is plausible. Working-set size can justify a cache. Storage growth can determine
partitioning and retention. Fanout can rule out synchronous writes. State uncertain inputs and test
whether a different assumption changes the architecture. Arithmetic that does not affect a decision
is usually lower value than completing the design.

</details>

### 2. How should access patterns drive the data model?

<details>
<summary>Sample answer</summary>

Begin with the critical reads, writes, filters, orderings, and invariants. Choose the source of truth,
primary key, partition key, and indexes to serve those operations. A normalized relational model is
useful when transactions and flexible relationships dominate. A query-shaped or denormalized model
can reduce read work at the cost of write amplification and consistency maintenance. Derived indexes
and caches should identify their authoritative source and repair path.

</details>

### 3. When does a cache improve a design, and when does it make it worse?

<details>
<summary>Sample answer</summary>

A cache helps when reads reuse a working set and some staleness or invalidation mechanism is
acceptable. Specify placement, key, TTL, eviction, invalidation, and behavior on a miss or cache
failure. It makes the design worse when reuse is low, correctness requires every read to observe the
authoritative write, or cache loss would overload the source without protection. A cache is an
optimization and shared failure domain, not an automatic component.

</details>

### 4. Why should the first architecture be simple and complete?

<details>
<summary>Sample answer</summary>

A complete baseline proves that the required read and write paths reach authoritative state. It also
makes each later component answer a specific bottleneck or guarantee. Premature queues, caches,
shards, and services can hide a missing transaction boundary or source of truth and consume time that
should be used for the prompt's crux. Add complexity after identifying the requirement it satisfies.

</details>

### 5. What is the difference between availability, durability, and reliability?

<details>
<summary>Sample answer</summary>

Availability asks whether the service can provide an acceptable response now. Durability asks
whether acknowledged data survives defined failures. Reliability is broader: the system consistently
meets its specified behavior over time, including correctness and latency. A system can be available
while serving stale data, durable while currently unavailable, or highly available while producing
incorrect results. Define each requirement separately.

</details>

### 6. Trace one acknowledged write and one read through a simple service.

<details>
<summary>Sample answer</summary>

For the write, validate and authorize the request, apply an idempotency policy, commit to the source
of truth, and acknowledge only at the promised durability boundary. Derived indexes, caches, and
events may update synchronously or asynchronously according to their freshness contract. For the
read, identify whether the source, cache, replica, or derived view answers it and what staleness is
possible. State behavior when each dependency is slow or unavailable.

</details>

### 7. When should communication be synchronous, queued, or streamed?

<details>
<summary>Sample answer</summary>

Use a synchronous request when the caller needs the result to continue and the dependency fits the
latency and availability budget. Use a queue to buffer work, absorb bursts, retry independently, or
transfer task ownership. Use a retained stream when multiple consumers need ordered history, replay,
or continuous derived views. Every asynchronous choice must define acknowledgement, ordering,
duplicate handling, backlog, and failure visibility.

</details>

### 8. How do you choose an API, index, and initial partition key?

<details>
<summary>Sample answer</summary>

Derive the API from critical use cases, including idempotency, pagination, errors, authorization, and
compatibility. Derive indexes from filters and ordering rather than indexing every field. Choose a
high-cardinality partition key that aligns with dominant access and distributes peak load. Identify
hot-key behavior and a future resharding path even if the initial system can remain unsharded.

</details>

## Stage 2: Data, Distribution, and Correctness

These questions correspond to [Stage 2](./README.md#stage-2-storage-distribution-and-correctness): DDIA
Chapters 5 to 9, Dynamo, Raft, selected storage papers, and targeted database internals.

### 1. How do B-trees and LSM trees differ?

<details>
<summary>Sample answer</summary>

B-trees update page-oriented sorted structures and commonly provide predictable point and range
reads for mixed OLTP workloads. LSM trees buffer writes in memory, flush immutable sorted runs, and
compact them later. This can improve write throughput but introduces read, write, and space
amplification plus compaction-driven latency variance. The choice depends on read/write mix, range
queries, storage medium, cache behavior, and acceptable background work, not a rule that one is
universally faster.

</details>

### 2. How do leader-based and leaderless replication differ?

<details>
<summary>Sample answer</summary>

Leader-based replication establishes one ordered write path for a shard, simplifying conflict
handling but requiring failover and fencing. Followers may serve stale reads when replication is
asynchronous. Leaderless systems accept writes through multiple replicas and reconcile versions,
which can preserve availability during some failures but exposes conflicts, repair, and weaker
client-visible guarantees. Quorum overlap alone does not prove linearizability when membership,
sloppy quorums, concurrent writes, or conflict resolution differ from the simple model.

</details>

### 3. What is the difference between linearizability and serializability?

<details>
<summary>Sample answer</summary>

Linearizability is a real-time property of an operation history: each operation appears to take
effect atomically between invocation and response. Serializability is a transaction-isolation
property: concurrent transactions produce an outcome equivalent to some serial order, but that order
need not respect wall-clock order. Strict serializability provides both. A design should separately
state replication consistency, transaction isolation, and the application invariant being protected.

</details>

### 4. Why are consensus and two-phase commit not interchangeable?

<details>
<summary>Sample answer</summary>

Consensus lets participants agree on a value or replicated log despite specified failures. Two-phase
commit decides whether one distributed transaction commits across all participants. A transaction
coordinator can use consensus-backed durable state, but classic two-phase commit can block prepared
participants when they cannot learn the coordinator's durable decision. Participant unavailability
before prepare normally prevents commit; unavailability after a durable decision delays completion.
Replicating each participant with consensus does not remove atomic coordination across transaction
participants.

</details>

### 5. What does a safe distributed lock require beyond a lease?

<details>
<summary>Sample answer</summary>

A lease prevents a crashed holder from retaining authority forever, but a paused process can resume
after expiration and still act. A monotonically increasing fencing token lets the protected resource
reject operations from an older holder. The resource must enforce the token. If it cannot, the lock
service alone cannot prevent stale actions. The design must also define clock, session, and partition
behavior.

</details>

### 6. How do local and global secondary indexes trade off?

<details>
<summary>Sample answer</summary>

A local index is colocated and partitioned with base data, keeping index maintenance local. Queries
that lack the base partition key may need scatter-gather. A global index is partitioned by its own
key and supports direct lookup, but each base write also updates separately partitioned state. That
can require distributed coordination or expose temporary lag. State which representation is
authoritative and how incomplete or stale index entries are detected and repaired.

</details>

### 7. How would you choose and reshard a partition key under a hot-key workload?

<details>
<summary>Sample answer</summary>

Measure load by candidate key and distinguish data-size skew from request skew. Choose a key that
preserves important locality while distributing peak work. A hot logical key may need a compound key,
bucket, write shard, cache, or separate treatment. Online resharding requires an authoritative
placement map, compatible reads during movement, idempotent copying or dual routing, validation,
traffic cutover, and cleanup.

</details>

### 8. How do single-leader, multi-leader, and leaderless replication affect an invariant?

<details>
<summary>Sample answer</summary>

A single leader can serialize writes for a shard but adds leader latency and failover concerns.
Multi-leader replication supports local writes in several regions but permits concurrent conflicts
that need deterministic or application-aware resolution. Leaderless replication can accept writes
through several replicas and repair divergence, but exposes similar conflict and quorum assumptions.
An invariant such as unique ownership or conserved balance needs coordination, ownership
partitioning, escrow, or a reformulated invariant; convergence alone is insufficient.

</details>

### 9. Which isolation or consistency guarantee prevents a specific anomaly?

<details>
<summary>Sample answer</summary>

Name the anomaly first. Read committed prevents dirty reads but permits non-repeatable reads. Snapshot
isolation gives a consistent snapshot but can permit write skew across disjoint writes. Serializable
isolation prevents outcomes that cannot match a serial transaction order. Linearizability adds
real-time ordering to operations. Causal consistency preserves observed dependencies, while
read-your-writes and monotonic reads are narrower session guarantees. Choose the weakest guarantee
that protects the actual invariant and user expectation.

</details>

### 10. Compare Dynamo, Cassandra, Bigtable, and Spanner without CAP labels.

<details>
<summary>Sample answer</summary>

Dynamo emphasizes available key-value writes, consistent hashing, sloppy quorums, version conflicts,
hinted handoff, and anti-entropy. Cassandra combines Dynamo-inspired distribution with a
Bigtable-like wide-column and LSM model, with modern behavior defined by current documentation.
Bigtable provides a sorted map partitioned into tablets and uses an LSM-style storage path plus a
coordination service. Spanner combines replicated state machines, MVCC, distributed transactions,
and bounded clock uncertainty for external consistency. Compare access model, write path, indexing,
replication, conflict behavior, recovery, and operating cost for the prompt.

</details>

### 11. When does quorum overlap contribute to a linearizable register?

<details>
<summary>Sample answer</summary>

Assume a fixed replica set, strict read and write quorums, a version order, and no sloppy substitution. `R + W > N` makes every successful read quorum intersect the last successful write quorum. Intersection is necessary but not sufficient: the protocol must select the latest completed version, handle concurrent writes, prevent stale authority, and often repair or complete partially propagated writes. Sloppy quorums, membership changes, last-write-wins clocks, or reads that accept any response can break the simple argument. If the requirement is only eventual or session consistency, the extra coordination may not be justified.

</details>

### 12. Why does synchronous replication not by itself provide linearizability?

<details>
<summary>Sample answer</summary>

Synchronous replication defines which replica acknowledgments are required before a write returns. Linearizability also requires one valid operation order that respects real time. The design must prevent split authority, order concurrent writes, route reads to state that includes completed writes, and fence an old leader during failover. A synchronously copied value can still be followed by a stale replica read or conflicting leader write. The answer changes if a consensus protocol and linearizable read mechanism provide those missing properties.

</details>

### 13. How should a sharded design preserve a transaction invariant?

<details>
<summary>Sample answer</summary>

First state the invariant and try to colocate all state needed to enforce it on one shard. An account-local uniqueness rule may fit one owner shard; a transfer across two account shards does not. Cross-shard choices include a serializable distributed transaction with durable atomic commit, escrow or reservations that preallocate rights, single-owner routing, or reformulating the product guarantee. Two-phase commit can leave prepared participants waiting when the decision is unavailable, so participants and the coordinator need durable, often consensus-replicated state, idempotent retries, and status resolution for unknown outcomes. Resharding must preserve one authority and account for in-flight transactions. If weaker semantics are acceptable, reconciliation may replace synchronous coordination, but it must not silently violate money, inventory, or uniqueness invariants.

</details>

### 14. What can and cannot be inferred from a CRDT?

<details>
<summary>Sample answer</summary>

Assume a specific conflict-free replicated data type (CRDT). A state-based CRDT needs an associative, commutative, and idempotent merge over its state lattice. An operation-based CRDT instead depends on its operation algebra and delivery assumptions, commonly reliable causal delivery with concurrent operations that commute. Replicas can then converge without coordinating every update. That does not preserve arbitrary cross-object invariants, authorization decisions, global uniqueness, or an ordinary counter that must never exceed a bound. Deletion may require tombstones or causal context, and metadata can grow. Escrow-like bounded counters protect some limits by distributing rights, but they change the data type and availability trade-off. Use a CRDT only when its semantics and delivery model match the product operation.

</details>

## Stage 3: Messaging, Processing, and Reliability

These questions correspond to [Stage 3](./README.md#stage-3-messaging-processing-and-reliability):
DDIA Chapters 10 and 11, Kafka, MapReduce, SRE, *Release It!*, Stripe idempotency, and *The Tail at
Scale*.

### 1. What must an exactly-once claim define?

<details>
<summary>Sample answer</summary>

It must define the boundary. A broker may deduplicate producer writes, a processor may restore state
and offsets atomically, and a transactional sink may commit output once within one system. None of
those automatically guarantees one external business effect. A common design uses at-least-once
publication, an idempotency key, and a consumer transaction that commits the deduplication record and
business mutation together. Unknown outcomes still require status lookup or reconciliation.

</details>

### 2. Queue or retained log: how do you choose?

<details>
<summary>Sample answer</summary>

Choose consumption and retention semantics first because products overlap. Consumer groups can
distribute log partitions among workers, and some queues support fanout or replay. Choose a work
queue when one worker should claim a task and the system primarily needs scheduling,
acknowledgement, retry, priority, or visibility timeout. Choose a retained log when multiple
independent consumers need the same ordered history, replay, stream processing, or change-data
capture. Ordering is normally scoped to a partition or key. Retention, consumer lag, rebalancing,
poison records, and per-tenant fairness are explicit design concerns.

</details>

### 3. How do batch and stream processing differ?

<details>
<summary>Sample answer</summary>

Batch processes a finite input and optimizes throughput, locality, and repeatable recomputation.
Streaming continuously processes an unbounded input and must manage backpressure and recovery when it holds state. Event-time windows additionally need event timestamps, watermarks, and a lateness policy when business meaning depends on occurrence time; stateless transforms or processing-time workflows may not. An algorithm can be mathematically exact while its execution still publishes duplicate or partial effects. Batch recovery needs attempt-isolated outputs and a single committed generation or an idempotent sink. A lambda architecture duplicates batch and speed paths and must reconcile them. A kappa architecture replays retained history through one processing model, but requires sufficient retention, replay capacity, versioned code and schemas, and safe replacement of live output.

</details>

### 4. How do retries cause cascading failure?

<details>
<summary>Sample answer</summary>

When a dependency slows, callers retain resources longer and may retry, multiplying load precisely
when capacity is lowest. Queues, connection pools, and threads fill, so latency spreads upstream.
Mitigations include end-to-end deadlines, bounded retry budgets, exponential backoff with jitter,
idempotency, concurrency limits, circuit breaking, load shedding, and degraded responses. Recovery
must account for cold caches and synchronized retry waves.

</details>

### 5. What should an SLO and alert describe?

<details>
<summary>Sample answer</summary>

An SLI measures a user-relevant property such as successful request rate, latency, freshness, or
correctness. An SLO sets the target over a window. Alerts should primarily detect actionable threats
to that objective, while diagnostic metrics explain causes. Component health alone can miss user
impact, and a single latency average can hide the tail. The design should connect the error budget to
release and reliability decisions. Define the eligible event population and good-event threshold,
then alert on fast and sustained error-budget burn over appropriate windows. Specify low-traffic
handling, ownership, and the expected response.

</details>

### 6. Trace recovery across a queue or stream pipeline.

<details>
<summary>Sample answer</summary>

A producer timeout leaves an unknown publication outcome, so retry with an idempotent producer key or
query status. Broker failure recovers from replicated durable data according to the acknowledgement
policy. A processor restores a consistent checkpoint containing state and source positions, then
replays later records. A sink must deduplicate or transact output with progress. Region loss requires
an explicit recovery point, ownership transition, backlog plan, and reconciliation before normal
traffic resumes.

</details>

### 7. How should a pipeline handle a poison record while preserving progress?

<details>
<summary>Sample answer</summary>

Classify transient and permanent errors. Retry transient failures with a bound and backoff. After the
bound, quarantine the record with its payload, schema, error, source position, and attempt history so
the partition can progress. Alert on quarantine rate and provide controlled replay after the cause is
fixed. If strict ordering forbids skipping, isolate the affected key or stop deliberately and surface
the availability trade-off.

</details>

### 8. What concrete signal should trigger load shedding, and what happens next?

<details>
<summary>Sample answer</summary>

Use a bounded resource signal tied to user impact, such as concurrency saturation, queue age,
deadline exhaustion, or error-budget burn, rather than CPU alone. Reject low-priority or excess work
before consuming the constrained dependency. Preserve critical traffic, return explicit retry
guidance where safe, and cap retries. Metrics show scope and impact, traces locate slow paths, and
structured logs explain individual decisions or failures.

</details>

### 9. Why does fanout amplify tail latency, and when is hedging safe?

<details>
<summary>Sample answer</summary>

A request that waits for many parallel subrequests is exposed to the slowest tail of the group, so a
rare per-node delay becomes common at the aggregate request level. Hedging can issue a duplicate only
after a delay threshold and use the first acceptable result. It is safest for idempotent reads with
cancellation and spare capacity. Unbounded speculative work increases load and can worsen the
overload that caused the tail, so cap it, measure amplification, and disable it under saturation.

</details>

### 10. Define producer and consumer acknowledgment for a work queue.

<details>
<summary>Sample answer</summary>

Assume a durable queue with at-least-once delivery. Producer acknowledgment states when the broker has durably accepted the message and under which replica failures it survives. Consumer delivery grants a claim or visibility lease; worker death or lease expiry makes the item eligible for redelivery. Deletion or offset advancement occurs only after the protected effect is durable. If the effect commits before acknowledgment, redelivery can duplicate it, so use a stable operation identity and idempotent or transactional sink. If acknowledgment occurs first, a crash can lose the effect. Lease renewal and stale acknowledgments also need ownership checks. Strict ordering may force an affected key to stop rather than skip a poison item.

</details>

### 11. What failure window remains in an outbox design?

<details>
<summary>Sample answer</summary>

Assume the business mutation and outbox row commit in the same transactional database. That closes the gap between those two records, but the relay can crash after publishing and before marking the row, so publication remains at least once. Give the event a stable identity, make consumers idempotent or transact deduplication with their mutation, bound and observe relay retries, quarantine malformed rows, retain enough history for recovery, and reconcile broker and database state. An outbox spanning nontransactional stores does not provide the same atomic boundary.

</details>

### 12. How should an external timeout with unknown outcome be resolved?

<details>
<summary>Sample answer</summary>

Record an internal operation with a stable idempotency key and a `pending` or `unknown` state before calling the provider. After timeout, do not assume failure and issue a compensating effect blindly. Use the provider's idempotency contract, status API, reference, or correlated webhook to establish authority. Bound retries and poll duration, reconcile disagreements or delayed finality, and route unresolved cases for controlled review. Compensation is safe only after the original outcome and the compensating operation's own idempotency boundary are known. If the provider offers neither status nor idempotency, the product must accept residual risk or use a different integration.

</details>

## Stage 4: Production Architecture and Evolution

These questions correspond to
[Stage 4](./README.md#stage-4-production-architecture-and-evolution): non-abstract large system design, online migrations,
postmortems, multi-region incidents, security, and selected engineering case studies.

### 1. What makes a capacity estimate useful?

<details>
<summary>Sample answer</summary>

Start with peak workload, per-unit resource demand, a tested or stated capacity assumption, headroom,
replication, and failure reserve. Convert that into partitions, machines, storage, and bandwidth.
Then identify sensitivity and the dominant cost. The estimate is useful only when it changes a
decision, exposes an impossible target, or defines when the architecture must evolve.

</details>

### 2. What is the difference between a control plane and a data plane?

<details>
<summary>Sample answer</summary>

The data plane handles the primary workload, such as serving reads, forwarding traffic, or processing
messages. The control plane manages placement, configuration, membership, policy, or lifecycle. A
control plane may be logically centralized without carrying data-plane throughput, but its loss can
still prevent changes or recovery. Define which existing data-plane operations continue during
control-plane failure and protect control actions with validation, rate limits, and rollback.

</details>

### 3. What are the phases of a safe online migration?

<details>
<summary>Sample answer</summary>

Make schemas and code compatible first. Establish propagation to the new representation, backfill
historical data, and measure completeness. Shadow or compare reads, then move a small percentage of
traffic with explicit rollback criteria. Separate read cutover from write authority when useful.
Reconcile divergence, complete the cutover, and remove obsolete paths only after the confidence
window. Define an ordered snapshot-to-CDC handoff, idempotent backfill, mixed-version operation,
per-record validation, and the exact write-authority transition. Dual writes need a partial-failure
policy, and rollback may require a reverse migration after new-only writes begin.

</details>

### 4. How do cells and multi-tenancy change failure isolation?

<details>
<summary>Sample answer</summary>

A cell contains a full serving stack for a bounded set of tenants or users, limiting deployment and
runtime blast radius. Shared multi-tenant infrastructure improves utilization but can create noisy
neighbors and correlated failures. Define placement, routing, quotas, fair scheduling, tenant-level
metrics, rebalancing, and capacity reserve. Cells add operational duplication and uneven utilization,
so their isolation benefit must justify that cost. Enumerate shared databases, control planes,
identity services, deployment systems, and regional networks outside the cell because they determine
the real correlated-failure boundary.

</details>

### 5. What distinguishes a useful postmortem from an incident narrative?

<details>
<summary>Sample answer</summary>

A useful postmortem quantifies impact, separates trigger from contributing system conditions,
explains why safeguards and detection did not contain the event, and avoids individual blame. Actions
have owners, priorities, and measurable completion criteria. Strong actions improve classes of
failure through limits, validation, testing, isolation, or recovery rather than patching only the
triggering command. Each action should include an effectiveness signal and a later verification step,
not only an owner and completion state.

</details>

### 6. How should a multi-region system assign write ownership and fail over?

<details>
<summary>Sample answer</summary>

Choose ownership per data item or operation. A regional primary simplifies conflicts but adds remote
write latency and failover coordination. Active-active writes require conflict semantics or
coordination that preserve the invariant. Define partition behavior, fencing during ownership
transfer, recovery point and time objectives, residency constraints, degraded operation, cold-start
capacity, and post-failover reconciliation. Automatic traffic movement is unsafe if data authority
has not moved consistently.

</details>

### 7. How do you isolate and attribute multi-tenant load?

<details>
<summary>Sample answer</summary>

Measure usage by tenant and shared resource. Apply quotas, concurrency limits, fair scheduling, and
priority before a tenant exhausts common pools. Attribute storage, compute, and egress for capacity
and cost decisions. Large or regulated tenants may require dedicated shards or cells. The design must
handle hot-tenant movement without violating data ownership or creating an unbounded rebalancing
event.

</details>

### 8. What security questions belong in a production design?

<details>
<summary>Sample answer</summary>

Identify actors and trust boundaries, then define authentication and resource-level authorization.
Protect service identity and secrets, encrypt data in transit and at rest, constrain privileged
operations, and audit sensitive access and mutations. Include abuse limits, retention, deletion,
residency, key rotation, and tenant isolation where relevant. Security controls require failure and
recovery behavior, not a closing statement that encryption will be added.

</details>

### 9. How do safe automation and recovery fit together?

<details>
<summary>Sample answer</summary>

Automation needs scoped permissions, validation, rate and blast-radius limits, staged rollout,
health gates, an emergency stop, and tested rollback. Recovery defines who owns the decision, how
authority moves, what state may be lost, and how service is restored without causing a second
overload. Afterward, reconcile divergent or delayed state and verify the corrective action reduced
recurrence or recovery time.

</details>

## Stage 5: Staff Depth and Interview Conversion

These questions correspond to
[Stage 5](./README.md#stage-5-staff-depth-judgment-and-interview-conversion): crux identification,
simplification, decision making, strategy, ownership, adoption, and targeted depth.

### 1. How do you identify the crux of a design prompt?

<details>
<summary>Sample answer</summary>

Ask which requirement makes the problem different from ordinary CRUD and which failure would violate
the most important invariant or objective. The crux may be contention, fanout, ordering, global
latency, safe execution, migration, or cost. Form a hypothesis early, build a simple complete system,
and spend deep-dive time on the decision most sensitive to that hypothesis. Revise it when the
interviewer adds evidence.

</details>

### 2. What does simplifying a Staff-depth design mean?

<details>
<summary>Sample answer</summary>

It means removing components, guarantees, or organizational boundaries that do not earn their cost.
Start from the stated scale and failure requirements, not a large company's final architecture.
Explain what one database, one service, a managed system, or weaker consistency can support and the
threshold that requires evolution. Simplicity includes operational ownership and coordination cost,
not only the number of boxes.

</details>

### 3. How should a candidate make a decision under ambiguity?

<details>
<summary>Sample answer</summary>

State the assumptions and the decision criterion, choose the best option under those assumptions,
name the strongest rejected alternative, and explain its cost. Identify the evidence that would
reverse the choice. This is stronger than listing trade-offs indefinitely or pretending uncertainty
does not exist. Prefer reversible experiments when evidence is cheap and reserve heavier analysis
for irreversible or high-blast-radius decisions.

</details>

### 4. How do organizational boundaries affect architecture?

<details>
<summary>Sample answer</summary>

Every service or platform boundary creates ownership, on-call, API evolution, capacity, and roadmap
coordination. A technically elegant split can fail if no team can operate it or adoption requires too
many synchronized migrations. Define the owner, consumer contract, success metric, rollout sequence,
support model, and deprecation path. Prefer boundaries that let teams change independently while
keeping invariants enforceable.

</details>

### 5. How do you use a production case study in an interview without copying it?

<details>
<summary>Sample answer</summary>

Extract the workload, constraints, failure history, and decision principle. Compare those assumptions
with the interview prompt before borrowing a mechanism. Explain why the published system needed its
complexity and what a smaller system should omit. Use the case as evidence for a trade-off or failure
mode, not as authority that one company's design is universally correct.

</details>

### 6. What belongs in a two-stage technical strategy?

<details>
<summary>Sample answer</summary>

Start with the business or reliability outcome and current constraint. Stage one should test the
highest-risk assumption through reversible work and deliver measurable value. Stage two makes the
larger commitment only after evidence supports it. Identify stakeholders, ownership, adoption
incentives, compatibility, support, success measures, irreversible decisions, deprecation, and what
will deliberately not be built. Include the signals that stop, revise, or accelerate the strategy.

</details>

## Sufficiency Check

The sample answers calibrate the concepts they directly address. The stage exit criteria and practice
designs test whether those concepts can be selected and applied under ambiguity. If an answer remains
memorized prose, return to its assigned reading and apply it to a design. Recall without application
is not sufficient preparation.
