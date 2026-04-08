---
type: source-summary
status: active
tags: [freshrss, rss, generated]
source_count: 20
updated: 2026-04-08
generator: scripts/update_freshrss.py
---

# FreshRSS Latest

## Summary

- generated_at: 2026-04-08T15:39:17+08:00
- total_items: 20
- accepted: 0
- maybe: 2
- rejected: 18
- staged_for_ingest: 2
- filter_input: source + title only before article fetch

## Notes

- This file is generated from FreshRSS metadata and should be updated by script, not edited by hand.
- Accepted items are fetched to `sources/inbox/freshrss/` for later ingest.
- FreshRSS credentials are read from local ignored config and are not stored here.

## Accepted

- none

## Maybe

- [Gemma 4 thinking system prompt](https://old.reddit.com/r/LocalLLaMA/comments/1sfjhsx/gemma_4_thinking_system_prompt/)
  - source: `LocalLlama`; published: `2026-04-08T13:02:33+08:00`; decision: `maybe`; score: `60`
  - reason: Relevant to post-training but signal is mixed before full-text fetch.
  - matched: `post-training`
  - downrank: `discussion-source`
- [Gemma 4, llama.cpp, tool calls, and tool results - ChatGPT fixed it for me](https://old.reddit.com/r/LocalLLaMA/comments/1sfj075/gemma_4_llamacpp_tool_calls_and_tool_results/)
  - source: `LocalLlama`; published: `2026-04-08T12:35:57+08:00`; decision: `maybe`; score: `64`
  - reason: Relevant to agent-workflows but signal is mixed before full-text fetch.
  - matched: `agent-workflows`
  - downrank: `discussion-source`

## Reject

- [Last Week in Multimodal AI - Local Edition](https://old.reddit.com/r/LocalLLaMA/comments/1sfk3ml/last_week_in_multimodal_ai_local_edition/)
  - source: `LocalLlama`; published: `2026-04-08T13:36:35+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [In terms of Quality, how good is Bonsai 8B?](https://old.reddit.com/r/LocalLLaMA/comments/1sfk2w5/in_terms_of_quality_how_good_is_bonsai_8b/)
  - source: `LocalLlama`; published: `2026-04-08T13:35:27+08:00`; decision: `reject`; score: `0`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `low-context-discussion`, `question-title`, `no-strong-interest-match`
- [ACE on a USB-HDMI Adapter](https://blazelight.dev/blog/ms2160.mdx)
  - source: `Hacker News`; published: `2026-04-05T05:44:55+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [Native Americans had dice 12k years ago](https://www.nbcnews.com/science/science-news/native-americans-dice-games-probability-study-rcna266426)
  - source: `Hacker News`; published: `2026-04-04T08:59:08+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [微软向“预览体验成员”发送中文邮件：我们对 Windows 质量的承诺](https://www.appinn.com/microsoft-sends-chinese-email-to-windows-insiders-quality-commitment/)
  - source: `小众软件`; published: `2026-04-08T11:51:41+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [Wait is attn rotate already enabled by default since this release tell it support SWA attention?](https://old.reddit.com/r/LocalLLaMA/comments/1sfhafc/wait_is_attn_rotate_already_enabled_by_default/)
  - source: `LocalLlama`; published: `2026-04-08T11:10:24+08:00`; decision: `reject`; score: `54`
  - reason: Low-value metadata due to discussion-source.
  - matched: `llm-systems`
  - downrank: `discussion-source`, `question-title`
- [Protect your shed](https://dylanbutler.dev/blog/protect-your-shed/)
  - source: `Hacker News`; published: `2026-04-08T11:03:33+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [LLM scraper bots are overloading acme.com's HTTPS server](http://acme.com/updates/archive/229.html)
  - source: `Hacker News`; published: `2026-04-08T11:02:56+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [Share your llama-server init strings for Gemma 4 models.](https://old.reddit.com/r/LocalLLaMA/comments/1sfh2ut/share_your_llamaserver_init_strings_for_gemma_4/)
  - source: `LocalLlama`; published: `2026-04-08T11:00:37+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [OpenAI says its new model GPT-2 is too dangerous to release (2019)](https://slate.com/technology/2019/02/openai-gpt2-text-generating-algorithm-ai-dangerous.html)
  - source: `Hacker News`; published: `2026-04-08T10:41:12+08:00`; decision: `reject`; score: `6`
  - reason: Low-value metadata due to discussion-source.
  - downrank: `discussion-source`, `no-strong-interest-match`
- [Desktoptop 3.1多屏版，中文名：这他妈才叫桌面多屏版！](https://www.appinn.com/desktoptop-3-1/)
  - source: `小众软件`; published: `2026-04-07T11:57:49+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [ClipBox – iPhone 剪贴板历史应用\[内购限免\]](https://www.appinn.com/clipbox-phone/)
  - source: `小众软件`; published: `2026-04-06T21:44:38+08:00`; decision: `reject`; score: `0`
  - reason: Low-value metadata due to promo-pricing.
  - downrank: `promo-pricing`, `no-strong-interest-match`
- [微软到底有多少个 Copilot？](https://www.appinn.com/how-many-microsoft-copilot/)
  - source: `小众软件`; published: `2026-04-06T14:45:19+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [高性价比（廉价）SSD VPS 提供商 CloudCone 优惠码，最低 83 元人民币/年](https://www.appinn.com/cloudcone-ssd-vps/)
  - source: `小众软件`; published: `2026-04-06T14:09:21+08:00`; decision: `reject`; score: `48`
  - reason: Low-value metadata due to promo-pricing.
  - matched: `self-hosting`
  - downrank: `promo-pricing`
- [发现频道：最近10日的热门排行榜\[2026年第14期\]](https://www.appinn.com/faxian-top10-2614/)
  - source: `小众软件`; published: `2026-04-06T09:00:54+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [Flare – 在一个应用中，聚合 RSS、X、微博、Mastodon、Bluesky、Misskey 和 Nostr：所有账户，一条时间线](https://www.appinn.com/flareapp-moe/)
  - source: `小众软件`; published: `2026-04-05T16:07:07+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [H.264 流媒体许可费从 10 万美元暴涨到 450 万美元](https://www.appinn.com/h264-vs-av1-hevc-license-change/)
  - source: `小众软件`; published: `2026-04-04T13:06:49+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`
- [阿耳忒弥斯2号上也有两个 Outlook](https://www.appinn.com/artemis-ii-two-outlook/)
  - source: `小众软件`; published: `2026-04-04T12:08:41+08:00`; decision: `reject`; score: `16`
  - reason: Low-value metadata due to no-strong-interest-match.
  - downrank: `no-strong-interest-match`

## Staged Files

- `sources/inbox/freshrss/2026-04-08-gemma-4-thinking-system-prompt-ed13779270.md`
- `sources/inbox/freshrss/2026-04-08-gemma-4-llama-cpp-tool-calls-and-tool-results-chatgpt-fixed-it-for-me-ed1377926f.md`
