# The Study System
### Companion to `saas-architect-study-plan.md` (Rev B)

The original version of this file prescribed daily Anki, a Sunday blank-page ritual and a NotebookLM habit. That system was abandoned for a straightforward reason: **it wasn't fun, so it didn't happen.** What replaced it is built on two things that do happen — *building against a brief* and *deciding under consequence*.

This file covers what survived the change: how the vault works, how to use AI as a sparring partner rather than a summariser, and what practice looks like in each phase.

For the links themselves see [[where-to-study]]. For the deliverables each phase owes you see [[deliverables/deliverables]].

---

# Part 1 — The capture system

## One home, one capture point per phase

```
concepts/<phase>/            one note per concept, plus diagrams/ and images/
concepts/<phase>/_inbox.md   raw dumps for that phase — the only place notes land
deliverables/                what you write: ADRs, decision docs, threat models, case studies
artifacts/                   the published study pages you actually review from
resources/                   PDFs, course links, reading lists
```

**The rule that fixes "where do I save this":** while studying, paste into the phase's `_inbox.md`. Nothing else. No filing decisions mid-flow — deciding where a note goes is a different mode of thought from learning, and switching between them kills both.

**Then ask Claude to distribute it.** The raw text becomes concept notes *and* gets merged into that phase's published sheet, republished at the same URL. That is the step that makes review possible without ever opening Obsidian.

## Which format for which knowledge

| If the knowledge is… | Save it as… | Example |
|---|---|---|
| A trade-off between options | A **decision aid** in `deliverables/decision-aids.md` | Shared schema vs DB-per-tenant |
| A process, flow or structure | An **Excalidraw diagram** in the phase's `diagrams/` | Request path through LB → app → cache → DB |
| An insight in your own words | An **evergreen concept note** | "Why microservices tax small teams" |
| A story of failure | A **case study** in `deliverables/` | "How GitLab lost their DB in 2017" |
| A scenario worth recalling cold | A `#card` **in the concept note** | "Payment API is timing out and threads pile up — which pattern, which three states?" |

Cards still exist, but they are not a separate ritual: they live inside the notes and surface on the phase sheet when you want to test yourself. Write them as **situations, not definitions** — that is the part your vault already gets right, and it is the difference between recall you can use in a design meeting and recall you can use in a quiz.

---

# Part 2 — Practice

## The two engines

**[The Build Bench](https://claude.ai/code/artifact/674ef97b-db8f-46c9-9050-06b83ba95e7b)** — eight client briefs with real constraints. Assemble a system from a bin of parts, submit for design review, get stamped. It penalises the microservices reflex, the premature shard, and the part that isn't earning its keep. One evening a week, fifteen minutes. **A rejected review is your reading list** — better than the one you wrote in advance.

**[Year One at Ledgerly](https://claude.ai/code/artifact/6f151972-b169-4e67-8676-ef1f3d243b5c)** — seventeen decisions across four quarters as founding architect. Decisions carry forward; the tenancy model you pick in week five is what an auditor interrogates in Q3. Sunday, ten minutes.

## AI as a sparring partner

The rule of hygiene: **AI explains and challenges; you produce the diagram or the answer first.** If the AI produced it, you didn't learn it.

Three prompts worth reusing every phase:

1. **Mock design review** — "I'll paste my architecture for X. Act as a skeptical principal engineer: find failure modes, question my trade-offs, ask me 5 hard follow-ups one at a time." Answer before scrolling.
2. **Scenario generator** — "Give me a realistic production incident for a system using [the pattern I just studied]. Reveal symptoms only. I'll diagnose step by step — only tell me whether my next step is reasonable."
3. **Feynman checker** — "Here's my explanation of eventual consistency. Find every imprecision, then tell me what I'd be asked next."

## Design katas

Weekly, timeboxed, 45–60 min: requirements → C4 container diagram → key trade-offs → one ADR. Prompt sources: Alex Xu's chapters (design it *before* reading his solution, then diff), Neal Ford's Architectural Katas, or your own — "design Calendly / a URL shortener with per-team quotas / a webhook delivery system."

## Real-case autopsy

Bi-weekly, 30 min. One postmortem or scaling story → a note in `deliverables/case-studies.md`. Phase 6 makes this required.

---

# Part 3 — Per-phase practice

**Phase 0 — Orientation.** One week. Read the *Fundamentals* table of contents and chapters 1–4, write the one-page list of what you don't know you don't know, and stop. Don't build a study apparatus; you already have one.

**Phase 1 — Architecture & Design.** Weekly design kata plus an AI mock design review on your real system's design. Decision aids: "monolith vs modular monolith vs microservices", "sync vs async". The five ADRs are the deliverable, and they start the capstone.

**Phase 2 — Data.** DDIA is dense — one chapter at a time, and stop after chapter 9. Decision aids: "choosing a multi-tenancy data model", "when to add a cache / replica / search engine". Practice: hand-execute an expand-backfill-contract migration plan on paper; AI scenario — "this query got slow at 10M rows, diagnose."

**Phase 3 — SaaS Mechanics.** Sketch the complete onboarding sequence (signup → tenant provisioning → first login) from memory. AI roleplay: "act as an enterprise customer's security team asking about SSO and tenant isolation." Then write the pricing sheet with schema implications beside each tier — that exercise is where pricing-versus-architecture stops being abstract.

**Phase 4 — Delivery & Cloud.** 80% hands-on: **doing is the retention.** Fewer notes, more terminal. Destroy and rebuild your infra from Terraform alone. Break your own pipeline and fix it. Kubernetes is vocabulary — read it, don't operate it.

**Phase 5 — Operate & Maintain.** Write a real runbook for the capstone, then run a **game day**: kill a container or the DB mid-request and follow your own runbook. Write the postmortem. Also the phase where testing strategy lands — including the tests that prove tenant isolation holds.

**Phase 6 — Scale.** Capacity estimation drills, one a week: "ten thousand tenants, fifty requests a day each, 2KB payloads — servers? DB size? bandwidth?" Then load-test the real thing and find out how wrong you were. Buy nothing this phase.

**Phase 7 — Security & Compliance.** Threat-model the capstone with STRIDE. AI roleplay: "act as a pentester describing how you'd attack my multi-tenant API." The deliverable is the tenant-isolation threat model and the test suite that backs it.

**The capstone.** Starts week 3. Everything converges: ADRs, runbooks, postmortems and diagrams all land in `deliverables/`. That is your portfolio and your permanent playbook.

---

## The whole system on one line

**Capture into the phase inbox → ask Claude to distribute → review on the published sheet → practise on the Bench and in Year One → write the phase's deliverable → re-mark the Atlas.**

If you only keep three habits: **the Build Bench commission, the Sunday Year One run, and the AI mock design review.**
