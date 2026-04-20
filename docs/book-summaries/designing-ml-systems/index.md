---
layout: doc

title: Designing ML Systems
author: Chip Huyen
tags: [book-summary, machine-learning, system-design]
---

# Designing ML Systems

## Book Details

- **Author:** Chip Huyen
- **Domain:** Machine Learning, System Design

## Changelog

| Date           | Change Description        |
| -------------- | ------------------------- |
| April 20, 2026 | Added notes for Chapter 1 |

## Chapter-wise Notes

### Chapter 1 - Overview of Machine Learning Systems

ML systems consist of a variety of components:

- End users
- Business Requirements
- Data Stack
- Logic to train, deploy, monitor and maintain models
- Interface between the ML system and users
- Infrastructure to implement the logic to train, deploy, monitor and maintain

It is important to identify if the objective needs an ML solution or simpler solution will suffice. The solution needs ML if:

- The objective is to learn complex patterns from existing data so that predictions can be made for new data
  - The patterns to learn are complex to learn and can change over time, especially with rule-based solutions
  - Data can be collected for the model to learn patterns. Alternatively, zero-shot learning or continual learning could be applied in the absence of directly available data
  - Making predictions from learned patterns instead of exact measures can be very helpful, especially in complex and compute-intensive tasks
  - The patterns learned by the model can be assumed to be similar to those in the new unseen data
- The task (and hence the patterns) are repetitive
- The cost of incorrect predictions, on average, is worth the tradeoff of the benefits of correct predictions
- The solution is being applied to get a large number of predictions, which helps better utilization of large compute and memory provisioning, and collection of large amounts of data

ML in research vs production have different requirements

| Aspect                 | Research                                                                         | Production                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Requirements           | Getting state-of-the-art (SOTA) results on benchmark datasets                    | Depends on the different stakeholders (ML Engineers, Product team, Data Analysts etc)                                 |
| Data                   | Typically clean and static data is used. Focus is exploring different algorithms | Data can be messy, imbalanced and can need lots of data cleaning and pre-processing                                   |
| Computational Priority | Focus is on fast training and high throughput                                    | Focus is on fast inference and low latency                                                                            |
| Fairness               | Not high in objectives (Focus is on achieving SOTA results)                      | Important in objectives since it can impact the results for different groups of end users                             |
| Interpretability       | Not high in objectives (Focus is on achieving SOTA results)                      | Important in objectives since model working and predictions must be explainable to developers, stakeholders and users |

Considerations to keep in mind when deploying ML models to production:

- Need methods for version control and testing of code, data and models
- Need effective measures to deploy models as they increase in size (number of parameters) at scale
- Need monitoring for changing data patterns, model performance - necessary for model observability and monitoring
