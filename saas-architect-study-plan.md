# From Full-Stack Engineer to SaaS Product Architect
### Revised plan — ~8 months at 6–8 hrs/week (~230 hours total)

**Philosophy:** You already know how to code. This plan teaches you how to *design, ship, operate, and scale* a SaaS product.

**Resource rule (changed):** **Books for judgment, video for tools.** Architecture, data modelling, multi-tenancy and resilience are trade-off skills — they live in long-form writing. Docker, Terraform, AWS and CI/CD are muscle memory — they live in video. Ignore any instinct to "start with a course" in the first three phases.

**Every resource below is tagged:**
- **[REQUIRED]** — do it, no substitute exists
- **[PICK ONE]** — two options teach the same thing; doing both is waste
- **[ONLY IF]** — conditional on a gap you actually have
- **[SKIP]** — in the original plan, cut and why

**Budget discipline:** 230 hours is the whole budget. The four required books are ~110 hours. That leaves ~120 for video, practice and the capstone. Every "nice to have" you add comes out of capstone time, which is where the learning actually compounds.

---

## Ground rules

**Read to a decision, not to completion.** For each chapter ask: *what would I now do differently in my product?* If the answer is nothing, skim faster.

**Every phase ends in a written artifact.** This is the only feedback loop in a solo study plan. Artifacts listed per phase.

**The capstone starts in week 3, not month 6.** See the capstone section.

---

## Phase 0 — Orientation (1 week, was 2)

Just enough vocabulary to know what you're missing.

**Internalize:** the product lifecycle (idea → design → build → deploy → operate → scale → maintain), and that every architecture decision buys something and costs something.

**Resources:**
- 📄 **[REQUIRED]** Read the *Fundamentals of Software Architecture* table of contents and chapters 1–4. That's your map. ~4 hours.
- 📚 **[SKIP]** *The Pragmatic Programmer* — you're past it. It's a mindset book for people who don't yet have the mindset.

**Artifact:** a one-page list of "things I don't know I don't know," revisited at the end.

---

## Phase 1 — Architecture & Design (6 weeks, ~45 hrs)

The core skill: turning requirements into a structure.

**Must-know concepts:**
- Architectural styles: layered, hexagonal/clean, modular monolith, microservices, event-driven, serverless — and when *not* to use microservices (usually: at the start)
- Quality attributes: availability, latency, throughput, consistency, maintainability — and how requirements drive architecture
- API design: REST maturity, versioning, idempotency, pagination, webhooks
- **API contracts for clients you can't force-update** *(added)* — mobile apps live in the wild for months on old versions. Versioning strategy, tolerant readers, feature negotiation, and what "deprecate" means when 8% of users are on v1
- Communication patterns: sync vs async, queues, pub/sub, event sourcing, CQRS — know what each solves before adopting it
- Strategic DDD: bounded contexts, ubiquitous language, aggregates — enough to keep a growing codebase organized by business capability
- Communicating architecture: C4 model, ADRs

**Resources:**
- 📚 **[REQUIRED]** *Fundamentals of Software Architecture* — Richards & Ford. The single best trade-off-thinking book. ~20 hrs.
- **[PICK ONE]** for systems breadth — these cover the same ground in different formats:
  - 🎥 Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Pogrebinsky (better if you learn by watching)
  - 📚 *System Design Interview Vol. 1* — Alex Xu (better if you learn by reading; skip Vol. 2 unless interviewing)
- **[PICK ONE]** for DDD — read the strategic half only, the tactical patterns can wait:
  - 📚 *Learning Domain-Driven Design* — Khononov (more thorough)
  - 📚 *Domain-Driven Design Distilled* — Vernon (~1/3 the length, 80% of the strategic value)
- 📚 **[SKIP]** *Clean Architecture* — Martin. Largely subsumed by Richards & Ford, and more dogmatic about dependency direction than the trade-off framing you want.
- 📚 **[SKIP]** Pogrebinsky's *Cloud Computing Software Architecture Patterns* if you took his first course — heavy overlap.

**Artifact:** C4 diagrams (context + container + one component) and 5 ADRs for a real system. Use your actual product, not a hypothetical.

---

## Phase 2 — Data (6 weeks, ~48 hrs)

**Must-know concepts:**
- Relational modelling seriously: normalization, indexing strategy, transactions, isolation levels, locking
- **Multi-tenancy data strategies:** shared schema + tenant_id vs schema-per-tenant vs database-per-tenant — cost, isolation, noisy neighbours, compliance
- Migrations at scale: zero-downtime schema changes, backfills, expand/contract
- Caching: layers, invalidation, cache-aside vs write-through
- When SQL isn't enough: search, OLAP vs OLTP, read replicas, queues
- Audit trails, soft deletes, retention policy as a schema concern

