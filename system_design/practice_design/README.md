# Practice Designs

A consolidated list of system design prompts to work through, pulling together what already
existed scattered across `system_design/plan/months/` and adding the designs identified as
commonly asked but previously missing or reading-only.

Work each one end to end using the structure in `system_design/framework/README.md`, out loud,
against a clock. Log the attempt in `schedule/tracker.md`, including which part of the framework
was weakest, since that is a better use of the log than simply marking a design as done.

## How to pick which ones to prioritize

If you are not targeting a specific company yet, prioritize breadth across the categories below
rather than depth on any one. If you are targeting a specific team, weight toward the category
that matches it, using the guidance in the "Adapting depth by company or team type" section of
`system_design/framework/README.md`.

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

## Media and content platforms

- Video platform, for example YouTube or Netflix
- Content delivery and geo-replication for a global content platform

## Coordination and infrastructure

- Distributed message queue, for example a Kafka-like system
- Rate limiter, as a service rather than as a class (see `low_level_design/README.md` for the
  class-level version of the same problem)
- Distributed lock service
- Metrics and observability platform

## Transactional and consistency-sensitive systems

- Payment or digital wallet system
- Ticket or seat reservation system, for example a Ticketmaster-style booking flow
- Collaborative document editor, for example Google Docs, including a discussion of operational
  transformation versus conflict-free replicated data types
- Ad click aggregation and analytics

## Social and graph-shaped systems

- Twitter-style timeline, with a comparison of fan-out on write versus fan-out on read
- Recommendation system, combining a batch-trained model with real-time signal
- File storage and sync, for example Dropbox or Google Drive, with a clear separation between
  metadata and blob storage

## Notes on using this list well

- Do not treat completing this list as the goal in itself. The goal is fluency with the framework
  and the underlying trade-offs; the list exists to give you varied enough contexts to build that
  fluency, not as a set of memorized designs to reproduce.
- Several of these overlap deliberately, for example the news feed and the Twitter-style timeline,
  or the distributed cache and the rate limiter. That overlap is intentional: solving a familiar
  trade-off in a new context is a good test of whether you actually understand it or only
  memorized the first version.
- Revisit two or three of the earliest designs you attempted later in your preparation, once
  you have covered more of `system_design/plan/`, and compare your answer to your first attempt.
  The gap between the two is a useful, concrete measure of progress.