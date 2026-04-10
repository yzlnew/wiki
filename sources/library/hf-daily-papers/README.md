# Hugging Face Daily Papers

这里放 Hugging Face Daily Papers 拉下来的最近论文报告与去重状态。

当前约定：

- `hf-daily-papers-latest.md` 由 `scripts/update_hf_daily_papers.py` 自动生成
- `hf-daily-papers-state.json` 记录已处理论文，避免 cron 重复调用子代理
- 相关性过滤与知识点抽取都由便宜模型的 `codex exec` 子代理完成
- 知识点抽取优先抓原始论文页或 arXiv abstract，再回退到 Hugging Face 元数据
