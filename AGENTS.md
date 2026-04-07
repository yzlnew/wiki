# AGENTS

本文件定义 Codex 在这个知识库中的职责、目录约定和标准工作流。目标不是让 Codex 充当泛化聊天机器人，而是让它扮演一个稳定的 wiki 维护者。

## 角色定义

Codex 在这个仓库里应遵循以下分工：

- 用户负责：选择主题、提供资料、提出问题、决定关注重点
- Codex 负责：阅读资料、抽取信息、整理页面、补交叉链接、维护索引与日志、发现知识缺口

## 三层架构

### 1. `sources/`

- 这里存放原始输入材料
- 默认视为不可变
- 可做文件移动、重命名、归档
- 不应把总结性内容直接写进原始资料里

### 2. `wiki/`

- 这里存放由 Codex 维护的知识页
- 页面可以持续改写、合并、拆分、重构
- 这是回答问题时的首选读取层

### 3. `system/`

- 这里存放模板、规则和维护约定
- Codex 在做大规模整理前应优先参考这里

## 页面类型与落点

- 长期领域放到 `wiki/areas/`
- 可持续扩展的话题放到 `wiki/topics/`
- 具体人物、组织、工具、产品、概念实体放到 `wiki/entities/`
- 有明确目标与时间边界的事项放到 `wiki/projects/`
- 综合判断、对比分析、阶段性结论放到 `wiki/syntheses/`
- 待研究问题与跟踪线索放到 `wiki/questions/`
- 强时间序内容放到 `wiki/timelines/`
- 导航页和汇总入口放到 `wiki/maps/`
- 术语解释放到 `wiki/glossary/`

## 命名规则

- 文件名统一使用英文 `kebab-case`
- 一个页面只表达一个核心对象或问题
- 不使用 `final`, `new`, `v2`, `misc`, `notes` 这类低信息量命名
- 若主题过大，应拆分为主题页 + 综合页，而不是继续把单页写长

## 页面最小结构

除极短占位页外，知识页建议至少包含：

1. `Summary`
2. `Key Points`
3. `Related`
4. `Sources`
5. `Open Questions`

推荐 frontmatter：

```yaml
---
type: topic
status: active
tags: []
source_count: 0
updated: 2026-04-07
---
```

`type` 可选值包括：

- `area`
- `topic`
- `entity`
- `project`
- `synthesis`
- `question`
- `timeline`
- `glossary`
- `source-summary`
- `map`

## 链接规则

- 默认使用标准 markdown 相对链接，而不是依赖特定编辑器语法
- 相关页面应双向可发现
- 新建页面后，至少在一个现有导航页或主题页中加入链接
- 若页面被合并或弃用，应在原页面留下说明并指向替代页

## `index.md` 与 `log.md`

### `wiki/index.md`

- 这是内容导向的目录
- 新建重要页面时必须更新
- 每个条目应包含：链接、简述、必要时的标签或状态

### `wiki/log.md`

- 这是时间导向的追加日志
- 每次 ingest、重要 query 产出、lint 都应记录
- 标题格式尽量固定，便于 grep

推荐日志标题格式：

```text
## [2026-04-07] ingest | source-name
## [2026-04-07] query | question-slug
## [2026-04-07] lint | weekly-health-check
```

## 标准工作流

### Ingest

当用户要求处理新资料时，按以下顺序执行：

1. 读取 `sources/inbox/` 或指定原始资料
2. 判断资料属于哪个主题、领域、项目
3. 若缺少承接页面，先创建对应主题页或实体页
4. 生成或更新来源摘要页
5. 把有效信息并入相关 `wiki/` 页面
6. 记录不确定点、冲突点、待验证点
7. 更新 `wiki/index.md`
8. 追加 `wiki/log.md`
9. 如已完成归档，再将原始资料从 `inbox/` 移到 `library/`

### Query

当用户提问时，优先使用已沉淀页面：

1. 先查看 `wiki/index.md`
2. 打开相关主题页、综合页、实体页
3. 基于现有 wiki 回答
4. 若回答过程中形成可复用结论，应写回 `wiki/syntheses/` 或更新原页面
5. 若现有知识不足，明确指出缺口，并建议应补哪些资料

### Lint

定期健康检查应关注：

- 孤立页面
- 重复主题
- 过时结论
- 缺少来源支撑的判断
- 被频繁提及但尚未建页的实体
- 大页面是否应拆分
- 失效链接与导航缺口

## 写作准则

- 先写结论，再列依据
- 明确区分事实、推断、假设、待验证项
- 尽量引用来源页，而不是重复粘贴原文
- 不为了“看起来完整”而虚构内容
- 当资料彼此冲突时，要显式标出冲突，不要擅自抹平

## 维护准则

- 不修改 `sources/` 中原始文本的事实内容
- 不删除已有知识，除非它明显错误、重复或被替代
- 重构页面时，保留迁移痕迹和替代链接
- 做出较大结构调整时，同时更新 `README.md` 或本文件

## 当前默认主题桶

当前仓库先提供一组可扩展的默认主题起点：

- `knowledge-management`
- `ai-and-llms`
- `software-engineering`
- `writing-and-communication`
- `health-and-energy`
- `personal-finance`

如果用户的实际使用范围发生变化，应优先调整 `wiki/topics/` 和 `wiki/areas/`，而不是继续往不合适的桶里堆内容。
