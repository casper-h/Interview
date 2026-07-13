# Key Ideas

## The core loop

- Repeat the question out loud, and make sure you understand what is actually being asked.
- Ask clarifying questions before writing any code.
  - What are the given assumptions?
  - Are there any special requirements?
  - What are the constraints, on input size and otherwise?
- Practice speaking through your thought process as you work, not only after you finish.
- Work through examples before committing to an approach.
  - The most optimal solution is often not obvious immediately. Start with a brute-force
    approach, then optimize from there.
  - Check edge cases and exceptions explicitly, rather than assuming they are covered.
  - Identify any known algorithm or pattern that applies, and say so out loud as you recognize it.
- When debugging, divide and conquer: isolate each component and trace back to find where
  behavior diverges from what you expect.
- Consider testing throughout, not only at the end.
  - How would this code actually be tested?
  - What edge cases and failure modes are worth testing for specifically?
- Understand the time and space complexity of your solution, and be ready to state it and justify
  it without being asked.

## What senior-level signal looks like, beyond the core loop

The core loop above is necessary but not sufficient at the Senior and Senior Plus level.
Interviewers at this level are also grading how you drive the interview, not only whether you
arrive at a correct answer. A few things that distinguish stronger signal from adequate signal in
a coding round:

- **Proactively discussing trade-offs**, rather than waiting to be asked. For example,
  volunteering that an approach trades space for time, or that a simpler solution is sufficient
  given the stated constraints and a more complex one would be premature optimization.
- **Catching your own bugs.** Reviewing your code before declaring it finished, and narrating that
  review, is a stronger signal than writing correct code silently on the first attempt and a much
  stronger signal than an interviewer having to point out the bug.
- **Discussing testing strategy unprompted**, even briefly: what you would test, and why, before
  being asked "how would you test this."
- **Generalizing the solution.** Noticing and mentioning how the approach would need to change
  under a different constraint, for example if the input no longer fit in memory, or if it needed
  to support concurrent updates.
- **Managing your own time.** Recognizing when an approach is not converging and being willing to
  step back and reconsider, rather than continuing to push on a path that is not working.

## A clarifying-question checklist for ambiguous prompts

Many prompts are deliberately left ambiguous to see whether you ask about the following before
writing code.

- Input size: are we optimizing for a small input, or does the input size rule out certain
  complexity classes entirely?
- Mutability: can the input be modified in place, or does it need to be preserved?
- Duplicates: can the input contain duplicate values, and if so, how should they be handled?
- Sortedness: is the input already sorted, and if not, is sorting it an acceptable first step?
- Null and empty inputs: what should happen on an empty array, an empty string, or a null value?
- Concurrency: will this ever be called from multiple threads, and does that change the design?

Asking two or three of the most relevant questions from this list, rather than working through
all of them mechanically, is itself part of the signal: it shows judgment about which assumptions
actually matter for the problem at hand.

## Complexity reference

Understanding time and space complexity is assumed at this level, not something to work out from
scratch in the interview. See the Big O cheat sheet at
[bigocheatsheet.com](https://www.bigocheatsheet.com/) for a refresher if any of the common
complexity classes are not immediately intuitive.