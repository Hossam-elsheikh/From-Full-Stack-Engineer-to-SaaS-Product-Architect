---
tags: [api, rest, rpc, grpc, design]
cards-deck: SaaS Architect::Phase 1::API Design
---
# API Design

APIs serve as contracts between engineers and client applications.

## API Types

- **Public** — open to any developer
- **Private** — internal use within organizations
- **Partner** — available to specific partners under agreements

Your startup builds a payment API. Banks get special terms, internal microservices use it, and any dev can try it. Which API type for each? #card
Partner (banks), Private (internal), Public (open developers)

## Best Practices

- **Encapsulation** — clients shouldn't need to understand internals
- **User-friendliness** — intuitive naming, consistent structure
- **Idempotent operations** — repeated requests don't cause unintended outcomes
- **Pagination** — manage large datasets via segments
- **Asynchronous APIs** — for long-running operations, immediate feedback
- **Versioning** — manage changes smoothly

A user clicks "place order" twice and gets charged twice. Which design practice was violated? #card
Idempotency — repeated requests should produce the same result

Your API returns 10k records and times out. What pattern fixes this? #card
Pagination — return data in smaller segments

## Remote Procedure Calls (RPC)

Makes remote method calls feel local. Uses an Interface Description Language (IDL).

- **Server stub** — listens for client messages
- **Client stub** — handles serialization and communication
- **DTOs** — generated from IDL types

Your backend service needs fast, typed, bidirectional calls to another service. REST or RPC? #card
RPC (specifically gRPC with HTTP/2 + Protocol Buffers)

### gRPC

Modern high-performance RPC by Google (2015).
- **Transport**: HTTP/2
- **IDL**: Protocol Buffers

What transport protocol and IDL does gRPC use? #card
HTTP/2 as transport, Protocol Buffers as Interface Description Language

## REST (Representational State Transfer)

Resource-oriented architecture using HTTP.
- Resources identified by URIs, hierarchical structure
- **Stateless** — enhances scalability
- **Cacheable** — clients store responses to reduce server load
- Operations: POST (create), PUT (update), DELETE, GET (retrieve)

3rd-party developers need a public API to access your platform. REST or gRPC? #card
REST — resource-oriented, cacheable, stateless, widely adopted for public APIs

![[concepts/phase-1-architecture/diagrams/rest-vs-rpc-decision.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
