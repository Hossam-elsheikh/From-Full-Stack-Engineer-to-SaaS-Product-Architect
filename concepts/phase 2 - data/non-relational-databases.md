---
tags: [databases, nosql, key-value, document, graph]
cards-deck: SaaS Architect::Phase 2::Non-relational Databases
---
# Non-relational Databases (NoSQL)

Emerged in the **mid-2000s** to address the limitations of relational databases.

## What Makes Them Different

- **Flexible schemas** — records can have different structures; no uniform schema or downtime to add new data types
- **Native data structures** — lists, arrays, maps align with programming languages and reduce reliance on ORMs
- **Faster queries** for specific use cases, but data analysis is harder without enforced relationships

Why do NoSQL databases reduce reliance on ORMs? #card
They store data in structures (lists, arrays, maps) that map directly to programming-language constructs

## Types

| Type | Strength | Typical Use |
|------|----------|-------------|
| **Key/Value** | Fast lookup by unique key | Caching, simple data retrieval |
| **Document** | JSON/XML documents map to programming constructs | Complex/nested data, profiles |
| **Graph** | Manages relationships between records | Fraud detection, recommendations |

You need a cache keyed by token, a store for user profiles as JSON docs, and a friend-recommendation engine. Which 3 NoSQL types? #card
Key/Value, Document, Graph

## Use Cases & Trade-offs

Beneficial for **unstructured data**, **real-time big data processing**, and **caching**. Traditional applications may still prefer relational for reliability and simplicity.

Your NoSQL model has no enforced relationships and records can differ. What's the cost? #card
Complex data analysis — no guaranteed structure or enforced relationships

## Related

- [[concepts/phase 2 - data/relational-databases]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
