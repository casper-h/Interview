# Practice Designs

A consolidated list of system design prompts to work through, pulling together what already
existed scattered across the [reading plan](../plan/README.md) and adding the designs identified as
commonly asked but previously missing or reading-only.

Work each one end to end using the structure in the [framework](../framework/README.md), out loud,
against a clock. Log the attempt in the [tracker](../../schedule/tracker.md), including which part of the framework
was weakest, since that is a better use of the log than simply marking a design as done.

## How to pick which ones to prioritize

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
  the [framework](../framework/README.md) (for example, the transactional and consistency-sensitive
  systems for a fintech loop, or the coordination and infrastructure ones for a platform team).

If you are not targeting a specific company yet, do all of Tier 1 for depth, then spread across the
categories below for breadth rather than going deep on any single one.

## Storage and retrieval systems

- URL shortener
- Distributed key-value store
- Distributed cache
- Distributed unique ID generator

## Feed, messaging, and real-time systems

- News feed
- Chat system, for example Slack or WhatsApp
- Notification system
- Real-time analytics pipeline

## Search and discovery

- Search autocomplete and typeahead
- Web crawler
- Proximity or nearby-friends service
- Ride-hailing service, for example Uber or Lyft: driver-rider matching, real-time location, ETA,
  and surge pricing, which is the full system the proximity service is only one piece of
- Google Maps or a navigation service: routing, tiling, and traffic aggregation over a road graph

## Media and content platforms

- Video platform, for example YouTube or Netflix
- Photo-sharing service, for example Instagram: the follower graph, feed, and the many-small-files
  storage and CDN pattern, which differs from the large-file video case
- Content delivery and geo-replication for a global content platform

## Coordination and infrastructure

- Distributed message queue, for example a Kafka-like system
- Rate limiter, as a service rather than as a class (see the [low-level design guide](../../low_level_design/README.md) for the
  class-level version of the same problem)
- Distributed lock service
- Distributed job scheduler, with dependency DAGs, retries, and priority, for example a cron or
  workflow service at scale
- Metrics and observability platform

## Transactional and consistency-sensitive systems

- Payment or digital wallet system
- Ticket or seat reservation system, for example a Ticketmaster-style booking flow
- Collaborative document editor, for example Google Docs, including a discussion of operational
  transformation versus conflict-free replicated data types
- Ad click aggregation and analytics

## Social and graph-shaped systems

- Twitter-style timeline, with a comparison of fan-out on write versus fan-out on read
- Real-time leaderboard, for example for a game: sorted sets, windowed rankings, and how a global
  ranking is partitioned
- Recommendation system, combining a batch-trained model with real-time signal
- File storage and sync, for example Dropbox or Google Drive, with a clear separation between
  metadata and blob storage

## Machine-learning systems

- An ML platform for a real feature, for example a ranking or fraud model: the feature store, offline
  training versus online serving, model deployment and rollback, and the A/B and monitoring
  infrastructure around it. Increasingly its own dedicated round at the senior level and above, and
  a distinct skill from designing the recommendation system's data flow.

## Notes on using this list well

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