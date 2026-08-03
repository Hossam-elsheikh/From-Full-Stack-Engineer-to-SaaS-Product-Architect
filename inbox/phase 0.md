---
tags: [inbox, phase-0, map]
---
# Phase 0 — Inbox (Processed)

Content distributed to concept notes below.

## Concept Notes Created
| Topic | File | With Flashcards | With Diagram |
|-------|------|:-:|:-:|
| Architectural Drivers | [[concepts/phase 1 - architecture & system design/architectural-drivers]] | ✅ | — |
| Requirement Gathering | [[concepts/phase 1 - architecture & system design/requirement-gathering]] | ✅ | ✅ |
| Quality Attributes | [[concepts/phase 1 - architecture & system design/quality-attributes]] | ✅ | ✅ |
| API Design (REST, RPC, gRPC) | [[concepts/phase 1 - architecture & system design/api-design]] | ✅ | ✅ |
| Load Balancers | [[concepts/phase 6 - scalability/load-balancers]] | ✅ | ✅ |
| Message Brokers | [[concepts/phase 1 - architecture & system design/message-brokers]] | ✅ | ✅ |
| API Gateway | [[concepts/phase 1 - architecture & system design/api-gateway]] | ✅ | ✅ |
| Content Delivery Networks | [[concepts/phase 6 - scalability/content-delivery-networks]] | ✅ | ✅ |
| Multi-Tier Architecture | [[concepts/phase 1 - architecture & system design/multi-tier-architecture]] | ✅ | ✅ |
| Microservices Architecture | [[concepts/phase 1 - architecture & system design/microservices]] | ✅ | ✅ |
| Event-Driven Architecture | [[concepts/phase 1 - architecture & system design/event-driven-architecture]] | ✅ | ✅ |
| CQRS | [[concepts/phase 1 - architecture & system design/cqrs]] | ✅ | ✅ |
| Relational Databases | [[concepts/phase 2 - data/relational-databases]] | ✅ | — |
| Non-relational Databases | [[concepts/phase 2 - data/non-relational-databases]] | ✅ | — |
| Database Indexing | [[concepts/phase 2 - data/database-indexing]] | ✅ | — |
| Database Replication | [[concepts/phase 2 - data/database-replication]] | ✅ | ✅ |
| Database Sharding | [[concepts/phase 2 - data/database-sharding]] | ✅ | ✅ |
| CAP Theorem | [[concepts/phase 2 - data/cap-theorem]] | ✅ | ✅ |
| Unstructured Data Storage | [[concepts/phase 2 - data/scalable-unstructured-data-storage]] | ✅ | — |

## Next Steps

- Start daily Anki review (open vault in Obsidian, click flashcard bolt icon)
- Weekly blank-page test: pick a concept, redraw its diagram from memory
- New raw notes go here first, distribute on Sunday



new content 


# Event stream processing (ESP)
Event stream processing (ESP) is a technology that allows for the continuous processing of data streams in real time. It involves handling and analyzing incoming events as they occur, which can be crucial for applications that require immediate insights and responses, such as anomaly detection or fraud detection.

Here are key components and concepts in event stream processing:

1. **Event Timings**: Every event has distinct timestamps:
    
    - **Event Time**: When the event occurred (recorded in the event’s payload).
    - **Application Time/Arrival Time**: When the event arrives at the consumer application.
    - **Processing Time**: When the event is processed by the system.
    
    Understanding these timestamps helps manage scenarios where events can arrive late or out of order, which is common in distributed systems.
    
2. **Windowing**: Since it's not feasible to analyze an infinite stream of events, ESP uses windowing techniques to process finite subsets of data. Common strategies include:
    
    - **Tumbling Windows**: Time is divided into fixed, non-overlapping intervals, with each event assigned to one window. This approach allows for manageable chunks of data to be analyzed almost in real-time.
3. **Aggregation and Insights**: Analyzing a series of events can provide meaningful insights that individual events may not offer. For instance, fraud detection systems can look at patterns across several events, such as a user’s transactions happening in different locations in a short time span.
    

Event stream processing is particularly beneficial in microservices architectures and big data pipelines, where the volume and velocity of incoming events demand immediate processing capabilities. By implementing ESP, systems can react to events as they happen, rather than relying on delayed processing which may not capture relevant information in time.

he hopping window event-stream processing strategy is introduced as a way to enhance the analysis of infinite streams of events by addressing some limitations of the tumbling window strategy.

# The hopping window concept:

1. **Overlapping Intervals**: Unlike the tumbling window, which divides time into fixed, non-overlapping intervals, the hopping window allows for overlapping time intervals. This means that multiple windows can contain the same event, leading to more detailed analysis.
    
2. **Advance Interval**: The hopping window is defined by both a window duration and an advance interval. The advance interval determines how often the window "hops" forward. This interval can be smaller, equal to, or larger than the window duration.
    
    - For effective use, the advance interval is often set smaller than the window duration. For example, with a one-hour window and a one-minute advance interval, results can be generated every minute, providing timely insights and allowing continuous monitoring.
3. **Real-Time Applications**: The lecture emphasizes practical applications, such as in stock trading, where metrics like averages and trends can be updated every few seconds. This rapid updating aids in quicker decision-making. Similarly, for system logs, metrics like the hourly error rate can be refreshed every minute to detect issues more swiftly.
    
4. **Trade-offs**: While hopping windows increase result frequency, they also require more memory and CPU power, as multiple overlapping windows need to be maintained. Additionally, this can lead to higher network resource consumption due to the increased amount of result data generated.
    
5. **Larger Advance Interval Option**: The hopping window can also be configured with an advance interval larger than the window size, effectively reverting to a strategy similar to the tumbling window. This can be useful for processing large data volumes with low variability, as it allows for sampling while ignoring less critical data.
    

Overall, the hopping window strategy is a powerful tool for achieving near real-time analytics and improving data-driven decision-making.