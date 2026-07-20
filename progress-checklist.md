# Progress Checklist — From Full-Stack Engineer to SaaS Product Architect

Tracks progress against [saas-architect-study-plan.md](./saas-architect-study-plan.md).

---

## Phase 0 — The Map (2 weeks)
- [ ] Internalize product lifecycle: idea → design → build → deploy → operate → scale → maintain
- [ ] Internalize trade-off thinking (every decision buys something, costs something)
- [ ] 📚 Skim *The Pragmatic Programmer* (Hunt & Thomas)
- [ ] 🎥 Udemy: *Software Architecture & Design of Modern Large Scale Systems* (Pogrebinsky)

## Phase 1 — Software Architecture & System Design (6–8 weeks)
- [ ] Architectural styles: layered, hexagonal/clean, modular monolith, microservices, event-driven, serverless
- [ ] Know when NOT to use microservices
- [ ] Quality attributes: availability, latency, throughput, consistency, maintainability
- [ ] API design: REST maturity, versioning, idempotency, pagination, webhooks
- [ ] Know when gRPC/GraphQL fit
- [ ] Communication patterns: sync vs async, queues, pub/sub, event sourcing, CQRS
- [ ] Domain modeling: bounded contexts, ubiquitous language, aggregates (strategic DDD)
- [ ] C4 model for drawing architecture
- [ ] ADRs (Architecture Decision Records)
- [ ] 🎥 Udemy: *The Complete Cloud Computing Software Architecture Patterns* (Pogrebinsky)
- [ ] 🎥 Udemy: *Microservices Architecture — The Complete Guide* (Memi Lavi)
- [ ] 📚 *Clean Architecture* — Robert C. Martin
- [ ] 📚 *Fundamentals of Software Architecture* — Richards & Ford
- [ ] 📚 *Learning Domain-Driven Design* — Vlad Khononov (strategic-design half)
- [ ] 📚 *System Design Interview Vol. 1 & 2* — Alex Xu
- [ ] **Practice:** Design a multi-tenant invoicing SaaS on paper (C4 diagrams + ADRs, no code)

## Phase 2 — Data: The Heart of Every SaaS (5–6 weeks)
- [ ] Relational modeling: normalization, indexing strategy, transactions, isolation levels, locking
- [ ] Multi-tenancy data strategies: shared schema+tenant_id vs schema-per-tenant vs database-per-tenant
- [ ] Migrations at scale: zero-downtime schema changes, backfills
- [ ] Caching: layers, invalidation, cache-aside vs write-through
- [ ] When SQL isn't enough: search (Elasticsearch), OLAP vs OLTP, read replicas, warehouses, queues
- [ ] Audit trails & soft deletes
- [ ] 📚 *Designing Data-Intensive Applications* — Martin Kleppmann
- [ ] 🎥 Udemy: *SQL and PostgreSQL: The Complete Developer's Guide* (Stephen Grider) — if SQL fundamentals need reinforcement
- [ ] 📄 Tod Golding's AWS SaaS Factory talks on multi-tenant data partitioning

