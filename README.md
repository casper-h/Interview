# Interview Prep

A structured, interleaved plan for senior-level software engineering interviews. It covers three
things you are evaluated on directly, coding, system design, and behavioural performance, and a
small set of supporting material for how you prepare and present.

## The Bar This Prepares For

The target is a strong Senior hire, and the reliable way to clear that bar is to prepare against the
Staff bar. Senior loops probe scope, judgment, and trade-off reasoning that shade into what a Staff
interviewer looks for, and a candidate who holds that altitude reads as a clear hire rather than a
borderline one. Throughout this repository, when a topic goes deeper than a minimum-viable Senior
answer, that is deliberate: the extra depth is what turns a lean hire into a strong hire. Nothing
here requires that you are Staff. It asks that you can reason like one when the interview opens the
door.

## How This Repository Is Organized

The material lives under three anchors, one for each thing an interview loop evaluates:

- **[Coding](./leetcode/README.md)** is the algorithmic round: pattern coverage, the
  [pattern-recall template](./leetcode/template.md), and the
  [interview-loop playbook](./leetcode/playbook.md) for what senior signal looks like
  in a coding round.
- **[System Design](./system_design/README.md)** is the design round, taken broadly. It holds the
  interview [framework](./system_design/framework.md) (a flat file, no longer a subdirectory), the reusable
  [building blocks](./system_design/building_blocks.md) library (also flat), the
  [reading plan](./system_design/plan/README.md), the
  [practice designs](./system_design/practice_design/README.md), the
  [white papers](./system_design/white_paper.md) (flat), the
  [low-level (object-oriented) design](./system_design/low_level_design/README.md) round, and the
  [foundations](./system_design/foundations/README.md) beneath distributed systems (networking,
  operating systems, database internals, and concurrency).
- **[Behavioural](./behavioural/README.md)** is how you present yourself and your work. It holds the
  STAR framework and story bank, the technical [deep dive on systems you built](./behavioural/experience_deep_dive.md)
  (a flat file, no longer a subdirectory), [resume and narrative](./behavioural/resume_and_narrative.md) work (also flat), and
  [company preparation](./behavioural/company_prep.md) (also flat) including offer evaluation and
  negotiation.

One supporting area sits outside the three anchors because it coordinates all of them rather than
belonging to any one:

- **[Schedule](./schedule/README.md)** is the phase-based plan that tells you how to move through the
  anchors in parallel, the [tracker](./schedule/tracker.md) for logging every problem and design you
  work through, and the [mock-interview](./schedule/mocks.md) (flat file, no longer a subdirectory) cadence and rubric.

Everything else is a sub-section under one of the four directories above. This README is the only
top-level document; every other guide lives inside one of those four directories.

## How to Use It

Start with the [schedule](./schedule/README.md). It lays out the phases of preparation and, more
importantly, how the anchors fit together week to week. The anchors are organized by topic rather
than by time, so the schedule is what tells you to interleave them instead of finishing one before
starting the next.

Log every problem, design, and mock you work through in the [tracker](./schedule/tracker.md). That
log is what turns a static reading list into an actual feedback loop.

A note on artifacts: this repository is deliberately a set of frameworks and checklists, not a bank
of memorized answers. It keeps no worked solutions to individual coding problems and no canned
write-ups of specific designs, because a memorized answer collapses the moment an interviewer
perturbs the prompt. The durable outputs of your practice are the pattern-recall checklist in
[the template](./leetcode/template.md), the feedback log in [the tracker](./schedule/tracker.md),
and your private behavioural story bank, not solution files.

## Reading Priority

Limited time goes to the highest-return material first. The order below reflects the
concept-to-hiring-band mapping in the
[concepts-by-level reference](./system_design/plan/concepts_by_level.md), and the
[reading plan](./system_design/plan/README.md) applies it in detail.

- **Read first (highest return).** *Designing Data-Intensive Applications* is the primary concepts
  book. The eight core [white papers](./system_design/white_paper.md), the
  [building blocks](./system_design/building_blocks.md) library, and a dozen practice designs worked
  out loud cover most of what a Senior loop tests.
- **Read for the upper-Senior and Staff range you are targeting.** *Database Internals* for
  storage-engine depth, *Specifying Systems* and the TLA+ material for formal reasoning, and jepsen.io
  for how consistency claims break in practice. The MIT 6.824 and CMU 15-445 lecture series are
  primary sources here, not optional extras. *Understanding Distributed Systems* and the System Design
  Primer are supporting material.
- **De-emphasize as a primary study path.** The interview-prep compilations (*Grokking the System
  Design Interview*, *System Design Interview* Volume 1, *Fundamentals of Software Architecture*) are
  useful as an applied warm-up for problem shape, not as a primary resource. Do not let them crowd out
  the material above.

## Additional Resources

- [Levels.fyi](https://www.levels.fyi): compensation data by company and level.
- [Techjobs.xyz](https://techjobs.xyz/): open roles.
- [Layoffs.fyi](https://layoffs.fyi/): context on company stability.

Offer evaluation and negotiation live with the rest of the logistics in
[Company Prep](./behavioural/company_prep.md), so the offer-handling material sits beside the
research and interview logistics it belongs with. The offer stage is part of the outcome, not an
afterthought: a strong hire is undersold if the offer is mishandled.
