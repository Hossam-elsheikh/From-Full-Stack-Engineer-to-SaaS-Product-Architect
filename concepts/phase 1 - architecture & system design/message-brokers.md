---
tags: [messaging, async, queue, pub-sub, events]
cards-deck: SaaS Architect::Phase 1::Message Brokers
---
# Message Brokers

Enable asynchronous communication by decoupling sender and receiver.

## Why Use a Message Broker

Synchronous communication requires both parties to be active simultaneously. This causes:
- User frustration (blocking waits)
- System crashes under high traffic
- Tight coupling between services

Message brokers solve this by allowing the sender to process without waiting for the receiver.

Your order service calls payment + notification synchronously. During a flash sale, payments slow down and orders queue up. What pattern, and how does it help? #card
Message Broker — decouples sender from receiver so the order service doesn't block waiting for slow dependencies

## How It Works

Messages are temporarily stored in **queues**, enabling background processing. The broker provides:
- **Message routing** — direct messages to correct consumers
- **Transformation** — convert message formats
- **Validation** — ensure message integrity
- **Load balancing** — distribute messages across consumers
- **Pub/Sub** — event-driven architecture support

A new analytics team wants to consume order events without modifying the order service. How? #card
Pub/Sub via message broker — add a new subscriber without changing the producer

## Quality Attributes

- Fault tolerance
- High availability
- Scalability
- Trade-off: slight added latency

## Solutions

**Open Source:** Apache Kafka (distributed event streaming, high throughput), RabbitMQ

**Cloud:** AWS SQS, GCP Pub/Sub + Cloud Tasks, Azure Service Bus + Event Hubs + Event Grid

You need a high-throughput event stream for real-time analytics across 50 microservices. Kafka or RabbitMQ? #card
Apache Kafka — built for distributed event streaming at scale

![[concepts/phase 1 - architecture & system design/diagrams/message-broker-pattern.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