**Resources:**
- 📚 **[REQUIRED]** *Designing Data-Intensive Applications* — Kleppmann, **chapters 1–9**. The most important book in this plan. ~35 hrs at reading-slowly pace. Chapters 10–12 (batch, stream, Lambda/Kappa) are excellent but not load-bearing for a transactional SaaS — read them when you have a genuine analytics or event-pipeline requirement, not before.
- 📄 **[REQUIRED]** Tod Golding's AWS SaaS Factory talks on multi-tenant data partitioning (free, YouTube). ~3 hrs, and there is no better source on this specific decision.
- 🎥 **[ONLY IF]** *SQL and PostgreSQL: The Complete Developer's Guide* — Grider. Take this **only if** you can't currently read an `EXPLAIN ANALYZE` plan and reason about index choice. If you can, skip it entirely and save 20 hours.

**Artifact:** a written multi-tenancy decision doc — which partitioning model, why, what it costs you at 10 / 1,000 / 10,000 tenants, and what would force a migration.

---

## Phase 3 — SaaS Mechanics (5 weeks, ~38 hrs)

The product machinery that makes it "a SaaS."

**Must-know concepts:**
- Multi-tenancy end-to-end: tenant identity, onboarding/provisioning, tenant-aware routing, per-tenant config and feature flags, pooled vs siloed tiering
- Identity & access: OAuth2/OIDC, SAML SSO for enterprise deals, RBAC → ABAC, session vs token auth
- Billing & subscriptions: metering, plans, proration, dunning, trials
- **Pricing ↔ architecture coupling** *(added)* — you cannot bill per seat if you didn't model seats; you cannot offer a usage tier if you never metered. Pricing decisions are schema decisions made 18 months early.
- **Cost architecture** *(added)* — cost per tenant, cost per active user, which infra line items scale with tenants vs with usage. A SaaS architect who can't answer "what does our worst tenant cost us?" is missing half the job.
- **Third-party integration architecture** *(added)* — payment gateways, notification providers, external APIs. Provider abstraction, webhook ingestion (idempotency, replay, ordering), graceful degradation when a vendor is down, and how to avoid a vendor becoming un-swappable.
- Feature flags, gradual rollouts, activation metrics (MRR, churn, NRR)

