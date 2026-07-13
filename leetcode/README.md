# LeetCode Practice Tracker

An extended, categorized list of problems for building pattern recognition, organized around the
patterns most commonly tested at Senior and Senior Plus level rather than around problem
difficulty alone.

## How to use this checklist

A checked box means you have solved the problem before, not that you have mastered the pattern.
Treat this list as a coverage map, and let two other files carry the actual weight of your
practice.

- Log every attempt, solved or not, in `schedule/tracker.md`, including how long it took and, if
  you struggled, why: a missed pattern, an implementation bug, a missed edge case, or a
  communication issue. That log is what tells you what to revisit; a checkmark by itself does
  not.
- Build `leetcode/templates.md` as you go. The goal of working through these problems is to
  internalize a small number of reusable algorithm skeletons through repetition and
  understanding, not to memorize solutions to individual problems. If you find yourself trying to
  recall "how did I solve this exact problem," that is a sign to go back to the underlying
  pattern instead.
- Time-box each attempt (a common approach is 30 to 45 minutes) before looking at a hint. Getting
  stuck and reasoning through why is part of building the pattern; open-ended, unbounded time
  spent on a single problem usually is not.
- Revisit problems on a spaced cadence rather than moving on permanently once checked. A problem
  you solved once under no time pressure and have not revisited in a month is not yet reliable
  under interview conditions.

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
- [x] Asteroid Collision
- [x] Next Greater Element I
- [x] Next Greater Element II
- [x] Final Prices With a Special Discount in a Shop
- [ ] Sliding Window Maximum (monotonic deque)
- [ ] Shortest Subarray with Sum at Least K (monotonic deque)

---

### Binary Search

- [x] Binary Search
- [ ] Search a 2D Matrix
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search in Rotated Sorted Array
- [ ] Median of Two Sorted Arrays
- [ ] Koko Eating Bananas (binary search on the answer)
- [ ] Capacity to Ship Packages Within D Days (binary search on the answer)

---

### Linked Lists

- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Reorder List
- [ ] Remove Nth Node From End
- [ ] Linked List Cycle

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
- [ ] Serialize and Deserialize Binary Tree

---

### Trie

- [ ] Implement Trie
- [ ] Word Search II
- [ ] Replace Words

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

### Dynamic Programming

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

---

### One-Dimensional and Two-Dimensional Dynamic Programming

- [ ] Unique Paths
- [ ] Minimum Path Sum
- [ ] Longest Increasing Subsequence
- [ ] Interleaving String

---

### Greedy

- [ ] Jump Game
- [ ] Jump Game II
- [ ] Gas Station
- [ ] Candy
- [ ] Merge Intervals
- [ ] Non-overlapping Intervals

---

### Intervals

- [ ] Insert Interval
- [ ] Merge Intervals
- [ ] Meeting Rooms
- [ ] Meeting Rooms II
- [ ] Non-overlapping Intervals

---

### Math and Bit Manipulation

- [ ] Sum of Two Integers
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Reverse Bits
- [ ] Missing Number
- [ ] Single Number
- [ ] Power of Two
- [ ] Rotate Image

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

### Design

- [ ] LRU Cache
- [ ] LFU Cache
- [ ] Design Twitter
- [ ] Design Hit Counter
- [ ] Serialize and Deserialize Binary Tree
- [ ] Design File System

These overlap with the practice list in `low_level_design/README.md`. Solving them here is about
the underlying data structure; solving the low-level design versions is about class design and
extensibility around the same core structure.