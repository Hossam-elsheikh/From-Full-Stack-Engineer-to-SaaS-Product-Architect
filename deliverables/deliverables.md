---
tags: [deliverables, artifacts, index]
---
# Deliverables — what each phase owes you

The plan's rule: **every phase ends in a written artifact.** In a solo study plan that document is the only feedback loop there is — it is what turns reading into a decision you can be wrong about.

Not to be confused with `artifacts/` — that folder holds the *published study pages* you review from. This folder holds the things **you** write.

| Phase | The artifact | Done |
|---|---|:-:|
| 0 · Orientation | One page of "things I don't know I don't know", revisited at the end of the plan | ☐ |
| 1 · Architecture & Design | C4 diagrams (context + container + one component) and **5 ADRs** → `adrs/` | ☐ |
| 2 · Data | Multi-tenancy decision doc: which partitioning model, why, cost at 10 / 1,000 / 10,000 tenants, what forces a migration | ☐ |
| 3 · SaaS Mechanics | Pricing/packaging sheet with the schema and metering implications of each tier, plus a cost-per-tenant estimate | ☐ |
| 4 · Delivery & Cloud | The product deployed via IaC, with a CI/CD pipeline doing a zero-downtime deploy and a rollback you have actually tested | ☐ |
| 5 · Operate & Maintain | SLOs for your top three user journeys, one runbook, and a postmortem for a failure you deliberately caused | ☐ |
| 6 · Scale | A load test of your own system, where it broke first, and the *next* scaling decision — not all of them | ☐ |
| 7 · Security & Compliance | A tenant-isolation threat model: every path where data crosses a tenant boundary, and the test that proves it doesn't | ☐ |

Write each one here as `phase-N-<name>.md`. They are your portfolio as much as your notes are.

## Also in this folder

- [[deliverables/adrs/adrs]] — the ADR log and its template. Phase 1's five records start it.
- [[deliverables/decision-aids]] — one-page decision diagrams and cheat sheets. By the end of the plan there should be 15–20; this collection *is* your value in a real design meeting.
- [[deliverables/case-studies]] — postmortems and engineering-blog autopsies: what broke, why, which pattern would have prevented it, what you'd have monitored.
