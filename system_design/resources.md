# Resource Roles and Book Assignments

Use this page to understand why a source exists. The curriculum in [README](./README.md) contains the required order and exact assignments.

## Core Sources

| Source | Role | Required scope |
|---|---|---|
| [Hello Interview System Design](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) | Delivery framework, core concepts, technologies, patterns, advanced topics, “In the Wild,” breakdowns, and level-aware practice | Assigned sections in Stages 1 to 5 |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | Early breadth, estimation, alternate explanations, practice index, real-world architecture index, OOD exercises, and optional Anki recall | Assigned Stage 1 sections; later use as reference |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | Conceptual spine for storage, replication, partitioning, transactions, distributed systems, batch, and streams | Chapters 1 to 11; Chapter 12 optional |
| [Database Internals](https://www.databass.dev/) | Storage engine and distributed database mechanisms | Chapters 1 to 7 required in Stage 2; Chapters 8 to 14 role-dependent |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) | Reliability concepts and production failure reasoning | Stage 3 and 4 selections |
| [Site Reliability Workbook](https://sre.google/workbook/table-of-contents/) | Applied SLO, alerting, capacity, incident, configuration, and pipeline practices | Stage 3 and 4 selections |
| [Release It!](https://pragprog.com/titles/mnee2/release-it-second-edition/) | Stability patterns, control planes, versions, deployment, and systemic failure | Stage 3 and 4 selections by exact title |
| [Building Secure and Reliable Systems](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html) | Threat-aware design, least privilege, resilience, recovery, and safe engineering | Stage 4 selections |

## Applied and Targeted Books

| Source | Use |
|---|---|
| [System Design Interview, Volumes 1 and 2](https://bytebytego.com/courses/system-design-interview) | Optional applied prompts after independent attempts. Volume 1 Chapters 1 to 3 support Stage 1. Select later designs by the current stage or diagnosed gap. |
| [Designing Distributed Systems](https://www.oreilly.com/library/view/designing-distributed-systems/9781491983638/) | The 2018 edition supplies reusable sidecar, replicated-service, sharding, ownership-election, work-queue, and coordinated-processing patterns. Stage 5 assigns the highest-return sections. |
| [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) | Service granularity, data ownership, workflows, sagas, contracts, and explicit trade-off analysis for Stage 5. |

Do not read the optional books cover to cover unless a target role or diagnosed weakness justifies it. Their purpose is application and comparison, not a competing conceptual spine.

## Primer Features Worth Using

- Use the short, medium, and long study guidance only to understand the Primer's own breadth. Follow this repository's one curriculum.
- Use its interview process as an alternate checklist after learning the framework here.
- Use its availability, consistency, database, cache, queue, networking, communication, and security summaries for quick recall, then verify consequential claims in primary sources.
- Attempt its system design questions before reading the repository solutions.
- Use object-oriented design questions only if the target loop includes low-level design (LLD). They are a parallel format, not HLD stages.
- The three Anki decks can support spaced recall. Do not review solution cards before the corresponding cold attempt.
