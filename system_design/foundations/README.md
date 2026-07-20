# Foundations

The layer beneath distributed systems design. The [framework](../framework.md) and
[building blocks](../building_blocks.md) teach you to design a system at a high level; this
area is what lets you answer when an interviewer probes below that level and asks how the pieces
actually work. It groups two related tracks:

- **[Fundamentals](./fundamentals.md):** networking, operating systems, and database internals.
  This is reference material for infrastructure-, platform-, systems-, and trading-adjacent loops
  that test below the distributed-systems layer. A candidate who can sketch Spanner but cannot
  explain a TCP handshake or a B-tree reads as having memorized system design rather than
  understood it.
- **[Concurrency](./concurrency.md):** threading, the memory model, and the coordination
  primitives that appear both as a standalone round and inside system-design deep dives. It bridges
  the thread-level reasoning of the low-level design round and the cross-process reasoning of the
  distributed systems track.

Both tracks are foundations rather than the main event. Fundamentals is largely review once you have
done the DDIA and Database Internals reading in the [reading plan](../plan/README.md). Concurrency
earns dedicated reps because it is commonly underprepared relative to how often it comes up. Weight
them by the teams you are targeting, using the "Adapting depth by company or team type" guidance in
the [framework](../framework.md).
