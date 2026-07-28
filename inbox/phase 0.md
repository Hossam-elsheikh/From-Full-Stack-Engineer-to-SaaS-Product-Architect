
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

# vital role of load balancers in software architecture for large-scale systems. 
Here are the main points:

1. **Purpose of Load Balancers**: They help distribute traffic evenly among multiple servers, preventing overload and maintaining system integrity, which is essential for achieving high availability and horizontal scalability.
    
2. **Key Quality Attributes**:
    
    - **High Scalability**: Load balancers allow for horizontal scaling by adding or removing servers based on current load, which is especially useful in cloud environments with auto-scaling features.
    - **High Availability**: They monitor the health of servers, ensuring that traffic is directed only to operational servers for efficient request handling.
    - **Performance**: Although there's a slight increase in latency, load balancers improve throughput by enabling numerous backend servers to handle requests simultaneously.
    - **Maintainability**: They support rolling updates, allowing servers to be taken offline one at a time for maintenance without affecting overall availability.
3. **Types of Load Balancing Solutions**:
    
    - **DNS Load Balancing**: A basic method that distributes requests using DNS, but lacks health monitoring and security.
    - **Hardware and Software Load Balancers**: Actively monitor server health and distribute load intelligently, hiding server details from clients for better security.
    - **Global Server Load Balancer (GSLB)**: Combines DNS functionality with intelligent routing based on user location and server health, optimizing performance and enabling disaster recovery.

### **Open Source Software Load Balancing Solutions**

#### [HAProxy](http://www.haproxy.org/)

HAProxy is a free and open-source, reliable, high performance TCP/HTTP load balancer.  
It is particularly suited for very high traffic web sites, and powers a significant portion of the world's most visited ones. It is considered the de-facto standard open-source load balancer, and is  shipped with most mainstream Linux distributions.  
HAProxy supports most Unix style operating systems.

#### [NGINX](https://www.nginx.com/)

