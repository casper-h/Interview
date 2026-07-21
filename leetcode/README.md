# Coding Practice Tracker

An extended, categorized list of problems for building pattern recognition, organized around the
patterns most commonly tested at the senior level and above rather than around problem difficulty
alone.

## How to Use This Checklist

A checked box means you have solved the problem before, not that you have mastered the pattern.
Treat this list as a coverage map, and let two other files carry the actual weight of your
practice.

- Log every attempt, solved or not, in the [tracker](../schedule/tracker.md), including how long it took and, if
  you struggled, why: a missed pattern, an implementation bug, a missed edge case, or a
  communication issue. That log is what tells you what to revisit; a checkmark by itself does
  not.
- Use [template](./template.md) as a pattern-recall self-test, not a set of skeletons to write out.
  The goal of working through these problems is to internalize a small number of reusable algorithm
  shapes through repetition and understanding, not to memorize solutions to individual problems. If
  you find yourself trying to recall "how did I solve this exact problem," that is a sign to go back
  to the underlying pattern instead.
- Time-box each attempt (a common approach is 30 to 45 minutes) before looking at a hint. Getting
  stuck and reasoning through why is part of building the pattern; open-ended, unbounded time
  spent on a single problem usually is not.
- Revisit problems on a spaced cadence rather than moving on permanently once checked. A problem
  you solved once under no time pressure and have not revisited in a month is not yet reliable
  under interview conditions.

## Core and Stretch Coverage

Each category below is split implicitly into **core** and **stretch**. Solving two problems in a
category is usually enough to establish the pattern and recognize it under pressure: that is the
core bar, and it is what "covered every category once" means in the schedule. The **stretch**
problems (the hard-tier and less common ones, flagged where they appear) are what you return to in
Phase 3 for the categories your mock feedback flags as weak. This is the concrete difference between
a hire and a strong hire in a coding round: a hire recognizes the pattern; a strong hire has also
drilled the hard variant the interviewer escalates to. Do not treat finishing every box as the
goal: depth in weak categories yields more than breadth that is never revisited.

## Two Behaviors Graded Beyond Correctness

These are graded even on problems you solve correctly. Practice them deliberately, not just when an
interviewer prompts you.

- **Clarify before coding.** Before writing anything, state the input constraints (size, value
  range, sortedness), whether the input may be mutated, whether duplicates or nulls are possible,
  and any performance requirement beyond big-O (in place, single pass, streaming). Even in solo
  practice, write these down first: it establishes the habit for interview conditions. See
  the [general coding guide](./playbook.md) for the fuller clarifying-question checklist.
- **Drill the optimization follow-up.** After you have a working solution, do not stop. Ask, out
  loud: can I reduce time complexity further? Can I reduce space? What is the trade-off, and when
  would each variant be preferred? How does this change if the input no longer fits in memory, or
  arrives as a stream, or must support concurrent updates? The interviewer's "can you do better?"
  is where the strong-hire signal lives, and it is a trainable reflex: log the optimization you
  found (or ruled out) in the tracker alongside the initial solve.

---

### Arrays and Hashing

- [x] Two Sum
- [x] Group Anagrams
- [x] Top K Frequent Elements
- [x] Contains Duplicate
- [x] Product of Array Except Self
- [x] Maximum Subarray
- [x] Longest Consecutive Sequence
- [ ] Encode and Decode Strings

---

### Prefix Sum and Difference Array

A distinct pattern from general array manipulation: precomputing running sums (or running
differences for range updates) to answer range queries in constant time after linear
preprocessing.

- [ ] Range Sum Query, Immutable
- [ ] Subarray Sum Equals K
- [ ] Product of Array Except Self (revisit through the prefix and suffix lens specifically)
- [ ] Range Addition

---

### Two Pointers

- [x] Valid Palindrome
- [x] Two Sum II
- [x] 3Sum
- [x] Container With Most Water
- [x] Trapping Rain Water
- [x] Push Dominoes

---

### Sliding Window

- [ ] Best Time to Buy and Sell Stock
- [ ] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [ ] Permutation in String
- [ ] Minimum Window Substring
- [ ] Sliding Window Maximum (also see Monotonic Deque below)

---

### Monotonic Stack and Monotonic Deque

Stack-based problems are grouped here with deque-based problems because they share the same core
idea: maintaining a monotonic ordering of candidates and discarding ones that can no longer be
the answer.

