---
tags: [eda, streaming, events, windowing, real-time]
cards-deck: SaaS Architect::Phase 1::Event Stream Processing
---
# Event Stream Processing (ESP)

Continuous, real-time processing of an **infinite stream of events** — analyzing events as they arrive rather than in delayed batches. Critical where insight must be immediate: anomaly detection, fraud detection, live metrics.

## Event Timings

Every event carries three distinct times:

- **Event time** — when the event actually occurred (recorded in the payload)
- **Application / arrival time** — when the event reaches the consumer application
- **Processing time** — when the system actually processes it

In distributed systems events arrive **late or out of order**, so these three diverge — which is why the distinction matters.

A fraud event happened at 12:00:00, reached your consumer at 12:00:09 and was processed at 12:00:11. Name the three timestamps. #card
Event time (12:00:00), application/arrival time (12:00:09), processing time (12:00:11)

Why can't you just use processing time for stream analytics? #card
Events arrive late and out of order in distributed systems — processing time would attribute an event to the wrong period

## Windowing

An infinite stream can't be analyzed as a whole, so ESP cuts it into finite **windows**.

| Strategy | How it works | Trade-off |
|----------|-------------|-----------|
| **Tumbling** | Fixed, non-overlapping intervals; every event belongs to exactly one window | Simple and cheap; results only at the end of each interval |
| **Hopping** | Window duration + **advance interval**; windows overlap, so an event can appear in several | Frequent, near real-time results; more memory, CPU and network |

With a one-hour window and a one-minute advance interval, results are produced every minute over the last hour — continuous monitoring instead of hourly jumps.

You need the hourly error rate refreshed every minute. Which windowing strategy, and with what parameters? #card
Hopping window — one-hour window duration with a one-minute advance interval

You want each event counted exactly once, in simple fixed buckets. Which windowing strategy? #card
Tumbling window — fixed, non-overlapping intervals

Your hopping windows are eating memory and CPU. Why? #card
Overlapping windows must all be maintained simultaneously, and each produces results — costing memory, CPU and network

What happens when the advance interval is larger than the window duration? #card
Windows stop overlapping and start skipping data — effectively sampling. Useful for high-volume, low-variability streams

## Aggregation & Insights

A series of events reveals what a single event cannot. Fraud detection is the canonical case: one card transaction is unremarkable; two transactions in different countries minutes apart is a pattern.

One card transaction looks fine on its own, but the account is being defrauded. What does stream processing add? #card
Aggregation across a window — patterns across several events (e.g. impossible travel between transactions) that no single event reveals

## Related

- [[concepts/phase-1-architecture/event-driven-architecture]]
- [[concepts/phase-1-architecture/message-brokers]]
- [[concepts/phase-1-architecture/cqrs]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
