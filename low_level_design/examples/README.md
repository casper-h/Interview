# Low-Level Design worked examples

These are reference skeletons, not solutions to memorize. Coding problems vary too much to bank
answers for, but low-level design patterns are stable, and seeing one clean, extensible structure
teaches more about class boundaries and where behavior should live than a blank page does.

Use them the way you would use a mock: read one for shape, notice where the extension points are
(the interface a new strategy would implement, the field a new subtype would set), then close it and
rebuild the design yourself against a requirement the skeleton does not handle. If you cannot absorb
that new requirement with a small, localized change, that is the gap to work on, and it is exactly
what the "extend the design live" step of the round is testing.

The examples are in Python for readability and are deliberately partial: signatures and the key
methods, with the rest left as the work you do. Translate the shape into your own interview language.

- [Parking lot](./parking_lot.py): the domain-modeling classic. Vehicle sizes, spot types, and a
  pluggable pricing strategy, chosen to show composition over inheritance and an extension point.
- [Rate limiter](./rate_limiter.py): a thread-safe token bucket behind a small interface, so a
  different algorithm (leaky bucket, sliding window) drops in without touching callers. Overlaps with
  the [concurrency track](../concurrency/README.md).
- [Logging framework](./logging_framework.py): levels, sinks, and formatters composed through the
  Strategy and Decorator patterns, the reusable-component style of problem that weighs more heavily
  at the senior level and above.
