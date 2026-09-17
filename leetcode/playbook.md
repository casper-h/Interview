# Coding Interview Playbook

## 1. Clarify

Restate the problem and confirm only the assumptions that change the solution:

- input size and value range;
- duplicates, nulls, malformed input, or cycles;
- sortedness and whether mutation is allowed;
- required output when several answers exist;
- time, memory, streaming, or concurrency constraints.

Work one small example before coding. Do not mechanically ask every possible question.

## 2. Choose an Approach

Explain a correct baseline and identify its limiting cost. Name the pattern only when you can state why it applies. Define the invariant in one sentence, such as “the window contains no duplicate characters” or “the heap contains the best `k` candidates seen so far.”

Choose an approach that satisfies the stated constraints. Do not implement a more complex optimum when a simpler method is sufficient unless the interviewer asks for it.

## 3. Implement

- Use clear names and small, testable units.
- Narrate decisions and invariants, not every line typed.
- Keep boundary conditions close to the logic they protect.
- If you discover a flaw, say what changed and repair it deliberately.
- Manage time. If an approach is not converging, return to the example or simpler version.

When stuck, identify the exact blocked step, relax one constraint, solve the simpler form, and add the constraint back. A precise request for a hint is better than prolonged silence.

## 4. Test

Trace at least one ordinary example and one edge case before declaring completion. Consider:

- empty, null, singleton, and two-element inputs;
- duplicates, negatives, zeros, and extreme values;
- sorted and reverse-sorted data;
- skewed trees, disconnected graphs, self-loops, and cycles;
- overflow, off-by-one boundaries, and input mutation;
- any case that falsifies the stated invariant.

Correct bugs you find and rerun the affected cases.

## 5. Explain Complexity

State total time and auxiliary space, including preprocessing and recursion.

- Dynamic-array append is usually `O(1)` amortized, not worst-case.
- Recursive tree traversal uses `O(h)` call-stack space and may use `O(n)` on a skewed tree. Replacing recursion with an explicit stack does not make that `O(1)`.
- Sorting followed by a linear scan is normally `O(n log n)` overall.
- Hash-table operations are commonly `O(1)` average case, subject to hashing assumptions.
- Union find with path compression and union by rank is `O(alpha(n))` amortized.

## 6. Handle Follow-Ups

After the working solution, discuss changes rather than guessing what the interviewer wants:

- Can time improve by using more memory?
- Can memory improve without violating the time target?
- What if input arrives as a stream or no longer fits in memory?
- What if updates and queries are interleaved?
- What if several callers mutate shared state concurrently?
- What adversarial input breaks average-case behavior?

Communication should make reasoning inspectable, but it should not become a continuous monologue that reduces solution quality.
