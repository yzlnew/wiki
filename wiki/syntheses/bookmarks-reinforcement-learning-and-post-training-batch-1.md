---
type: source-summary
status: active
tags: [bookmarks, rl, post-training, reasoning, templates]
source_count: 3
updated: 2026-04-07
source_path: ../../sources/library/bookmarks/bookmarks.md
---

# Bookmarks Reinforcement Learning and Post-Training Batch 1

## Source

- 原始文件：`sources/library/bookmarks/bookmarks.md`
- 处理日期：2026-04-07
- 本批次聚焦：reinforcement learning / post-training / reasoning training

## Summary

这一批剩余书签把后训练问题收束成三件事：训练目标怎么定义，训练样本和模板怎么组织，以及这些方法和传统预训练系统有什么不同。

`Deep RL Course` 提供了强化学习基础语境，`Long-context GRPO` 代表面向 reasoning 的后训练策略，`Unsloth chat templates` 则把数据模板和对话格式放到训练链路里看。三者合在一起，说明这里关注的不是“再训练一次模型”，而是“通过目标函数、样本结构和模板约束改变模型行为”。

## Key Claims

- 后训练的核心是行为塑形，不是单纯扩大训练规模
- reasoning 相关方法往往更依赖数据形态、模板和长上下文组织方式
- 与传统训练系统相比，这里更在意策略、偏好和输出结构，而不只是损失收敛
- RL / post-training 和推理能力的关系，比一般监督微调更紧密

## Evidence Notes

- `Welcome to the Deep RL Course`：给出强化学习的基础概念和术语背景
- `Long-context GRPO (R1 Reasoning)`：指向 reasoning 场景下的后训练方法
- `https://docs.unsloth.ai/basics/chat-templates`：说明 chat template 在实际训练管线里不是附属物，而是控制样本结构的一部分

## Related

- [Reinforcement Learning and Post-Training](../topics/reinforcement-learning-and-post-training.md)
- [AI and LLMs](../topics/ai-and-llms.md)
- [LLM Systems and Training](../topics/llm-systems-and-training.md)
- [Agent Workflows](../topics/agent-workflows.md)

## Follow-ups

- 需要继续补哪些 RLHF、偏好优化或 reasoning recipe 资料？
- 后训练是否值得再拆出一页专门讲 `chat templates` 与数据格式？
- 这些内容里哪些已经足够稳定，可以升级成实体页或操作指南？
