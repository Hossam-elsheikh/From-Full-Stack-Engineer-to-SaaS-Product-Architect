---
tags: [architecture, quality-attributes, performance, scalability, availability]
cards-deck: SaaS Architect::Phase 1::Quality Attributes
---
# Quality Attributes (Non-functional Requirements)

Systems are redesigned not because of functional requirements, but because the system:
- isn't fast enough
- doesn't scale
- is slow to develop
- is hard to maintain
- isn't secure enough

> No single software architecture can provide all quality attributes. Certain QAs contradict each other — you must make the right trade-off.

## Performance

- **Response time** = processing time + waiting time (latency)
- **Throughput** = amount of tasks / data per second (bits, bytes, MB/s)
- Measure using **percentile distributions and tail latency** (P99, P95), NOT simple averages

Your API reports avg response time = 200ms but P99 = 2s. Why is the average misleading? #card
Averages hide tail latency — use percentile distributions (P99, P95) to see true performance under load

## Scalability

1. **Vertical (Scaling Up)** — upgrade existing machine (CPU, RAM). Easy but finite ceiling, low fault tolerance
2. **Horizontal (Scaling Out)** — add more machines. Near-unlimited scale but adds complexity, may require code changes
3. **Team Scalability** — productivity vs team size. Modularize codebase or adopt microservices to counter coordination overhead

Your monolith is struggling under load. What's the quick cheap fix vs the scalable long-term fix? #card
Vertical = bigger machine (cheap but finite ceiling); Horizontal = more machines (complex but near-unlimited)

## Availability

$Availability\% = \frac{Uptime}{Uptime + Downtime}$ or $\frac{MTBF}{MTBF + MTTR}$

- **MTBF** = Mean Time Between Failures
- **MTTR** = Mean Time To Recovery

A client demands 99.99% availability. What's the max yearly downtime? #card
~52.6 minutes (4 nines)

Your system has MTBF = 720h and MTTR = 4h. Calculate availability. #card
99.45% (720 / 724)

### Fault Tolerance Tactics

- **Failure prevention** — running on multiple servers (active-active, active-passive)
- **Time redundancy** — retry until succeed or give up
- **Failure detection** — monitoring/health checks
- **Recovery** — automated failover

Your payment service is running on a single server and it crashes. What fault tolerance tactic was missing? #card
Failure prevention — run on multiple servers with active-passive or active-active

## SLA / SLO / SLI

- **SLA** — Service Level Agreement (contract with penalties)
- **SLO** — Service Level Objective (internal target)
- **SLI** — Service Level Indicator (measured value)

The ops team argues whether they met the contract. Which term is the contract, the target, and the measurement? #card
SLA = contract, SLO = target, SLI = measurement

![[concepts/phase 1 - architecture & system design/diagrams/quality-attributes-tradeoffs.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
