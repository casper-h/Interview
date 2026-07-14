# System Design Interview Framework

The material in the [reading plan](../plan/README.md) builds deep knowledge. This document is different: it is
the repeatable structure that turns that knowledge into a coherent 45-to-60-minute interview
performance instead of a rambling knowledge dump. Read this before doing any practice design, and
review it weekly until the structure below becomes automatic.

## The structure: use this every time, out loud, explicitly

1. **Clarify requirements (roughly 3-to-5 minutes).** Identify the functional requirements: what
   does the system actually need to do? List the core use cases and separate the critical few from
   the nice-to-have. Then work the non-functional requirements as a checklist rather than prose,
   because a missed dimension here quietly wrecks a later decision:
   - **Scale:** daily/monthly active users, queries per second (average *and* peak), total data
     volume, and growth rate.
   - **Latency:** target percentiles (p50/p95/p99) for the key operations, not a single average.
   - **Availability:** the target (how many 9s), and whether it differs for reads vs writes.
   - **Consistency:** strong, causal, or eventual, decided *per data type*, since one system often
     needs different guarantees for different data. A quick heuristic to apply on the spot: strong
     for anything a stale read makes wrong (balances, inventory, unique constraints), read-your-writes
     or causal for a user needing to see their own action reflected, and eventual for feeds, counts,
     and caches where staleness is annoying but not incorrect. Making this call in the requirements
     step, rather than deferring all of it to the deep dive, is itself a senior signal.
   - **Durability:** how much recent data you can afford to lose on failure (none, seconds, minutes).
   - **Read/write ratio** and hot/cold data split, which drive caching and storage choices.

   Explicitly scope out what you are not designing, and say so out loud; this is a senior signal,
   since it shows you can bound a problem.
2. **Back-of-envelope estimation (roughly 3-to-5 minutes).** Estimate traffic (queries per
   second, peak versus average), storage growth, and bandwidth. See the cheat sheet below. This
   should directly inform later choices; for example, "at this write volume, a single relational
   leader cannot keep up, so we need to partition or shard."
3. **API design (roughly 3-to-5 minutes).** Define the three to five core endpoints or contracts
   (REST, gRPC, or GraphQL), briefly justifying the choice. Include the request and response
   shape for the one or two most important operations.
4. **High-level architecture (roughly 10-to-15 minutes).** Draw the major components and how data
   flows between them, narrating as you go. Don't over-design upfront; start with something
   reasonably simple, then justify each addition.
5. **Data model and storage choice (roughly 5-to-10 minutes).** Decide what is stored where, and
   explain why that storage system, whether SQL, NoSQL, wide-column, or a blob store, given the
   access patterns and consistency needs identified earlier. Sketch the key schema or entities,
   not every field.
6. **Deep dive (roughly 10-to-15 minutes), usually interviewer-directed.** Pick one or two
   components to go deep on. This is where replication, partitioning, consistency trade-offs, and
   the content covered in the [reading plan](../plan/README.md) actually get used, and where you reach into the
   [building blocks](../building_blocks/README.md) toolkit by name, naming the component, the
   alternative you rejected, and how it fails. Follow the interviewer's signal; if they lean into
   one area, that is where depth is expected.
7. **Bottlenecks, failure modes, and trade-offs (roughly 5-to-10 minutes).** Discuss single points
   of failure, hot partitions, the risk of cascading failure, and what happens under a partition
   or regional outage. State trade-offs explicitly rather than presenting a single "correct"
   answer; this is usually the highest-signal part of the interview.
8. **Wrap-up (roughly 2-to-3 minutes).** Cover monitoring and observability concretely: the key
   metrics per component, and SLIs/SLOs rather than a vague "we'd add monitoring" (see the
   observability block in the [building blocks](../building_blocks/README.md)). Touch on cost at scale if it
   is a meaningful lever (storage, compute, cross-region bandwidth), since Staff-level rounds often
   probe it. Then state what you would do with more time and what you would reconsider at ten times
   the scale.

A time-boxing note: in a 45-minute interview, you will not hit every step at full depth, and that
is expected. What is graded is that you have the structure and can navigate it, not that you
exhaustively complete every step. If time is short, say so explicitly; for example, "given the
time we have, I'd like to go deeper on X or Y. Which would you prefer I prioritize?"

## Drawing it, and recovering when you go wrong

The diagram is half the communication, so keep it legible: boxes for stateless services, cylinders
for datastores, labeled arrows for the protocol and direction, and a rough left-to-right or
top-to-bottom flow from client to storage. Draw it incrementally as you narrate, starting with the
few core components and leaving whitespace for what the deep dive will add, rather than crowding
everything on at once.

