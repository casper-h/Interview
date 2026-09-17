# Practice Designs

For every prompt, use four passes:

1. **Attempt:** Design from a blank page before opening a solution.
2. **Compare:** Compare requirements, guarantees, and decisions with the references. Do not memorize their architecture.
3. **Mutate:** Apply the listed constraint change or a Staff-depth variant.
4. **Reattempt:** Redesign aloud without notes and explain what changed.

## Core Catalog

“Core” describes coverage, not an instruction to complete all twelve before interviewing. Each stage says which prompts are required or offers a choice.

### P1: URL Shortener or Paste Service

- **Stage:** 0 and 1.
- **Prerequisites:** None for the diagnostic; Stage 1 before the second attempt.
- **Tests:** Requirements, identifier generation, API design, data model, cache, expiration, abuse, and decision-relevant estimation.
- **Mutation:** Links can be edited while analytics must preserve the historical destination.
- **References:** [Hello Interview Bitly](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly); [Primer Pastebin](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/pastebin).

### P2: Rate Limiter

- **Stage:** 1.
- **Prerequisites:** APIs, caching, and basic partitioning.
- **Tests:** Limit semantics, token bucket or sliding windows, atomic updates, distributed enforcement, fairness, and failure behavior.
- **Mutation:** Enforce hierarchical limits by user, tenant, endpoint, and region during a control-plane outage.
- **References:** [Hello Interview Distributed Rate Limiter](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter); *System Design Interview*, Volume 1, “Design A Rate Limiter.”

### P3: Distributed Cache

- **Stage:** 1 diagnostic and Stage 2 full design.
- **Prerequisites:** Caching, consistent hashing, replication, and failure detection.
- **Tests:** Routing, eviction, consistency, stampedes, hot keys, membership changes, replication, and failure recovery.
- **Mutation:** Lose an entire cache cluster while the source database has little spare capacity.
- **References:** [Hello Interview Distributed Cache](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-cache); [Scaling Memcache at Facebook](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala).

### P4: Key-Value Store

- **Stage:** 2.
- **Prerequisites:** Storage engines, replication, partitioning, consistency, and consensus.
- **Tests:** API and data model, partition map, replication, quorum assumptions, conflict resolution, durability, repair, and resharding.
- **Mutation:** Add compare-and-set with linearizable semantics for selected keys without imposing it on every operation.
- **References:** [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf); [Bigtable](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/); *System Design Interview*, Volume 1, “Design A Key-value Store.”

### P5: News Feed

- **Stage:** 2.
- **Prerequisites:** Data modeling, caching, partitioning, and asynchronous work.
- **Tests:** Fanout-on-write versus fanout-on-read, celebrity skew, ranking, pagination, deletions, freshness, and cache invalidation.
- **Mutation:** A privacy change must remove a post from every derived feed quickly and audibly.
- **References:** [Hello Interview FB News Feed](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed); [TAO](https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson).

### P6: Chat

- **Stage:** 2.
- **Prerequisites:** Partitioning, ordering, data modeling, and session guarantees.
- **Tests:** Connection management, conversation ordering, delivery and read receipts, offline sync, group fanout, media, and multi-device state.
- **Mutation:** Support active-active regional writes while preserving per-conversation order and avoiding split ownership.
- **References:** [Hello Interview WhatsApp](https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp); System Design Primer additional question “Design a chat app like WhatsApp.”

### P7: Distributed Message Queue

