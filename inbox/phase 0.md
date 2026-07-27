
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