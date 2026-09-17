# Senior Interview Preparation

This is a months-long guide for a strong Senior software engineering candidate who wants enough system design depth and production judgment to handle Staff-level follow-up questions. Study can improve knowledge and interview execution. It does not substitute for the experience, scope, and organizational impact expected of a Staff engineer.

## Start Here

| Area | What it develops | First action |
|---|---|---|
| [System design](./system_design/README.md) | Architecture, distributed systems, reliability, evolution, and technical judgment | Run the [Stage 0 cold diagnostic](./system_design/README.md#stage-0-cold-diagnostic-and-format-baseline). |
| [Coding](./leetcode/README.md) | Pattern recognition, correct implementation, testing, and follow-up reasoning | Attempt the first core problems in [Arrays and hashing](./leetcode/patterns.md#arrays-and-hashing). |
| [Behavioural](./behavioural/README.md) | Ownership, influence, judgment, impact, and clear career narrative | Build a [story inventory](./behavioural/story_guide.md#story-inventory). |

Work on all three areas every week. Do not finish one track before starting the others.

## Preparation Sequence

The system design stages define the main progression. The dates below are pacing guidance, not a second curriculum.

| Period | System design | Coding | Behavioural |
|---|---|---|---|
| First month | Typically complete Stages 0 and 1. Learn one interview framework and the basic components. | Diagnose core patterns. Solve mostly easy and medium representative problems. | Draft the career narrative and four versatile stories. |
| Months 2 and 3 | Work through Stage 2. Read DDIA, storage papers, and correctness material while designing repeatedly. | Rotate through core patterns. Reattempt misses without notes. | Expand toward six to eight stories and prepare one experience deep dive. |
| Months 3 and 4 | Work through Stage 3. Add messaging, processing, reliability, and overload. | Begin timed mixed sets and continue targeted repetition. | Probe stories and the deep dive with another person. |
| Months 5 to 7 | Work through Stages 4 and 5. Add production evolution, cost, security, and organizational constraints. | Use target-specific mixed practice and mocks. | Add a backup deep dive if useful and rehearse target-specific material. |
| Interview-specific period | Rehearse the target format, prompts, duration, and collaboration medium. Review weak dimensions rather than adding broad new material. | Match the company's known coding format and language constraints. | Map true stories to current company values and verify the loop with the recruiter. |

These are typical ranges, not deadlines. Exit criteria override dates. Move more slowly when a stage is not reliable.

## Weekly Allocation

| Weekly time | System design | Coding | Behavioural and company preparation |
|---:|---:|---:|---:|
| 6 hours | 3 hours | 2 hours | 1 hour |
| 10 hours | 5 hours | 3 hours | 2 hours |
| 15 hours | 7 hours | 5 hours | 3 hours |

Each system design block should mix reading with active recall or a design. Each coding block should include attempts and revisits. Behavioural work should include spoken practice, not only writing.

For example, a six-hour week can contain two 90-minute system design sessions, two 60-minute coding sessions, and one 60-minute behavioural session. Use one system design session for bounded reading and companion questions, and the other for a prompt or failure exercise.

## Mocks and Feedback

Begin low-stakes mocks after you can complete a basic end-to-end attempt, usually near the end of system design Stage 1 and after several weeks of coding and story preparation. Early mocks diagnose habits while there is time to change them. In the final four to six weeks, run full-length mocks in the expected medium and increase their frequency without abandoning targeted drills.

After any practice session, record only what helps the next attempt:

- the requirement or pattern you missed;
- the root cause, such as knowledge, implementation, prioritization, or communication;
- one corrective exercise;
- a reattempt date.

No checked-in tracker is prescribed. Use whatever private system you will maintain.

## Working Method

1. Attempt before reading a solution.
2. Build a simple complete answer before adding scale mechanisms.
3. State assumptions, guarantees, and failure boundaries.
4. Compare decisions, not diagrams.
5. Change one major constraint and reattempt.
6. Treat sample answers as calibration, not scripts.
7. Verify each target company's current process. Interview formats and level expectations change.
