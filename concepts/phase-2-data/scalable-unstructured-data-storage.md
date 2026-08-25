---
tags: [storage, object-stores, distributed-filesystems, s3]
cards-deck: SaaS Architect::Phase 2::Unstructured Data Storage
---
# Scalable Unstructured Data Storage

## Workloads

1. **User data uploads** — images, videos for sharing or backup
2. **Database backup & archiving** — snapshots for disaster recovery and legal purposes
3. **Web hosting** — media content delivery
4. **Analytics & machine learning** — sensor data, images at scale

Name the 4 categories of unstructured-data workloads. #card
User uploads, DB backups/archives, web hosting, analytics/ML

## Two Solutions

### Distributed File Systems
- Data stored across a network, resembling a local file system
- Efficient modifications, high-performance operations
- Limits: scalability issues with a very large number of files; no easy web API access

### Object Stores
- Built for **internet-scale** storage of binary objects with large file sizes
- Easy **HTTP REST APIs** for web content
- Support **versioning**
- Limits: objects are **immutable**; special APIs for data access

Users upload millions of large images you serve over the web. Which storage type, and which 2 features make it the fit? #card
Object store — internet-scale binary objects + easy HTTP REST APIs (e.g., S3)

You need to run a compute job doing high-throughput file modifications on a small set of files. Which storage type performs better? #card
Distributed file system — efficient modifications + high-performance operations

Why do object stores support versioning but not in-place edits? #card
Objects are immutable — a new version replaces the old one via a special API

## Rule of Thumb

Distributed file systems excel at **high-throughput operations**; object stores excel at **web content and scalability**.

## Solutions

**Cloud object stores:** AWS S3, GCP Cloud Storage, Azure Blob Storage, Alibaba Cloud OSS

**Open source (S3-compatible):** MinIO, Ceph, OpenIO

You need S3-compatible object storage you can run on your own Kubernetes cluster. Which open-source options? #card
MinIO, Ceph, OpenIO

## Source

Udemy: *Software Architecture & Design of Modern Large Scale Systems* — Michael Pogrebinsky
