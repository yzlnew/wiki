# Wiki Log

本页记录知识库的关键动作，按时间追加，不回写历史。

## [2026-04-07] scaffold | initial-repo-structure

- 创建了 `system/`、`sources/`、`wiki/`、`archive/` 四层骨架
- 新增 `README.md` 与 `AGENTS.md`
- 新增 `wiki/index.md`、`wiki/log.md` 与一组起始主题页
- 新增常用模板，供后续 ingest / synthesis / question 页面复用
- 新增 `wiki/syntheses/repo-architecture-baseline.md` 作为当前结构基线页

## [2026-04-07] ingest | bookmarks-batch-1

- 从 `sources/library/bookmarks/bookmarks.md` 中拆出 4 个主题批次：`agent-workflows`、`llm-systems-and-training`、`self-hosting-and-home-lab`、`maker-and-3d-printing`
- 新增 4 个主题页与 4 个来源摘要页，并把它们接回 `wiki/index.md`、`wiki/maps/home.md` 和相关 area/topic 页
- 新增 [Bookmarks Next Batches](questions/bookmarks-next-batches.md) 记录尚未落位的剩余书签与下一步 ingest 建议

## [2026-04-07] ingest | bookmarks-batch-2

- 继续消费剩余链接，新增 [Reinforcement Learning and Post-Training](topics/reinforcement-learning-and-post-training.md) 与对应来源摘要页
- 为 [LLM Systems and Training](topics/llm-systems-and-training.md) 补入第二批 residuals，并新增 [Bookmarks LLM Systems Batch 2](syntheses/bookmarks-llm-systems-batch-2.md)
- 更新 `wiki/index.md`、`wiki/maps/home.md`、`wiki/topics/ai-and-llms.md`、`wiki/areas/learning-and-research.md` 与 backlog 页，明确剩余低信号尾项

## [2026-04-07] query | taste-and-interest-profile

- 基于已 ingest 的 topic 与 synthesis 页面，整理出一页 [Taste and Interest Profile](syntheses/taste-and-interest-profile.md)
- 将当前稳定兴趣、偏好的内容形态、弱信号主题和默认降权项整理为后续 RSS 过滤的起始规则
- 更新 `wiki/index.md` 与 `wiki/maps/home.md`，确保该画像页可直接从导航进入

## [2026-04-07] query | rss-filter-prompt-template

- 新增脚本可直接调用的模板 [rss-filter-prompt](../system/templates/rss-filter-prompt.md)
- 明确了候选 RSS 条目的输入字段、判定规则、评分区间与 JSON 输出结构
- 在 [Taste and Interest Profile](syntheses/taste-and-interest-profile.md) 中补入模板入口，区分解释层和执行层

## [2026-04-08] scaffold | freshrss-source-pipeline

- 新增 `scripts/update_freshrss.py`，通过 FreshRSS Google Reader API 拉最近订阅项
- 在抓全文前先用 `来源 + 标题` 做兴趣过滤，并把过滤报告写到 `sources/library/freshrss/freshrss-latest.md`
- 将入选条目正文写入 `sources/inbox/freshrss/`，供后续 ingest 使用
- 新增 `.env.freshrss.example` 与本地忽略的 `.env.freshrss.local` 约定，并更新仓库说明

## [2026-04-10] scaffold | hf-daily-papers-source-pipeline

- 新增 `scripts/update_hf_daily_papers.py`，通过 Hugging Face 官方 `daily_papers` API 拉最近论文
- 用便宜的 `codex exec` 子代理先做兴趣相关性过滤，再基于原始论文页 / arXiv abstract 提炼知识点
- 将报告写到 `sources/library/hf-daily-papers/hf-daily-papers-latest.md`，将入选论文写入 `sources/inbox/hf-daily-papers/`
- 新增 `.env.hf-daily-papers.example`、两份 prompt 模板与 README 中的 cron 约定

## [2026-04-10] scaffold | daily-source-digest-email

- 新增 `scripts/send_daily_digest.py`，串行运行 `bookmarks`、`freshrss`、`hf-daily-papers` 三条 update
- 每日汇总三份来源报告的关键计数、入选项与 staged 文件，再通过本机 `sendmail` 发送摘要邮件
- 新增 `.env.daily-digest.example` 与 README 中的日更邮件说明
