# Integrated Study Schedule

This is a phase-based plan rather than a calendar-locked one. There is no hard deadline driving
this, so the guidance below is: don't compress depth to hit an artificial date, but also don't let
any one track (especially System Design, which has the most existing material) run so long in
isolation that Coding or Behavioural prep atrophies. As a rough sizing, expect the whole plan to
take on the order of three to four months of consistent, interleaved effort (longer if a track
needs it, and it's fine to move faster where you're already strong). That's a target to size your
expectations against, not a deadline, and not an invitation to prepare indefinitely: the exit
conditions, not the clock, tell you when to move on. The core principle stays the same regardless of
total duration: interleave all tracks every week rather than finishing them in sequence. Skills that
sit untouched for a month tend to decay before the real interview.

Each phase below has a rough minimum duration and an exit condition. Move to the next phase when
you hit the exit condition, not when a calendar date arrives. If System Design needs longer, let
it; just keep touching Coding and Behavioural weekly throughout.

## Phase 1: Foundations and Diagnostic

Minimum duration: one to two weeks.

- Read the [system design framework](../system_design/framework.md) (and memorize the estimation cheat sheet) and
  the [low-level design guide](../system_design/low_level_design/README.md) end to end first, so the baseline mocks below measure your reasoning
  rather than your unfamiliarity with the format.
- Take one baseline mock in each format: coding, high-level system design, low-level design, and
  behavioural. Don't skip this; it tells you where your real gaps are instead of leaving you to
  guess. Treat it as diagnostic, not evaluative; it is *supposed* to expose gaps, so don't read a
  rough first mock as a verdict. Read the [strong-hire thresholds](./mocks.md) before you
  grade these, so you are calibrating against the real bar from the start rather than in Phase 4.
  For the low-level design mock, prefer a problem with shared mutable state (a thread-safe cache or
  rate limiter) so you find out early whether concurrency is a gap, since that track otherwise does
  not start until the second half of Phase 2.
- Draft your resume narrative and your first two or three behavioural stories, using
  the [behavioural guide](../behavioural/README.md) and the [resume and narrative guide](../behavioural/resume_and_narrative.md).
- List the two or three systems you would use for the [experience deep dive](../behavioural/experience_deep_dive.md)
  and write a one-paragraph technical summary of each. Do this now, not in Phase 3: if you struggle
  to find two systems you drove the design of, that gap needs the full runway to develop into a
  credible narrative, and it is far better to discover it in week one than in week ten.
- Do a light coding warm-up of ten to fifteen easy problems to shake off rust, and skim
  the [pattern-recall template](../leetcode/template.md) so you know the self-test you'll be using throughout.
- Skim the [building blocks](../system_design/building_blocks.md) once so you know what's in the toolkit before the
  practice designs in Phase 2 start pulling from it.

Exit condition: you have a baseline score, or at least notes, in all four areas, and you know
which one is weakest.

## Phase 2: Core Build

Minimum duration: six to ten weeks; longer is fine.

Run all tracks in parallel every week.

- **Coding.** Work through two to three problems a day, focusing on one or two patterns per
  week, following the category order in the [coding tracker](../leetcode/README.md). Core coverage
  is roughly the two to four unflagged problems in each category, at easy and medium difficulty; that
  is what "covered every category once" means. Hit that across every category before circling back
  for the *stretch* problems (the ones flagged stretch, and the hard tier); don't grind one category
  to completion while others sit untouched. Log every attempt in
  the [tracker](./tracker.md), and run the pattern-recall self-test in the [template](../leetcode/template.md) as each
  pattern is covered.
- **System Design.** Work through the [reading plan](../system_design/plan/README.md) part by part, at whatever pace suits you
  now that it isn't compressed into a fixed timeline. Keep the optional deep-dive material optional:
  pull from it when a practice design or mock exposes a gap, not by default, so it doesn't crowd out
  the weekly designs. Do at least one full practice design per week, end to end, using the framework
  in the [framework](../system_design/framework.md), reaching into
  the [building blocks](../system_design/building_blocks.md) for components, and drawing from
  the [practice designs](../system_design/practice_design/README.md) (start with its Tier 1).
- **Low-Level Design.** Do one problem per week once the framework document is read.
- **Concurrency.** Start the standalone problems in the [concurrency track](../system_design/foundations/concurrency.md) in the
  second half of this phase, timed to land alongside the System Design replication, consensus, and
  distributed-locks topics so the thread-level and cross-process versions of the same idea reinforce
  each other.
- **Behavioural.** Draft and rehearse one new story per week, out loud, and revisit and tighten
  earlier ones. Include at least one of the scope/influence/leadership stories (rows 11 to 20 in the
  [behavioural guide](../behavioural/README.md)) in this phase; those take the most iteration to get right.
