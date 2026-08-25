---
tags: [practice, artifacts, index]
---
# Where You Study

You do not read notes in Obsidian. You read them here. Start at the Atlas — everything links from it.

## The map

[**The Architect's Atlas**](https://claude.ai/code/artifact/f3e583da-ec48-4778-8d52-e1c0a4764fcd) — all 9 stations, every concept in the plan, captured or ahead of you. Blue chips are in your vault, dashed chips are territory you have not reached. Mark each Not yet / Shaky / Solid; it keeps score. It also carries the reviewer's notes on the plan itself.

## Phase sheets — reading and self-testing

| Sheet | Concepts | Cards |
|---|:-:|:-:|
| [Architecture & Design](https://claude.ai/code/artifact/59673390-3b25-411f-ab78-508abaf0ffa8) — phase 1 | 12 | 49 |
| [Data at Scale](https://claude.ai/code/artifact/c28d2dd1-5735-4dc9-9307-b1b87b51dc91) — phase 2 | 7 | 23 |
| [The Traffic Layer](https://claude.ai/code/artifact/fb4c2c7d-6646-44ed-b7a5-1409b6038962) — phase 6 | 2 | 6 |

Each sheet is every note for that phase in reading order, with the cards folded in and the phase's reading list at the end. Reviewed marks are saved per browser. Phases 0, 3, 4, 5, 7 and the capstone get a sheet the first time they have notes.

## Simulations — production, not recognition

| Sheet | What it is | Use it |
|---|---|---|
| [The Build Bench](https://claude.ai/code/artifact/674ef97b-db8f-46c9-9050-06b83ba95e7b) | 8 client briefs, one per phase. Place parts into 6 layers, submit for design review, get stamped. Traps for the microservices reflex, the premature shard, the gateway with business logic. | One evening a week, ~15 min |
| [Year One at Ledgerly](https://claude.ai/code/artifact/6f151972-b169-4e67-8676-ef1f3d243b5c) | 17 decisions across 4 quarters as founding architect. Choices carry forward — the tenancy model you pick in week 5 is what an auditor attacks in Q3. | Sunday, ~10 min |

## The loop

- **Mon–Thu** — 45 min of reading (books for judgment) or video (video for tools); paste raw notes into the phase's `_inbox.md`. No filing decisions mid-study.
- **When the inbox fills** — ask Claude to distribute it. Notes become concept files *and* get merged into the phase sheet, republished at the same link.
- **One evening** — a Build Bench commission for the phase you are in. A rejected review is your reading list.
- **Sunday, 20 min** — open the phase sheet, write a concept from memory, then reveal its cards and diff.
- **Sunday, 10 min** — play Year One. The principles it says you paid for go on next week's list.
- **Per phase** — re-mark the Atlas, and write the phase's artifact into `deliverables/`. Still amber means over-study it.

## The thing that actually compounds

The capstone starts in **week 3**, not month 6. Every phase feeds it — see the week table in `progress-checklist.md`. If you already have a real product in flight, use that; the "simulate year two" exercises come free with it.

See also: [[study-system]] for the sparring-partner prompts and per-phase practice, [[deliverables/deliverables]] for the written artifacts each phase owes you.
