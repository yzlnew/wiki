---
type: topic
status: active
tags: [llm, training, systems, optimization, interpretability]
source_count: 2
updated: 2026-04-07
---

# LLM Systems and Training

## Summary

承接大模型训练系统、优化方法、分布式计算、可解释性和推理训练相关内容的主题页。

## Key Points

- 这个主题位于 `AI and LLMs` 的工程化一侧，和 `Software Engineering`、`Learning and Research` 都有强交叉
- 它的核心不是单篇论文，而是把训练配方、系统约束、数学基础和解释框架放在同一张图里看
- 当前更适合沉淀“可复用判断”，例如训练规模如何扩展、何时需要并行策略、哪些优化器/归一化值得关注
- 当前已经有两批 bookmarks 资料接入：一批偏系统主干，一批偏系统余量、数学底座和小规模实验验证

## Subtopics

- Training playbooks and scaling laws
- Distributed training, parallelism, and GPU collectives
- Optimizers, normalization, and loss behavior
- Interpretability and circuit tracing
- Reasoning data, RLHF, and post-training
- Core math for tensor operations and gradient descent
- Architecture experiments and efficient small-scale training

## Related

- [AI and LLMs](ai-and-llms.md)
- [Software Engineering](software-engineering.md)
- [Learning and Research](../areas/learning-and-research.md)
- [Knowledge Management](knowledge-management.md)

## Sources

- [Bookmarks LLM Systems Batch 1](../syntheses/bookmarks-llm-systems-batch-1.md)
- [Bookmarks LLM Systems Batch 2](../syntheses/bookmarks-llm-systems-batch-2.md)

## Open Questions

- 这批资料里，训练系统和可解释性是否应该拆成两个独立 topic？
- 你当前最常用的训练栈是哪个，是否需要单独建实体页？
- 需要继续补哪些后训练、评测或推理加速资料？
- `nanochat`、`mHC Visualizer`、`GDN vs Mamba2` 这类实验型链接是否应拆成实体或 synthesis？
