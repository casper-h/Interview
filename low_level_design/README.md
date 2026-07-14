# Low-Level Design / Object-Oriented Design

This track is distinct from both algorithmic (LeetCode) rounds and high-level system design.
Here, you are graded on class and interface design, on extensibility, and on applying
object-oriented principles live, often including extending your own design on the fly when the
interviewer adds a new requirement partway through.

See also the [concurrency track](./concurrency/README.md) for the concurrency-specific track.

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

Two related principles come up constantly in the follow-ups and are worth stating in your own words:

- **Composition over inheritance.** Prefer giving an object a collaborator (has-a) over subclassing
  (is-a) when you want to add or vary behavior. Inheritance couples you to a base class and its
  changes; composition lets behavior be swapped at runtime and keeps the hierarchy shallow. A common
  follow-up is "refactor this inheritance tree," and the answer is almost always composition.
- **Design for testability.** Inject dependencies (pass a collaborator through the constructor)
  rather than constructing them inside a class, so a test can substitute a fake. Small interfaces
  make those fakes cheap to write, and avoiding global mutable state (one reason Singleton is
  suspect) keeps tests from becoming order-dependent.

## Design patterns worth recognizing and applying live

There's no need to memorize the full Gang of Four catalog. Know the following well, since they
cover most interview scenarios.

- **Strategy.** Interchangeable algorithms behind a common interface, for example different
  pricing or matching strategies.
- **Observer.** Event or notification systems, for example notifying subscribers on a state
  change.
- **Factory, or Abstract Factory.** Decouples object creation from object usage.
- **Builder.** Constructs a complex object step by step behind a fluent interface, for example an
  HTTP request or a query with many optional fields. Separates how an object is assembled from what
  it ends up being, and avoids a constructor with a dozen arguments.
- **Adapter.** Converts one interface into another the caller expects, for example wrapping a
  third-party or legacy API so the rest of your code depends on your own interface. This is the
  pattern that answers the common "now integrate with an external system that returns a different
  shape" follow-up.
- **Decorator.** Adds behavior to an object without modifying its class, for example stacking
  discounts or building middleware-style request handling.
- **Composite.** Treats a single object and a group of objects uniformly through one interface, for
  example a file-system tree where files and directories both implement the same node type.
- **Chain of Responsibility.** Passes a request along a chain of handlers, each deciding whether to
  handle it or forward it, for example a middleware or request-filter pipeline.
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

## Sketching the class diagram

Most low-level design rounds happen on a whiteboard or a shared diagramming tool, and the drawing is
half the communication. You do not need formal UML, but the relationships have to be unambiguous, so
know the notation and use it consistently.

- **A class** is a box with its name, key fields, and key methods. You rarely need all three
  compartments; name plus the methods that matter is usually enough.
- **Inheritance and interfaces:** a hollow arrow from subtype to base type ("is-a"), and mark an
  interface with `<<interface>>` so it reads as a contract rather than a concrete class.
- **Composition vs association:** a filled diamond on the owner for composition (the part does not
  outlive the whole, for example a `ParkingLot` owning its `Level`s), a plain line for a looser
  reference. Being deliberate here is exactly the composition-over-inheritance judgment made visible.
- **Cardinality:** label the ends (`1`, `0..1`, `1..*`) so "a lot has many levels, a level has many
  spots" is on the page, not only in your narration.

Draw incrementally rather than all at once: start with the two or three core entities, add
relationships as you talk, and leave whitespace so the new class the interviewer asks for has
somewhere to go.

## Practice problem list

Work through the following using the framework above, ideally writing real skeleton code in your
interview language rather than only talking through it. The [examples](./examples/README.md) folder
has a few worked skeletons to study for shape (how the classes and interfaces fit together), not to
memorize; the value is in seeing an extensible structure, then closing the file and rebuilding it
yourself against a new requirement.

- Parking lot
- Elevator system
- Vending machine
- Tic-tac-toe or chess (move validation, board state)
- In-memory key-value store with a time-to-live and eviction policy (this connects naturally to
  the LeetCode LRU and LFU cache problems)
- A rate limiter implemented as a reusable library or class, using the token bucket or leaky
  bucket algorithm; this is distinct from the system-level rate limiter design covered in the
  [system design practice list](../system_design/practice_design/README.md)
- Splitwise-style expense-sharing system
- Library management system
- Movie ticket booking system, scoped to a single service rather than the distributed version
- ATM, which is a clean State-pattern exercise (idle, card inserted, authenticated, dispensing)
  layered over a small transaction model
- An in-memory file system with files and directories, `ls`, `cd`, and `mkdir`, which is the
  canonical Composite-pattern problem
- Logging framework, with levels, sinks, and formatters, which is good practice for the Decorator
  and Strategy patterns
- A REST API for a resource such as orders or users, as a design exercise: resource modeling, the
  HTTP verbs and status codes, pagination and filtering, versioning, and error shapes. This is a
  common senior-level variant at companies whose product is an API.

**Component and library design.** Alongside the domain-modeling classics above, prepare a few
problems that are about designing a reusable *component* rather than modeling a real-world domain.
At the senior level and above, the signal increasingly shifts toward "design a clean, extensible
library other engineers will build on," and these exercise interfaces and extensibility more
directly than the domain problems do.

- Retry-with-backoff and circuit-breaker utility, with pluggable backoff and failure policies
- A validation framework, composing rules with clear error reporting (good Strategy/Composite
  practice)
- An in-process task scheduler or job queue, with priorities and retries
- A configuration system with layered overrides (defaults, environment, runtime) and typed access

For each problem, log the attempt in the [tracker](../schedule/tracker.md), noting what you would extend if given
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