- [x] Valid Parentheses
- [x] Min Stack
- [x] Daily Temperatures
- [x] Largest Rectangle in Histogram
- [x] Next Greater Element II (the circular variant; the plain Next Greater Element I and Final
  Prices are the same shape, so one is enough)
- [x] Asteroid Collision
- [ ] Sliding Window Maximum (monotonic deque)
- [ ] Shortest Subarray with Sum at Least K (monotonic deque)

---

### Binary Search

- [x] Binary Search
- [ ] Search a 2D Matrix
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search in Rotated Sorted Array
- [ ] Koko Eating Bananas (binary search on the answer)
- [ ] Capacity to Ship Packages Within D Days (binary search on the answer)
- [ ] Split Array Largest Sum (binary search on the answer, the harder escalation)
- [ ] Median of Two Sorted Arrays (stretch)

---

### Linked Lists

- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Reorder List
- [ ] Remove Nth Node From End
- [ ] Linked List Cycle
- [ ] Add Two Numbers
- [ ] Copy List with Random Pointer

---

### Matrix and Grid Traversal

Grid-based breadth-first and depth-first search is common enough, and different enough from
general graph problems in its boundary handling, to warrant its own category rather than sitting
inside Graphs.

- [ ] Number of Islands
- [ ] Flood Fill
- [ ] Rotting Oranges
- [ ] Surrounded Regions
- [ ] Pacific Atlantic Water Flow
- [ ] Walls and Gates

---

### Trees (Depth-First and Breadth-First Search)

- [ ] Maximum Depth of Binary Tree
- [ ] Same Tree
- [ ] Invert Binary Tree
- [ ] Subtree of Another Tree
- [ ] Binary Tree Level Order Traversal
- [ ] Lowest Common Ancestor of a Binary Search Tree
- [ ] Diameter of Binary Tree
- [ ] Serialize and Deserialize Binary Tree (stretch; also appears under Data-Structure Design, so
  do it once there rather than twice)

---

### Trie

- [ ] Implement Trie
- [ ] Replace Words
- [ ] Word Search II (stretch; a trie-plus-backtracking combination, not core trie)

---

### String Matching (Stretch)

