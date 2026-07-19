# The Study System: Retain, Recall, Apply
### Companion to the SaaS Architect Study Plan

Two problems, two systems:
1. **"I forget concepts and don't know where/how to save them"** → a Capture & Recall system
2. **"Some topics need practice and real-case scenarios"** → a Practice & Simulation system

Set both up in week 1 of Phase 0. They take ~1 hour to set up and save you months of re-learning.

---

# PART 1 — The Capture & Recall System

## 1.1 One home for everything: your "Second Brain"
**Tool: Obsidian** (free, local markdown, future-proof) or Notion if you prefer.

Folder structure — keep it stupid-simple:

```
/inbox          → raw dumps, clean weekly
/concepts       → one note per concept (evergreen notes)
/decisions      → your ADRs and trade-off tables
/patterns       → reusable diagrams & cheat sheets
/case-studies   → real-world stories you analyzed
/reviews        → weekly & monthly review notes
```

**The rule that fixes "I don't know where to save it":** everything goes to `/inbox` first, zero friction. Every Sunday (15 min), you empty the inbox into the right folder. Never decide "where does this go" while studying — it kills flow.

## 1.2 The three formats — pick by question type
Not everything should be a flashcard. Use this decision rule:

| If the knowledge is... | Save it as... | Example |
|---|---|---|
| A fact / definition / threshold | **Anki flashcard** | "What are the 4 ACID properties?" |
| A trade-off between options | **Decision table/diagram** | Shared schema vs DB-per-tenant |
| A process / flow / structure | **Diagram** (Excalidraw/draw.io) | Request path through LB → app → cache → DB |
| An insight in your own words | **Evergreen concept note** | "Why microservices tax small teams" |
| A story of failure/success | **Case-study note** | "How GitLab lost their DB in 2017" |

## 1.3 Flashcards done right (Anki)
Spaced repetition is the scientifically proven fix for forgetting — but only with good cards:

- **Write cards in question form**, from the "using" perspective, not the "defining" one.
  - ❌ "What is a circuit breaker?"
  - ✅ "Your payment provider's API is timing out and threads are piling up. Which resilience pattern, and what are its 3 states?"
- **One idea per card.** Never paste paragraphs.
- **Make cards only for things you'll need without Google in a design discussion** (trade-offs, patterns, orders of magnitude, isolation levels). Skip anything you'd look up anyway (exact CLI flags, API syntax).
- **Latency numbers deck:** make cards for the classic "numbers every engineer should know" (RAM vs SSD vs network round-trip, etc.) — these power your capacity estimations forever.
- Daily habit: **10 min of Anki with morning coffee.** Non-negotiable, tiny, compounding.
- Target: ~15–25 new cards per week. More = you're carding trivia.

## 1.4 Decision diagrams — your personal architecture playbook
For every major trade-off you study, build a **one-page decision aid** in Excalidraw/draw.io/Mermaid:

- A flowchart: "Choosing a multi-tenancy model" → questions about isolation needs, compliance, tenant count → arrows to shared schema / schema-per-tenant / DB-per-tenant
- Or a comparison table with a "choose this when..." row

By the end of the plan you'll have ~15–20 of these. **This collection IS your value as an architect** — it's what you'll open in real design meetings.

## 1.5 The recall schedule (this is what beats forgetting)
Passive re-reading does nothing. Schedule **active recall**:

| Cadence | Ritual | Time |
|---|---|---|
| Daily | Anki review | 10 min |
| End of each study session | Close everything, write from memory a 5-bullet "what did I learn" note | 5 min |
| Weekly (Sunday) | Empty inbox + **blank-page test**: pick one topic from this week, explain it on a blank page with a diagram, no sources. Then compare & patch gaps | 30 min |
| End of each phase | **Feynman test**: record yourself explaining the phase's 3 core ideas as if to a junior dev. Where you stumble = your Anki cards for next week | 30 min |
| Monthly | Re-open one old decision diagram and try to redraw it blind | 15 min |

---

# PART 2 — The Practice & Simulation System

Concepts stick when they're used under mild pressure. Three engines:

