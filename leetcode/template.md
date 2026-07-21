# Pattern Recall Checklist

This is a self-test, not a worksheet. It is deliberately not a collection of code skeletons to write
out and memorize: a copied template collapses the moment a problem deviates from the exact shape you
memorized, and maintaining a bank of skeletons is busywork that does not survive interview pressure.
Instead, this file is a list of pattern *names*. The point of working through the [coding tracker](./README.md) is
that, after enough reps, you can picture the shape of each pattern from its name alone.

## How to Use It

Before a mock or a real interview, read down the list and, for each name, ask: **can I picture the
shape (the core loop, the state I maintain, the termination condition) without looking anything
up?** You do not need to write it out. If a name draws a blank, that is a specific, actionable signal:
go solve another problem or two in that category, rather than re-reading anything and calling it
handled. A confident mental picture for every name below means you are in good shape. The blanks are
your study list.

If you *want* a written note for a pattern whose edge cases keep tripping you (say, the exact
boundary conditions in binary search), keep it in your own words, kept short, and only for the
handful that actually need it: not as a completionist exercise across the whole list.

## The Patterns

- Two pointers, converging from both ends
- Sliding window, fixed size
- Sliding window, variable size (grow, then shrink to restore the invariant)
- Fast and slow pointers (cycle detection)
- Binary search, standard (and the off-by-one boundary you always have to think about)
- Binary search on the answer (when the check is monotonic in the answer)
- Backtracking: subsets, permutations, combinations, and the pruning step that distinguishes them
- DFS and BFS on a graph
- DFS and BFS on a grid, including boundary handling
- Topological sort (both Kahn's algorithm and the DFS ordering)
- Union-Find, with path compression and union by rank
- Monotonic stack (next greater / next smaller element)
- Monotonic deque (sliding-window extremum)
- Dynamic programming, top-down with memoization
- Dynamic programming, bottom-up with tabulation, and how to convert one to the other
- State-machine DP (the buy/sell/cooldown family)
- Interval DP (choosing the last operation over a range)
- Prefix sum, and difference array for range updates
- Trie insert and search
- Dijkstra's shortest path (and when Bellman-Ford is needed instead)
- Minimum spanning tree (Prim's or Kruskal's)
- Heap / priority queue for top-K and merge-K
- Two heaps (a max-heap and a min-heap balanced for the running median)
- Sweep line (sort the interval endpoints into events, then sweep maintaining an active set)

## The Point, Restated

Reviewing this list is a fast diagnostic you can run in five minutes before a session. The blanks
tell you where to spend a rep or two. The ones you can picture confidently, you leave alone.
