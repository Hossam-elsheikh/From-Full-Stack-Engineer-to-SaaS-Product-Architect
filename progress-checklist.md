# Progress Checklist — From Full-Stack Engineer to SaaS Product Architect

Tracks progress against [saas-architect-study-plan.md](./saas-architect-study-plan.md) (Rev B).
**~230 hours over ~8 months at 6–8 hrs/week.** Review through [the Atlas](https://claude.ai/code/artifact/f3e583da-ec48-4778-8d52-e1c0a4764fcd), not by opening notes.

Every phase ends in a **written artifact** — that is the only feedback loop a solo plan has. They live in `deliverables/`.

---

## Phase 0 — Orientation (1 week, ~4 hrs)
- [x] Internalize the product lifecycle: idea → design → build → deploy → operate → scale → maintain
- [ ] Internalize trade-off thinking (every decision buys something, costs something)
- [ ] 📄 **[REQUIRED]** *Fundamentals of Software Architecture* — table of contents + chapters 1–4
- [ ] ✍️ **Artifact:** one page of "things I don't know I don't know", revisited at the end of the plan
- [x] ~~*The Pragmatic Programmer*~~ — **[SKIP]**, you're past it

## Phase 1 — Architecture & Design (6 weeks, ~45 hrs)
- [ ] Architectural styles: layered, hexagonal/clean, modular monolith, microservices, event-driven, serverless — and when *not* to use microservices (usually: at the start)
- [ ] Quality attributes: availability, latency, throughput, consistency, maintainability
- [ ] API design: REST maturity, versioning, idempotency, pagination, webhooks
- [ ] **API contracts for clients you can't force-update** — tolerant readers, feature negotiation, what "deprecate" means when 8% of users are on v1
- [ ] Communication patterns: sync vs async, queues, pub/sub, event sourcing, CQRS
- [ ] Strategic DDD: bounded contexts, ubiquitous language, aggregates
- [ ] Communicating architecture: C4 model, ADRs
- [ ] 📚 **[REQUIRED]** *Fundamentals of Software Architecture* — Richards & Ford (~20 hrs)
- [ ] **[PICK ONE]** 🎥 Pogrebinsky's Udemy course **or** 📚 *System Design Interview Vol. 1* — Alex Xu
- [ ] **[PICK ONE]** 📚 *Learning Domain-Driven Design* (Khononov) **or** *DDD Distilled* (Vernon) — strategic half only
- [ ] ✍️ **Artifact:** C4 diagrams (context + container + one component) and 5 ADRs for your real system
- [ ] ~~*Clean Architecture*~~, ~~Pogrebinsky's cloud-patterns course~~ — **[SKIP]**

## Phase 2 — Data (6 weeks, ~48 hrs)
- [ ] Relational modelling: normalization, indexing strategy, transactions, isolation levels, locking
- [ ] **Multi-tenancy data strategies:** shared schema + tenant_id vs schema-per-tenant vs database-per-tenant
- [ ] Migrations at scale: zero-downtime schema changes, backfills, expand/contract
- [ ] Caching: layers, invalidation, cache-aside vs write-through
- [ ] When SQL isn't enough: search, OLAP vs OLTP, read replicas, queues
- [ ] Audit trails, soft deletes, retention policy as a schema concern
- [ ] 📚 **[REQUIRED]** *Designing Data-Intensive Applications* — Kleppmann, **ch 1–9** (~35 hrs)
- [ ] 📄 **[REQUIRED]** Tod Golding's AWS SaaS Factory talks on multi-tenant data partitioning (~3 hrs, free)
- [ ] 🎥 **[ONLY IF]** Grider's SQL/Postgres course — only if you can't read an `EXPLAIN ANALYZE` plan
- [ ] ✍️ **Artifact:** multi-tenancy decision doc — which model, why, cost at 10 / 1,000 / 10,000 tenants, what forces a migration

## Phase 3 — SaaS Mechanics (5 weeks, ~38 hrs)
- [ ] Multi-tenancy end-to-end: tenant identity, onboarding/provisioning, tenant-aware routing, per-tenant config, pooled vs siloed tiering
- [ ] Identity & access: OAuth2/OIDC, SAML SSO, RBAC → ABAC, session vs token auth
- [ ] Billing & subscriptions: metering, plans, proration, dunning, trials
- [ ] **Pricing ↔ architecture coupling** — pricing decisions are schema decisions made 18 months early
- [ ] **Cost architecture** — cost per tenant, cost per active user, what your worst tenant costs you
- [ ] **Third-party integration architecture** — provider abstraction, webhook ingestion (idempotency, replay, ordering), graceful degradation
- [ ] Feature flags, gradual rollouts, activation metrics (MRR, churn, NRR)
- [ ] 📚 **[REQUIRED]** *Building Multi-Tenant SaaS Architectures* — Tod Golding (~20 hrs)
- [ ] 🎥 **[REQUIRED]** One OAuth 2.0 / OIDC course (~8 hrs)
- [ ] 📄 **[REQUIRED]** stripe.com/docs/billing (~4 hrs, free)
- [ ] ✍️ **Artifact:** pricing/packaging sheet with schema + metering implications per tier, plus a cost-per-tenant estimate
- [ ] ~~A "Build a SaaS in <stack>" course~~ — skip entirely if you're already building a real product

## Phase 4 — Delivery & Cloud (6 weeks, ~45 hrs)
- [ ] Containers: images, layers, compose, registries, multi-stage builds
- [ ] CI/CD: pipelines, environments, blue-green and canary, rollbacks, trunk-based development
- [ ] Infrastructure as Code: declarative infra, state, modules — the *mindset* more than the syntax
- [ ] One cloud, shallowly but correctly: networking, compute, managed DBs, object storage, load balancers, IAM
- [ ] Secrets management, artifact versioning, environment parity
- [ ] Kubernetes — **vocabulary only**: pods, deployments, services, ingress, autoscaling. Enough to read a doc.
- [ ] 🎥 **[REQUIRED]** *Docker & Kubernetes: The Practical Guide* — **Docker sections only**
- [ ] 🎥 **[REQUIRED]** One CI/CD course, GitHub Actions or GitLab CI (~6 hrs)
- [ ] 🎥 **[REQUIRED]** One Terraform course — stop when you can write a module and explain state (~8 hrs)
- [ ] **[PICK ONE]** 📄 A targeted six-service docs path — VPC, ECS/App Runner, RDS, S3, ALB, IAM (~10 hrs, **the better default**) **or** 🎥 Maarek's AWS SA-Associate cert (~30 hrs, only for the credential)
- [ ] **[PICK ONE]** 📚 *Accelerate* (**recommended**) **or** *The Phoenix Project*
- [ ] ✍️ **Artifact:** product deployed via IaC, CI/CD pipeline doing a zero-downtime deploy and a rollback you have actually tested

## Phase 5 — Operate & Maintain (5 weeks, ~38 hrs)
- [ ] Observability: logs vs metrics vs traces, structured logging, dashboards, SLIs/SLOs, alerting that doesn't cry wolf
- [ ] Incident response: on-call basics, runbooks, blameless postmortems
- [ ] Resilience patterns: timeouts, retries with backoff, circuit breakers, bulkheads, graceful degradation, backpressure
- [ ] Backups & DR: RPO/RTO, restore drills — a backup you've never restored doesn't exist
- [ ] **Testing strategy** *(the plan's largest gap)* — unit vs integration vs e2e ratios, testing multi-tenant isolation specifically, seeding realistic tenant data, contract testing, environments that don't rot
- [ ] Long-term maintenance: dependency updates, tech-debt budgeting, deprecation strategy
- [ ] 📚 **[REQUIRED]** *Release It!* (2nd ed.) — Nygard (~18 hrs)
- [ ] 📄 **[REQUIRED]** Google SRE Book, **Parts I–II selectively** — SLOs, alerting, postmortems (~8 hrs, free)
- [ ] 🎥 **[ONLY IF]** Grafana/Prometheus — only *when* you're actually standing up observability
- [ ] ✍️ **Artifact:** SLOs for your top three user journeys, one runbook, and a postmortem for a failure you deliberately caused
- [ ] ~~*Working Effectively with Legacy Code*~~ — **[SKIP for now]**, a year-3 book

## Phase 6 — Scale (4 weeks, ~30 hrs) · **buy nothing**
- [ ] Horizontal vs vertical scaling; stateless services; sticky sessions and why to avoid them
- [ ] Load balancing, CDN, rate limiting (per-tenant especially)
- [ ] The database scaling ladder: indexes → read replicas → partitioning → sharding, **in that order**
- [ ] Async everything: job queues, the outbox pattern, eventual consistency and how to explain it to users
- [ ] **Offline and sync** — local-first reads, queued writes, conflict resolution, why "last write wins" loses someone's data
- [ ] Capacity planning and load testing
- [ ] CAP/PACELC intuition in plain terms
- [ ] 📚 **[REQUIRED]** Re-read DDIA chapters 5–9 (~10 hrs — the highest-return re-read in the plan)
- [ ] 📄 **[REQUIRED]** Engineering blogs — Stripe, Shopify, Figma, Discord (~6 hrs, ongoing)
- [ ] ✍️ **Artifact:** a load test of your own system, where it broke first, and the scaling decision you'd make *next*

## Phase 7 — Security & Compliance (3 weeks, ~22 hrs)
- [ ] OWASP Top 10, secure SDLC basics, dependency scanning
- [ ] **Tenant isolation as a security boundary** — a missing `WHERE tenant_id` is a data breach
- [ ] Encryption at rest and in transit, key management
- [ ] Compliance literacy: GDPR, SOC 2, data residency, plus sector rules for your domain
- [ ] Audit logging
- [ ] 📄 **[REQUIRED]** OWASP Cheat Sheet Series (~8 hrs, free)
- [ ] 📄 **[REQUIRED]** Vanta or Drata blog on SOC 2 in plain English (~3 hrs)
- [ ] ✍️ **Artifact:** tenant-isolation threat model — every path where data crosses a tenant boundary, and the test that proves it doesn't

---

## The Capstone — starts **week 3**, runs throughout

If you already have a real product in flight, use it. A live multi-tenant system beats a throwaway invoicing app.

| Week | From phase | Do | ✓ |
|---|---|---|:-:|
| 3–8 | 1 | C4 diagrams + ADRs written *before* code | [ ] |
| 9–14 | 2 | Multi-tenancy model chosen and documented; one zero-downtime migration | [ ] |
| 15–19 | 3 | RBAC, SSO-ready auth, subscription billing with metering | [ ] |
| 20–25 | 4 | Dockerized, IaC-provisioned, CI/CD with tested rollback | [ ] |
| 26–30 | 5 | Dashboards, SLOs, alerts, runbooks; testing strategy in place | [ ] |
| 31–34 | 6 | Load-test it, break it, write the postmortem | [ ] |
| 35–36 | 7 | Threat model, tenant-isolation test suite | [ ] |

**Then the year-two simulation:**
- [ ] Add a module without touching the others
- [ ] Run a zero-downtime migration on a table with real data
- [ ] Deprecate an API version while old mobile clients are still calling it

---

## Buy these four. They are the plan.
- [ ] *Designing Data-Intensive Applications* — Kleppmann (ch 1–9)
- [ ] *Building Multi-Tenant SaaS Architectures* — Golding
- [ ] *Release It!* — Nygard
- [ ] *Fundamentals of Software Architecture* — Richards & Ford