## 2.1 Design katas (weekly, 45–60 min)
Once a week, take a prompt and produce: requirements → C4 container diagram → key trade-offs → one ADR. Timebox it. Sources of prompts:
- Alex Xu's book chapters (do the design BEFORE reading his solution, then diff)
- "Architectural Katas" (Neal Ford's kata list, free online)
- Your own: "Design Calendly / a URL shortener with per-team quotas / a webhook delivery system"

## 2.2 AI as your sparring partner (the real unlock)
Use AI tools not to summarize FOR you, but to **pressure-test you**:

**NotebookLM (Google) — your book companion:**
- Upload chapters/notes of DDIA, Release It!, Golding's SaaS book → ask questions against the source, generate the **Audio Overview "podcast"** and listen while commuting (great pre-read or refresher)
- After finishing a chapter, ask it to quiz you: "Generate 10 hard questions from this chapter" → answer from memory → check
- Keep one notebook per phase; it becomes a searchable, ask-able version of your own materials

**Claude / ChatGPT — three killer prompts to reuse every phase:**
1. **Mock design review:** "I'll paste my architecture for X. Act as a skeptical principal engineer: find failure modes, question my trade-offs, ask me 5 hard follow-ups one at a time." (Answer before scrolling.)
2. **Scenario generator ("prediction helper"):** "Give me a realistic production incident for a system using [pattern I just studied]. Reveal symptoms only. I'll diagnose step by step — only tell me if my next step is reasonable." — this trains the prediction muscle you asked for.
3. **Feynman checker:** "Here's my explanation of eventual consistency. Find every imprecision or wrong statement, and tell me what a candidate would be asked next in an interview."

**Rule of hygiene:** AI explains and challenges; **you** produce the diagram/answer first. If the AI produced it, you didn't learn it.

## 2.3 Real-case autopsy (bi-weekly, 30 min)
Read one real postmortem or engineering-blog scaling story → write a case-study note: *What broke / why / which pattern would've prevented it / what I'd have monitored.* Goldmines: GitHub/Cloudflare/GitLab public postmortems, danluu's postmortem list, Shopify/Stripe/Figma engineering blogs.

---

# PART 3 — Phase-by-Phase Toolkit

**Phase 0 — The Map**
- Build the Obsidian vault + Anki deck + NotebookLM account NOW
- First artifact: a one-page mindmap of the whole SaaS lifecycle (redraw it blind at the end of every phase — watch it get richer)

**Phase 1 — Architecture & System Design**
- Anki: architectural styles & when-to-use, quality attributes, API design rules
- Decision diagrams: "monolith vs modular monolith vs microservices", "sync vs async"
- Practice: weekly design kata + AI mock design review on your invoicing-SaaS design
- NotebookLM: notebook with Richards & Ford + Khononov chapters; quiz yourself per chapter

**Phase 2 — Data**
- Anki: isolation levels (scenario cards!), index types, latency numbers, cache patterns
- Decision diagrams: "choosing a multi-tenancy data model", "when to add a cache/replica/search engine"
- Practice: AI scenario prompts — "this query got slow at 10M rows, diagnose"; hand-execute a zero-downtime migration plan on paper
- DDIA is dense → NotebookLM podcast per chapter as a pre-read, then read, then Anki

**Phase 3 — SaaS-Specific**
- Anki: OAuth flows (as scenario cards: "mobile app + your API → which flow?"), billing edge cases (proration, dunning)
- Decision diagram: tenant tiering (pooled vs siloed), RBAC vs ABAC
- Practice: sketch the complete onboarding sequence diagram (signup → tenant provisioning → first login) from memory; AI roleplay: "act as an enterprise customer's security team asking about my SSO & tenant isolation"

**Phase 4 — DevOps & Cloud**
- This phase is 80% hands-on: **doing IS the retention.** Fewer cards, more terminal.
- Anki only for: K8s object relationships, deployment strategies (blue-green vs canary vs rolling), VPC building blocks
- Practice: destroy and rebuild your infra from Terraform alone; break your own pipeline and fix it
- Keep a `/patterns` note: "my standard pipeline stages" — you'll reuse it in every job

**Phase 5 — Operating & Maintaining**
- Anki: resilience patterns as symptom→pattern scenario cards; RPO vs RTO
- Practice: write a real runbook for your capstone; run a **game day** — kill a container/DB mid-request and follow your own runbook; write a blameless postmortem template and use it
- Real-case autopsies shine here — 1 public postmortem per week

**Phase 6 — Scalability**
- Anki: the database scaling ladder, back-of-envelope numbers
- Practice: **capacity estimation drills** (your "prediction helper"): "10k tenants, 50 req/day each, 2KB payloads — servers? DB size? bandwidth?" Do one weekly; AI checks your math
- Decision diagram: "system is slow → diagnosis tree" (CPU-bound? IO? lock contention? N+1?)

**Phase 7 — Security & Compliance**
- Anki: OWASP Top 10 as attack-scenario cards ("user sends ?id=../../ — which class, which defense?")
- Practice: threat-model your capstone (STRIDE checklist); AI roleplay: "act as a pentester describing how you'd attack my multi-tenant API"

**Capstone**
- Everything converges: your ADRs, runbooks, postmortems, and diagrams from the capstone go straight into your vault — that's your portfolio AND your permanent playbook.

---

## The whole system on one line
**Capture to inbox → sort weekly → facts to Anki, trade-offs to diagrams, insights to notes → recall daily (Anki) & weekly (blank page) → apply via katas, AI sparring, and autopsies.**

If you only adopt three habits: **10-min daily Anki, the Sunday blank-page test, and the AI mock design review.** Those three alone solve both of your problems.