- **Mocks.** Start one mock interview per week partway through this phase (see [mocks](./mocks.md)), rotating
  the format each time rather than repeating your comfort format. A workable rotation is coding  to 
  high-level design to low-level design to behavioural, repeating, so you hit each at least twice
  before Phase 3. In the last week or two of this phase, run one full back-to-back loop (two or three
  rounds with only short breaks) so pacing and context-switching fatigue surface now rather than for
  the first time in Phase 4.

Exit condition: you have covered every coding pattern category at its core level at least once,
completed a full pass of the system design plan's required reading, have six or more behavioural
stories (including at least one scope/leadership story), and have done several mocks in each format
with notes logged.

## Phase 3: Volume and Weak-Spot Targeting

Minimum duration: three to six weeks.

- Stop following the checklist mechanically. Use the [tracker](./tracker.md) and your mock feedback to
  find what's actually weak, and spend the majority of your time there, including the *stretch*
  coding problems in your weak categories, which is where the hire-to-strong-hire delta lives.
- Increase mocks to two per week, and weight them toward your weak formats rather than rotating
  evenly: if coding is solid and behavioural is shaky, do more behavioural mocks, rather than
  defaulting back to the format you enjoy. The point of this phase is to close the specific gaps the
  tracker is showing you, not to keep exercising what already works.
- This is a natural place to go deeper into the optional deep-dive system design material, such
  as the fuller white paper list or extra books, for any topic that came up shaky in mocks. With
  no hard timeline, it's fine to let this phase run long if a particular area needs it.
- Prepare the [experience deep dive](../behavioural/experience_deep_dive.md) round now: pick two or three systems you built and
  drill them, since this round needs your Phase 2 system-design vocabulary to be fluent first.
- Revisit your resume narrative and [project walkthrough](../behavioural/resume_and_narrative.md) and
  tighten them against the behavioural stories that matured in Phase 2; the walkthrough is the
  opening of the experience deep dive, so they should reinforce each other.

Exit condition: mock feedback stops surfacing new categories of gaps; you're seeing the same
fixable mistakes repeat rather than encountering new ones.

## Phase 4: Mock Interview Sprint

Minimum duration: two weeks.

- Continue the full-loop simulated interviews you started at the end of Phase 2: coding, system
  design, and behavioural, back to back, timed as close to the real format as possible, aiming for
  two or three across this phase. Record sessions where feasible.
- Grade every mock against the [rubric](./mocks.md). Log gaps in the tracker, and fix them
  with targeted practice rather than broad re-study.
- Once you're targeting specific companies, work through the [company prep guide](../behavioural/company_prep.md): the research per
  company, the logistics check, and reading the offer/negotiation framework *before* offers land so
  the leverage-creating moves (clustering your loops) happen in time.

Exit condition: you're consistently rated "strong hire" across formats, not just "hire" or "lean
hire," and validated by at least one external mock (an interviewing.io session or a coach who
doesn't know you), not only your own or a friendly peer's rubric, since self- and peer-grading both
tend to inflate.

## Phase 5: Taper

Roughly the final week before real interviews.

- Review only: the pattern-recall self-test ([the template](../leetcode/template.md)), the estimation cheat sheet,
  the building-blocks toolkit at a glance, the story bank, and the system design framework
  checklist.
- Introduce no new material. Protect your sleep and energy; this reliably outperforms
  last-minute cramming at this level.
- If interview anxiety is a factor for you, extend this to two or three weeks. The extra time is
  for review and rest, not more material; if you catch yourself cramming to quiet the nerves, that
  is the signal to step back to review-only, since going in rested beats going in over-studied.

## Notes on the relaxed timeline

- It's fine, and arguably beneficial, to let Phase 2 run long and use the extra time to keep more
  of the System Design optional deep-dive material (the fuller white paper list, the extra books)
  in active rotation rather than skipping it, since that material was originally trimmed mainly
  for time pressure, not because it lacks value. There is a line, though: if you have been in Phase 2
  for more than about twelve weeks and your mock scores in a format have stopped moving over the last
  three mocks in it, that is a plateau, and the fix is to move to Phase 3 and target the weak spot
  directly rather than to keep reading more papers. Open-ended breadth past that point is usually
  avoidance wearing the costume of thoroughness.
- The one thing not to relax is the interleaving. Even if you spend three months in Phase 2, keep
  touching Coding, Low-Level Design, and Behavioural every single week, rather than doing System
  Design for six weeks straight before switching.
- Re-run the Phase 1 diagnostic mock periodically, roughly every four to six weeks, to confirm
  you're actually improving across all four areas and not just the one you enjoy studying most.

See the [tracker](./tracker.md) for the log template used across all phases.