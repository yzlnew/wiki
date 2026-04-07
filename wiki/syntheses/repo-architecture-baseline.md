---
type: synthesis
status: active
tags: [architecture, baseline]
source_count: 2
updated: 2026-04-07
---

# Repo Architecture Baseline

## Thesis

当前知识库采用三层结构：`sources/` 负责保留原始资料，`wiki/` 负责承载 Codex 持续维护的知识页，`system/` 负责固化 agent 的规则与模板。这种结构的目标是让知识成为可积累、可重构、可追踪的资产，而不是一次性聊天输出。

## Supporting Points

- 原始资料与总结层分离，能降低“边读边改原文”造成的混乱
- `wiki/index.md` 和 `wiki/log.md` 分别承担内容导航和时间追踪，适合持续增长的仓库
- `areas/` 与 `topics/` 作为上层组织骨架，能在早期避免过细拆分
- `syntheses/`、`questions/`、`entities/` 等目录为后续演化预留了清晰落点

## Counterpoints

- 当前主题桶仍然偏通用，后续需要按实际使用轨迹重构
- 目前还没有本地搜索或自动校验工具，后续规模增大后会出现检索摩擦

## Related

- [Home](../maps/home.md)
- [Knowledge Management](../topics/knowledge-management.md)
- [Wiki Index](../index.md)

## Sources

- [仓库说明](../../README.md)
- [Agent 规则](../../AGENTS.md)

## Open Questions

- 什么时候开始为高频实体建立 `entities/` 页面？
- 什么时候需要补充自动化搜索与 lint 工具？
