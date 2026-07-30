---
tags: [load-balancing, scalability, availability, infrastructure]
cards-deck: SaaS Architect::Phase 6::Load Balancers
---
# Load Balancers

Distribute traffic evenly across servers to prevent overload and maintain system integrity.

## Quality Attributes Enabled

- **High Scalability** — horizontal scaling: add/remove servers based on load
- **High Availability** — health monitoring, route only to operational servers
- **Performance** — slight latency increase but massive throughput gain
- **Maintainability** — rolling updates: take servers offline one at a time

Traffic spikes and one server dies. Users report errors. What pattern solves both problems, and which two features? #card
Load Balancer — horizontal scaling (add servers for spikes) + health checks (route around dead servers)

You need to deploy a new version without downtime. How does a load balancer help? #card
Rolling updates — take servers offline one at a time while LB routes traffic to healthy ones

## Types of Load Balancing

- **DNS Load Balancing** — basic, no health monitoring, no security
- **Hardware/Software LB** — active health monitoring, intelligent routing, hides backend topology
- **Global Server LB (GSLB)** — DNS + intelligent routing by user location + health, enables disaster recovery

Your European users experience high latency hitting US servers. What LB type fixes this? #card
Global Server LB (GSLB) — routes by user geography + server health

![[concepts/phase 6 - scalability/diagrams/load-balancer-architecture.excalidraw]]

## Solutions

**Open Source:** HAProxy, NGINX

**Cloud:** AWS ELB (Application, Network, Gateway, Classic), GCP Cloud Load Balancing, Azure Load Balancer (Standard, Gateway, Basic)

**GSLB:** AWS Route 53, AWS Global Accelerator, GCP Cloud DNS, Azure Traffic Manager

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
