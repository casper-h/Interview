# System Design

Start with the framework, then work through the reading plan and practice designs in parallel,
following the guidance in the [schedule](../schedule/README.md) rather than treating this as a
standalone track.

## [Interview Framework](./framework/README.md)

The structure to use in every practice design and every real interview: the step-by-step
approach, the requirements and estimation checklists, the API design primer, and the security
checklist. Read this first, before doing any practice design.

## [Building Blocks](./building_blocks/README.md)

The reusable component library (load balancing, caching, partitioning, replication, consensus,
queues, rate limiting, and the rest) that you reach for during the deep-dive step of a design.
The framework tells you the steps; this tells you what to slot into them. Read it alongside the
framework and revisit it whenever a practice design surfaces a component you can't yet reason about
crisply.

## [Reading Plan](./plan/README.md)

The staged reading plan, covering storage engines, replication, consensus, distributed
computation, and reliability. It marks the academic-depth material (extra textbooks, lecture series,
the long white-paper tail) as optional so it doesn't crowd out practice. Its
[deep reasoning companion](./plan/companion.md) pairs each part with integration questions and
worked answers.

## [Practice Designs](./practice_design/README.md)

The consolidated, tiered list of system design prompts to work through end to end, using the
interview framework above.

## [White Papers](./white_paper/README.md)

A required core set of roughly eight papers with the highest direct return for a senior-level loop,
plus an optional deep-dive tier for infrastructure-heavy teams or for going deeper once mock
interview feedback points at a specific gap.