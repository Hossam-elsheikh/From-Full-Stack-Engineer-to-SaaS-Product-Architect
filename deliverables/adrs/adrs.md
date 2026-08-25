---
tags: [adr, decisions, index]
---
# Architecture Decision Records

Phase 1's artifact is **five ADRs for a real system** — not a hypothetical. Written *before* the code, in capstone weeks 3–8.

Template:

```markdown
# ADR-###: Title
- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Deprecated
- **Context:** Why are we making this decision?
- **Options:** Option A: ..., Option B: ...
- **Decision:** Chosen option
- **Consequences:** What this means going forward
```

The **Consequences** section is the one that earns its keep. If you cannot name what the choice costs, you have not made it yet.

## Candidates for the first five

- Monolith vs modular monolith vs microservices
- Shared schema vs schema-per-tenant vs DB-per-tenant *(also the phase 2 artifact)*
- REST vs gRPC vs GraphQL for the public API
- Sync vs async for inter-service communication
- API versioning strategy for clients you cannot force-update

## Log

| # | Title | Date | Status |
|---|---|---|---|
| — | *(none yet)* | | |
