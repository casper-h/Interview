# Low-Level Design / Object-Oriented Design

This track is distinct from both algorithmic (LeetCode) rounds and high-level system design.
Here, you are graded on class and interface design, on extensibility, and on applying
object-oriented principles live, often including extending your own design on the fly when the
interviewer adds a new requirement partway through.

See also `low_level_design/concurrency/README.md` for the concurrency-specific track.

## Core principles to have crisp, example-backed definitions for

**SOLID.**

- **Single Responsibility.** A class should have one reason to change.
- **Open/Closed.** A class should be open for extension but closed for modification; favor adding
  new classes over editing existing ones when adding behavior.
- **Liskov Substitution.** Subtypes must be substitutable for their base types without breaking
  correctness.
- **Interface Segregation.** Prefer several small, specific interfaces over one large one.
- **Dependency Inversion.** Depend on abstractions, not on concrete implementations.

Be ready to explain why each of these matters for extensibility and testability, not just to
define them.

## Design patterns worth recognizing and applying live

There's no need to memorize the full Gang of Four catalog. Know the following well, since they
cover most interview scenarios.

- **Strategy.** Interchangeable algorithms behind a common interface, for example different
  pricing or matching strategies.
- **Observer.** Event or notification systems, for example notifying subscribers on a state
  change.
- **Factory, or Abstract Factory.** Decouples object creation from object usage.
- **Decorator.** Adds behavior to an object without modifying its class, for example stacking
  discounts or building middleware-style request handling.
- **Singleton.** Know it, but also be ready to explain why it is often considered an anti-pattern
  in interviews, due to global state and testability issues, and when it is actually appropriate.
- **State.** An object's behavior changes based on its internal state, for example the lifecycle
  of an order or a connection.
- **Command.** Encapsulates a request as an object, useful for undo and redo behavior or for task
  queues.

## The framework: use this structure out loud

1. **Clarify requirements.** What are the core use cases, and what is explicitly out of scope?
2. **Identify the core objects and nouns.** Pull these directly from the requirements.
3. **Define relationships and interfaces.** Decide between composition and inheritance, and
   determine what should be an interface versus a concrete class, and how objects reference one
   another.
4. **Write skeleton classes.** Provide method signatures and key fields; there's no need to fully
   implement every method unless asked.
5. **Walk through the core use cases against your design.** Does it actually satisfy them?
6. **Extend the design live.** The interviewer will very likely add a new requirement, for
   example, "now also support X." This is usually the single most important signal of the whole
   round. A design that can absorb the new requirement with a small, localized change, such as a
   new class or strategy, rather than a rewrite, is what is being tested.

## Practice problem list

Work through the following using the framework above, ideally writing real skeleton code in your
interview language rather than only talking through it.

- Parking lot
- Elevator system
- Vending machine
- Tic-tac-toe or chess (move validation, board state)
- In-memory key-value store with a time-to-live and eviction policy (this connects naturally to
  the LeetCode LRU and LFU cache problems)
- A rate limiter implemented as a reusable library or class, using the token bucket or leaky
  bucket algorithm; this is distinct from the system-level rate limiter design covered in
  `system_design/practice_designs/`
- Splitwise-style expense-sharing system
- Library management system
- Movie ticket booking system, scoped to a single service rather than the distributed version
- Logging framework, with levels, sinks, and formatters, which is good practice for the Decorator
  and Strategy patterns

For each problem, log the attempt in `schedule/tracker.md`, noting what you would extend if given
an additional requirement, and where the design would break.

## Common mistakes at the senior level

- Jumping straight to code before clarifying requirements or naming the core entities.
- Over-engineering upfront by adding patterns or abstractions the stated requirements don't yet
  need. A senior signal is knowing when not to add abstraction, not just knowing the patterns
  themselves.
- Under-engineering, producing a design that cannot absorb the interviewer's follow-up requirement
  without a rewrite.
- Ignoring concurrency entirely when the problem implies shared or mutable state, for example in
  a parking lot or a rate limiter accessed by multiple threads. See the concurrency track for
  this.