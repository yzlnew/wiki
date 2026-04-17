---
type: topic
status: active
tags: [agents, prompting, research]
source_count: 1
updated: 2026-04-07
---

# Agent Workflows

## Summary

围绕 agent 的工作流设计、上下文管理、提示工程和研究型使用方式的主题页。

## Key Points

### Factual Observations

- 这批 bookmarks 明显聚集在 Claude Code、slash commands、agent skills、context engineering、deep research 和 reasoning workflow 这些方向。
- 相关材料既包含实操型 setup / cheat sheet，也包含 Anthropic、OpenAI 和 Manus 等平台上的方法论文章。
- 还有一小组链接在讨论 reasoning 训练、评估与任务集合，说明“agent workflow”与“模型能力边界”在这里是连在一起看的。

### Current Judgment

- 最可复用的不是单条 prompt，而是可重复执行的工作流骨架：命令入口、上下文组织、可复用技能、长任务运行时约束，以及必要的评估信号。
- Claude Code 这一支更偏“操作系统化”的 agent 使用，而 deep research / o1 / reasoning 这一支更偏“任务分解与产出质量控制”。
- 未来若资料继续增多，这个主题大概率需要再拆成“Claude Code 实操”和“通用 agent 方法”两页。

## Subtopics

- Claude Code 操作与配置
- Slash commands 与可复用入口
- Agent skills 与能力封装
- Context engineering 与长任务 harness
- Prompting、deep research 与 reasoning workflow

## Related

- [[ai-and-llms|AI and LLMs]]
- [[software-engineering|Software Engineering]]
- [[knowledge-management|Knowledge Management]]
- [[home-ops-and-systems|Home Ops and Systems]]

## Sources

- [[bookmarks-agent-workflows-batch-1|Bookmarks Agent Workflows Batch 1]]

## Open Questions

- 哪些 workflow 约定是跨工具稳定的，哪些只对 Claude Code 成立？
- 应该把“prompting”单独拆成 topic，还是继续放在 agent workflow 里？
- 是否需要尽快补一个 Claude Code 实体页或工具页？
