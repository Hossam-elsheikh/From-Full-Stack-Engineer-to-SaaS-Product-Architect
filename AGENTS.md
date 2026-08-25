# AGENTS.md — SaaS Architect Study Vault

Obsidian vault for the **SaaS Architect study plan** (`saas-architect-study-plan.md`, Rev B; companion: `study-system.md`). The core job here: turn raw study notes into durable, reviewable knowledge — and into the published artifacts that are the only place the user actually reads them. `CLAUDE.md` has the end-to-end workflow; this file is the formatting reference.

## What the vault holds

```
saas-architect-study-plan.md   the plan (Rev B — ~230 hrs, 8 months)
study-system.md                how the study system works
where-to-study.md              the artifact links, the weekly loop
progress-checklist.md          tracker, mirrors the plan's phases

concepts/                      one evergreen note per concept, by phase
  concepts.md                    index (MOC)
  phase-0-orientation/
  phase-1-architecture/
  phase-2-data/
  phase-3-saas-mechanics/
  phase-4-delivery-cloud/
  phase-5-operate-maintain/
  phase-6-scale/
  phase-7-security/
  capstone/
    _inbox.md                    raw dumps for that phase — the only capture point
    diagrams/                    Excalidraw files (*.excalidraw.md)
    images/                      screenshots / exported PNGs

deliverables/                  what the user writes: the per-phase written artifacts
  deliverables.md                the table of what each phase owes
  adrs/                          ADR log + template
  decision-aids.md               decision diagrams and cheat sheets
  case-studies.md                postmortem autopsies

artifacts/                     the published study pages + build system (see artifacts/artifacts.md)
resources/                     PDFs, course links, reading lists
```

There is **no top-level `inbox/`** and no separate `phases/` tree — one capture point per phase, one resources folder.

## The workflow

1. **Capture** — raw notes go into the phase's `_inbox.md` while studying. Never decide "where does this go" mid-study.
2. **Distribute** — convert inbox content into concept notes (below), **merge them into the phase artifact**, then clear the raw text and record the topic in the inbox's table. See `CLAUDE.md` — step 3 is the one that must not be skipped.
3. **Review** — entirely through the published artifacts (`where-to-study.md`). The user does not open notes.

## Distributing inbox content → concept notes

### Where does a topic go?

Map to the plan's phases:
- Architecture, quality attributes, API design, messaging, microservices, EDA, CQRS, DDD, C4/ADRs → `concepts/phase-1-architecture/`
- Databases, indexing, replication, sharding, CAP, caching, migrations, tenancy data models → `concepts/phase-2-data/`
- SaaS mechanics: tenancy end-to-end, auth, billing, pricing/cost, integrations, flags → `concepts/phase-3-saas-mechanics/`
- Containers, CI/CD, IaC, cloud, secrets → `concepts/phase-4-delivery-cloud/`
- Observability, incidents, resilience, DR, testing strategy → `concepts/phase-5-operate-maintain/`
- Scaling, load balancing, CDN, rate limiting, async/outbox, offline sync → `concepts/phase-6-scale/`
- Security & compliance → `concepts/phase-7-security/`

**Rule: one concept per note.** Don't dump multiple topics into one file.

### Concept note format (follow exactly)

```markdown
---
tags: [<lowercase keywords>]
cards-deck: SaaS Architect::<Phase N>::<Note Title>
---
# <Title>

<1–2 sentence intro>

## <Section>

- bullets
- with **bold** key terms

<Scenario-style question> #card
<answer on the next line>

![[concepts/<phase>/diagrams/<diagram-name>.excalidraw]]

## Related

- [[concepts/<phase>/<other-note>]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
```

### Flashcard guidelines

- Format: `Question` followed by `#card` on the same line, answer on the next line.
- **Question form, from the "using" perspective** — not definitions. Give a scenario or symptom, ask for the pattern, decision or trade-off. This is what the phase sheets surface for self-testing.
- One idea per card. If a note needs more than ~6, it's trivia — cut.
- Only card what you'd need without Google in a design discussion (patterns, trade-offs, orders of magnitude). Skip exact CLI flags and API syntax.
- Keep `cards-deck` consistent per note.

### Diagram guidelines

- Create an Excalidraw file (`.excalidraw.md`) in the note's `diagrams/` folder whenever a concept is a **flow / structure / process** (tiers, replication, sharding, CAP triangle, EDA, microservices).
- File format: `excalidraw-plugin: parsed` frontmatter + `# Excalidraw Data` + `## Text Elements` + JSON under `## Drawing`. Match the existing diagrams.
- Standard colours:
  - producer/client/primary = blue (`#1971c2` on `#e7f5ff`)
  - broker/application = red (`#e03131` on `#fff5f5`)
  - consumer/replica/shard = green (`#2f9e44` on `#ebfbee`)
  - entry points / orchestration = purple (`#7048e8` on `#f3f0ff`)
  - arrows/labels = gray (`#868e96`)
- Add a one-line caption; reference with `![[...]]`. Move source PNGs into the note's `images/` folder — never leave stray images in the repo root.

## After distributing, update these

- `artifacts/data/phase-N.json` **and republish** — see `CLAUDE.md`. Not optional.
- `concepts/concepts.md` — add new notes to the correct phase section.
- `deliverables/decision-aids.md` — add links under "Related concept notes" for new patterns.
- `deliverables/adrs/adrs.md` — if a trade-off decision was actually made, write an ADR; otherwise leave it listed as a candidate.
- The phase's `_inbox.md` — replace distributed raw content with the "Distributed" table, keep the header.
- `progress-checklist.md` — check items off only if the user asks.

## Verification before finishing

1. Every new note has: frontmatter with `cards-deck`, at least one `#card`, a `## Source` section.
2. Every `![[...]]` points to a file that exists.
3. Diagrams contain valid JSON that parses.
4. `python3 artifacts/build.py` runs clean, and the phase sheet **and** the Atlas are republished to their existing URLs.
5. Indexes reflect all new files, and no inbox has leftover raw content.
