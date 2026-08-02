---
tags: [inbox, phase-0, map]
---
# Phase 0 — Inbox (Processed)

Content distributed to concept notes below.

## Concept Notes Created

| Topic | File | With Flashcards | With Diagram |
|-------|------|:-:|:-:|
| Architectural Drivers | [[concepts/phase 1 - architecture & system design/architectural-drivers]] | ✅ | — |
| Requirement Gathering | [[concepts/phase 1 - architecture & system design/requirement-gathering]] | ✅ | ✅ |
| Quality Attributes | [[concepts/phase 1 - architecture & system design/quality-attributes]] | ✅ | ✅ |
| API Design (REST, RPC, gRPC) | [[concepts/phase 1 - architecture & system design/api-design]] | ✅ | ✅ |
| Load Balancers | [[concepts/phase 6 - scalability/load-balancers]] | ✅ | ✅ |
| Message Brokers | [[concepts/phase 1 - architecture & system design/message-brokers]] | ✅ | ✅ |
| API Gateway | [[concepts/phase 1 - architecture & system design/api-gateway]] | ✅ | ✅ |
| Content Delivery Networks | [[concepts/phase 6 - scalability/content-delivery-networks]] | ✅ | ✅ |

## Next Steps

- Start daily Anki review (open vault in Obsidian, click flashcard bolt icon)
- Weekly blank-page test: pick a concept, redraw its diagram from memory
- New raw notes go here first, distribute on Sunday



new content : 

# Introduction to Relational Databases
 acknowledging the vast array of database options, emphasizing the careful selection of a database based on specific use cases.
    
2. **Core Structure**: Data is organized into tables with rows representing unique records identified by primary keys, and relationships between records are defined through columns. The schema is predefined, allowing for robust query capabilities using SQL, the industry standard for database interaction.
    
3. **Advantages**:
    
    - **Complex Querying**: SQL allows for sophisticated data insights.
    - **Efficient Storage**: Relationships between tables reduce data duplication.
    - **User-Friendly Structure**: The tabular format is intuitive and easy to understand.
    - **ACID Transactions**: Ensures data integrity during operations, which is essential for reliability.
4. **Practical Example**: An online store is used to demonstrate how relational databases can manage product and order data efficiently without redundancy.
    
5. **Disadvantages**:
    
    - **Rigid Schema**: Changes to the schema require downtime, complicating maintenance.
    - **Complexity and Cost**: The need to support SQL and ACID properties can increase maintenance costs.
    - **Slower Read Operations**: Read performance can be slower when compared to non-relational databases.
6. **Conclusion**: Relational databases are suited for scenarios that need complex queries and ACID guarantees. However, for situations where relationships are minimal or read performance is critical, alternative database solutions should be considered. 

# non-relational databases
 also known as NoSQL databases, which emerged in the mid-2000s to address the limitations of traditional relational databases. Here are the key points:

1. **Flexible Schemas**: Non-relational databases allow for different record structures without needing a uniform schema, unlike relational databases that require schema alterations when new data types are added.
    
2. **Data Structures**: While relational databases use tables, non-relational databases utilize various structures, such as lists, arrays, and maps. This design aligns better with programming languages and reduces reliance on Object-Relational Mapping (ORM) tools.
    
3. **Performance**: Non-relational databases often provide faster query performance, making them suited for specific use cases, but they come with complexities in data analysis due to their lack of enforced relationships and variable record structures.
    
4. **Types of Non-Relational Databases**:
    
    - **Key/Value Stores**: Store data using a unique key and are great for caching and simple data retrieval.
    - **Document Stores**: Store structured documents (like JSON or XML) that map well to programming constructs, enabling the representation of complex data.
    - **Graph Databases**: Focus on managing relationships between records efficiently, making them ideal for applications such as fraud detection and recommendations.
5. **Use Cases**: Non-relational databases are beneficial for handling unstructured data, real-time big data processing, and caching. However, for traditional applications, relational databases might remain preferable due to their reliability and simplicity.