---
tags: [distributed-systems, cap, consistency, availability, partitioning]
cards-deck: SaaS Architect::Phase 2::CAP Theorem
---
# CAP Theorem

In the event of a **network partition**, a distributed database cannot guarantee both **Consistency** and **Availability** at the same time — it must prioritize one.

## The Three Properties

- **Consistency** — every read returns the latest write, or an error; all clients see the same value
- **Availability** — every request gets a non-error response, whether or not it's the latest value
- **Partition Tolerance** — the system keeps operating despite network issues

Name the 3 CAP properties. #card
Consistency, Availability, Partition tolerance

## Why the Trade-off Exists

Example: a NoSQL key-value store with replicas. Normally all replicas stay consistent. During a partition, one service updates a counter on one replica while another replica is isolated. A read can either:
- Return an **outdated value** → favors **Availability** (AP)
- Return an **error** → favors **Consistency** (CP)

Two replicas can't talk and a service writes to one side. A read returns a stale value. Which trade-off is being made? #card
Availability over consistency (AP) — a stale value instead of an error

A client demands every read be the latest write or an error, even when replicas are partitioned. Which property is prioritized? #card
Consistency (CP) — availability is sacrificed during partitions

## What the Choices Look Like

- **CA** — consistent + available but not partition-tolerant (a centralized database; limits scalability)
- **CP** — consistent + partition-tolerant, sacrifice availability
- **AP** — available + partition-tolerant, sacrifice consistency

Why can't a distributed DB offer CA in practice? #card
Network partitions are unavoidable — you must tolerate them and choose between C and A during a partition

## When to Prioritize What

Application needs decide the trade-off: **inventory systems** lean consistency, **social media** leans availability.

![[concepts/phase-2-data/diagrams/cap-theorem.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
