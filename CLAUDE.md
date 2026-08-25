# CLAUDE.md — SaaS Architect Study Vault

Hossam studies the SaaS-architect plan here and **reviews entirely through published artifacts**, not by opening notes. Markdown notes are the source of record; the artifacts are the interface. When new notes arrive, the job is not finished until the matching artifact is rebuilt and republished.

See `AGENTS.md` for the vault layout and note formatting (frontmatter, `#card` flashcards, Excalidraw conventions) and `artifacts/artifacts.md` for the artifact URLs and build system. The plan is `saas-architect-study-plan.md` (Rev B — ~230 hrs over ~8 months); `progress-checklist.md` mirrors its phases.

---

## The standing job: new notes → artifact

Raw notes arrive in a phase's `concepts/phase-N-.../_inbox.md` — that is the only capture point; there is no top-level `inbox/`. Whenever they do, or whenever the user says "I added notes", run this loop:

**1 · Find what is new.** `git status` and `git log --oneline -5`, plus any `_inbox.md` with raw content under its `---` separator. Read every new or changed note in full — never summarise from a filename.

**2 · Distribute the raw content.** Turn each topic into its own concept note in the right phase folder, following the format in `AGENTS.md` exactly: frontmatter with `cards-deck`, scenario-style `#card` flashcards, a `## Source` section. Then clear the raw text out of the inbox file and add the topic to its "Distributed" table, keeping the inbox header.

**3 · Merge into the phase artifact — this is the step that must not be skipped.** Add each concept to `artifacts/data/phase-N.json`:

```jsonc
{
  "id": "database-indexing",              // kebab-case, unique across the phase
  "t": "Database Indexing",
  "vault": "concepts/phase-2-data/database-indexing.md",
  "lede": "One or two sentences. What it is and why it matters.",
  "drill": "Year One · Shard now?",       // where a simulation exercises it, if it does
  "blocks": [                              // in reading order
    {"h": "Types", "items": ["**Single-column** — one column", "**Composite** — several"]},
    {"h": "Trade-offs", "p": "A paragraph instead of bullets."},
    {"h": "Optional heading", "num": ["ordered", "list"]},
    {"table": {"cols": ["Type", "Use"], "rows": [["**Key/Value**", "Caching"]]}},
    {"call": "A pull-quote worth remembering.", "blue": true},
    {"svg": "cap", "cap": "Caption under the figure"}
  ],
  "cards": [["Scenario-style question?", "The answer."]]
}
```

Rules: `**bold**`, `*italic*` and `` `code` `` work inside any string. Available `svg` keys are defined at the top of `artifacts/template/phase.body.html` — currently `three-tier`, `cap`, `windows`, `scaling-ladder`; add a new one there rather than inlining SVG in the data. Cards come from the note's `#card` blocks, reworded only for punctuation. Order concepts so the sheet reads top to bottom as a lesson, not alphabetically.

Also remove the concept from that phase's `ghosts` array in `artifacts/data/atlas.json` if it was listed there as not-yet-captured — otherwise it appears twice on the map.

**4 · If the phase has no artifact yet** (phases 0, 3, 4, 5, 7 and the capstone), create `artifacts/data/phase-N.json` with `phase`, `title`, `weeks`, `lede`, `source`, `foot`, `links`, `concepts` and `resources` — copy the shape of `phase-2.json`. Take the `resources` entries from that phase's section of `saas-architect-study-plan.md`, **keeping the plan's tags** (`[REQUIRED]`, `[PICK ONE]`, `[ONLY IF]`, `[SKIP]`) as the `k` label, and end the list with the phase's written artifact. Give it a real name, not "Phase N" (compare: *Data at Scale*, *The Traffic Layer*). Then add `"sheet": "phase-N"` to that phase in `atlas.json`, publish the new page, and write both its URL and `"url": "..."` back into `atlas.json` and `artifacts/artifacts.md`.

**5 · Rebuild and republish.**

```bash
python3 artifacts/build.py
```

Then publish **the phase sheet and the Atlas**, each with its existing URL passed as the `url` parameter (see `artifacts/artifacts.md`). Publishing without `url` creates a duplicate and strands the link the user already has.

**6 · Update the indexes**: `concepts/concepts.md`, `deliverables/decision-aids.md` and `deliverables/adrs/adrs.md` where relevant, and the phase's `_inbox.md`. Leave `progress-checklist.md` alone unless asked.

**7 · Tell the user what changed** — which concepts landed, on which sheet, and the link. Not a file listing.

---

## The simulations

`build-bench.html` (eight design-brief puzzles) and `year-one.html` (a seventeen-decision narrative) are hand-edited: their data sits inline in the page's `<script>`. New notes do **not** automatically belong in them — add a brief or a chapter only when the user asks, or when a whole phase has been captured and has no scenario exercising it. Both pages use the same tokens and title-block identity as everything else; read `artifacts/artifacts.md` before editing either.

## What this study system is for

The plan was rewritten (Rev B) after the first version came in ~2.5x overbooked. It is now ~230 hours inside a ~230-hour budget: four required books, four pick-one pairs, four tool courses. Two consequences for how you should advise:

- Do not reinforce a phase-by-phase march. The capstone is the spine — it starts in **week 3** and every phase feeds it, so tie next steps to what building it actually needs.
- **Do not add resources back.** Every nice-to-have comes out of capstone time. If the user asks about a book or course, check the plan's cut list before endorsing it.
- **Every phase ends in a written artifact** (`deliverables/`). That is the plan's only feedback loop — treat a phase without its artifact as unfinished.
- The user rejected the original Anki / blank-page ritual as no fun. He responds to **building** (assemble a system against a brief, get it graded) and **narrative simulation** (decisions with consequences). Keep new practice in those two shapes; don't propose drill routines.
