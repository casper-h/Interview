# Mock Interviews

Solo study does not train two things that are explicitly graded in a real interview: verbalizing
your thought process under time pressure, and reading and responding to an interviewer's live
signal. Mock interviews are the only practice format that trains both, which is why they are
weighted heavily in the [schedule](./README.md) from Phase 2 onward.

## Where to Run Them

- Peer swaps with other senior engineers, ideally people also preparing for interviews, so the
  exchange is mutually valuable.
- Platforms such as interviewing.io or Pramp, which pair you with an interviewer for a realistic,
  timed session.
- Where available, a trusted colleague or mentor willing to run a full-length mock and give
  direct feedback.

## Cadence

Follow the cadence in the [schedule](./README.md): roughly one per week starting partway through Phase
2, increasing to two per week in Phase 3, and full back-to-back loops in Phase 4. Rotate format
each time (coding, high-level system design, low-level design, behavioural) rather than
repeating the same one.

## Running the Mock

- Time it exactly as the real interview would be timed. Do not pause the clock to think, since
  the ability to think under time pressure is exactly what is being trained.
- Narrate out loud the entire time, even in a solo or recorded session. If practicing alone,
  record yourself and review the recording, since it will surface filler words, pacing issues,
  and moments where you went quiet while thinking.
- For system design and low-level design mocks, use the frameworks in
  the [system design framework](../system_design/framework.md) and the [low-level design guide](../system_design/low_level_design/README.md) explicitly, and note
  afterward whether you actually followed the structure or drifted from it under pressure.

## Grading Rubric

Use this rubric consistently across sessions so your notes are comparable over time, rather than
each mock producing a differently shaped piece of feedback.

- **Structure.** Did you follow a clear, recognizable structure, and did the interviewer or
  observer find it easy to follow along?
- **Communication.** Did you narrate your thinking clearly, at an appropriate level of detail, and
  did you check in with the interviewer rather than working silently?
- **Correctness.** For coding, did the solution work, and did you test it. For design rounds, did
  the design actually satisfy the stated requirements?
- **Trade-off depth.** Did you identify and discuss the real trade-offs, or default to a single
  answer presented as the only correct one?
- **Time management.** Did you pace yourself appropriately across the interview, or run out of
  time on one section at the expense of another?

Rate each dimension, note the single biggest gap, and log it in the [tracker](./tracker.md) under the
mock interviews section, along with a specific follow-up action rather than a general intention
to "practice more."

## The Strong-Hire Bar on This Rubric

The [schedule](./README.md) gates the final phase on being "consistently rated strong
hire," which is only useful if you know where that line sits. Rate each dimension against the bar
below, not against your own sense of whether it "went fine." A useful heuristic: a hire clears the
bar, a strong hire clears it without help and volunteers the next level of depth unprompted. Grade
honestly, since self- and peer-grading both drift generous, and treat anything you needed a hint for
as not yet clearing the bar.

- **Correctness (coding).** Hire: a working, optimal-complexity solution. Strong hire: the same, plus
  you caught at least one bug or edge case yourself and walked concrete test cases before calling it
  done. Lean hire: correct only after a hint, or a suboptimal complexity you did not notice.
- **Correctness (design).** Hire: the design meets every stated requirement with no missing major
  component. Strong hire: the same, plus you named the primary bottleneck and how the system degrades
  under it. Lean hire: a plausible sketch with a gap you did not surface.
- **Structure.** Hire: a recognizable order the interviewer could follow. Strong hire: you drove the
  order (requirements, estimation, API, data model, deep dive, trade-offs for design; clarify,
  approach, code, test for coding) without being steered, and scoped out what you were not building.
- **Communication.** Hire: your reasoning was clear when you spoke. Strong hire: you narrated
  continuously, with no silent stretches longer than roughly ten seconds, and the interviewer never
  had to ask what you were thinking.
- **Trade-off depth.** Hire: you mentioned a trade-off when asked. Strong hire: you volunteered at
  least two real alternatives with their costs and justified your choice against them, rather than
  presenting one answer as the only one.
- **Time management.** Hire: you finished the core of the problem. Strong hire: you hit every major
  phase with time to spare for testing or the deep dive, and did not have to scramble in the last few
  minutes.

Score it: strong hire is at or above the strong-hire line on all five (coding folds the two
correctness rows into one), hire is four of five with the last one close, and lean hire is three of
five. The Phase 4 exit condition is met when you are landing at strong hire across formats,
validated by at least one external mock rather than only your own grading.

## After the Mock

- Fix the specific gap identified before your next mock in the same format, rather than only
  doing more volume in the same shape.
- Every four to six weeks, compare your rubric scores over time. If a particular dimension is not
  improving despite repeated mocks, that is a sign to change the approach, for example by
  rereading the relevant framework document, rather than to keep repeating mocks in the same way.