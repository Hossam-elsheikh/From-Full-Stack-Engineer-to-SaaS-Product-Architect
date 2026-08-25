---
tags: [patterns, decision-aids, index]
---
# Decision Aids

One-page decision diagrams and cheat sheets — a flowchart or a comparison table with a "choose this when…" row, built for every major trade-off you study. By the end of the plan there should be 15–20 of them.

**This collection is your value as an architect.** It is what you open in a real design meeting, and it is the reason the reading was worth doing.

## Planned

- Choosing a multi-tenancy data model — isolation needs, compliance, tenant count → shared schema / schema-per-tenant / DB-per-tenant
- The database scaling ladder — and the number that justifies each next rung
- Communication patterns: sync vs async, queues, pub/sub, event sourcing, CQRS
- Resilience pattern decision flow: timeouts, retries, circuit breaker, bulkhead
- Deployment strategy comparison: blue-green, canary, rolling
- "System is slow" diagnosis tree — CPU-bound? IO? lock contention? N+1?
- Testing strategy: what to unit vs integration vs end-to-end test, and the multi-tenant isolation tests

## Related concept notes

- [[concepts/phase-6-scale/load-balancers]]
- [[concepts/phase-1-architecture/message-brokers]]
- [[concepts/phase-1-architecture/api-gateway]]
- [[concepts/phase-1-architecture/event-driven-architecture]]
- [[concepts/phase-1-architecture/lambda-and-kappa-architecture]]
- [[concepts/phase-1-architecture/cqrs]]
- [[concepts/phase-1-architecture/microservices]]
