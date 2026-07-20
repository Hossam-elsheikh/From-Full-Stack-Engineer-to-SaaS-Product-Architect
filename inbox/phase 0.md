
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
