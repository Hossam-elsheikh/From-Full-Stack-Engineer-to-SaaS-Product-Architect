---
tags: [microservices, monolith, architecture]
cards-deck: SaaS Architect::Phase 1::Microservices
---
# Microservices Architecture

A system of small, independently deployable services, each owning its own business capability and database.

## Why Not Monolith

Monoliths suffer from:
- Difficult troubleshooting
- Feature additions that ripple across the codebase
- Team management issues and code merge conflicts
- One broken component takes everything down

## Microservices Benefits

- **Loosely coupled services** — small teams manage each service independently
- **Easier development & troubleshooting** — smaller codebases
- **Performance & scalability** — each service can scale horizontally by adding instances
- **Fault isolation** — an issue in one service is contained, enhancing security

Your team of 30 is stuck: merge conflicts, slow deploys, one failing service takes the whole app down. What architectural shift, and which 2 problems does it fix? #card
Microservices — independent teams/deployments + fault isolation

An attacker compromises one microservice. Why doesn't the whole app fall? #card
Fault isolation — issues are contained within the single compromised service

## Cautions

- **Don't rush it** — without best practices you create a 'Big Ball of Mud'
- Apply the **Single Responsibility Principle** per service
- Each service should own a **separate database** to avoid coupling

Two microservices share one database and every schema change breaks the other. What best practice was violated? #card
Each service should own its separate database to avoid coupling

A junior engineer proposes splitting a 2-service app into 20 microservices on day one. What's the counter-argument? #card
Microservices add complexity — start monolithic and split when complexity warrants it; rushing creates a Big Ball of Mud

![[concepts/phase-1-architecture/diagrams/microservices-architecture.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
