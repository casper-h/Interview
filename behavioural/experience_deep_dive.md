# Experience Deep Dive

Senior loops almost always include a round that is neither a behavioural STAR interview nor a generic
system-design prompt: a deep technical grilling on something *you actually built*. The interviewer
picks a system from your background and drills (architecture, data model, failure modes, the
decisions you made and the ones you'd revisit) for 30 to 45 minutes. This is where genuine technical
judgment is probed most directly, because you can't hand-wave through the details of your own work,
and it is the round candidates most often under-prepare because it feels like it needs no preparation.
This round requires preparation.

This is distinct from two adjacent tracks and should not be collapsed into either:

- The **[behavioural story bank](./README.md)** is about *how you operated*: ownership,
  conflict, influence. This round is about *what you engineered* and whether it holds up under
  scrutiny.
- The **[practice designs](../system_design/practice_design/README.md)** are generic, greenfield
  systems. This round is your real, messy, constraint-laden system, where "why didn't you just use
  X" has an actual answer rooted in what you knew and had at the time.

## Pick Two or Three Systems and Prepare Them Cold

Choose systems that are recent, that you owned a meaningful part of, and that have real technical
depth (distributed behavior, scale, a hard trade-off, an interesting failure). For each, be able to
whiteboard and defend the following without notes:

- **The problem and the constraints.** What were you actually solving, and what were the real
  constraints (scale, deadline, existing systems, team size, org politics)? The constraints are what
  make the story credible and the decisions defensible.
- **The architecture.** Draw it. Components, data flow, and the boundaries between services. Be
  ready to zoom into any box the interviewer points at.
- **The data model.** Key entities, the schema or storage choice, how it was partitioned and
  indexed, and why that store over the alternatives.
- **The key decision and its alternatives.** The one or two decisions that defined the system, the
  options you weighed, and why you chose as you did. "Why X over Y" is the most common probe: have
  the answer for your real Y. This includes the build-versus-buy calls: "why didn't you just use a
  managed service or an off-the-shelf library" is asked constantly, and the answer has to rest on
  what you knew and what it would have cost, not on not having considered it.
- **Scale, performance, and cost.** Rough numbers: traffic, data volume, latency, and where the
  bottleneck was. What you'd need to change to handle ten times the load. Be ready for the cost
  angle too, since at the senior level the trade-off is rarely pure performance: what the system
  cost to run, and where you spent compute or storage to buy latency or simplicity.
- **How it evolved.** How the problem or the requirements shifted over the system's life, which of
  your early assumptions broke, and how the design absorbed the change. This is the probe for whether
  you over-designed for a future that never came or under-designed for one you should have seen.
- **Failure modes and operations.** How it failed or could fail, how it was monitored, what the
  on-call story was, and any real incident and what you changed afterward. Have the cross-cutting
  answers ready as well: the security model (authentication, authorization, how sensitive data was
  protected), any compliance constraints, and the disaster-recovery story (backups, failover, and
  roughly what recovery would cost in time and data).
- **What you'd do differently.** The honest retrospective: the tech debt you took on knowingly, the
  decision that aged badly, the thing you'd redesign now. This is a strong-hire signal, the same way
  it is in the behavioural round.

## How to Prepare It

- Write a one-page brief per system for *your own* use (architecture sketch, data model, the two or
  three decisions, the numbers). This is working material to internalize, not a script to recite:
  the same principle as everywhere else in this repo. No memorized answers, because the interviewer
  will perturb the prompt.
- Have a mock partner play the interviewer and drill one of your systems for 30 minutes. The goal is
  to find the questions you can't yet answer crisply: those are your study list.
- Reconcile it with your resume and your [project walkthrough](./resume_and_narrative.md). The
  90-second walkthrough is the *opening* of this round, and the deep dive is what happens when the
  interviewer pulls a thread from it.

## Common Failure Modes

- **Vagueness about your own system.** "The service scaled well" without numbers, or "we used a
  queue" without being able to say which delivery semantics and why, reads as shallow ownership.
- **Claiming more than you did.** Be precise about your specific contribution versus the team's;
  overclaiming collapses fast under probing about details only the actual owner would know. Be ready
  for the collaboration angle too: "how did you get the team aligned on this" and "who pushed back"
  are common, and they test whether you drove a decision alone or built the consensus behind it.
- **No trade-offs, only wins.** A system with no tech debt, no regrets, and no alternatives
  considered is not a credible system. Name the trade-offs you made deliberately.

## Ask Your Own Questions at the End

This is still an interview, not only a grilling, so leave a few minutes to ask questions of your
own, and let them build on the conversation you just had. Because the interviewer has been deep in
your system, the strongest questions turn the deep dive into a peer exchange: what the hardest
technical decision their team is facing right now looks like, or how they would have approached the
trade-off they just pushed you on. That reads as an engineer sizing up the work, which is exactly the
altitude this round is assessing.
