# Pattern Templates

This file is not a reference sheet to memorize before an interview. It is a place to write down,
in your own words and your own syntax, the skeleton of each pattern once you have solved enough
problems in that category to recognize the shape yourself. The point of working through
`leetcode/README.md` is to arrive at these skeletons through repetition and understanding. If you
copy a template in here before you have actually derived it from practice, it will not hold up
under interview pressure, since you will not be able to adapt it when the problem deviates from
the exact shape you memorized.

A reasonable process: after solving three or four problems in a pattern, attempt to write the
skeleton from memory, without looking at your previous solutions. Compare it against what you
actually wrote, note where it differs, and only then update this file.

## Suggested skeletons to build

Fill these in as you reach them, rather than all at once.

- Two pointers (converging, from both ends)
- Sliding window, fixed size
- Sliding window, variable size
- Fast and slow pointers (cycle detection)
- Binary search, standard
- Binary search on the answer
- Backtracking (subsets, permutations, combinations, and the pruning step that distinguishes
  them)
- Depth-first search and breadth-first search on a graph
- Depth-first search and breadth-first search on a grid, including boundary handling
- Topological sort (both the Kahn's algorithm and depth-first orderings)
- Union-Find, with path compression and union by rank
- Monotonic stack
- Monotonic deque
- Dynamic programming, top-down with memoization
- Dynamic programming, bottom-up with tabulation, and how to convert from the top-down version
- Prefix sum, and difference array for range updates
- Trie insert and search
- Dijkstra's algorithm

## A note on how to actually use this once built

Before a real interview, review the list of skeleton names above, not the code. If you can
picture the shape of each one from the name alone, you are in good shape. If a name draws a
blank, that is a specific, actionable signal to go back and solve another problem or two in that
category, rather than to re-read the skeleton and consider it handled.