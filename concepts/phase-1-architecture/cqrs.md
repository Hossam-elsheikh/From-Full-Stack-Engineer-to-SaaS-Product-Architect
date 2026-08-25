---
tags: [cqrs, patterns, consistency, event-sourcing]
cards-deck: SaaS Architect::Phase 1::CQRS
---
# CQRS — Command Query Responsibility Segregation

Separates operations that **modify data (commands)** from operations that **retrieve data (queries)**.

## Problem 1: Database Optimization

When one database handles high loads of both reads and writes, **contention** occurs and transactions slow down. CQRS dedicates separate services/databases to reads and to writes, each tailored to its workload.

Your single DB contends under mixed heavy reads and writes and transactions slow down. Which pattern, and how does it help? #card
CQRS — separate read and write paths into dedicated services/databases, each optimized for its workload

## Problem 2: Data Consistency

The read side may lag behind writes. Pairing CQRS with **event sourcing** mitigates this: events are published as changes occur, consumers listen and update their read state → **eventual consistency** at high performance.

After splitting reads and writes, a user's new post isn't visible yet on the read side. What's this, and how is it resolved? #card
Eventual consistency — pair CQRS with event sourcing; consumers listen to events and update their read state

## Aggregating Data Across Services

A ranking service needs both votes and comments. Instead of direct calls, it subscribes to those services' events — reducing load and improving overall performance.

A ranking service needs votes + comments data without hammering those services. How? #card
Subscribe to their events (CQRS/event-driven) instead of making direct service calls

![[concepts/phase-1-architecture/images/CQRS.png]]

## Related

- [[concepts/phase-1-architecture/event-driven-architecture]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
