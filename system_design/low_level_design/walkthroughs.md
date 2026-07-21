# Worked Design Walkthroughs

These five walkthroughs demonstrate the pattern anchors: where a strategy plugs in, how composition
wins over inheritance, where a new requirement lands as a class rather than a rewrite. Each applies
that discipline to the hardest follow-up the problem typically gets, the extend-live moment that
separates a lean design from a strong one, and names its core objects, the pattern to reach for, and
how a well-factored design absorbs the follow-up. For additional worked code examples, see the
[system-design-primer's object-oriented design solutions](https://github.com/donnemartin/system-design-primer#object-oriented-design-interview-questions-with-solutions),
which cover parking lot, LRU cache, call center, deck of cards, hash map, and online chat.

### Parking Lot

Core objects: `Vehicle`, `ParkingSpot`, `Level`, `ParkingLot`, and `PricingStrategy`. For a worked
code example see the [parking lot solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/parking_lot/parking_lot.ipynb)
in the system-design-primer. The trap is building a vehicle hierarchy (`Motorcycle`, `Car`, `Van`)
and then trying to extend it when the interviewer asks for EV charging spots. Reach for
[Strategy](https://refactoring.guru/design-patterns/strategy) and composition instead: give
`ParkingSpot` a `spotType` field (`COMPACT`, `LARGE`, `EV_CHARGING`) and inject a `PricingStrategy`
interface (`calculate(vehicle, duration) -> cost`) so a new pricing rule is a new class, not an edit
to every existing spot. The follow-up, "add EV charging," becomes a new `SpotType` value plus an
`EVPricingStrategy`. Nothing else changes. Clean extension is the signal here, not enumerating vehicle
types from memory.

### ATM

Core objects: `ATM`, `Card`, `Account`, `Transaction`, and most importantly `ATMState`. Model the
lifecycle as a state machine using [State](https://refactoring.guru/design-patterns/state):
`IdleState`, `CardInsertedState`, `AuthenticatedState`, `DispensingState`, each implementing a common
`ATMState` interface whose methods (`insertCard()`, `enterPIN()`, `selectAmount()`, `dispense()`)
delegate to the current state. The hardest follow-up is "support multi-account selection" or "add a
CardBlockedState." Both land cleanly: multi-account adds a state and a transition; a blocked card adds
one more state. The state pattern localizes behavior per phase, so extending the lifecycle is a new
class plus wiring, not a rewrite of every operation.

### In-Memory File System

Core objects: `FileSystemNode` as an interface, `File` and `Directory` as implementations, with
`Directory` holding a map of children. This is the textbook
[Composite](https://refactoring.guru/design-patterns/composite) problem: treat files and directories
uniformly through `size()`, `ls()`, and `remove()`. The follow-up is usually "add symbolic links" or
"add permissions." A symbolic link becomes a third `FileSystemNode` type that delegates to a target,
staying inside the composite structure; permissions add a `canRead()` / `canWrite()` check at each
node without touching the relationship between files and directories. If your design couples directory
operations to concrete file types, the follow-up breaks it. Depend on the interface, not the concrete
classes.

### Logging Framework

Core objects: `Logger`, `LogLevel`, `LogSink` (interface: `write(message)`), and `Formatter`
(interface: `format(level, message) -> string`). Use
[Strategy](https://refactoring.guru/design-patterns/strategy) for both sinks (console, file, network)
and formatters (JSON, plain text), then layer
[Decorator](https://refactoring.guru/design-patterns/decorator) on top for an async or buffered sink
that wraps another sink and adds behavior without modifying it. The hardest follow-up is "change the
log level at runtime" or "add a sink without restarting." Both require sinks and level to be mutable
state injected through a setter or builder, not fixed at construction. A library that cannot
reconfigure itself live reads as over-rigid; make that mutability explicit upfront.

### Elevator System

Core objects: `Elevator`, `Request`, `ElevatorController`, `DispatchStrategy`, and `ElevatorState`
(idle, moving up, moving down). Model each elevator's motion with
[State](https://refactoring.guru/design-patterns/state) and extract the dispatch logic into a
[Strategy](https://refactoring.guru/design-patterns/strategy): `NearestCarStrategy`,
`MinimizeWaitStrategy`. The killer follow-up is "add express elevators that skip certain floors" or
"change the dispatch policy live." Express elevators need an `allowedFloors` set per elevator and a
check inside `canService(request)`; a new dispatch policy is a new strategy class. If dispatch is
baked into the controller as one hardcoded method, the follow-up forces a rewrite. Depend on the
strategy interface, not the algorithm.