Lower frequency than the categories above and safe to skip for a generalist product loop, but worth
one working implementation each if you are targeting search, compiler, or text-heavy teams, or want
full coverage. The core idea across all three is avoiding the naive O(n*m) rescan by precomputing
structure in the pattern (KMP's failure function) or hashing a rolling window (Rabin-Karp).

- [ ] Implement strStr (KMP)
- [ ] Repeated Substring Pattern (KMP failure function, or rolling hash)
- [ ] Longest Palindromic Substring (Manacher's, as the optimal follow-up to the DP version)

---

### Heap and Priority Queue

- [ ] Kth Largest Element in an Array
- [ ] Top K Frequent Elements
- [ ] Find Median from Data Stream
- [ ] Merge K Sorted Lists

---

### Backtracking

- [ ] Subsets
- [ ] Subsets II
- [ ] Combination Sum
- [ ] Permutations
- [ ] Word Search
- [ ] N-Queens
- [ ] Sudoku Solver

---

### Graphs (Depth-First and Breadth-First Search)

- [ ] Clone Graph
- [ ] Number of Islands (also see Matrix and Grid Traversal)
- [ ] Graph Valid Tree
- [ ] Number of Provinces
- [ ] Is Graph Bipartite
- [ ] Course Schedule (also see Topological Sort)
- [ ] Pacific Atlantic Water Flow (also see Matrix and Grid Traversal)
- [ ] Word Ladder

---

### Topological Sort

A distinct pattern from general graph traversal, worth practicing explicitly rather than only
encountering incidentally through Course Schedule.

- [ ] Course Schedule
- [ ] Course Schedule II
- [ ] Alien Dictionary
- [ ] Sequence Reconstruction

---

### Shortest Path and Weighted Graphs

Plain BFS/DFS handles unweighted reachability, but weighted-graph problems need their own
algorithms, and their absence is a real gap at companies that lean on graph or infrastructure
problems (Google, and infra- or trading-adjacent teams). Know when to reach for each: BFS for
unweighted shortest path, Dijkstra for non-negative weights, Bellman-Ford when negative weights are
possible, Floyd-Warshall for all-pairs on small graphs, and a minimum-spanning-tree algorithm
(Prim's or Kruskal's) for lowest-cost connectivity.

- [ ] Network Delay Time (Dijkstra)
- [ ] Cheapest Flights Within K Stops (Bellman-Ford, or Dijkstra with a hop constraint)
- [ ] Path with Maximum Probability (Dijkstra variant)
- [ ] Swim in Rising Water (Dijkstra or binary search + union-find)
- [ ] Min Cost to Connect All Points (minimum spanning tree: Prim's or Kruskal's) (stretch)
- [ ] Find the City With the Smallest Number of Neighbors at a Threshold Distance (Floyd-Warshall) (stretch)

---

### Dynamic Programming

Kept as one category rather than split by dimension: the one-dimensional and two-dimensional
problems share the same core skill of defining a state and a transition, and artificially splitting
them weakens the mental model. Build the foundation here first, then move to the advanced variants
below.

- [ ] Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Longest Palindromic Substring
- [ ] Palindromic Substrings
- [ ] Longest Common Subsequence
- [ ] Coin Change
- [ ] Partition Equal Subset Sum
- [ ] Decode Ways
- [ ] Edit Distance
- [ ] Unique Paths (two-dimensional grid)
- [ ] Minimum Path Sum (two-dimensional grid)
- [ ] Longest Increasing Subsequence
- [ ] Interleaving String

---

### Advanced Dynamic Programming

The hard-tier DP variants an interviewer escalates to once you have the foundation. These are the
stretch problems that most distinguish a strong hire in a DP round: the interviewer rarely stops at
Coin Change. Practice recognizing which sub-shape a problem is: state-machine, interval, bitmask, or
DP over a tree.

- [ ] Best Time to Buy and Sell Stock with Cooldown (state-machine DP)
- [ ] Best Time to Buy and Sell Stock with Transaction Fee (state-machine DP)
- [ ] House Robber III (DP on a tree)
- [ ] Binary Tree Maximum Path Sum (DP on a tree, also appears under Trees)
- [ ] Burst Balloons (interval DP)
- [ ] Minimum Cost to Merge Stones (interval DP)
- [ ] Shortest Path Visiting All Nodes (bitmask DP over subsets)
- [ ] Partition to K Equal Sum Subsets (bitmask DP)

---

### Greedy and Interval Scheduling

Interval problems are fundamentally greedy (sort, then sweep), so they are grouped with the rest of
the greedy pattern rather than split into a near-duplicate category. The recurring idea is that a
locally optimal choice (earliest finishing interval, farthest reachable index) yields a globally
optimal result, and being able to say *why* that holds for a given problem is part of the signal.

- [ ] Jump Game
- [ ] Jump Game II
- [ ] Gas Station
- [ ] Candy
- [ ] Merge Intervals
- [ ] Insert Interval
- [ ] Non-overlapping Intervals
- [ ] Meeting Rooms
- [ ] Meeting Rooms II (minimum number of rooms: the classic follow-up)

---

### Math and Bit Manipulation

Low frequency overall, but each sub-area is a fast signal when it comes up, and a blank on
fast-exponentiation or the sieve is an avoidable stumble. Keep one representative of each idea.

- [ ] Sum of Two Integers
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Reverse Bits
- [ ] Missing Number
- [ ] Single Number
- [ ] Power of Two
- [ ] Rotate Image
- [ ] Pow(x, n) (fast exponentiation)
- [ ] Count Primes (Sieve of Eratosthenes)
- [ ] Greatest Common Divisor of Strings (Euclidean algorithm) (stretch)

---

### Union Find

- [ ] Number of Connected Components in an Undirected Graph
- [ ] Graph Valid Tree
- [ ] Accounts Merge
- [ ] Redundant Connection

---

### Segment Tree and Binary Indexed Tree

Less frequently tested than the categories above, but worth having at least one working
implementation of each for harder rounds, particularly at infrastructure-heavy or
trading-adjacent companies.

- [ ] Range Sum Query, Mutable (binary indexed tree or segment tree)
- [ ] Count of Smaller Numbers After Self
- [ ] Range Sum Query 2D, Mutable

---

### Data-Structure Design

These problems are about implementing a data structure to hit specific complexity targets (for
example, an LRU cache with O(1) get and put): the algorithmic skill of choosing and combining
structures. That is distinct from the low-level design track, where the same prompts are about class
design, interfaces, and extensibility. Do them here for the structure; see
the [low-level design guide](../system_design/low_level_design/README.md) for the design-round version, and do not double-count the two.

- [ ] LRU Cache
- [ ] LFU Cache (stretch)
- [ ] Design Twitter
- [ ] Design Hit Counter
- [ ] Serialize and Deserialize Binary Tree
- [ ] Insert Delete GetRandom O(1)
- [ ] Min Stack (also appears under Monotonic Stack)