---
type: topic
status: active
tags: [rl, post-training, reasoning, rlhf]
source_count: 1
updated: 2026-04-07
---

# Reinforcement Learning and Post-Training

## Summary

承接大模型强化学习、后训练、reasoning 数据与模板设计的主题页。它位于训练系统与应用工作流之间，重点关注“模型如何从基础预训练走向可用的推理与行为控制”。

## Key Points

### Factual Observations

- 这批 bookmarks 里，`Deep RL Course`、`Long-context GRPO` 和 `Unsloth chat templates` 聚成了一个很明确的后训练簇。
- 这些资料共同关心的不是基础预训练本身，而是 RL、数据格式、模板、长上下文策略和 reasoning 行为的塑造。
- 其中一部分内容与 `LLM Systems and Training` 重叠，但它们更偏训练目标变化和行为塑形，而不是分布式系统或优化底座。

### Current Judgment

- 这个主题适合放 RLHF、GRPO、reasoning data、chat template、policy shaping 之类内容。
- 它和 [LLM Systems and Training](llm-systems-and-training.md) 的边界在于：后者解决“如何把训练跑起来并稳定扩展”，这里解决“训练到底要优化什么行为”。
- 它和 [Agent Workflows](agent-workflows.md) 的边界在于：后者关注运行时的工具使用与任务编排，这里关注模型在训练阶段被塑造成什么样的行为策略。
- 如果后续书签继续增多，这里很可能要再拆成“RLHF / preference optimization”和“reasoning / post-training recipes”两页。

## Subtopics

- Deep reinforcement learning basics
- GRPO and reasoning optimization
- RLHF and preference-style post-training
- Chat templates and data formatting
- Reasoning behavior and long-context post-training

## Related

- [AI and LLMs](ai-and-llms.md)
- [LLM Systems and Training](llm-systems-and-training.md)
- [Agent Workflows](agent-workflows.md)
- [Knowledge Management](knowledge-management.md)
- [Learning and Research](../areas/learning-and-research.md)

## Sources

- [Bookmarks Reinforcement Learning and Post-Training Batch 1](../syntheses/bookmarks-reinforcement-learning-and-post-training-batch-1.md)

## Open Questions

- 这里是否应该进一步拆成 `RLHF`、`reasoning` 和 `chat templates` 三条子线？
- 后训练里的“模板”应该归到数据工程，还是归到模型行为控制？
- 哪些后训练方法已经足够稳定，可以抽成实体页或操作指南？
