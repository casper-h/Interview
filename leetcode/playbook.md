# The Coding Round Playbook

How to run a coding interview from the first clarifying question to the final complexity statement.
This is the process half of the [Coding](./README.md) anchor: the [pattern coverage map](./README.md)
lists what to practice, the [template](./template.md) is the pattern-recall diagnostic, and this file
is how you conduct yourself in the room once a problem is in front of you.

## The Core Loop

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

## What Senior-Level Signal Looks Like, Beyond the Core Loop

The core loop above is necessary but not sufficient at the senior level and above. Interviewers at
this level are also grading how you drive the interview, not only whether you arrive at a correct
answer. A few things that distinguish stronger signal from adequate signal in a coding round:

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
  to support concurrent updates. This is the seam where a coding round touches system design: "if
  the input did not fit in memory, this becomes an external sort or a streaming pass, and at scale a
  sharded one." Reaching for that vocabulary (see the [building blocks](../system_design/building_blocks.md))
  when the constraint invites it is a strong senior signal.
- **Managing your own time.** Recognizing when an approach is not converging and being willing to
  step back and reconsider, rather than continuing to push on a path that is not working.

## What to Say Out Loud, Phase by Phase

"Speak through your thought process" is the advice everyone gives and few operationalize. Solving
the problem in silence and only narrating at the end reads as having got lucky, not as having
reasoned. The point is not a script to recite, since that collapses the moment the problem deviates,
but a sense of what belongs in the air at each phase so that narrating becomes automatic under
pressure.

- **While clarifying:** name the assumption you are making and the one you are checking. "I'll assume
  the array fits in memory and can contain duplicates. Should it return the first match or all of
  them?"
- **While choosing an approach:** name the pattern and why the constraint points to it. "This is a
  sliding-window problem because we want the longest contiguous run under a limit. The brute force is
  O(n squared); the window makes it O(n)."
- **While coding:** say what invariant each piece maintains, not a line-by-line readout. "This
  pointer tracks the start of the current window, and I shrink it whenever the count goes over."
- **Before declaring finished:** trace one real example and one edge case out loud, then state the
  complexity without being asked. "Empty input returns zero, a single element returns one. Time is
  O(n), space is O(1) since I reuse the counts."

## When You Get Stuck

Time-boxing an attempt only helps if you have something to do inside the box other than stare. When
an approach stalls for more than a few minutes, work this loop out loud rather than going quiet,
because recovering under observation is part of the evaluation.

- Re-read the prompt for a constraint you dropped or an assumption you never checked.
- Work a small example by hand and find the exact step where your mental model and the correct output
  diverge.
- Say which patterns the constraints suggest. Sorted input points to binary search or two pointers;
  "all combinations" points to backtracking; "shortest path" points to BFS.
- Solve the easier version first. Relax a constraint (assume no duplicates, a smaller input, one
  query instead of many), get that working, then add the constraint back.
- If none of that lands, state the specific thing you are blocked on. Naming it precisely often
  surfaces the gap, and it lets the interviewer give a hint that costs you far less signal than
  silence does.

## Edge Cases Worth Checking Every Time

Do not wait to be asked "what about edge cases?" Walking these before you declare a solution
finished is part of the signal, and the specific list depends on the structure you are working with.

- **Always:** empty input, a single element, two elements (where off-by-one errors surface), and all
  elements identical.
- **Arrays and strings:** already sorted or reverse-sorted, negatives and zero, and the maximum size
  the constraints allow.
- **Linked lists:** null head, one node, two nodes for a reversal, and a cycle.
- **Trees:** null root, a single node, and a fully skewed tree where height equals the node count.
- **Graphs:** a disconnected component, a self-loop, and a cycle where the algorithm assumes a DAG.

## Stating Complexity So It Survives a Follow-Up

Stating complexity is expected; stating it wrong is worse than staying quiet, because the follow-up
will find it. A few traps worth naming correctly:

- **Amortized is not worst-case.** A dynamic array append is O(1) amortized but O(n) on the resize.
  If the problem needs a guaranteed bound, say amortized explicitly.
- **Recursion costs stack space.** A depth-first traversal is O(h) space for the call stack, which is
  O(n) on a skewed tree, not O(1). If O(1) space is required, an explicit stack or iteration is the
  honest answer.
- **Sorting is not free.** "O(n) after sorting" is really O(n log n), dominated by the sort. State
  the total.
- **Hashing is average-case O(1).** Under adversarial keys or a bad hash it degrades. Say "O(1)
  average" rather than claiming a worst-case guarantee you do not have.
- **Union-Find is near-constant, not constant.** With path compression and union by rank it is
  O(alpha(n)), effectively constant but not literally O(1); saying so is a fast senior signal.

## A Clarifying-Question Checklist for Ambiguous Prompts

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

## Complexity Reference

Understanding time and space complexity is assumed at this level, not something to work out from
scratch in the interview. See the Big O cheat sheet at
[bigocheatsheet.com](https://www.bigocheatsheet.com/) for a refresher if any of the common
complexity classes are not immediately intuitive.