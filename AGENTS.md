# AGENTS.md — SaaS Architect Study Vault

Obsidian vault for the **SaaS Architect study plan** (see `saas-architect-study-plan.md` and `study-system-and-retention-guide.md`). The core job here: turn raw study notes into durable, reviewable knowledge artifacts.

## What the vault holds

```
inbox/             → raw dumps. Everything lands here first. Cleaned weekly.
concepts/          → one evergreen note per concept, organized by phase
  <phase N - name>/   e.g. "phase 1 - architecture & system design", "phase 2 - data"
    diagrams/          → Excalidraw files (*.excalidraw.md)
    images/            → embedded screenshots / exported PNGs
patterns/          → reusable diagrams, cheat sheets, decision trees
decisions/         → ADRs (Architecture Decision Records), trade-off tables
case-studies/      → real-world postmortems: what broke / why / what prevented it
reviews/           → weekly & monthly recall notes
phases/            → per-phase resources (PDFs, links)
```

## The workflow

1. **Capture** — raw notes go straight into `inbox/` while studying. Never decide "where does this go" mid-study.
2. **Distribute (weekly)** — convert inbox content into concept notes (see below), then **empty the inbox** into a "Concept Notes Created" table.
3. **Review daily** — Anki cards (flashcard bolt in Obsidian); weekly blank-page test; end-of-phase Feynman test.

## Distributing inbox content → concept notes

### Where does a topic go?

Map to the study-plan phases (`progress-checklist.md`):
- Architecture, quality attributes, API design, messaging, microservices, EDA, CQRS, multi-tier → `concepts/phase 1 - architecture & system design/`
- Databases (relational, NoSQL, indexing, replication, sharding, CAP, storage) → `concepts/phase 2 - data/`
- SaaS mechanics (tenancy, auth, billing, feature flags) → `concepts/phase 3 - saas-specific/`
- DevOps, cloud, delivery → `concepts/phase 4 - devops-cloud/`
- Observability, incident response, resilience → `concepts/phase 5 - operating-maintaining/`
- Scaling, load balancing, CDN, rate limiting → `concepts/phase 6 - scalability/`
- Security & compliance → `concepts/phase 7 - security-compliance/`

Create the phase folder if it doesn't exist yet. **Rule: one concept per note.** Don't dump multiple topics into one file.

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
- **Question form, from the "using" perspective** — not definitions. Give a scenario/symptom, ask for the pattern/decision/trade-off.
- One idea per card. Target ~15–25 new cards/week; if a note needs more, it's trivia — cut.
- Only card what you'd need without Google in a design discussion (patterns, trade-offs, orders of magnitude). Skip exact CLI flags / API syntax.
- Keep `cards-deck` consistent per note so cards group in Anki.

### Diagram guidelines

- Create an Excalidraw file (`.excalidraw.md`) in the note's `diagrams/` folder whenever a concept is a **flow / structure / process** (tiers, replication, sharding, CAP triangle, EDA, microservices).
- File format: `excalidraw-plugin: parsed` frontmatter + `# Excalidraw Data` + `## Text Elements` + JSON under `## Drawing`. Match the style of existing diagrams in `concepts/*/diagrams/`.
- Use the standard color scheme used in this vault:
  - producer/client/primary = blue (`#1971c2` on `#e7f5ff`)
  - broker/application = red (`#e03131` on `#fff5f5`)
  - consumer/replica/shard = green (`#2f9e44` on `#ebfbee`)
  - entry points / orchestration = purple (`#7048e8` on `#f3f0ff`)
  - arrows/labels = gray (`#868e96`)
- Add a one-line caption. Reference the diagram in the note with `![[...]]`.
- Move any source images (PNG) into the note's `images/` folder and reference them with `![[...]]`; never leave stray images in the repo root.

## After distributing, update these

- `concepts/concepts.md` — add new notes to the correct phase section (create the section if the phase is new).
- `patterns/patterns.md` — add links under "Related Concept Notes" for new patterns (EDA, CQRS, microservices, etc.).
- `decisions/decisions.md` — if a trade-off decision was actually made, write an ADR; otherwise leave "Planned".
- `inbox/<file>.md` — replace distributed raw content with the "Concept Notes Created" table (Topic | File | With Flashcards | With Diagram), then keep the "Next Steps" section.
- `progress-checklist.md` — check off items only if the user asks; don't update unilaterally.

## Verification before finishing

1. Every new note has: frontmatter with `cards-deck`, at least one `#card` flashcard, a `## Source` section.
2. Every `![[...]]` link points to a file that actually exists (diagram/image or concept).
3. Diagrams contain valid JSON that parses (`python3 -c "import json,re; ..."` if unsure).
4. Indexes (`concepts.md`, `patterns.md`) reflect all new files.
5. Inbox has no leftover raw content.
