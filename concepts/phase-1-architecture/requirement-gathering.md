---
tags: [requirements, uml, process]
cards-deck: SaaS Architect::Phase 1::Requirements
---
# Requirement Gathering Methods

## Use Cases & User Flows

Use Cases describe a situation/scenario in which the system is used. User Flows are step-by-step/graphical presentations of each use case.

### Three Steps

1. Identify all actors/users in the system
2. Capture and describe all possible use cases/scenarios
3. Create user flows — expand each use case through a flow of events (each event contains action + data)

You're designing a login system. Walk through the 3 steps to capture requirements via use cases. #card
1) Identify actors (users, admins), 2) Capture use cases (login, reset password), 3) Create user flows with action + data per step

During API design, your colleague says "I'm not sure which endpoints we need." What earlier artifact would have this mapped out? #card
User flows — each action maps to an API call

## UML Sequence Diagram

A diagram representing interactions between actors and objects (entities). Part of UML.

Your team needs to visualize how a user and the database interact over time during checkout. Which UML diagram? #card
Sequence Diagram

![[concepts/phase-1-architecture/diagrams/uml-sequence-diagram.excalidraw]]

![[concepts/phase-1-architecture/images/Pasted image 20260720211523.png]]
![[concepts/phase-1-architecture/images/Pasted image 20260720211652.png]]
![[concepts/phase-1-architecture/images/Pasted image 20260720211712.png]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
