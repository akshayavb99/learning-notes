---
title: Reasoning Models Struggle to Control Chain of Thought
author:
    - Chen Yueh-Han
    - Robert McCarthy
    - Bruce W. Lee
    - He He
    - Ian Kivlichan
    - Bowen Baker
    - Micah Carroll
    - Tomek Korbak

tags:
    - paper-summary
    - reasoning-models
updated_date: 2026-05-24
url: https://arxiv.org/abs/2603.05706
---

# [Reasoning Models Struggle to Control Chain of Thought](https://arxiv.org/abs/2603.05706)

## Three Takeaways

**1. Modern reasoning models are surprisingly poor at controlling their chain-of-thought (CoT)**

- The paper introduces CoT controllability: whether a model can intentionally shape or suppress parts of its reasoning while still solving the task correctly. 
- Across many frontier reasoning models, success rates were extremely low (roughly 0.1%–15%). 
- Even when explicitly instructed to avoid certain concepts or words, models often leaked them into their reasoning traces anyway.

**2. This weakness may actually improve AI safety**

- A major motivation for the work is whether models can hide dangerous intent from human oversight systems. 
- The authors argue that current models are not very capable of covertly manipulating their reasoning traces, which means CoT monitoring remains a useful safety mechanism. 
- If a model cannot reliably conceal its internal reasoning, then humans and automated monitors have a better chance of detecting unsafe behavior.

**3. More reasoning and more RL training can reduce controllability further**

- One interesting result is that giving models more room to “think” often worsened their ability to obey CoT constraints. 
- Reinforcement-learning-trained reasoning models also tended to have lower controllability than expected. 
- This suggests that current reasoning behavior is not fully deliberate or strategically editable; instead, reasoning traces emerge in ways that models themselves cannot tightly regulate.

## Potential Missing Considerations

- The paper’s biggest weakness is that its evaluation setup may not reflect true adversarial deception. 
- The models are tested on artificial constraints like “do not use this word” or “avoid mentioning this concept,” but real-world deceptive behavior could involve much more strategic planning.
-  A model that fails simple lexical constraints today might still learn more sophisticated concealment strategies in future generations. 
-  The paper demonstrates weak controllability under current benchmark conditions, but it does not prove that future systems will remain transparent.

## Conclusion

The paper strongly suggests that chain-of-thought monitoring is currently one of the most promising practical AI safety tools. Since today’s reasoning models struggle to intentionally disguise their reasoning, developers should invest heavily in systems that inspect, analyze, and audit reasoning traces during deployment. At the same time, this advantage may only be temporary. Future AI systems could become better at selectively hiding information, so controllability itself should become a standard capability benchmark alongside accuracy and reasoning performance.