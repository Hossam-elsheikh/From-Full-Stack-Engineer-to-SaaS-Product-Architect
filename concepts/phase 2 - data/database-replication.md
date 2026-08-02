---
tags: [databases, replication, availability, fault-tolerance]
cards-deck: SaaS Architect::Phase 2::Database Replication
---
# Database Replication

Creates multiple database instances across different servers.

## Benefits

- **High availability & fault tolerance** — removes the single point of failure
- **Better load distribution** — reads spread across replicas
- **Improved performance**

A single DB instance goes down and your app is down with it. What technique, and which 2 benefits? #card
Database Replication — availability + fault tolerance by removing the single point of failure

## Costs

- **Concurrency complexity** — managing concurrent updates across instances
- **Data consistency** — ensuring every replica converges on the same state

You replicated your DB across 3 servers and reads are faster, but writers must coordinate. What's the new complexity? #card
Managing concurrent updates and ensuring data consistency across replicas

![[concepts/phase 2 - data/diagrams/database-replication.excalidraw]]

## Related

- [[concepts/phase 2 - data/database-indexing]]
- [[concepts/phase 2 - data/database-sharding]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
