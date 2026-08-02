---
tags: [databases, relational, sql, acid]
cards-deck: SaaS Architect::Phase 2::Relational Databases
---
# Relational Databases

Data is organized into **tables**: rows represent unique records identified by **primary keys**, and relationships between records are defined through columns. The **schema is predefined**, enabling robust querying with SQL.

## Advantages

- **Complex querying** — SQL powers sophisticated data insights
- **Efficient storage** — relationships between tables reduce data duplication
- **User-friendly structure** — tabular format is intuitive
- **ACID transactions** — data integrity during operations, essential for reliability

What 4 properties does ACID stand for? #card
Atomicity, Consistency, Isolation, Durability

## Disadvantages

- **Rigid schema** — schema changes require downtime, complicating maintenance
- **Complexity and cost** — supporting SQL + ACID raises maintenance costs
- **Slower read operations** — reads can be slower than non-relational databases

Your schema changes weekly and you need high-speed reads at massive scale. What are the 2 main pain points of a relational DB here? #card
Rigid schema (changes need downtime) + slower reads than non-relational databases

## Practical Example

An online store manages product and order data efficiently: products and orders are stored once and linked via relationships (columns), avoiding redundancy.

An online store stores products and orders. Why does the relational model avoid redundancy? #card
Relationships between tables via columns let you store each record once and reference it, instead of duplicating it

## When to Choose

Relational databases fit scenarios needing **complex queries** and **ACID guarantees**. When relationships are minimal or read performance is critical, consider alternatives.

You need to enforce data integrity across multi-step money transfers and run complex analytical queries. Which database family, and which 2 properties make it the fit? #card
Relational — ACID transactions for integrity + SQL for complex querying

## Related

- [[concepts/phase 2 - data/non-relational-databases]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
