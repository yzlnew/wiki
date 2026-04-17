---
type: source-summary
status: active
tags: [freshrss, rss, inbox]
source_count: 1
updated: 2026-04-11
source_url: https://old.reddit.com/r/LocalLLaMA/comments/1shus54/glm_51_crushes_every_other_model_except_opus_in/
feed_source: LocalLlama
published: 2026-04-11T02:23:15+08:00
decision: accept
score: 80
generator: scripts/update_freshrss.py
---

# GLM 5.1 crushes every other model except Opus in agentic benchmark at about 1/3 of the Opus cost

## Summary

- source_feed: `LocalLlama`
- original_url: https://old.reddit.com/r/LocalLLaMA/comments/1shus54/glm_51_crushes_every_other_model_except_opus_in/
- published: `2026-04-11T02:23:15+08:00`
- filter_reason: Strong fit for agent-workflows with useful signal in source/title.

## Feed Metadata

- source_home: https://old.reddit.com/r/LocalLlama/
- categories: `user/-/state/com.google/reading-list`, `user/-/label/未分类`, `user/-/state/org.freshrss/main`, `r/LocalLLaMA`
- feed_summary: https://preview.redd.it/s9lg647zjeug1.png?width=1161&format=png&auto=webp&s=4d0c361b5fbee97e4084e2d48543cafbc299ce25 I want to know whether GLM is another benchmark optimized model or actually useful in agents like OpenClaw, so I tested GLM 5.1 in our agentic benchmark. Turns out it reaches Opus 4.6 level performanc...
- fetched_page_title: GLM 5.1 crushes every other model except Opus in agentic benchmark at about 1/3 of the Opus cost : LocalLLaMA
- fetched_page_description: !\[img\](s9lg647zjeug1) I want to know whether GLM is another benchmark optimized model or actually useful in agents like OpenClaw, so I tested GLM...

## Full Text

https://preview.redd.it/s9lg647zjeug1.png?width=1161&format=png&auto=webp&s=4d0c361b5fbee97e4084e2d48543cafbc299ce25
I want to know whether GLM is another benchmark optimized model or actually useful in agents like OpenClaw, so I tested GLM 5.1 in our agentic benchmark.
Turns out it reaches Opus 4.6 level performance with just 1/3 of the cost (~$0.4 per run vs ~$1.2 per run) based on my tests. It outperforms all other models tested. Pushes the cost effectiveness frontier quite a bit.
I don't quite trust any static benchmarks, seen many models optimized for it, ranking high on those leaderboard but not working well in real agentic tasks. So we uses OpenClaw to test the agentic performance of models in real environment + real tasks (user submitted). Chatbot Arena/LMArena style battle, LLM as judge.
Based on the result, I would say GLM 5.1 is one of the top models for OpenClaw type of agents now.
Qwen 3.6 also did a good job, but it does not support prompt caching yet (on openrouter) so the current price is inflated. With prompt caching I except it to reach minimax m2.7 level cost per run and becomes another great choice for cost effectiveness.
Full leaderboard, cost-effectiveness analysis, and methodology can be found at https://app.uniclaw.ai/arena?via=reddit . Strongly recommend submitting your own task and see how different models on it.
[Edit 1]
It seems many people confused price per token and price per task.
GLM 5.1 price per token is < 1/5 of Opus. But GLM also uses about 2x token per task compared to Opus, on the same task, based on our benchmark. Reason is that GLM uses tools aggressively, more than 2x tool calls per task compared to Opus. That's why the actual cost per task is about 1/3 of Opus.
submitted by /u/zylskysniper
[link] [comments]
