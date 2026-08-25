---
tags: [artifacts, registry]
---
# Artifact Registry

**Every URL below is permanent.** To update a page, republish it **with its URL passed as the `url` parameter** — publishing without it creates a duplicate instead of updating the page the user has open.

| File | Artifact | URL | Built from |
|------|----------|-----|-----------|
| `atlas.html` | The Architect's Atlas | https://claude.ai/code/artifact/f3e583da-ec48-4778-8d52-e1c0a4764fcd | `data/atlas.json` + every `data/phase-*.json` |
| `phase-1.html` | Architecture & Design | https://claude.ai/code/artifact/59673390-3b25-411f-ab78-508abaf0ffa8 | `data/phase-1.json` |
| `phase-2.html` | Data at Scale | https://claude.ai/code/artifact/c28d2dd1-5735-4dc9-9307-b1b87b51dc91 | `data/phase-2.json` |
| `phase-6.html` | The Traffic Layer | https://claude.ai/code/artifact/fb4c2c7d-6646-44ed-b7a5-1409b6038962 | `data/phase-6.json` |
| `build-bench.html` | The Build Bench | https://claude.ai/code/artifact/674ef97b-db8f-46c9-9050-06b83ba95e7b | hand-edited (brief data is inline) |
| `year-one.html` | Year One at Ledgerly | https://claude.ai/code/artifact/6f151972-b169-4e67-8676-ef1f3d243b5c | hand-edited (chapter data is inline) |

Superseded, do not use: `f284174f-3c69-4b93-9a0e-cfd3f6698545` — an accidental duplicate of the Atlas.

Phases 0, 3, 4, 5, 7 and the capstone have no sheet yet — they get one the first time they have notes (`CLAUDE.md` step 4). The Atlas already lists their concepts as ghosts.

## Build

```bash
python3 artifacts/build.py            # everything
python3 artifacts/build.py phase-2    # one phase (the Atlas is not rebuilt)
```

`build.py` fails loudly on a missing required key or a duplicate concept id. The Atlas is generated from the phase files, so a concept added to a phase appears on the map automatically — always rebuild and republish both.

## Anatomy

```
artifacts/
  build.py              generator
  artifacts.md          this registry
  data/
    atlas.json          the map: phases, and concepts NOT yet captured ("ghosts")
    phase-N.json        one phase's captured concepts, cards and reading list
  template/
    base.css            shared drafting-sheet identity (all six pages)
    phase.css           phase-sheet layout
    phase.body.html     phase-sheet markup + script (__DATA__ placeholder)
    atlas.css           atlas layout
    atlas.body.html     atlas markup + script (__DATA__ placeholder)
  *.html                generated / hand-edited pages — publish these
```

## Design constraints for any edit

- **Theme**: colours come from the CSS custom properties in `base.css` only. Never write a raw hex in a component rule, and never define a colour solely inside a `@media` or `[data-theme]` block.
- **Self-contained**: no external requests except Google Fonts. Inline everything else.
- **`[hidden]`**: `base.css` ends with `[hidden]{display:none !important}` — it is load-bearing. Fixed overlays (`.drawer`, `.review`) set `display:flex`, which otherwise beats the browser's `[hidden]` rule and leaves an invisible panel swallowing every click.
- **Fonts**: Saira Condensed (display / title blocks), IBM Plex Sans (body), IBM Plex Mono (labels and data).
