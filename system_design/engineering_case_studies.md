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

## Frontier AI Systems

This is a targeted Stage 5 branch for frontier-lab, AI infrastructure, training, inference, or agent
platform roles. It is not required for a general backend interview. Read the compact foundation, then
choose one specialization.

### Compact Foundation

| Source | Workload and constraint | Extract |
|---|---|---|
| [Google: Pathways](https://research.google/pubs/pathways-asynchronous-distributed-dataflow-for-ml/) | Heterogeneous computations gang-scheduled across thousands of accelerators | Separate asynchronous, logically centralized control from sharded data-plane execution. |
| [JAX: The Scaling Book](https://jax-ml.github.io/scaling-book/) | Models requiring combinations of data, tensor, pipeline, sequence, and expert parallelism | Build a quantitative compute, memory, and communication model before naming a parallelism strategy. |
| [OpenAI: Techniques for Training Large Neural Networks](https://openai.com/index/techniques-for-training-large-neural-networks/) | Models exceed one accelerator's memory and compute | Parallelism moves bottlenecks among memory, compute, pipeline bubbles, and communication rather than removing them. |
| [Meta: How Meta Trains Large Language Models at Scale](https://engineering.fb.com/2024/06/12/data-infrastructure/training-large-language-models-at-scale-meta/) | Long-running jobs occupy tens of thousands of GPUs and amplify rare hardware faults | Treat qualification, placement, collectives, checkpointing, spare capacity, storage, and recovery as one reliability system. |
| [Microsoft: Orca](https://www.usenix.org/conference/osdi22/presentation/yu) | Variable-length autoregressive inference with sequence dependencies | Schedule at iteration granularity and distinguish dependency-aware batching from request batching. |
| [PagedAttention and vLLM](https://arxiv.org/abs/2309.06180) | Key-value cache fragmentation limits inference batch size and throughput | Apply virtual-memory-style paging to variable sequence state and make memory allocation part of scheduling. |

### Training and Recovery

| Source | Workload and constraint | Extract |
|---|---|---|
| [Megatron-LM](https://arxiv.org/abs/1909.08053) | Transformer layers do not fit or run efficiently on one GPU | Align tensor-parallel boundaries with layer algebra and physical network topology. |
| [ZeRO](https://arxiv.org/abs/1910.02054) | Replicated parameters, gradients, and optimizer state exhaust high-bandwidth memory | Trade redundant state for communication deliberately and include transient materialization in the memory model. |
| [Meta: Building GenAI Infrastructure](https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/) | Large H100 clusters expose routing, collective startup, storage fan-in, and debugging limits | Small-cluster benchmarks do not extrapolate; topology, startup, checkpoint bursts, and observability matter at full scale. |
| [Meta: RoCE Networks for Distributed AI Training](https://engineering.fb.com/2024/08/05/data-center-engineering/roce-network-distributed-ai-training-at-scale/) | Synchronized collectives create bursty, low-entropy elephant flows | Co-design rank placement, routing, and congestion control for the actual collective traffic pattern. |
| [Orbax Checkpointing](https://orbax.readthedocs.io/en/latest/guides/checkpoint/orbax_checkpoint_101.html) | Many hosts save sharded training state asynchronously | Treat a checkpoint as a distributed commit with atomic visibility, compatible metadata, and partial-writer recovery. |

### Inference and Capacity

| Source | Workload and constraint | Extract |
|---|---|---|
| [SARATHI](https://www.microsoft.com/en-us/research/publication/sarathi-efficient-llm-inference-by-piggybacking-decodes-with-chunked-prefills/) | Compute-heavy prefills interfere with latency-sensitive decodes | Chunk work to make scheduling preemptible and constrain throughput optimization by decode latency. |
| [Splitwise](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) | Prefill and decode have different compute, memory, and power profiles | Disaggregate phases only after accounting for key-value transfer, queue coupling, admission, and failure. |
| [Google SAXML](https://github.com/google/saxml) | Many large models share accelerator slices and require loading and reconfiguration | Use a cell-level admin control plane, model-aware assignment, discovery, isolation, and reconfiguration around model servers. |
| [NVIDIA: Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) | Autoregressive serving trades first-token latency, inter-token latency, throughput, and memory | Evaluate batching, paging, quantization, speculation, and model parallelism against several SLOs, not one throughput number. |

### Agents, Evaluation, and Safety

| Source | Workload and constraint | Extract |
|---|---|---|
| [Anthropic: How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) | Long-running agents use parallel tools under token limits, partial failure, and live version changes | Persist artifacts outside context, checkpoint resumable state, trace trajectories, and run versions side by side. |
| [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Nondeterministic agents alter environments over many turns | Evaluate end-state invariants with deterministic, model, and human graders rather than prescribing one path. |
| [OpenAI Preparedness Framework](https://openai.com/safety/preparedness/) | Deployment decisions depend on severe capability evaluations and mitigations | Make thresholds, escalation ownership, reassessment, and deployment gates executable operational controls. |
| [Google DeepMind Frontier Safety Framework](https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/) | Model capability and attack techniques change after an initial assessment | Map capability evaluations to concrete security and deployment controls, then reassess as conditions change. |

Vendor and lab sources describe their own systems and incentives. Treat benchmark and cost claims as
workload-specific evidence. Prefer papers, repositories, and detailed engineering accounts over
cluster-size announcements or product marketing.

## Engineering Source Indexes

Use an index to discover a role-specific study, not as a reading assignment:

- [Uber Engineering](https://www.uber.com/us/en/blog/engineering/)
- [Pinterest Engineering](https://medium.com/pinterest-engineering)
- [Snap Engineering](https://eng.snap.com/blog)
- [Netflix TechBlog](https://netflixtechblog.com/)
- [Dropbox.Tech](https://dropbox.tech/)
- [Google Research software systems](https://research.google/research-areas/software-systems/)
- [Engineering at Meta](https://engineering.fb.com/)
- X Engineering, as a historical source whose current archive may block automated access
- [Jane Street Blog](https://blog.janestreet.com/)
- [All Things Distributed](https://www.allthingsdistributed.com/)
- [High Scalability](https://highscalability.com/)
- [System Design Primer company blogs](https://github.com/donnemartin/system-design-primer#company-engineering-blogs)
- [Engineering Blogs index](https://github.com/kilimchoi/engineering-blogs)

Some indexes contain historical or rebranded URLs, and Medium-hosted publications may block
automated clients. Confirm an article's current primary source before assigning it.
