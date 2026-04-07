---
type: source-summary
status: active
tags: [bookmarks, llm, training, systems, interpretability, math]
source_count: 16
updated: 2026-04-07
source_path: ../../sources/library/bookmarks/bookmarks.md
---

# Bookmarks LLM Systems Batch 1

## Source

- 原始文件：`sources/library/bookmarks/bookmarks.md`
- 批次范围：与 LLM 训练系统、可解释性、基础数学和推理训练最相关的书签
- 处理日期：2026-04-07

## Summary

这一批链接把 `LLM systems` 拆成五条主线：训练配方和规模化、分布式并行与通信、优化器与归一化、可解释性和电路追踪、以及推理/后训练数据。

整体上，它们更像一组互相咬合的参考坐标，而不是孤立资料。训练 playbook 和超大规模训练指南提供系统层面视角；`NCCL`、`parallelisms` 和 GPU glossary 提供基础设施语言；`norms`、`Muon`、`gradient descent` 和 `einsum` 补足数学底座；`biology`、`circuit tracing` 和 `o1` 相关书签则把模型内部机制与推理行为连起来。

## Key Claims

- 训练大型 LLM 时，系统约束和算法选择是耦合的，不能只看模型结构本身
- 并行策略和通信原语是扩展训练规模的前提，而不是后置优化
- 优化器、归一化和损失形状会直接影响训练稳定性与可扩展性
- 可解释性资料更适合和训练资料并读，因为它们都在回答“模型到底学到了什么”
- 推理模型与通用 chat 模型在目标和数据形态上已经开始分化

## Evidence Notes

- `The Smol Training Playbook` 和 `The Ultra-Scale Playbook`：提供训练配方与大规模训练组织方式
- `Parallelisms — NVIDIA NeMo` 和 `Collective Operations — NCCL 2.25.1 documentation`：说明并行训练与 collective communication 的基础
- `What’s in a norm?`、`Deriving Muon`、`How does gradient descent work?`、`Einsum in Depth`：覆盖优化、归一化和张量运算基础
- `On the Biology of a Large Language Model` 和 `Circuit Tracing`：提供机制解释与 tracing 方法语境
- `Reinforcement Learning From Human Feedback`、`Open-Reasoning-Tasks`、`Bespoke-Stratos-32B`、`o1 isn’t a chat model`：把 reasoning / RLHF / post-training 串起来
- `GPU Glossary`：补齐面向工程实践的硬件术语层

## Related

- [LLM Systems and Training](../topics/llm-systems-and-training.md)
- [AI and LLMs](../topics/ai-and-llms.md)
- [Software Engineering](../topics/software-engineering.md)
- [Learning and Research](../areas/learning-and-research.md)

## Follow-ups

- 这批书签里哪些内容需要进一步拆成实体页，例如 `NCCL`、`Muon`、`o1` 或 `DeepSeek-R1`？
- 是否要单独建立一个 reasoning / post-training 的 synthesis 页？
- 还缺哪类来源：评测、推理加速、数据配方，还是训练稳定性案例？

## Links

- [The Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook#mystery-3--the-noisy-loss)
- [The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=high_level_overview)
- [Parallelisms — NVIDIA NeMo Framework User Guide](https://docs.nvidia.com/nemo-framework/user-guide/24.09/nemotoolkit/features/parallelisms.html)
- [Collective Operations — NVIDIA NCCL 2.25.1 documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)
- [What’s in a norm?](https://docs.modula.systems/intro/whats-in-a-norm/)
- [Deriving Muon](https://jeremybernste.in/writing/deriving-muon)
- [How does gradient descent work?](https://centralflows.github.io/part1/)
- [Einsum in Depth](https://einsum.joelburget.com/)
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- [Reinforcement Learning From Human Feedback](https://newfacade.github.io/notes-on-reinforcement-learning/17-ppo-trl.html)
- [GitHub - NousResearch/Open-Reasoning-Tasks](https://github.com/NousResearch/Open-Reasoning-Tasks)
- [Bespoke-Stratos-32B X post](https://x.com/madiator/status/1882131703927652762)
- [o1 isn’t a chat model (and that’s the point)](https://www.latent.space/p/o1-skill-issue)
- [GPU Glossary](https://modal.com/gpu-glossary)
- [MIT 6.5940 Fall 2024 TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940)
