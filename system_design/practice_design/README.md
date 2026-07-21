# Practice Designs

A consolidated list of system design prompts to work through, pulling together what already
existed scattered across the [reading plan](../plan/README.md) and adding the designs identified as
commonly asked but previously missing or reading-only.

Work each one end to end using the structure in the [framework](../framework.md), out loud,
against a clock. Log the attempt in the [tracker](../../schedule/tracker.md), including which part of the framework
was weakest, since that is a better use of the log than simply marking a design as done.

## How to Pick Which Ones to Prioritize

The full list below is more than anyone needs to do end to end. Use these tiers rather than working
top to bottom:

- **Tier 1: do these (roughly ten).** The highest-frequency prompts that also each exercise a
  distinct core skill: URL shortener, distributed cache, news feed, chat system, notification
  system, rate limiter, distributed message queue, key-value store, video platform, and a payment
  or wallet system. Clearing these end to end is the "minimum viable pass" for a Senior loop; it
  maps to the same gate in the [reading plan](../plan/README.md).
- **Tier 2: breadth.** The rest of the list, worked as time allows to widen the range of contexts
  you can apply the framework in.
- **Tier 3: targeted.** Weight toward the category matching a specific team you're interviewing
  with, using the "Adapting depth by company or team type" section of
  the [framework](../framework.md) (for example, the transactional and consistency-sensitive
  systems for a fintech loop, or the coordination and infrastructure ones for a platform team).

If you are not targeting a specific company yet, do all of Tier 1 for depth, then spread across the
categories below for breadth rather than going deep on any single one.

## Storage and Retrieval Systems

- URL shortener
- Distributed key-value store
- Distributed cache
- Distributed unique ID generator

## Feed, Messaging, and Real-Time Systems

- News feed
- Chat system, for example Slack or WhatsApp
- Notification system
- Real-time analytics pipeline

## Search and Discovery

- Search autocomplete and typeahead
- Web crawler
- Proximity or nearby-friends service
- Ride-hailing service, for example Uber or Lyft: driver-rider matching, real-time location, ETA,
  and surge pricing, which is the full system the proximity service is only one piece of
- Google Maps or a navigation service: routing, tiling, and traffic aggregation over a road graph

## Media and Content Platforms

- Video platform, for example YouTube or Netflix
- Photo-sharing service, for example Instagram: the follower graph, feed, and the many-small-files
  storage and CDN pattern, which differs from the large-file video case
- Content delivery and geo-replication for a global content platform

## Coordination and Infrastructure

- Distributed message queue, for example a Kafka-like system
- Rate limiter, as a service rather than as a class (see the [low-level design guide](../low_level_design/README.md) for the
  class-level version of the same problem)
- Distributed lock service
- Distributed job scheduler, with dependency DAGs, retries, and priority, for example a cron or
  workflow service at scale
- Metrics and observability platform

## Transactional and Consistency-Sensitive Systems

- Payment or digital wallet system
- Ticket or seat reservation system, for example a Ticketmaster-style booking flow
- Collaborative document editor, for example Google Docs, including a discussion of operational
  transformation versus conflict-free replicated data types
- Ad click aggregation and analytics

## Social and Graph-Shaped Systems

- Twitter-style timeline, with a comparison of fan-out on write versus fan-out on read
- Real-time leaderboard, for example for a game: sorted sets, windowed rankings, and how a global
  ranking is partitioned
- Recommendation system, combining a batch-trained model with real-time signal
- File storage and sync, for example Dropbox or Google Drive, with a clear separation between
  metadata and blob storage

## Machine-Learning Systems

- An ML platform for a real feature, for example a ranking or fraud model: the feature store, offline
  training versus online serving, model deployment and rollback, and the A/B and monitoring
  infrastructure around it. Increasingly its own dedicated round at the senior level and above, and
  a distinct skill from designing the recommendation system's data flow.

## Notes on Using This List Well

- Do not treat completing this list as the goal in itself. The goal is fluency with the framework
  and the underlying trade-offs; the list exists to give you varied enough contexts to build that
  fluency, not as a set of memorized designs to reproduce.
- Several of these overlap deliberately, for example the news feed and the Twitter-style timeline,
  or the distributed cache and the rate limiter. That overlap is intentional: solving a familiar
  trade-off in a new context is a good test of whether you actually understand it or only
  memorized the first version.
- Revisit two or three of the earliest designs you attempted later in your preparation, once
  you have covered more of the [reading plan](../plan/README.md), and compare your answer to your first attempt.
  The gap between the two is a useful, concrete measure of progress.

## Worked Walkthroughs

Four of the Tier-1 prompts are worked end to end in the [worked walkthroughs](./walkthroughs.md): Pastebin
(the content-storing member of the shortlink family), the distributed cache, the news feed, and the
payment system. Each follows the framework step by step and ends on the trade-off a strong hire states
unprompted. Read one, then rebuild it from a blank page against a clock rather than rereading it.

## Reference Solutions and Resources

Every prompt below maps either to a worked solution in the
[system-design-primer](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics)
or, where no primer solution exists, to the closest analog plus the one white paper from the
[reading list](../white_paper.md) that grounds the hardest part. Jump to the example first,
then work the prompt yourself; the primer solutions are for calibration, not for copying.