## Phase 3 — SaaS-Specific Architecture (4–5 weeks)
- [ ] Multi-tenancy end-to-end: tenant identity, onboarding/provisioning, tenant-aware routing, per-tenant config/feature flags, tiering
- [ ] Identity & access: OAuth2/OIDC, SSO (SAML), RBAC → ABAC, session vs token auth
- [ ] Billing & subscriptions: metering, plans, proration, dunning, trials
- [ ] Feature flags, gradual rollouts, A/B foundations
- [ ] Product analytics & activation metrics (MRR, churn, NRR)
- [ ] 📚 *Building Multi-Tenant SaaS Architectures* — Tod Golding (O'Reilly)
- [ ] 🎥 Udemy: a "Build a SaaS" course in your stack (practical lab)
- [ ] 🎥 Udemy: *OAuth 2.0 and OpenID Connect* course
- [ ] 📄 stripe.com/guides + SaaStr blog

## Phase 4 — DevOps, Cloud & Delivery (8–10 weeks)
- [ ] Containers: Docker images, compose, registries
- [ ] Orchestration: Kubernetes fundamentals (deployments, services, ingress, config/secrets, autoscaling)
- [ ] CI/CD: pipelines, environments, blue-green & canary deploys, rollbacks, trunk-based development
- [ ] Infrastructure as Code: Terraform mindset (declarative infra, state, modules)
- [ ] One cloud deeply — AWS: VPC/networking, compute, managed DBs, object storage, load balancers, IAM
- [ ] Secrets management, artifact versioning, environment parity
- [ ] 🎥 Udemy: *Docker & Kubernetes: The Practical Guide* (Maximilian Schwarzmüller)
- [ ] 🎥 Udemy: *Ultimate AWS Certified Solutions Architect Associate* (Stéphane Maarek)
- [ ] 🎥 Udemy: *Terraform* course (Maarek or Zeal Vora)
- [ ] 🎥 Udemy: GitLab CI / GitHub Actions pipeline course
- [ ] 📚 *The Phoenix Project*
- [ ] 📚 *Accelerate*

## Phase 5 — Operating & Maintaining in Production (4–5 weeks)
- [ ] Observability: logs vs metrics vs traces, structured logging, dashboards, SLIs/SLOs, alerting
- [ ] Incident response: on-call basics, runbooks, blameless postmortems
- [ ] Resilience patterns: timeouts, retries with backoff, circuit breakers, bulkheads, graceful degradation, backpressure
- [ ] Backups & disaster recovery: RPO/RTO, restore drills
- [ ] Long-term maintenance: dependency updates, tech-debt budgeting, deprecation strategy, safe legacy refactoring
- [ ] 📚 *Release It!* (2nd ed.) — Michael Nygard
- [ ] 📄 Google SRE Book (Parts I–II)
- [ ] 🎥 Udemy: Observability with Grafana/Prometheus course
- [ ] 📚 *Working Effectively with Legacy Code* — Michael Feathers

## Phase 6 — Scalability & Reliability (4–5 weeks)
- [ ] Horizontal vs vertical scaling; stateless services; avoid sticky sessions
- [ ] Load balancing, CDN, rate limiting
- [ ] Database scaling ladder: indexes → read replicas → partitioning → sharding
- [ ] Async everything: job queues, outbox pattern, eventual consistency
- [ ] Capacity planning & load testing
- [ ] CAP/PACELC intuition
- [ ] Re-read DDIA chapters 5–9
- [ ] 🎥 Revisit Pogrebinsky's system design courses (scaling sections)
- [ ] 📄 Engineering blogs: Shopify, Stripe, Figma scaling stories

## Phase 7 — Security & Compliance (3 weeks)
- [ ] OWASP Top 10, secure SDLC basics, dependency scanning
- [ ] Tenant isolation as a security boundary
- [ ] Encryption at rest/in transit, key management
- [ ] Compliance literacy: GDPR, SOC 2, data residency
- [ ] Audit logging
- [ ] 🎥 Udemy: Web Security & OWASP Top 10 course
- [ ] 📄 OWASP Cheat Sheet Series; Vanta/Drata SOC 2 blogs

## The Capstone (months 6–9, parallel with later phases)
- [ ] Modular monolith organized by business capability, C4 diagrams + ADRs written first
- [ ] Shared-schema multi-tenancy, RBAC, SSO-ready auth
- [ ] Subscription billing with metering
- [ ] Dockerized, IaC-provisioned, CI/CD with zero-downtime deploys
- [ ] Full observability: dashboards, SLOs, alerts, runbooks
- [ ] Load-test it, break it, write a postmortem
- [ ] Simulate "year 2": add a module, zero-downtime migration, deprecate an API version

## Priority reading list (if you only read 5 books)
- [ ] *Designing Data-Intensive Applications* — Kleppmann
- [ ] *Building Multi-Tenant SaaS Architectures* — Golding
- [ ] *Release It!* — Nygard
- [ ] *Fundamentals of Software Architecture* — Richards & Ford
- [ ] *Learning Domain-Driven Design* — Khononov (strategic half)
