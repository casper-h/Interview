# Experience Deep Dive

An experience deep dive examines a real system or project you helped build. Unlike a short behavioural story, it may last 30 to 60 minutes. Unlike a hypothetical system design interview, it tests what actually happened under real constraints rather than an ideal greenfield answer.

## Select the System

Prepare one system completely. A second system is a useful backup when the target loop asks the interviewer to choose from several projects. Choose work that is recent, technically substantial, and connected to something you personally owned. A useful choice includes a difficult trade-off, meaningful production behavior, organizational constraints, and at least one decision you would now revisit.

Do not disclose confidential architecture, customer data, incidents, or business metrics. Generalize details while preserving the technical reasoning.

## One-Page System Brief

### Problem and Scope

- What user or business problem did the system solve?
- What existed before it?
- What was explicitly out of scope?
- What did you personally own, and what did others own?

### Constraints and Invariants

- What were the real traffic, data, latency, reliability, security, cost, deadline, and staffing constraints?
- Which constraints were measured and which were assumptions?
- What correctness or business invariants could not be violated?

### Architecture and Data

- Draw the components, trust boundaries, and end-to-end data paths.
- Identify sources of truth and derived state.
- Explain schemas, indexes, partitioning, caching, asynchronous work, and external dependencies.
- State the acknowledgment and consistency boundaries.

### Decisions

- What were the two most consequential decisions?
- Which alternatives did you consider?
- What evidence and organizational constraints shaped the choice?
- What would have reversed the decision?
- Which build-versus-buy trade-offs were material?

### Production Operation

- What were the actual scale, bottlenecks, cost drivers, and service objectives?
- How did the system handle overload, retries, timeout, partial failure, and recovery?
- What telemetry supported operation and debugging?
- Describe one real incident or near miss and the changes that followed.

### Evolution

- Which early assumptions changed?
- How did schemas, APIs, clients, and data migrate during mixed-version operation?
- Which debt was deliberate, and which surprised the team?
- What would fail at ten times the load or one-tenth the budget?

### Organization and Impact

- Which teams and stakeholders participated?
- How were ownership, on-call, contracts, and decision rights divided?
- How did you build alignment and adoption?
- What changed for users, the business, the system, and the engineers operating it?
- How was that impact measured?

### Retrospective

- What did you get wrong?
- What would you preserve?
- What would you redesign now, and why was that not necessarily the correct choice then?
- How did the experience change your later engineering judgment?

## Practice Method

1. Open with the 90-second [project walkthrough](./story_guide.md#project-walkthrough).
2. Draw the system from memory in five minutes.
3. Ask a partner to choose the next branch rather than delivering a prepared lecture.
4. Require evidence for scale, impact, and claimed guarantees.
5. Probe one technical decision, one failure, one migration, and one organizational boundary.
6. Record questions you could not answer precisely and repair the underlying knowledge.

The goal is accurate ownership and reflective judgment. Do not inflate scope or convert every historical decision into the architecture you now wish had existed.
