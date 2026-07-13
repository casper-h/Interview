# Concurrency and Multithreading

A smaller track than Low-Level Design or System Design, but worth deliberate coverage: it appears
both as a standalone topic and embedded inside system design deep dives, and it is commonly
underprepared relative to how often it comes up.

## Core concepts to be able to explain clearly

- **Race conditions.** What they are, a concrete example of one, and why they are hard to catch
  through testing alone.
- **Deadlock and livelock.** The conditions required for deadlock (mutual exclusion, hold and
  wait, no preemption, circular wait), and at least one strategy for avoiding it, such as
  consistent lock ordering.
- **Locks versus lock-free structures.** When a simple mutex is the right tool, and when
  contention makes a lock-free or compare-and-swap-based structure worth the added complexity.
- **Thread pools.** Why they exist, how they bound resource usage compared to spawning a thread
  per task, and the basic trade-off in choosing pool size.
- **Producer-consumer.** The pattern itself, and how a bounded queue between producer and
  consumer relates to backpressure, which also shows up in the system design track.

## Language-specific idioms

Prepare this section for whichever language you expect to interview in.

- **Java**: `synchronized`, the `java.util.concurrent` package, `ExecutorService`, and
  `CompletableFuture`.
- **Python**: the Global Interpreter Lock and what it does and does not protect you from,
  `threading` versus `multiprocessing`, and `asyncio` for I/O-bound concurrency.
- **Go**: goroutines and channels, and the idiom of communicating by sharing memory versus sharing
  memory by communicating.

## How concurrency shows up inside system design answers

This is where the standalone concepts above connect back to the System Design track, and is worth
being ready to raise unprompted during a deep dive.

- **Idempotency keys**, to handle retried requests safely, which is really a concurrency-adjacent
  correctness problem at the API layer.
- **Optimistic versus pessimistic concurrency control**, when multiple writers might update the
  same record, and the trade-off between retry-on-conflict and locking up front.
- **Distributed locks**, for example built on Redis or ZooKeeper, when coordination is needed
  across processes or machines rather than threads within one process.
- **Compare-and-swap**, as the building block behind both lock-free data structures and optimistic
  concurrency control.

## Practice approach

Rather than a long dedicated problem list, fold this in naturally: when working through the
System Design track's replication and consensus material, pause and ask how the same correctness
problem would be solved at the thread level within a single process, and vice versa. The two
tracks reinforce each other more than either does alone.