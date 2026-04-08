# FreshRSS

这里放 FreshRSS 拉下来的订阅元数据报告。

当前约定：

- `freshrss-latest.md` 由 `scripts/update_freshrss.py` 自动生成
- 先根据 `来源 + 标题` 做兴趣过滤，再决定是否抓全文
- 入选文章正文写入 `sources/inbox/freshrss/`，等待后续 ingest
