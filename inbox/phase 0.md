
- The user doesn't always know what he need exactly, but he knows the problem he need to solve. (high level requirements)
- Gathering requirements from the beginning is important, cause there's a cost of change things later (costs changes, time, reputation ...etc)
# Requirements classification/Architectural drivers:
- Functional/Feature requirements are describing a feature or how the system operations work, it doesn't determine the architecture. 
- Quality Attributes / Non-functional requirements are system properties (scalability, availability, performance ...etc) which the system must have, i dictate the architecture of the system.
- System constraints (time, financial or staffing constraints)

# Methods of Gathering Requirements 
- Use Cases : situation/scenario in which our system is used
- User Flows : A step-by-step/graphical presentation of each use case
- ### steps 
  1- identify all the actors/users in our system.
  2- capture and describe all the possible use-cases/scenarios
  3- user flow - expand each use case through flow of events and each event contains action and data.
# Unified Modeling Language - Sequence Diagram
it's a diagram represents interactions between actors and objects (entities), it's a part of UML. 

a great side benefit of capturing the user flow is to help building the API, as every action representing an API call. 
![[Pasted image 20260720211523.png]]
![[Pasted image 20260720211652.png]]
![[Pasted image 20260720211712.png]]


# Quality Attributes - Non-functional requirements
systems are frequently redesigned not because of functional requirements, but because the system as it stands:
- isn't fast enough
- doesn't scale
- slow to develop
- hard to maintain
- not secure enough
```
No single software architecture can provide all the quality attributes!
certain quality attributes contradict with each other.
you've to make the right tradeoff
```


# System Constraints
types of constraints
- Technical constraints : having to use a particular framework, or using on-premise instead of cloud solutions.
- Business constraints : limited budget, strict deadlines, using 3rd party services or integrations with certain payments, this may drive the architecture and the implementation. 
- Regulatory/Legal constraints : HIPAA, GPDR ... etc
`there's some constraints have a room of nogtioation and other haven't`
`using loosly coupled architecture is good to do in case we're free from that constraint that we had before. i.e make sure that our system is not tightly coupled to a certain technology or APIs`



# Most Important Quality attributes 
## Performance
metrics : 
- response time = processing time + waiting time (latency)
- Throughput : amount of tasks(or data processed in bits/bytes/MGbytes)/second 
measuring response time : 
- percentile distributions and tail latency analysis instead of simple averages and median measurements 
- performance degradation - high resource utilization 

## Scalability 
1. **Vertical Scalability (Scaling Up)**: Upgrading existing resources on a single machine, like CPU or memory, to handle more load. This method is easy to implement but has limitations due to hardware constraints and can result in a centralized system with low availability and fault tolerance.
    
2. **Horizontal Scalability (Scaling Out)**: Adding more machines to distribute the load, which enhances performance and availability. While this method offers almost unlimited scaling potential, it adds complexity and may require significant code changes.
    
3. **Team Scalability**: Involves the productivity of development teams. As teams expand, productivity can increase initially but may decline due to coordination challenges. To counteract this, organizations can modularize codebases or adopt microservices for better team efficiency.

# Availability 
Availability% =  uptime / (uptime + Downtime) 
MTBF > mean time between failures (not considered in cloud services)
MTTR > mean time to recovery (average downtime of our system)
Availability = MTBF / (MTBF+MTTR)
## The nines 
99.9% 3 nines 
99.99% 4 nines

### Fault tolerance tactics 
- failure prevention (running on multiple servers)
time redundancy > running the request until succeed or give up
-active - active arch 
-active - passive arch 
- failure detection
-monitoring service send periodic health check messages
- recovery from failure 


SLA - service level agreement
SLOs - service level objectives 
SLIs - service level indicators 

Real World SLA Examples from the Industry

#### **Cloud Vendor SLA Examples**