**Resources:**
- 📚 **[REQUIRED]** *Building Multi-Tenant SaaS Architectures* — Tod Golding (O'Reilly). The only serious book on this. ~20 hrs. It covers Phase 3 and reinforces Phase 2.
- 🎥 **[REQUIRED]** One OAuth 2.0 / OIDC course, any highly-rated one. Auth is worth a dedicated week and video is the right format — the flows are diagrams. ~8 hrs.
- 📄 **[REQUIRED]** stripe.com/docs/billing — the billing guides, free, and better than any course on subscription mechanics. ~4 hrs.
- 🎥 **[PICK ONE — or neither]** A "Build a SaaS in <your stack>" Udemy course. Use it as a *lab* to see wiring, never as architecture guidance. **If you're already building a real product, skip this entirely** — you have a better lab.

**Artifact:** a pricing/packaging sheet for your product with the schema and metering implications of each tier written next to it, plus a cost-per-tenant estimate.

---

## Phase 4 — Delivery & Cloud (6 weeks, ~45 hrs — was 8–10)

**Cut hard.** The original plan spent ~30% of total budget here. Ops tooling is learnable on demand and changes fast; architecture judgment doesn't. You need to ship reliably, not to pass a cloud certification.

**Must-know concepts:**
- Containers: images, layers, compose, registries, multi-stage builds
- CI/CD: pipelines, environments, blue-green and canary, rollbacks, trunk-based development
- Infrastructure as Code: declarative infra, state, modules — the *mindset* more than the syntax
- One cloud, shallowly but correctly: networking basics, compute options, managed DBs, object storage, load balancers, IAM
- Secrets management, artifact versioning, environment parity
- Kubernetes: **vocabulary only** — pods, deployments, services, ingress, why autoscaling works. Enough to read an architecture doc. You do not need to operate it.

**Resources:**
- 🎥 **[REQUIRED]** *Docker & Kubernetes: The Practical Guide* — Schwarzmüller, **Docker sections only**. Do the K8s sections **only if** you have a concrete plan to deploy on Kubernetes within 6 months. Otherwise stop after Docker and save ~15 hrs.
- 🎥 **[REQUIRED]** One CI/CD pipeline course in your ecosystem (GitHub Actions or GitLab CI). ~6 hrs. Short courses are fine here.
- **[PICK ONE]** for cloud:
  - 🎥 *Ultimate AWS Certified Solutions Architect Associate* — Maarek. ~30 hrs. Take it **only if** you want the cert as an external forcing function or a credential for enterprise deals.
  - 📄 A targeted path: AWS (or your provider's) docs + workshops for exactly the six services you'll use — VPC, ECS/App Runner, RDS, S3, ALB, IAM. ~10 hrs, and you'll retain more of it because you'll apply it immediately. **This is the better default.**
- 🎥 **[REQUIRED]** One Terraform course — Maarek or Zeal Vora, ~8 hrs. Stop when you can write a module and explain state; don't complete the cert track.
- **[PICK ONE]** for DevOps culture:
  - 📚 *Accelerate* — Forsgren, Humble, Kim. Short, evidence-based, tells you which metrics matter. **Recommended.**
  - 📚 *The Phoenix Project* — a novel. Same lesson, 5× the pages. Only if you prefer narrative.

**Artifact:** your product deployed via IaC with a CI/CD pipeline that does a zero-downtime deploy and a rollback you've actually tested.

---

## Phase 5 — Operate & Maintain (5 weeks, ~38 hrs)

Most engineers stop at deploy. Products are won here.

**Must-know concepts:**
- Observability: logs vs metrics vs traces, structured logging, dashboards, SLIs/SLOs, alerting that doesn't cry wolf
- Incident response: on-call basics, runbooks, blameless postmortems
- Resilience patterns: timeouts, retries with backoff, circuit breakers, bulkheads, graceful degradation, backpressure
- Backups & DR: RPO/RTO, restore drills — a backup you've never restored doesn't exist
- **Testing strategy** *(added — the plan's largest gap)* — what to unit vs integration vs end-to-end test and why the ratio matters, testing multi-tenant isolation specifically, seeding realistic tenant data, contract testing between services and clients, test environments that don't rot, and what "good enough coverage" means when you're small
- Long-term maintenance: dependency updates, tech-debt budgeting, deprecation strategy

**Resources:**
- 📚 **[REQUIRED]** *Release It!* (2nd ed.) — Nygard. The production-failure patterns book; nothing on video matches it. ~18 hrs.
- 📄 **[REQUIRED]** Google SRE Book (sre.google/books), **Parts I–II only**, and selectively — the chapters on SLOs, alerting, and postmortems. Free. ~8 hrs. Skip the Google-scale-specific chapters.
- 🎥 **[ONLY IF]** A Grafana/Prometheus course — take it **only when** you're actually standing up observability, not before. It's a tool course and will go stale. ~6 hrs.
- 📚 **[SKIP for now]** *Working Effectively with Legacy Code* — Feathers. Excellent, but it's a technique book for rescuing untested legacy systems. If you're building greenfield, this is a year-3 book. Revisit when you have code you're afraid to change.

**Artifact:** SLOs defined for your top three user journeys, one runbook, and a postmortem written for a failure you deliberately caused.

---

## Phase 6 — Scale (4 weeks, ~30 hrs)

Revisit architecture with production scars. **Buy nothing in this phase.**

**Must-know concepts:**
- Horizontal vs vertical scaling; stateless services; sticky sessions and why to avoid them
- Load balancing, CDN, rate limiting (per-tenant rate limiting especially)
- The database scaling ladder: indexes → read replicas → partitioning → sharding, **in that order**. Most products never reach step 4.
- Async everything: job queues, the outbox pattern, eventual consistency and how to explain it to users
- **Offline and sync** *(added)* — if you ship a mobile client: local-first reads, queued writes, conflict resolution, and why "last write wins" eventually loses someone's data
- Capacity planning and load testing
- CAP/PACELC intuition in plain terms

**Resources:**
- 📚 **[REQUIRED]** Re-read DDIA chapters 5–9. They read completely differently after Phases 4–5. ~10 hrs, and it's the highest-return re-read in the plan.
- 📄 **[REQUIRED]** Engineering blogs — Stripe, Shopify, Figma, Discord. Real war stories beat any course, and they're free. ~6 hrs, ongoing.
- 🎥 **[SKIP]** Revisiting Pogrebinsky's scaling sections — you already have this from Phase 1 plus DDIA. Redundant.

**Artifact:** a load test of your own system, a written analysis of where it broke first, and the scaling decision you'd make *next* (not all of them).

---

## Phase 7 — Security & Compliance (3 weeks, ~22 hrs)

Enterprise deals die without this.

**Must-know concepts:**
- OWASP Top 10, secure SDLC basics, dependency scanning
- **Tenant isolation as a security boundary** — the #1 SaaS vulnerability class. A missing `WHERE tenant_id` is a data breach.
- Encryption at rest and in transit, key management
- Compliance literacy: GDPR, SOC 2 (what auditors actually ask for), data residency — plus whatever sector rules apply to your domain (health, financial, education data all carry extra retention and consent requirements)
- Audit logging

**Resources:**
- 📄 **[REQUIRED]** OWASP Cheat Sheet Series. Free, dense, reference-quality. ~8 hrs.
- 🎥 **[PICK ONE — or neither]** A Web Security / OWASP Top 10 Udemy course, **only if** the cheat sheets aren't landing for you. Video adds little here; the cheat sheets are better organized than most courses.
- 📄 **[REQUIRED]** Vanta or Drata blog on SOC 2 in plain English. ~3 hrs.

**Artifact:** a tenant-isolation threat model — every path where data crosses a tenant boundary, and the test that proves it doesn't.

---

## The Capstone — **starts week 3, runs throughout**

The original plan started this at month 6. That's five months of input with no feedback, which is how study plans quietly fail. Start early and let the phases feed it.

**If you already have a real product in flight, use it.** A live multi-tenant system with real users beats a throwaway invoicing app, and the "simulate year 2" exercises come free.

Layer the work as the phases land:

| Week | From phase | Do |
|---|---|---|
| 3–8 | 1 | C4 diagrams + ADRs written *before* code |
| 9–14 | 2 | Multi-tenancy model chosen and documented; one zero-downtime migration |
| 15–19 | 3 | RBAC, SSO-ready auth, subscription billing with metering |
| 20–25 | 4 | Dockerized, IaC-provisioned, CI/CD with tested rollback |
| 26–30 | 5 | Dashboards, SLOs, alerts, runbooks; testing strategy in place |
| 31–34 | 6 | Load-test it, break it, write the postmortem |
| 35–36 | 7 | Threat model, tenant-isolation test suite |

**Then the year-2 simulation:** add a module without touching the others, run a zero-downtime migration on a table with real data, and deprecate an API version while old mobile clients are still calling it.

---

## The final resource list

**Buy these four. They are the plan.**
1. *Designing Data-Intensive Applications* — Kleppmann (ch 1–9)
2. *Building Multi-Tenant SaaS Architectures* — Golding
3. *Release It!* — Nygard
4. *Fundamentals of Software Architecture* — Richards & Ford

**Then pick exactly one from each pair:**
- Systems breadth: Pogrebinsky's course **or** Alex Xu Vol. 1
- DDD: Khononov **or** Vernon's *Distilled*
- Cloud: Maarek's AWS cert course **or** a targeted six-service docs path *(prefer the latter)*
- DevOps culture: *Accelerate* **or** *The Phoenix Project* *(prefer Accelerate)*

**Take these courses, they're tool skills:**
- Docker (Schwarzmüller, Docker sections only)
- One CI/CD pipeline course
- One Terraform course
- One OAuth2/OIDC course

**Conditional — take only if the gap is real:**
- Grider's SQL/Postgres course → only if you can't reason about query plans
- Kubernetes sections → only if deploying to K8s within 6 months
- Grafana/Prometheus → only when actually building observability
- A web security course → only if the OWASP cheat sheets aren't landing

**Cut from the original plan:**
- *The Pragmatic Programmer* — you're past it
- *Clean Architecture* — subsumed by Richards & Ford
- Pogrebinsky's second (cloud patterns) course — overlaps the first
- Alex Xu Vol. 2 — interview-oriented, low marginal value
- *Working Effectively with Legacy Code* — a year-3 book, not a year-1 book
- The Phase 6 course revisit — you'll have it from DDIA
- A "Build a SaaS" course, if you're already building one

**Free and load-bearing:** DDIA is the only thing here you truly can't substitute. But Golding's SaaS Factory talks, the Google SRE book, OWASP cheat sheets, Stripe's billing docs and the big engineering blogs cover a genuine fifth of this plan at zero cost — don't skip them because they're free.

---

## What changed from v1, in one paragraph

Cut the resource list from ~13 books and ~10 courses to 4 required books, 4 pick-one pairs and 4 tool courses — the original was oversubscribed roughly 2.5× against a 230-hour budget, which meant you'd have dropped things at random. Reversed the "Udemy first" rule to books-for-judgment, video-for-tools. Cut Phase 4 from 8–10 weeks to 6 and demoted Kubernetes to vocabulary. Moved the capstone from month 6 to week 3. Added four missing topics: testing strategy, cost-per-tenant architecture, third-party integration architecture, and client contract design for clients you can't force-update. Added a written artifact to every phase so you have a feedback loop.
