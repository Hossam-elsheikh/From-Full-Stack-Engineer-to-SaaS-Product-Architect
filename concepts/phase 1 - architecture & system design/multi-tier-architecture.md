---
tags: [architecture, multi-tier, scaling, monolith]
cards-deck: SaaS Architect::Phase 1::Multi-Tier Architecture
---
# Multi-Tier Architecture

Organizes a system into **tiers** — each tier runs on its own infrastructure. Multi-Tier (separate infrastructure) is often confused with Multi-Layer (internal separation within one application).

## Three-Tier Architecture

- **Presentation Tier** — handles user interaction; exposes no business logic
- **Application Tier** — processes data and contains business logic
- **Data Tier** — manages data storage and persistence

Your team says "we split controllers from services so we're multi-tier." Why is that actually multi-layer? #card
Multi-layer = internal separation within one application; multi-tier = separate infrastructure per tier

## Benefits

- Versatile for web-based services
- Facilitates horizontal scaling (scale the Application tier independently)
- Simplifies maintenance by centralizing business logic

## Drawbacks

- The Application tier can become **monolithic** — performance issues and slower development as the codebase grows

Your three-tier app's Application tier has grown into a huge codebase and deploys are slow. What's the known failure mode? #card
The Application tier becomes monolithic, hurting performance and slowing development

## Variants

- **Two-Tier** — merges Presentation and Application tiers
- **Four-Tier** — adds a tier for API management

Which tier must never expose business logic? #card
The Presentation tier — it only handles user interaction

![[concepts/phase 1 - architecture & system design/diagrams/three-tier-architecture.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
