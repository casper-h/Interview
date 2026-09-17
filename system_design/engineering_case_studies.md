# Engineering Case Studies

Primary engineering material shows why a real system accepted complexity. Extract the workload, constraints, invariant, central decision, failure domain, operating cost, and what would be excessive for a smaller system. The stage column is the canonical assignment.

## Core Studies

| Stage | Source | Workload and constraints | Extract |
|---:|---|---|---|
| 2 | [Meta: TAO, the power of the graph](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/) | Social graph reads at extreme scale with geographically distributed caches and hot objects | Shape an API around dominant access patterns; make selective consistency and cache coherence explicit. |
| 2 | [Uber: Schemaless, Part One](https://www.uber.com/us/en/blog/schemaless-part-one-mysql-datastore/) | Mission-critical trip data, high writes, asynchronous indexes, and strong MySQL operating experience | Append-only versioned records can simplify change capture and recovery; operational familiarity is a valid constraint. |
| 3 | [Stripe: Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) | Financial mutations over unreliable networks with ambiguous outcomes | Give operations stable identities, persist outcomes, and combine safe retry with status resolution. |
| 3 | [AWS: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Deep service stacks where retries amplify an outage | Budget end-to-end deadlines, retry at a controlled layer, cap attempts, and add jitter. |
| 3 | [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) | Queues, retries, cold caches, health checks, and reduced capacity form positive feedback | Bound resources, fail cheaply, degrade deliberately, and test through breakage and recovery. |
| 3 | [Slack: Scaling Slack's Job Queue](https://slack.engineering/scaling-slacks-job-queue/) | An in-memory Redis queue could not recover while producers continued to overwhelm it | A durable log can decouple acceptance from the queue and permit controlled replay, but adds another operated system. |
| 4 | [AWS: Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) | A regional service must survive zone loss when replacement capacity or control-plane actions are unavailable | Pre-provision failure reserve and let the data plane continue from last-known-good configuration. |
| 4 | [Cloudflare: Control-plane and analytics outage](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/) | Facility loss exposed hidden local dependencies while the edge data plane mostly continued | Test removal of whole failure domains, inventory transitive dependencies, and control recovery load. |
| 4 | [Discord: How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) | Hot partitions, compaction debt, tail latency, and a no-downtime Cassandra-to-ScyllaDB migration | Fix access patterns, isolate workload, dual-write, shadow-read, checkpoint backfill, and preserve reversal. |
| 4 | [Slack: Scaling datastores with Vitess](https://slack.engineering/scaling-datastores-at-slack-with-vitess/) | Thousands of MySQL hosts, workspace hotspots, compatibility requirements, and gradual adoption | Introduce routing and operations incrementally, prove semantics with shadow traffic, and make ownership explicit. |
| 4 | [Cloudflare: July 2, 2019 outage](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/) | A pathological WAF rule consumed CPU globally through rapid configuration propagation | Treat configuration as production code with cost limits, staged rollout, independent kill switches, and emergency access. |

## Targeted Studies

| Stage | Source | Use when studying | Extract |
|---:|---|---|---|
| 2 | [Meta: CacheLib](https://engineering.fb.com/2021/09/02/open-source/cachelib/) | Cache policy, memory cost, or heterogeneous workloads | Standardize the substrate while keeping admission, eviction, and allocation policy measurable and pluggable. |
| 3 | [Stripe: Canonical log lines](https://stripe.com/blog/canonical-log-lines) | Logging and telemetry schema | Prefer information-dense, stable request records that support unanticipated analysis. |
| 4 | [Microsoft: Socrates](https://www.microsoft.com/en-us/research/publication/socrates-the-new-sql-server-in-the-cloud/) | Cloud databases and disaggregation | Separate compute, durable log, page storage, and backup while preserving database semantics. |
| 4 | [Microsoft: Autopilot](https://www.microsoft.com/en-us/research/publication/autopilot-automatic-data-center-management/) | Fleet automation and repair | Applications must expose coherent health and control loops before automation can manage them safely. |
| 4 | [Meta: October 4, 2021 outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) | Network control planes and incident recovery | Understand safeguard failure, out-of-band access, dependency restoration order, and recovery-induced load. |
| 4 | [LinkedIn: Kafka at seven trillion messages per day](https://www.linkedin.com/blog/engineering/open-source/apache-kafka-trillion-messages) | Very large logs and metadata control planes | Metadata scale, controller behavior, maintenance state, and upgrade testing can dominate data throughput. |
| 5 | [OpenAI: Scaling Kubernetes to 7,500 nodes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/) | ML training platforms and very large cluster control planes | Look for quadratic control behavior, isolate control components, filter telemetry, smooth admission, and test hardware. |
| 5 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Agent or ML application infrastructure | Start with deterministic workflows; add autonomy only when measured quality justifies latency, cost, tool, and safety complexity. |

The System Design Primer's [real-world architectures](https://github.com/donnemartin/system-design-primer#real-world-architectures) and [company engineering blogs](https://github.com/donnemartin/system-design-primer#company-engineering-blogs) are useful indexes for role-specific exploration. Many linked architectures are historical. Confirm current official sources before describing modern product behavior.