### Storage and Retrieval Systems

- **URL shortener or Pastebin.** [Pastebin solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/pastebin), and the worked [walkthrough](./walkthroughs.md). The two differ in per-record size and whether content needs a separate object store; the walkthrough works the Pastebin variant and notes the distinction.
- **Distributed key-value store.** No primer solution; ground it in the Dynamo paper (consistent hashing, vector clocks, quorum reads and writes for an available store).
- **Distributed cache.** [Query cache solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/query_cache), and the worked [walkthrough](./walkthroughs.md).
- **Distributed unique ID generator.** No primer solution; the standard analog is Snowflake (timestamp plus worker ID plus sequence), with Spanner as the reference for globally ordered IDs at scale.

### Feed, Messaging, and Real-Time Systems

- **News feed.** [Twitter timeline solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter), and the worked [walkthrough](./walkthroughs.md).
- **Chat system.** Closest analog is the [Twitter timeline solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter) for the fan-out and delivery shape; ground ordering and durability in the Kafka paper.
- **Notification system.** Closest analog is the fan-out delivery in the [Twitter timeline solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter), plus distributed-queue concepts for retry and dedupe.
- **Real-time analytics pipeline.** No primer solution; ground it in the MapReduce paper (batch aggregation) and the Kafka paper (ingestion, windowing, late-arriving data).

### Search and Discovery

- **Search autocomplete and typeahead.** No primer solution; the analog is a trie plus a caching tier, so borrow the caching layer from the [query cache solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/query_cache).
- **Web crawler.** [Web crawler solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/web_crawler).
- **Proximity or nearby-friends service.** [Social graph solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/social_graph), extended with geospatial indexing (geohash or quadtree).
- **Ride-hailing service.** Closest analog is the [social graph solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/social_graph) for the proximity piece; add geospatial indexing and a matching queue for the full system.
- **Google Maps or navigation.** No primer solution; the analog is graph routing over tiled storage with a CDN, grounding large-tile storage in the GFS paper and the spatial index in the Bigtable paper.

### Media and Content Platforms

- **Video platform.** No primer solution; use the [scaling AWS solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/scaling_aws) for the iterative-scaling method, plus a CDN and chunked streaming, grounding large-file storage in the GFS paper.
- **Photo-sharing service.** Closest analog is the follower graph and feed in the [Twitter timeline solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter), plus the many-small-files object-storage pattern.
- **Content delivery and geo-replication.** [Scaling AWS solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/scaling_aws) plus CDN concepts, with the Cassandra paper for multi-datacenter replication.

### Coordination and Infrastructure

- **Distributed message queue.** No primer solution; ground it in the Kafka paper (partitioned commit log, offset-based replay).
- **Rate limiter as a service.** Closest analog is the counter tier in the [query cache solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/query_cache); the algorithms (token bucket, leaky bucket) are in the [low-level design guide](../low_level_design/README.md).
- **Distributed lock service.** No primer solution; ground it in the Raft paper (consensus) and the ZooKeeper or Chubby papers (lock and coordination primitives, fencing tokens).
- **Distributed job scheduler.** No primer solution; the analog is a priority queue plus a dependency DAG and a state machine, with ZooKeeper for coordination and Kafka for the task queue.
- **Metrics and observability platform.** No primer solution; ground ingestion in the Kafka paper, time-series storage in the Bigtable paper, and batch rollups in the MapReduce paper.

### Transactional and Consistency-Sensitive Systems

- **Payment or digital wallet.** [Mint solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/mint) for the pipeline shape, the Spanner paper for strong consistency and distributed transactions, and the worked [walkthrough](./walkthroughs.md) for the correctness depth.
- **Ticket or seat reservation.** No primer solution; the analog is inventory with optimistic or pessimistic locking, grounded in the Spanner paper for serializable transactions and Dynamo for the availability trade-off.
- **Collaborative document editor.** No primer solution; the analog is operational transformation or CRDTs, with the Spanner paper for global ordering (CRDT literature sits outside this repo).
- **Ad click aggregation.** Closest analog is the write-heavy pipeline in the [Mint solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/mint), plus the MapReduce paper for batch rollups.

### Social and Graph-Shaped Systems

- **Twitter-style timeline.** [Twitter timeline solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter), and the worked news-feed [walkthrough](./walkthroughs.md) for the fan-out-on-write versus fan-out-on-read comparison.
- **Real-time leaderboard.** [Sales rank solution](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/sales_rank), extended with sorted sets and windowed rankings.
- **Recommendation system.** No primer solution; the analog is offline batch training plus online serving plus a feature store, grounding batch in the MapReduce paper and feature storage in the Bigtable paper.
- **File storage and sync.** No primer solution; ground blob storage in the GFS paper and metadata indexing in the Bigtable paper, with delta-sync change tracking as the piece neither covers.

### Machine-Learning Systems

- **ML platform for a real feature.** No primer solution; the analog is a feature store plus a training pipeline plus model serving plus A/B infrastructure, grounding batch training in the MapReduce paper, feature storage in the Bigtable paper, and consistent experiment assignment in the Spanner paper.