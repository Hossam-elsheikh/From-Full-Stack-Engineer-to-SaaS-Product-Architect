---
tags: [cdn, performance, caching, delivery]
cards-deck: SaaS Architect::Phase 6::CDN
---
# Content Delivery Networks (CDNs)

Reduce latency caused by physical distance between users and servers by caching content on **edge servers** closer to users.

## Benefits

- Reduced latency and faster load times
- Improved availability (distributed traffic)
- DDoS protection (absorb attack traffic at the edge)

## Integration Strategies

| Strategy | How it Works | Pros | Cons |
|----------|-------------|------|------|
| **Pull** | CDN fetches content from origin as needed. Configure cache TTL | Easy maintenance | First request slower for uncached content |
| **Push** | Upload content to CDN proactively | Users always get latest version | More active management required |

Your video platform users in Asia experience 3s load times because the server is in Virginia. What fixes this? #card
CDN — cache content on edge servers geographically closer to users

Your marketing site content rarely changes. You want minimal maintenance. Pull or Push? #card
Pull — CDN fetches on cache miss; easy to maintain with TTL configuration

Your pricing page must update instantly worldwide after a product launch. Pull or Push? #card
Push — proactively upload new content to CDN so users always get the latest version

## Solutions

**Providers:** Cloudflare, Fastly, Akamai, Amazon CloudFront, GCP CDN, Azure CDN

![[concepts/phase-6-scale/diagrams/cdn-flow.excalidraw]]

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
