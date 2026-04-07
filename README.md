# 个人知识库 Wiki

这是一个面向 Codex 协作的个人知识库仓库。它采用类似 Andrej Karpathy 在 `llm-wiki` 中描述的模式：把原始资料、LLM 维护的 wiki、以及 agent 的维护规则分开管理，让知识不是“每次问都临时检索”，而是被持续整理、交叉链接和累积沉淀。

参考思路：
- Karpathy, `llm-wiki`: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 目标

这个仓库默认服务于三类操作：

1. `ingest`：把新资料纳入知识库。
2. `query`：基于已经整理过的 wiki 回答问题，并把高价值回答沉淀回仓库。
3. `lint`：周期性检查知识库是否存在断链、重复、过时或缺失的页面。

## 仓库结构

```text
.
├── AGENTS.md              # Codex 的协作规范与工作流
├── README.md              # 仓库总说明
├── system/                # 规则、模板、约定
├── sources/               # 原始资料，默认不可变
│   ├── inbox/             # 待处理入口
│   ├── library/           # 已归档原始资料
│   └── assets/            # 本地图片、附件、数据文件
├── wiki/                  # Codex 维护的知识页
│   ├── index.md           # 内容索引
│   ├── log.md             # 时间日志
│   ├── maps/              # 导航页 / 主题地图
│   ├── areas/             # 长期领域
│   ├── topics/            # 主题页
│   ├── entities/          # 人物 / 公司 / 术语 / 工具等实体页
│   ├── projects/          # 项目页
│   ├── syntheses/         # 综合分析 / 结论页
│   ├── questions/         # 待回答问题与研究线索
│   ├── timelines/         # 时间线
│   └── glossary/          # 术语表
└── archive/               # 冷存档与废弃内容
```

## 设计原则

- `sources/` 是事实输入层。这里放原文、PDF、网页转存、截图、附件，默认不直接改写。
- `wiki/` 是知识编译层。这里放主题总结、实体关系、对比分析、问题追踪和结论。
- `system/` 是 agent 配置层。这里定义 Codex 应如何命名、落盘、交叉引用和维护一致性。
- `index.md` 偏内容导航，`log.md` 偏时间顺序。两者都应该持续维护。
- 高价值对话结论不应只留在聊天记录里，应该沉淀为 `wiki/` 中的新页面或现有页面更新。

## 推荐使用方式

### 1. 加资料

把新材料先放进 `sources/inbox/`，或者从 bookmarks 服务同步到本地 markdown，例如：

- 一篇网页导出的 markdown
- 一份 PDF
- 一张图表或截图
- 一组会议纪要
- 一批来自 bookmarks 列表的链接

然后告诉 Codex：

```text
请 ingest sources/inbox/xxx.md，把重要结论并入现有 wiki。
```

如果资料来自 bookmarks：

```text
先更新 sources/library/bookmarks/bookmarks.md，然后从里面挑出和 AI agent tooling 相关的链接做一轮 ingest。
```

### 2. 问问题

直接围绕 `wiki/` 提问，例如：

```text
基于现有 wiki，总结一下 AI agent tooling 这条线的核心判断，并补成一页 synthesis。
```

### 3. 做体检

定期让 Codex 执行整理，例如：

```text
请 lint 一下 wiki，找出孤立页面、重复主题、缺失的实体页和过时结论。
```

## 命名约定

- 目录名和文件名统一使用英文 `kebab-case`
- 页面正文可以用中文，也可以中英混写
- 一类信息一个页面，不把不相干内容堆进大杂烩页面
- 优先写“可链接页面”，而不是只写一次性的聊天答案

## 起步建议

- 先围绕 5-10 个核心主题持续积累，不要一开始就把目录切得太细
- 先让 `topics/` 和 `syntheses/` 长起来，再按需要补 `entities/` 和 `timelines/`
- 每次 ingest 至少更新三处：相关主题页、`wiki/index.md`、`wiki/log.md`

## 可选下一步

- 初始化 git：`git init`
- 用 Obsidian 打开本目录，直接浏览 `wiki/`
- 后续补一个本地搜索脚本，用于快速检索 `wiki/` 和 `sources/`

## Bookmarks 同步

仓库内置了一个同步脚本：

```text
python3 scripts/update_bookmarks.py
```

它会读取本地忽略的 `.env.bookmarks.local`，然后更新：

```text
sources/library/bookmarks/bookmarks.md
```

建议流程：

1. 复制 `.env.bookmarks.example` 为 `.env.bookmarks.local`
2. 在本地填入 bookmarks 服务地址和 API key
3. 运行同步脚本
4. 再让 Codex 基于 `bookmarks.md` 选择值得 ingest 的链接

示例定时任务：

```cron
15 * * * * cd /root/wiki && python3 scripts/update_bookmarks.py >> /tmp/bookmarks-sync.log 2>&1
```

注意：

- 实例地址和 API key 只放在 `.env.bookmarks.local`，不会进入 git
- 生成的 `bookmarks.md` 默认会进入仓库；如果你不想让收藏链接进入 git，可以额外把该文件加入 `.gitignore`
- 如果你的实例有 IP / 证书兼容问题，可在 `.env.bookmarks.local` 里补 `BOOKMARKS_FORCE_IPV4=1`、`BOOKMARKS_FORCE_IPV6=1` 或 `BOOKMARKS_VERIFY_TLS=0`
