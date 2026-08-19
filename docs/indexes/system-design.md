---
title: System Design Index
tags:
  - system-design
  - index
---

# System Design Index

Notes and resources on distributed systems and system design.

## Important Terms

1. **Scalability**: Ability of a system to handle varying loaded
2. **Horizontal Scaling (Scaling out)**: Add nodes with similar capacity to existing nodes in distributed system. Can be done dynamically while system is running. Eg: Cassandra, MongoDB
3. **Vertical Scaling (Scaling up)**: Add more CPU, memory etc to existing node(s). Can result in downtime. Eg: MySQL
4. **Diagonal Scaling**: Combines horizontal and vertical scaling. Scale up first, then scale out.

## Resources

### Concepts

- (Book) Designing ML Systems [My Notes](../book-summaries/designing-ml-systems/)
- [(Course) Hello Interview - System Design in a Hurry](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction)
- [(Course) DesignGurus - Learn System Design](https://www.designgurus.io/learn-system-design/)

## Practice Questions

- [Hello Interview - Design Bitly](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly)
- [Hello Interview - Design Dropbox](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox)
- [Hello Interview - Local Delivery Service (Gopuff)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/gopuff)
