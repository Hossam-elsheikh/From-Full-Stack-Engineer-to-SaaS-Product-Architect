---
tags: [databases, indexing, performance]
cards-deck: SaaS Architect::Phase 2::Database Indexing
---
# Database Indexing

Accelerates data retrieval with **helper structures** that map column values to records — enabling faster searches and sorting, especially on large datasets.

## Types

- **Single-column index** — one column
- **Composite index** — multiple columns (e.g., `user_id` + `created_at`)

A query filtering by `user_id` + `created_at` is slow at 10M rows. What two index options do you have? #card
A single-column index or a composite index over (user_id, created_at)

## Trade-offs

- More **storage space** consumed
- **Slower writes** — every write must also update the index

You added an index and writes got slower. Why? #card
Every write must also update the index — storage and write cost are the trade-off

A column is queried constantly for sorting. What do indexes enable besides faster lookups? #card
Faster searching and sorting on large datasets

## Related

- [[concepts/phase-2-data/database-replication]]
- [[concepts/phase-2-data/database-sharding]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
