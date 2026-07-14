# Practice Tracker

Log every coding problem, low-level design problem, system design practice, and mock interview
here. The value of this file lives almost entirely in the "root cause" column. Without it, this
is just a checklist; with it, it becomes a feedback loop that tells you what to actually spend
time on. The first row of each table is a filled-in example showing the level of detail that makes
the log useful; replace or delete it once you have your own entries.

## Coding

| Date | Problem | Pattern | Time taken | Outcome | Root cause if struggled | Re-attempt date |
|---|---|---|---|---|---|---|
| 2026-01-05 | Longest Substring Without Repeating | Sliding window | 28 min | Solved, needed a nudge | Knew the pattern but botched the shrink step: moved the left pointer one at a time instead of jumping past the duplicate. Edge-case, not pattern miss. | 2026-01-12 |
| | | | | | (pattern miss, bug, edge case, or communication issue) | |

## Low-Level Design

| Date | Problem | Time taken | Outcome | Root cause if struggled | Re-attempt date |
|---|---|---|---|---|---|
| 2026-01-06 | Parking lot | 45 min | Design broke on follow-up | Modeled spot sizes as Vehicle subclasses, so "add EV spots with charging" forced edits across the hierarchy. Should have used a SpotType field plus composition. Under-engineered the extension point. | 2026-01-13 |
| | | | | | |

## System Design (practice designs)

| Date | Design | Time taken | Framework followed fully? | Weakest part of the answer | Re-attempt date |
|---|---|---|---|---|---|
| 2026-01-08 | URL shortener | 40 min | No, skipped estimation | Jumped to the data model without sizing QPS, so I couldn't justify the cache layer when pushed. Do the back-of-envelope step even when the design feels familiar. | 2026-01-20 |
| | | | | | |

## Behavioural

| Date | Story or question practiced | Length (target: 90 seconds to 2.5 minutes) | Feedback | Revised? |
|---|---|---|---|---|
| 2026-01-09 | Conflict with a peer (row 2) | 3 min 10 s | Ran long, and spoke in "we" for the resolution so my specific contribution was unclear. Tighten the situation, use "I" in the action. | Yes |
| | | | | |

## Mock interviews

| Date | Format (coding, high-level design, low-level design, behavioural, or full loop) | Interviewer or peer | Self or peer rating | Key gaps identified | Follow-up action |
|---|---|---|---|---|---|
| 2026-01-10 | High-level design | Peer (senior eng) | Hire, not strong hire | Went quiet for two to three minutes while thinking through the data model; strong on trade-offs once talking. | Practice narrating continuously; do two design mocks next week. |
| | | | | | |