---
tags: [architecture, requirements]
cards-deck: SaaS Architect::Phase 1::Architectural Drivers
---
# Architectural Drivers

The user doesn't always know exactly what they need — but they know the problem. Gathering requirements early is critical because the cost of change grows over time.

## Three Categories of Requirements

- **Functional/Feature requirements** — describe what the system does. They do NOT determine the architecture.
- **Quality Attributes (Non-functional)** — system properties (scalability, availability, performance) that dictate the architecture.
- **System Constraints** — boundaries the system must operate within.

You're in a design meeting. The PM lists features, the CTO asks "what determines the architecture?" Which requirement type dictates architecture? #card
Non-functional requirements / Quality Attributes

## System Constraints

- **Technical** — must use a specific framework, on-premise vs cloud
- **Business** — limited budget, strict deadlines, 3rd-party integrations
- **Regulatory/Legal** — HIPAA, GDPR, SOC 2

Your startup has a strict budget, must use AWS, and handles EU user data. What three constraint types are you facing? #card
Business (budget), Technical (AWS), Regulatory (GDPR)

A PM wants to change a core feature after 6 months of dev. Why is this costly? #card
Cost of change grows over time — late requirement changes cost more in time, money, and reputation

Some constraints have room for negotiation, others don't. Use loosely-coupled architecture so future changes don't require rewriting everything.

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
