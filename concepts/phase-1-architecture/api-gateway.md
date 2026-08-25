---
tags: [api-gateway, microservices, architecture]
cards-deck: SaaS Architect::Phase 1::API Gateway
---
# API Gateway

A single entry point that manages complexity in large-scale systems with many services.

## What It Does

- **API Composition** — consolidates multiple APIs into one endpoint; changes don't impact consumers
- **Centralized Security** — auth/authz in one place, rate limiting to prevent DoS
- **Performance** — single client call instead of many; response caching
- **Monitoring & Alerting** — observability into traffic patterns and load
- **Protocol Translation** — connect systems using different protocols

Your 15 microservices require every client to handle auth, rate limiting, and service discovery. What solves this? #card
API Gateway — single entry point centralizing auth, routing, rate limiting, and monitoring

## Anti-patterns & Risks

- Don't put **business logic** in the gateway (returns to monolith)
- Risk of **single point of failure** — deploy multiple instances
- Avoid over-optimization that bypasses the gateway's decoupling purpose

A junior dev adds discount calculation logic to the API Gateway. What's the problem? #card
Anti-pattern: business logic in the gateway turns it into a monolith and a single point of failure

## Solutions

**Open Source:** Netflix Zuul

**Cloud:** AWS API Gateway, GCP API Gateway + Apigee, Azure API Management

![[concepts/phase-1-architecture/diagrams/api-gateway-pattern.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
