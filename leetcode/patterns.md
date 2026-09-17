# Coding Pattern Catalog

Problems are grouped by the main idea worth practicing. **Core** problems establish the pattern. **Reinforcement** adds variation. **Harder or targeted** material is optional unless diagnostics or a target loop justify it.

## Arrays and Hashing

- **Core:** Two Sum; Group Anagrams; Product of Array Except Self; Longest Consecutive Sequence.
- **Reinforcement:** Contains Duplicate; Maximum Subarray; Top K Frequent Elements; Encode and Decode Strings.

Invariant: stored counts, positions, or prefix information represent exactly the portion already processed.

## Two Pointers and Sliding Window

- **Core:** Valid Palindrome; 3Sum; Longest Substring Without Repeating Characters; Longest Repeating Character Replacement.
- **Reinforcement:** Container With Most Water; Permutation in String; Minimum Window Substring.
- **Harder:** Trapping Rain Water; Sliding Window Maximum.

Invariant: the window or pointer region satisfies a stated condition, and each move makes monotonic progress.

## Prefix Sums

- **Core:** Range Sum Query, Immutable; Subarray Sum Equals K.
- **Reinforcement:** Product of Array Except Self; Range Addition.

Invariant: a prefix summary allows a range result to be derived from two boundaries.

## Stack and Monotonic Structures

- **Core:** Valid Parentheses; Min Stack; Daily Temperatures.
- **Reinforcement:** Asteroid Collision; Next Greater Element II.
- **Harder:** Largest Rectangle in Histogram; Shortest Subarray with Sum at Least K.

Invariant: candidates that remain on the structure are ordered and have not yet been invalidated by later input.

## Binary Search

- **Core:** Binary Search; Search in Rotated Sorted Array; Koko Eating Bananas.
- **Reinforcement:** Search a 2D Matrix; Find Minimum in Rotated Sorted Array; Capacity to Ship Packages Within D Days.
- **Harder:** Split Array Largest Sum; Median of Two Sorted Arrays.

Invariant: the remaining interval contains every feasible answer, often because a predicate is monotonic.

## Linked Lists

- **Core:** Reverse Linked List; Merge Two Sorted Lists; Linked List Cycle.
- **Reinforcement:** Remove Nth Node From End; Reorder List; Copy List with Random Pointer; Add Two Numbers.

Invariant: identify which links still represent the unprocessed list before mutating pointers.

## Trees

- **Core:** Maximum Depth of Binary Tree; Binary Tree Level Order Traversal; Lowest Common Ancestor of a Binary Search Tree; Diameter of Binary Tree.
- **Reinforcement:** Invert Binary Tree; Same Tree; Subtree of Another Tree; Serialize and Deserialize Binary Tree.
- **Harder:** Binary Tree Maximum Path Sum.

Invariant: define precisely what each recursive return value or breadth-first level represents.

## Graphs and Grids

- **Core:** Number of Islands; Clone Graph; Course Schedule; Rotting Oranges.
- **Reinforcement:** Graph Valid Tree; Pacific Atlantic Water Flow; Word Ladder; Is Graph Bipartite.
- **Harder:** Alien Dictionary; Sequence Reconstruction.

Invariant: visited state means a node has been discovered or fully processed. Choose the meaning deliberately for cycle detection and shortest paths.

## Weighted Graphs and Union Find

- **Core:** Network Delay Time; Number of Connected Components; Redundant Connection.
- **Reinforcement:** Cheapest Flights Within K Stops; Accounts Merge; Min Cost to Connect All Points.
- **Harder:** Swim in Rising Water; Path with Maximum Probability.

Know why breadth-first search handles unweighted shortest paths, Dijkstra requires nonnegative weights, Bellman-Ford tolerates negative weights, and union find answers dynamic connectivity rather than general path queries.

## Heap and Priority Queue

- **Core:** Kth Largest Element in an Array; Top K Frequent Elements; Merge K Sorted Lists.
- **Reinforcement:** Find Median from Data Stream; Meeting Rooms II.

Invariant: the heap contains the best bounded candidate set or the next item from each ordered source.

## Intervals and Greedy

- **Core:** Merge Intervals; Non-overlapping Intervals; Jump Game.
- **Reinforcement:** Insert Interval; Meeting Rooms; Gas Station; Jump Game II.
- **Harder:** Candy.

State the exchange argument or monotonic property that makes a local choice safe.

## Backtracking

- **Core:** Subsets; Combination Sum; Permutations; Word Search.
- **Reinforcement:** Subsets II; N-Queens.
- **Harder:** Sudoku Solver.

Invariant: the current path satisfies all decisions made so far; restore mutable state before exploring the next branch.

## Dynamic Programming

- **Core:** Climbing Stairs; House Robber; Coin Change; Longest Common Subsequence.
- **Reinforcement:** Decode Ways; Partition Equal Subset Sum; Longest Increasing Subsequence; Unique Paths.
- **Harder:** Edit Distance; Interleaving String; Burst Balloons; House Robber III.

Define the state, recurrence, base cases, evaluation order, and whether state can be compressed before coding.

## Trie and Data-Structure Design

- **Core:** Implement Trie; LRU Cache; Insert Delete GetRandom O(1).
- **Reinforcement:** Replace Words; Design Hit Counter; Serialize and Deserialize Binary Tree.
- **Harder:** Word Search II; LFU Cache.

Derive the required operations and complexity targets before combining structures.

## Targeted Topics

Use only when relevant to a role or diagnosed gap:

- **Bit manipulation:** Single Number; Counting Bits; Sum of Two Integers.
- **Math:** Pow(x, n); Count Primes; Rotate Image.
- **Range structures:** Range Sum Query, Mutable; Count of Smaller Numbers After Self.
- **String algorithms:** Implement strStr with KMP; Rabin-Karp; Manacher's algorithm.