- **Stage:** 3.
- **Prerequisites:** Logs, replication, consumer state, and idempotency.
- **Tests:** Queue versus log semantics, partitioning, ordering, acknowledgment, visibility, retention, retry, poison messages, replay, and backpressure.
- **Mutation:** Add scheduled delivery and strict ordering per account without allowing one poison message to block unrelated accounts.
- **References:** [Hello Interview Kafka](https://www.hellointerview.com/learn/system-design/deep-dives/kafka); [Kafka books and papers](https://kafka.apache.org/books-and-papers); *System Design Interview*, Volume 2, “Distributed Message Queue.”

### P8: Notification System

- **Stage:** 3.
- **Prerequisites:** Queues, idempotency, retries, and user preferences.
- **Tests:** Channel routing, templates, provider failure, deduplication, priority, rate limits, scheduling, preferences, and delivery observability.
- **Mutation:** A provider timeout has an unknown outcome and duplicate messages are legally sensitive.
- **References:** [Hello Interview Notification System](https://www.hellointerview.com/learn/system-design/problem-breakdowns/notification-system); *System Design Interview*, Volume 1, “Design A Notification System.”

### P9: Metrics or Observability Platform

- **Stage:** 3.
- **Prerequisites:** Streams, aggregation, time-series storage, SLOs, and multi-tenancy.
- **Tests:** Ingestion, cardinality, labels, rollups, retention, query fanout, alert evaluation, late data, and tenant isolation.
- **Mutation:** Cut cost by 70 percent without weakening paging SLOs.
- **References:** [Hello Interview Metrics Monitoring](https://www.hellointerview.com/learn/system-design/problem-breakdowns/metrics-monitoring); [Monarch](https://research.google/pubs/monarch-googles-planet-scale-in-memory-time-series-database/).

### P10: Job Scheduler

- **Stage:** 3.
- **Prerequisites:** Queues, leases, fencing, retries, and checkpoints.
- **Tests:** Scheduling, dependencies, worker ownership, duplicate execution, heartbeats, retries, priorities, fairness, and long-running recovery.
- **Mutation:** Some jobs cannot be repeated, but workers can lose contact after causing an external effect.
- **References:** [Hello Interview Job Scheduler](https://www.hellointerview.com/learn/system-design/problem-breakdowns/job-scheduler); [Managing Long Running Tasks](https://www.hellointerview.com/learn/system-design/patterns/long-running-tasks).

### P11: Ticket Reservation

- **Stage:** 2 and 4.
- **Prerequisites:** Transactions, isolation, leases, queues, and overload.
- **Tests:** Inventory invariants, holds, expiration, payment unknown outcomes, contention, fairness, hot events, and reconciliation.
- **Mutation:** A flash sale creates 100 times normal peak and requires a waiting room with auditable fairness.
- **References:** [Hello Interview Ticketmaster](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster); *System Design Interview*, Volume 2, “Hotel Reservation System.”

### P12: Payments or Ledger

- **Stage:** 2 and 4.
- **Prerequisites:** Transactions, idempotency, unknown outcomes, audit, and reconciliation.
- **Tests:** Money conservation, double entry, authorization versus capture, provider integration, idempotency, immutable history, disputes, and regional ownership.
- **Mutation:** Migrate from one payment processor to two while preserving status resolution and reconciliation.
- **References:** [Hello Interview Payment System](https://www.hellointerview.com/learn/system-design/problem-breakdowns/payment-system); [Stripe idempotency](https://stripe.com/blog/idempotency); *System Design Interview*, Volume 2, “Payment System.”

## Targeted Prompts

Use these when a stage outcome or target role calls for them:

| Prompt | Stage | Primary concepts | Suggested reference |
|---|---:|---|---|
| Blob or photo storage | 2 | Metadata, object placement, small files, CDN, repair | [Haystack](https://www.usenix.org/conference/osdi10/finding-needle-haystack-facebooks-photo-storage) |
| Collaborative document | 2 or 4 | Concurrency, operation ordering, offline clients, history | [Hello Interview Google Docs](https://www.hellointerview.com/learn/system-design/problem-breakdowns/google-docs) |
| Web crawler | 3 | Frontier scheduling, politeness, deduplication, retries, storage | [Primer Web Crawler](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/web_crawler) |
| Real-time aggregation | 3 | Windows, watermarks, state, replay, correction | [MillWheel](https://research.google/pubs/millwheel-fault-tolerant-stream-processing-at-internet-scale/) |
| Proximity service | 4 | Spatial indexes, partitioning, freshness, uneven density | [Hello Interview Proximity Search](https://www.hellointerview.com/learn/system-design/deep-dives/proximity-search) |
| Authorization service | 4 | Relationship model, consistency, caching, audit | [Zanzibar](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/) |
| ML training platform | 4 or 5 | Scheduling, quotas, checkpoints, data locality, control planes | [OpenAI Kubernetes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/) |

## Staff-Depth Variants

Apply these to completed prompts rather than treating them as separate canned designs:

1. Move from one region to active-active.
2. Replace the primary datastore online.
3. Operate at one-tenth the budget.
4. Handle ten times the peak.
5. Add multi-tenancy and noisy-neighbor isolation.
6. Survive a regional outage without depending on a healthy control plane.
7. Recover from silent corruption.
8. Divide ownership across several teams.
9. Meet a new residency, audit, deletion, or encryption requirement.
10. Migrate from an existing monolith without a flag day.
