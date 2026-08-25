---
tags: [architecture, streaming, batch, lambda, kappa, data-pipeline]
cards-deck: SaaS Architect::Phase 1::Lambda & Kappa Architecture
---
# Lambda & Kappa Architecture

Two answers to one tension: you want **complete, accurate results over all history**, and you want **an answer about what happened three seconds ago**. A single pipeline optimised for one is bad at the other. Lambda runs both and merges; Kappa argues you no longer need to.

## The two processing styles

| | Batch processing | Stream processing |
|---|---|---|
| **Input** | A bounded dataset already at rest (HDFS, S3) | An unbounded stream off a broker (Kafka, Kinesis) |
| **Cadence** | Recomputed from scratch on a schedule | Incrementally, as events arrive |
| **Strength** | Accurate, complete, **replayable** — fix the logic, rerun over immutable raw data | Millisecond-to-second latency; you react while the event still matters |
| **Weakness** | Latency — a terabyte scan takes minutes to hours, so your view is always one window stale | Approximation — limited memory, out-of-order arrivals, sketches (HyperLogLog, Count-Min), and no easy "un-process" |

Your nightly job produced a wrong number because the logic had a bug. Why is this recoverable in a batch pipeline but painful in a streaming one? #card
Batch keeps the immutable master dataset — fix the code and rerun, and the output is correct. A stream processed each event once in flight, so there is nothing to recompute from unless the log itself is retained.

## Lambda architecture

Nathan Marz's answer: **don't choose — run both, and merge at read time.** The same raw event stream is fanned out to two independent pipelines.

| | Batch layer | Speed layer |
|---|---|---|
| Input | Immutable master dataset | Live stream |
| Output | Batch views (complete, correct) | Real-time views (recent, approximate) |
| Covers | Everything up to the last run | Only the gap since the last batch run |
| Role | Source of truth | Stopgap |

The **serving layer** answers a query by combining the two: the authoritative batch view, plus the real-time view covering the window batch has not caught up on. Once a batch run covers that window, the corresponding real-time view is discarded.

Lambda's speed layer uses approximations. Why is that acceptable? #card
Its errors are transient — every real-time view is eventually overwritten by a correct batch view covering the same window. That is the central elegance of the design.

Which layer in a Lambda architecture is the source of truth, and which is the stopgap? #card
The batch layer is the source of truth; the speed layer only covers the gap since the last batch run.

## The canonical example — ad tech

The impression funnel (**see → click → purchase**) forks every event:

- **Batch path** — events land as immutable raw logs; a periodic job recomputes advertiser billing, conversion attribution, campaign ROI and audience segments. These must be *exactly* right: you are invoicing real money and a miscount is a legal problem.
- **Speed path** — events hit a broker and become live views: current click-through rate, remaining campaign budget, whether to keep serving this creative. An ad exchange has ~100 ms to decide whether to bid. It cannot wait for last night's batch.

Why is ad tech the textbook Lambda case? #card
It has both requirements at maximum intensity in the same system — sub-second bidding decisions *and* audit-grade financial reporting over billions of events.

## What Lambda costs

1. **Duplicate business logic.** Sessionization, attribution, fraud filtering — implemented twice, in two frameworks with different programming models. Every requirement change is a two-sided change.
2. **Divergence bugs.** The implementations drift. Batch says 4.1% CTR, stream says 4.4%, and you are now debugging across two stacks to find which is lying.
3. **Operational weight.** Two clusters, two pipelines, two monitoring setups, plus a non-trivial serving layer that must merge views correctly.

Your batch and speed layers report different conversion numbers for the same hour. What kind of bug is this, and what caused it structurally? #card
A divergence bug — the inevitable consequence of implementing the same business logic twice in two frameworks. It is Lambda's main cost, not a one-off mistake.

## Kappa architecture — the reaction

Jay Kreps proposed dropping the batch layer entirely. Keep **the log itself as the immutable master dataset** with long retention, and "recompute" by replaying the stream from the beginning through a new version of the streaming job. One codebase, one framework. Event-time semantics, watermarks and exactly-once state make this viable in a way it was not in 2011 — Flink and Spark Structured Streaming now deliberately treat a batch as simply a bounded stream.

You need to recompute a metric after a logic fix, and you have no batch layer. How does Kappa handle it? #card
Replay the retained log from the beginning through the new version of the streaming job — the log *is* the master dataset.

## Practical takeaway

> Lambda is a pattern born from a historical constraint: early stream processors could not guarantee correctness.

Designing today, start **streaming-first (Kappa-style)** and add a separate batch path only for a concrete reason: regulatory reconciliation, backfills over data older than your log retention, or genuinely different algorithms for historical versus live computation.

You are designing a new analytics pipeline in 2026. Lambda or Kappa, and what would change your mind? #card
Start with Kappa — one codebase, one framework. Add a batch layer only for regulatory reconciliation, backfills older than log retention, or genuinely different historical-vs-live algorithms.

## Related

- [[concepts/phase-1-architecture/event-stream-processing]]
- [[concepts/phase-1-architecture/event-driven-architecture]]
- [[concepts/phase-1-architecture/message-brokers]]
- [[concepts/phase-1-architecture/cqrs]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
