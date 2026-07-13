# Integrated Study Schedule

This is a phase-based plan rather than a calendar-locked one. There is no hard deadline driving
this anymore, so the guidance below is: don't compress depth to hit an artificial date, but also
don't let any one track (especially System Design, which has the most existing material) run so
long in isolation that Coding or Behavioural prep atrophies. The core principle stays the same
regardless of total duration: interleave all tracks every week rather than finishing them in
sequence. Skills that sit untouched for a month tend to decay before the real interview.

Each phase below has a rough minimum duration and an exit condition. Move to the next phase when
you hit the exit condition, not when a calendar date arrives. If System Design needs longer, let
it; just keep touching Coding and Behavioural weekly throughout.

## Phase 1: Foundations and Diagnostic

Minimum duration: one to two weeks.

- Take one baseline mock in each format: coding, high-level system design, low-level design, and
  behavioural. Don't skip this; it tells you where your real gaps are instead of leaving you to
  guess.
- Read `system_design/framework/README.md` and memorize the estimation cheat sheet.
- Read `low_level_design/README.md` end to end once.
- Draft your resume narrative and your first two or three behavioural stories, using
  `behavioural/README.md`.
- Do a light coding warm-up of ten to fifteen easy problems to shake off rust, and start
  `leetcode/templates.md`.

Exit condition: you have a baseline score, or at least notes, in all four areas, and you know
which one is weakest.

## Phase 2: Core Build

Minimum duration: six to ten weeks; longer is fine.

Run all tracks in parallel every week.

- **Coding.** Work through two to three problems a day, focusing on one or two patterns per
  week, following the category order in `leetcode/README.md`, including the newer categories
  such as matrix and grid traversal, prefix sums, monotonic deques, topological sort, and segment
  trees or binary indexed trees. Log every attempt in `schedule/tracker.md`, and update
  `leetcode/templates.md` as each pattern is covered.
- **System Design.** Work through `system_design/plan/` month by month, at whatever pace suits
  you now that it isn't compressed into a fixed four months. Since the timeline is flexible, it
  is fine to also work through more of the optional deep-dive white papers here rather than
  skipping them, as long as this doesn't crowd out weekly practice designs. Do at least one full
  practice design per week, end to end, using the framework in
  `system_design/framework/README.md` and drawing from `system_design/practice_designs/`.
- **Low-Level Design.** Do one problem per week once the framework document is read.
- **Concurrency.** Fold this in once you reach the System Design topics where it naturally comes
  up, such as replication, consensus, and distributed locks; it doesn't need its own dedicated
  block of weeks.
- **Behavioural.** Draft and rehearse one new story per week, out loud, and revisit and tighten
  earlier ones.
- **Mocks.** Start one mock interview per week partway through this phase (see `/mocks`),
  rotating the format each time.

Exit condition: you have covered every coding pattern category at least once, completed a full
pass of the system design plan's core reading, have six or more behavioural stories, and have
done several mocks in each format with notes logged.

## Phase 3: Volume and Weak-Spot Targeting

Minimum duration: three to six weeks.

- Stop following the checklist mechanically. Use `schedule/tracker.md` and your mock feedback to
  find what's actually weak, and spend the majority of your time there.
- Increase mocks to two per week, spanning coding, high-level design, low-level design, and
  behavioural.
- This is a natural place to go deeper into the optional deep-dive system design material, such
  as the fuller white paper list or extra books, for any topic that came up shaky in mocks. With
  no hard timeline, it's fine to let this phase run long if a particular area needs it.

Exit condition: mock feedback stops surfacing new categories of gaps; you're seeing the same
fixable mistakes repeat rather than encountering new ones.

## Phase 4: Mock Interview Sprint

Minimum duration: two weeks.

- Run full-loop simulated interviews: coding, system design, and behavioural, back to back, timed
  as close to the real format as possible. Record sessions where feasible.
- Grade every mock against the rubric in `mocks/README.md`. Log gaps in the tracker, and fix them
  with targeted practice rather than broad re-study.

Exit condition: you're consistently rated "strong hire" on your own or a peer's rubric across
formats, not just "hire" or "lean hire."

## Phase 5: Taper

Roughly the final week before real interviews.

- Review only: pattern templates, the estimation cheat sheet, the story bank, and the system
  design framework checklist.
- Introduce no new material. Protect your sleep and energy; this reliably outperforms
  last-minute cramming at this level.

## Notes on the relaxed timeline

- It's fine, and arguably beneficial, to let Phase 2 run long and use the extra time to keep more
  of the System Design optional deep-dive material (the fuller white paper list, the extra books)
  in active rotation rather than skipping it, since that material was originally trimmed mainly
  for time pressure, not because it lacks value.
- The one thing not to relax is the interleaving. Even if you spend three months in Phase 2, keep
  touching Coding, Low-Level Design, and Behavioural every single week, rather than doing System
  Design for six weeks straight before switching.
- Re-run the Phase 1 diagnostic mock periodically, roughly every four to six weeks, to confirm
  you're actually improving across all four areas and not just the one you enjoy studying most.

See `schedule/tracker.md` for the log template used across all phases.