When the interviewer signals your approach is wrong, treat it as information, not as a verdict.
Acknowledge it directly ("you're right, that breaks down under X"), state the constraint it exposed,
and propose the correction concisely, then move. A clean pivot narrated out loud is a strong signal;
what reads badly is defending a broken approach, or apologizing and spiraling instead of adjusting.

## Back-of-envelope estimation cheat sheet

A few latency numbers are worth having memorized. The orders of magnitude matter more than the
exact figures.

- L1/L2 cache reference: roughly 1-to-4 nanoseconds.
- Main memory (RAM) reference: roughly 100 nanoseconds.
- SSD random read: roughly 10-to-100 microseconds (NVMe at the low end, SATA at the high end).
- Round trip within the same data center: roughly 0.5 milliseconds.
- Disk seek on a spinning disk: roughly 10 milliseconds.
- Round trip across a country or region: roughly 50-to-150 milliseconds.
- Packet round trip, for example between the US and Europe: roughly 150 milliseconds.

A useful rule of thumb: memory is roughly one hundred times faster than SSD, and SSD is roughly
one hundred times faster than a network round trip within a region. A cross-region round trip
dwarfs everything else, which is the core justification for regional replicas and CDNs whenever
that topic comes up.

**Traffic and storage math.**

- Queries per second from daily active users: take daily active users, multiply by average
  requests per user per day, and divide by 86,400 seconds for the average. Multiply by a peak
  factor, commonly two-to-three times the average (or use a stated peak-to-average ratio if one
  is given), for the peak figure.
- Storage: multiply records per day by average record size and by the retention period, then
  account for the replication factor (commonly three times) and index or metadata overhead
  (roughly an additional 20-to-30 percent).
- Bandwidth: multiply queries per second by average payload size, calculated separately for the
  read path and the write path.
- A few reminders on units: one day is approximately 86,400 seconds, and one million requests per
  day works out to roughly 12 queries per second on average. Always sanity-check peak against
  average explicitly, rather than computing only one of the two.
- A single server can typically handle low thousands of queries per second for simple reads,
  though this is highly workload-dependent; state your assumption out loud rather than presenting
  it as fact.

The numbers above are meant to sanity-check your reasoning, not to be memorized with precision.
Interviewers care that your estimation process is sound and that you actually use the result to
drive a design decision, such as justifying caching, ruling out a single-leader relational
database, or motivating geo-replication.

## API design primer

- **REST versus gRPC versus GraphQL.** REST is simple, cacheable, and widely understood, making
  it a good default for public or external APIs. gRPC uses an efficient binary protocol with
  strong typing, which suits internal service-to-service calls at high throughput and low
  latency, though it has weaker browser support. GraphQL is a good fit when clients need flexible,
  varying shapes of data, such as mobile versus web, but it gives up simple HTTP caching and
  introduces query-complexity and rate-limiting concerns of its own.
- **Idempotency keys.** For any write or mutation endpoint that might be retried, such as after a
  client timeout or a network blip, be ready to discuss how you would prevent duplicate side
  effects, for example a payment being processed twice. The standard pattern is a client-generated
  idempotency key paired with a server-side deduplication table.
- **Pagination.** Offset-based pagination is simple but breaks under concurrent writes; cursor- or
  keyset-based pagination is stable under writes and is the standard choice for feeds and large
  collections. Default to cursor-based pagination whenever scale or write concurrency is
  meaningful.
- **Versioning.** Compare URL versioning, such as `/v1/...`, with header-based versioning, and
  mention backward compatibility as a constraint on any schema change.

## Security and trust checklist

Weave these in briefly; they don't need to become a separate track.

- **Authentication and authorization.** How are users and services authenticated, for example
  through tokens or OAuth, and how is authorization scoped, for example through role-based access
  control or resource-level checks?
- **Rate limiting for abuse.** This is distinct from rate limiting for load shedding. Mention
  per-user or per-IP limits for public-facing write endpoints.
- **Encryption.** Cover encryption at rest, which may be storage-level or field-level for
  sensitive data, and encryption in transit, typically TLS. A single sentence is usually
  sufficient unless the interviewer probes further.
- **PII and data retention.** If the system stores user data, briefly note retention and deletion
  considerations; this is increasingly expected without being prompted, at the senior level.

## Adapting depth by company or team type

- **Product companies, or consumer-facing feature teams,** tend to emphasize scale, latency,
  caching, API design, and user-facing trade-offs.
- **Infrastructure or platform teams** tend to probe more deeply into the storage engine,
  consensus, and replication internals covered in the [reading plan](../plan/README.md), and the optional
  deep-dive white papers are more likely to be directly relevant here.
- **Fintech or payments companies** tend to focus explicitly on consistency, idempotency,
  auditability, and correctness under failure, over raw throughput.

Use this to calibrate which direction to volunteer for the deep dive when the interviewer offers
you the choice.