---
tags: [databases, sharding, partitioning, scalability]
cards-deck: SaaS Architect::Phase 2::Database Sharding
---
# Database Partitioning (Sharding)

Splits data across multiple database instances.

## Benefits

- More **storage capacity** across instances
- **Parallel query processing** — queries run concurrently across shards

Why does sharding improve performance beyond just adding capacity? #card
Queries can run in parallel across shards

## Relational vs Non-relational

Straightforward in **non-relational** databases. Complex in **relational** databases because:
- Multi-record queries (joins) must span shards
- ACID properties are hard to maintain across shards

Your relational DB is out of storage. You split users by ID range across 4 instances. What technique, and what's harder in relational than NoSQL? #card
Sharding/Partitioning — multi-record queries (joins) and ACID transactions across shards

![[concepts/phase-2-data/diagrams/database-sharding.excalidraw]]

## Related

- [[concepts/phase-2-data/database-indexing]]
- [[concepts/phase-2-data/database-replication]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
