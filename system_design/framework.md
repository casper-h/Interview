# System Design Interview Framework

Use this as a recovery structure, not a script. A typical 45-minute interview may spend about 5 minutes on requirements, 5 minutes on entities and interfaces, 10 to 15 minutes on the high-level design (HLD), and the remaining time on deep dives. Follow interviewer signals and the prompt's crux.

## 1. Frame the Problem

Clarify the users and prioritize roughly three core functional requirements. State non-goals. Ask for or propose scale, latency, availability, durability, consistency, security, and compliance requirements only when material.

Write the important invariants in plain language. Examples include “a seat is sold at most once,” “money is conserved,” or “an acknowledged message survives one broker failure.” Do not choose a consistency or transaction mechanism before naming what it protects.

Estimate a quantity only if it may alter the architecture. Useful estimates include peak requests per second, fanout, working-set size, storage growth, bandwidth, and required failure reserve. State assumptions and sensitivity.

## 2. Define Entities and Interfaces

Identify the minimum durable entities and their ownership. Sketch the API or event contract for critical flows, including identifiers, idempotency, pagination, errors, authorization, and compatibility.

For pagination, state ordering and mutation behavior. Keyset pagination can avoid large offsets, but it does not provide a stable snapshot unless the data source and cursor encode the required snapshot semantics.

## 3. Draw a Simple Complete System

Show one end-to-end write and read path through a replicated logical gateway or load-balancing tier, stateless application logic where appropriate, and an authoritative store. Add a cache, queue, stream, search index, or specialized store only after identifying the requirement it serves.

For every component, state:

- why it exists;
- its partition or routing key;
- what state is authoritative;
- when a caller receives acknowledgment;
- how it fails and recovers.

## 4. Deep Dive on the Crux

Choose the one or two decisions that make this prompt unusual. Common cruxes are fanout, contention, ordering, hot keys, global latency, a strict invariant, replay, migration, or cost.

Compare viable options, then decide. State the rejected alternative and the requirement or evidence that would reverse the decision.

Keep guarantees separate:

- Linearizability concerns real-time ordering of operations.
- Serializability concerns equivalence to a serial transaction order.
- Strict serializability provides both.
- Replication mode, isolation level, durability, and availability are separate choices.
- Consensus agrees on ordered state despite a defined failure model.
- Two-phase commit coordinates atomic transaction outcome across participants.

## 5. Test Failure and Evolution

Inject slow dependencies, timeout with unknown outcome, duplicate requests, stale replicas, partitions, hot tenants, overload, corruption, and regional loss where relevant.

For asynchronous flows, define ordering, retry ownership, deduplication, poison-record handling, replay, backlog limits, and reconciliation. An outbox can atomically record a business mutation and publication intent. It does not prevent duplicate publication by itself.

For leases, explain how the protected resource rejects stale holders with fencing or equivalent authority checks.

Explain how the system changes online: compatible code and schema, backfill, validation, shadowing, gradual cutover, mixed-version operation, rollback, reconciliation, and cleanup.

## 6. Close

Summarize the requirements met, the main decision, the largest remaining risk, and the next measurement or experiment. Do not end with a list of technologies.
