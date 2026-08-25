---
tags: [eda, events, event-sourcing, async, messaging]
cards-deck: SaaS Architect::Phase 1::Event-Driven Architecture
---
# Event-Driven Architecture (EDA)

Services communicate through **events** — immutable statements of change — instead of direct API calls.

## Components

- **Event emitters (producers)** — publish events
- **Event consumers** — react to events
- **Event channel (message broker)** — routes events between them

What are the 3 components of event-driven architecture? #card
Producers (emitters), consumers, and an event channel (message broker)

## Benefits

- **Decoupling services** — enhanced scalability and flexibility; e.g., a banking front-end emits user-action events while the account service consumes them without direct interconnection
- **Easier integration** — new services (mobile notifications, fraud detection) subscribe without touching existing services
- **Real-time data processing** — immediate response to event-stream patterns, critical for fraud detection

A banking app needs to add fraud detection and push notifications without modifying the account service. Which architecture enables this? #card
Event-driven — new consumers subscribe to existing event streams

Why are events called "immutable statements of change"? #card
They represent facts that already happened — they are never overwritten or mutated like state

## Architectural Patterns

- **Event Sourcing** — store events instead of current state; replay them to reconstruct past states → solid audit trail, simpler error handling
- **CQRS (Command Query Responsibility Segregation)** — separates read and write operations into different services, optimizing each

You need a full audit trail and the ability to reconstruct past states. Which pattern stores events instead of current state? #card
Event Sourcing — replay stored events to rebuild state

![[concepts/phase-1-architecture/diagrams/event-driven-architecture.excalidraw]]

## Related

- [[concepts/phase-1-architecture/cqrs]]
- [[concepts/phase-1-architecture/message-brokers]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