- [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/?aws-sla-cards.sort-by=item.additionalFields.serviceNameLower&aws-sla-cards.sort-order=asc&awsf.tech-category-filter=*all)
- [Google Cloud Platform Service Level Agreements](https://cloud.google.com/terms/sla)
- [Microsoft Azure Service Level Agreement](https://azure.microsoft.com/en-us/support/legal/sla/)

#### **Other Examples**

- [GitHub Enterprise Service Level Agreement](https://github.com/customer-terms/github-online-services-sla)
- [Atlassian Products Service Level Agreement](https://support.atlassian.com/subscriptions-and-billing/docs/service-level-agreement-for-atlassian-cloud-products/)


1. **Importance of APIs**: APIs serve as contracts between engineers and client applications, facilitating communication between various systems.
    
2. **Types of APIs**:
    
    - **Public APIs**: Open to any developer.
    - **Private APIs**: Used internally within organizations.
    - **Partner APIs**: Available to specific business partners under agreements.
3. **Best Practices for API Design**:
    
    - **Encapsulation**: Clients should not need to understand the internal workings of the system.
    - **User-friendliness**: APIs should be intuitive, with clear naming and consistent structures.
    - **Idempotent Operations**: Ensures repeated requests do not cause unintended outcomes.
    - **Pagination**: Helps manage large datasets by allowing clients to request smaller data segments.
    - **Asynchronous APIs**: Suitable for long-running operations, allowing clients to receive immediate feedback.
    - **Versioning**: Essential for managing API changes and ensuring smooth transitions for clients.


# Remote Procedure Calls (RPC)
which enable client applications to execute subroutines on remote servers just as if they were local method calls. Here are the main points covered:

1. **Local Transparency**: Emphasizes that developers experience consistency in method invocation whether the call is local or remote.
    
2. **RPC Operation**: It explains how RPC functions, particularly the use of interface description languages for defining APIs and data types, and the subsequent generation of client and server stubs to manage remote communication.
    
3. **Key Components**:
    
    - **Server Stub**: Listens for client messages.
    - **Client Stub**: Handles data encoding (serialization) and initiates communication.
4. **Data Transfer Objects (DTOs)**: Generation from custom object types defined in the interface description language.
    
5. **Benefits of RPC**: Offers developers the convenience of abstracting network communication complexities, making method calls appear local.
    
6. **Drawbacks**: Addresses potential issues such as slower performance and unreliability due to network problems.
    
7. **Best Practices**: Suggests using asynchronous methods for long operations and ensuring idempotency to enhance reliability.
    
8. **When to Prefer RPC**: Discusses RPC's suitability for backend communications and scenarios needing network abstraction.

#### [**gRPC**](https://grpc.io/)

[_gRPC_](https://grpc.io/) is a modern open source high performance Remote Procedure Call (RPC) framework. It was originally developed by Google in 2015 as the next generation of its own internal RPC infrastructure.

It uses [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2) as its transport protocol and [Protocol Buffers](https://developers.google.com/protocol-buffers) as its **_Interface Description Language._**


# REST API
which stands for Representational State Transfer, an architectural style for designing web APIs. Here are the main points:

1. **Resource-Oriented Architecture**: Unlike RPC APIs, which focus on method-based interactions, REST APIs are designed around resources, allowing clients to interact with named resources through a limited set of operations.
    
2. **Use of HTTP**: REST APIs utilize HTTP for requesting resources, with the server responding with the current state of the requested resource.
    
3. **Statelessness**: REST's stateless nature enhances scalability, allowing for distribution of requests across multiple servers without retaining session information.
    
4. **Cacheability**: Clients can store responses to reduce server load, improving performance and availability.
    
5. **Hierarchical Resource Organization**: REST APIs use a hierarchical structure where each resource is identified by a unique URI, and resources can have sub-resources.
    
6. **Naming Conventions**: Best practices include using clear, meaningful resource names and ensuring their uniqueness.
    
7. **Limited Operations**: The primary operations in REST APIs—create, update, delete, and retrieve—correspond to HTTP methods: POST, PUT, DELETE, and GET.
    
8. **Implementation Example**: A step-by-step example of creating a REST API is provided, focusing on a movie streaming service, which involves identifying entities, mapping them to URIs, selecting representations (like JSON), and determining HTTP methods for resource manipulation.