NGINX is a free, open-source, high-performance HTTP server and reverse proxy (load balancer). It is known for its high performance, stability, rich feature set and simple configuration.  
For a full tutorial on how to install, configure and use NGINX follow this [link](https://www.nginx.com/resources/wiki/start/).
#### **Cloud Based Load Balancing Solutions  
**[AWS - Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/)

Amazon ELB is a highly scalable load balancing solution.

It is an ideal solution for running on AWS, and integrates seamlessly with all of AWS services.

It can operate on 4 different modes:

1. [Application (Layer 7) Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/?nc=sn&loc=2&dn=2) - Ideal for advanced load balancing of HTTP and HTTPS traffic
    
2. [Network (Layer 4) Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/?nc=sn&loc=2&dn=3) - Ideal for load balancing of both TCP and UDP traffic
    
3. [Gateway Load Balancer](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/) - Ideal for deploying, scaling, and managing your third-party virtual appliances.
    
4. [Classic Load Balancer](https://aws.amazon.com/elasticloadbalancing/classic-load-balancer/?nc=sn&loc=2&dn=5) (Layer 4 and 7) - Ideal for routing traffic to EC2 instances.
    

For the full documentation on Amazon ELB and its autoscaling policies follow this [link](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)

#### [GCP - Cloud Load Balancing](https://cloud.google.com/load-balancing)

Google Cloud Platform Load Balancer is Google's highly scalable and robust load-balancing solution.

"Cloud Load Balancing allows you to put your resources behind a single IP address that is externally accessible or internal to your Virtual Private Cloud (VPC) network".

Some of the load balancer types available as part of the [GCP Cloud Load Balancing](https://cloud.google.com/load-balancing/docs) are:

1. [External HTTP(S) Load Balancer](https://cloud.google.com/load-balancing/docs/https) - Externally facing HTTP(s) (Layer 7) load balancer which enables you to run and scale your services behind an internal IP address.
    
2. [Internal HTTP(S) Load Balancer](https://cloud.google.com/load-balancing/docs/l7-internal) - Internal Layer 7 load balancer that enables you to run and scale your services behind an internal IP address.
    
3. E[xternal TCP/UDP Network Load Balancer](https://cloud.google.com/load-balancing/docs/network) - Externally facing TCP/UDP (Layer 4) load balancer
    
4. [Internal TCP/UDP Load Balancer](https://cloud.google.com/load-balancing/docs/internal) - Internally facing TCP/UDP (Layer 4) load balancer.
    

#### [Microsoft Azure Load Balancer](https://azure.microsoft.com/en-us/services/load-balancer/)

Microsoft Azure load balancing solution provides 3 different types of load balancers:

1. [Standard Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview) - Public and internal Layer 4 load balancer
    
2. [Gateway Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/gateway-overview) - High performance and high availability load balancer for third-party Network Virtual Appliances.
    
3. [Basic Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/skus) - Ideal for small-scale application
    

#### **GSLB Solutions**

- [Amazon Route 53](https://aws.amazon.com/route53/) - Amazon Route 53 is a highly available and scalable cloud [Domain Name System (DNS)](https://aws.amazon.com/route53/what-is-dns/) web service.
    
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) -  A networking service that helps you improve the availability, performance, and security of your public applications.
    
- [Google Cloud Platform Load Balancer](https://cloud.google.com/load-balancing) & [Cloud DNS](https://cloud.google.com/dns) - Reliable, resilient, low-latency DNS serving from Google's worldwide network with everything you need to register, manage, and serve your domains.
    
- [Azure Traffic Manager](https://azure.microsoft.com/en-us/services/traffic-manager/) - DNS-based load balancing

# Message Brokers

play a vital role in asynchronous architectures. Here are the main points:

1. **Need for Message Brokers**: The lecture highlights the limitations of synchronous communication, where both sender and receiver must be active, which can complicate processes, especially during high traffic or long operation times.
    
2. **Use Case Illustration**: An example of a ticket reservation system is used to showcase issues like user frustration and potential system crashes when the front-end service has to wait for completion by the ticket service.
    
3. **Decoupling Sender and Receiver**: Message brokers enable asynchronous communication, allowing the sender to process messages without waiting for the receiver. This helps improve user experience by providing immediate acknowledgments.
    
4. **Queue Data Structure**: Messages are temporarily stored in queues, facilitating background processing and efficient operation handling.
    
5. **Functionalities Provided**: Message brokers offer message routing, transformation, validation, and load balancing, supporting the publish-subscribe pattern for event-driven architectures.
    
6. **Flexibility in Service Integration**: The design allows the addition of services (like analytics or notifications) without modifying existing architectures, making systems more adaptable to changes.
    
7. **Quality Attributes**: Key benefits of implementing message brokers include improved fault tolerance, high availability, scalability, and the ability to manage increased traffic loads, although it may introduce slight latency.
# **Message Brokers Solutions & Cloud Technologies**

#### **Open Source Message Brokers**

- [**Apache Kafka**](https://kafka.apache.org/) - The most popular open-source message broker nowadays. Apache Kafka is a distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.
    
- [**RabbitMQ**](https://www.rabbitmq.com/) **-** A widely deployed open-source message broker. It is used worldwide at small startups and large enterprises.
    

#### **Cloud Based Message Brokers**

- [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) - Fully managed message queuing service that enables you to decouple and scale micro-services, distributed systems, and serverless applications.
    
- GCP [Pub/Sub](https://cloud.google.com/pubsub/docs/overview) and [Cloud Tasks](https://cloud.google.com/tasks/docs/dual-overview) - Publisher/Subscriber and message queue solutions offered by Google Cloud Platform. See [this article](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-cloud-tasks) for comparison between the two offerings.
    
- **Microsoft Azure**:
    
    - [Service Bus](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) - Fully managed enterprise message broker with message queues and publish-subscribe topics.
        
    - [Event Hubs](https://azure.microsoft.com/en-us/products/event-hubs/) - Fully managed real-time data ingestion service. Allows streaming millions of events per second from any source. Integrates seamlessly with Apache Kafka clients without any code changes. A perfect solution for Big Data.
        
    - [Event Grid](https://azure.microsoft.com/en-us/products/event-grid/) - Reliable, serverless event delivery system at a massive scale. It uses the publish-subscribe model. It is Dynamically scalable, Low cost with a pay-as-you-go model, and guarantees "At least once delivery of an event"