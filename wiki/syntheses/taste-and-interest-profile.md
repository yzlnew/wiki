---
type: synthesis
status: active
tags: [profile, interests, rss]
source_count: 12
updated: 2026-04-07
---

# Taste and Interest Profile

## Summary

基于当前已经 ingest 的书签与主题页，可以先把你的兴趣画像概括为两条主轴：一条是 `AI / agents / LLM engineering`，另一条是 `personal infrastructure / home lab / maker workflows`。你的 taste 明显偏向系统、方法、工作流和可维护性，而不是泛泛新闻、消费导向评测或纯热点转发。

这个画像适合拿来做 RSS 的第一版过滤规则，但它仍是阶段性结论；后续如果 ingest 进来新的高密度主题，应该继续修正。脚本直接调用时，应优先使用 [[rss-filter-prompt]] 作为 prompt 模版，把本页视为它背后的解释层。

## Key Points

### Stable Interest Areas

- 高优先级兴趣之一是 `agent workflows`：尤其是 `Claude Code`、slash commands、agent skills、context engineering、deep research 和 reasoning workflow。
- 高优先级兴趣之一是 `LLM systems and training`：尤其是 scaling、parallelism、GPU / NCCL、优化器、归一化、loss behavior、可解释性和 circuit tracing。
- 高优先级兴趣之一是 `post-training`：尤其是 `RLHF`、`GRPO`、reasoning data、chat templates 和行为塑形。
- 高优先级兴趣之一是个人基础设施：尤其是 bookmarks、paperless、code-server、n8n、memos 这类可长期维护的知识与自动化系统。
- 高优先级兴趣之一是 home lab / networking：尤其是 `AdGuard Home`、`mosdns`、`OpenClash`、`sing-box`、透明代理分流、Linux / VPS 初始化、虚拟化和 SR-IOV。
- 高优先级兴趣之一是 maker / 3D printing：尤其是 `Gridfinity`、生成式建模、问题导向的可打印部件，以及和家庭整理直接相关的实物制作能力。

### Taste Signals

#### Facts

- 已沉淀的重主题集中在 `Agent Workflows`、`LLM Systems and Training`、`Reinforcement Learning and Post-Training`、`Self-Hosting and Home Lab`、`Maker and 3D Printing`。
- 多个来源摘要都反复强调 workflow、系统约束、运行时结构、训练配方、网络控制面和家庭系统维护，而不是单条资讯。
- 当前剩余未落位链接被明确归因为低信号、一次性或上下文不足，说明你过去的收藏里已经能区分“长期主题”和“路过条目”。

#### Inferences

- 你偏好“可操作的工作流”胜过“零散技巧”，尤其重视能复用、能组合、能长期维护的方法。
- 你偏好工程解释、机制理解和系统 trade-off，胜过泛泛观点、行业情绪或营销式解读。
- 你对 AI 的兴趣更偏工程和研究交界处，而不只是产品使用层。
- 你对居家系统的兴趣也偏“基础设施化”，重视本地控制、自动化、可维护性和实体环境改造。
- 你对 maker 的兴趣偏功能性、组织性和工具链整合，而不是纯展示型作品。

### RSS Filtering Hints

#### Strong Positive Signals

- 文章主题涉及 `agents`、`Claude Code`、`context engineering`、`tool use`、`skills`、`deep research`、`reasoning workflows`。
- 文章主题涉及 `LLM training systems`、scaling、parallelism、GPU 通信、优化器、归一化、interpretability、circuit tracing。
- 文章主题涉及 `RLHF`、`GRPO`、reasoning training、chat templates、post-training recipes。
- 文章主题涉及自托管、知识流、文档流、事件驱动自动化、远程开发、家庭网络、代理分流、Home Assistant、边缘设备接入。
- 文章主题涉及 `Gridfinity`、3D 打印工作流、生成式建模、针对家庭或工作台收纳的 maker 方案。

#### Style Preferences

- 优先保留提供 setup、playbook、架构判断、实现细节、实验记录、benchmark 或可复用实践的内容。
- 优先保留横跨两个兴趣轴的内容，例如 AI agent + developer workflow、self-hosted knowledge pipeline、生成式 3D + 家庭收纳。
- 对“讲原理同时能落地”的内容应给更高权重；对只有观点没有做法的内容应降低权重。

#### Secondary Or Weak Signals

- 创作素材或资源目录类内容目前是弱信号，例如 `uchu`、`Free Music Archive`、`FMHY`。
- 泛娱乐、单点消费或低上下文条目目前是弱信号，例如 ROM hack、点播直播资源、单次发布页。
- 只有链接但缺少注释、问题语境或复用价值的条目，应默认低优先级，除非后续再次命中。

#### Default Downrank Rules

- 泛 AI 新闻、产品发布速报、没有技术细节的模型排行榜。
- 只讨论 prompt 小技巧、但没有 workflow / evaluation / system context 的内容。
- 通用消费电子评测、泛生活方式内容、与个人系统建设无关的娱乐资讯。
- 资源大合集或“免费大全”类页面，除非它们和当前任务直接相关。

## Related

- [[ai-and-llms|AI and LLMs]]
- [[agent-workflows|Agent Workflows]]
- [[llm-systems-and-training|LLM Systems and Training]]
- [[reinforcement-learning-and-post-training|Reinforcement Learning and Post-Training]]
- [[self-hosting-and-home-lab|Self-Hosting and Home Lab]]
- [[maker-and-3d-printing|Maker and 3D Printing]]
- [[learning-and-research|Learning and Research]]
- [[home-ops-and-systems|Home Ops and Systems]]

## Sources

- [[agent-workflows|Agent Workflows]]
- [[llm-systems-and-training|LLM Systems and Training]]
- [[reinforcement-learning-and-post-training|Reinforcement Learning and Post-Training]]
- [[self-hosting-and-home-lab|Self-Hosting and Home Lab]]
- [[maker-and-3d-printing|Maker and 3D Printing]]
- [[bookmarks-agent-workflows-batch-1|Bookmarks Agent Workflows Batch 1]]
- [[bookmarks-llm-systems-batch-1|Bookmarks LLM Systems Batch 1]]
- [[bookmarks-llm-systems-batch-2|Bookmarks LLM Systems Batch 2]]
- [[bookmarks-reinforcement-learning-and-post-training-batch-1|Bookmarks Reinforcement Learning and Post-Training Batch 1]]
- [[bookmarks-self-hosting-home-lab-batch-1|Bookmarks Self-Hosting and Home Lab Batch 1]]
- [[bookmarks-maker-3d-batch-1|Bookmarks Maker 3D Batch 1]]
- [[bookmarks-next-batches|Bookmarks Next Batches]]

## Open Questions

- 后续 RSS 过滤时，是否要把 `AI / LLM` 和 `home lab / maker` 拆成两套不同权重的规则？
- 家庭网络 / 代理类内容是持续高优先级，还是阶段性高密度主题？
- `creative assets` 是否会成长为独立兴趣线，还是继续保持弱信号状态？
- 是否需要再整理一版更机器可读的关键词白名单 / 黑名单？

## Prompt Template

- 供脚本直接使用的模板在 [[rss-filter-prompt]]
- 本页负责解释“为什么是这些规则”，模板页负责定义“脚本怎么喂输入、模型怎么回输出”
