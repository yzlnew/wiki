# System

这里存放知识库的”元规则”：

- `AGENTS.md` 负责定义 Codex 的总体行为
- `templates/` 提供常用页面模板和 LLM prompt 模板
- `interests.json` 集中管理个人兴趣配置（过滤规则、prompt 注入、主题桶等）

首次使用时，复制 `interests.example.json` 为 `interests.json` 并根据自己的兴趣修改。

当你准备调整知识库结构或写作规范时，优先改这里，而不是临时在聊天中约定。
