---
type: source-summary
status: active
tags: [freshrss, rss, inbox]
source_count: 1
updated: 2026-04-08
source_url: https://old.reddit.com/r/LocalLLaMA/comments/1sfjhsx/gemma_4_thinking_system_prompt/
feed_source: LocalLlama
published: 2026-04-08T13:02:33+08:00
decision: maybe
score: 60
generator: scripts/update_freshrss.py
---

# Gemma 4 thinking system prompt

## Summary

- source_feed: `LocalLlama`
- original_url: https://old.reddit.com/r/LocalLLaMA/comments/1sfjhsx/gemma_4_thinking_system_prompt/
- published: `2026-04-08T13:02:33+08:00`
- filter_reason: Relevant to post-training but signal is mixed before full-text fetch.

## Feed Metadata

- source_home: https://old.reddit.com/r/LocalLlama/
- categories: `user/-/state/com.google/reading-list`, `user/-/label/未分类`, `user/-/state/org.freshrss/main`, `r/LocalLLaMA`
- feed_summary: I like to be able to enable and disable thinking using a system prompt, so that I can control what which prompts generate thinking tokens rather than relying on the model to choose for me. It's one of the reasons I loved Qwen-30b-A3b. I'm having trouble getting this same setup working for the gemma 4 models. Right n...
- fetched_page_title: Gemma 4 thinking system prompt : LocalLLaMA
- fetched_page_description: I like to be able to enable and disable thinking using a system prompt, so that I can control what which prompts generate thinking tokens rather...

## Full Text

I like to be able to enable and disable thinking using a system prompt, so that I can control what which prompts generate thinking tokens rather than relying on the model to choose for me. It's one of the reasons I loved Qwen-30b-A3b.
I'm having trouble getting this same setup working for the gemma 4 models. Right now playing with the 26b. The model will sometimes respond to a system prompt asking it to skip reasoning, sometimes not. If I put `<thought off>` in the user prompt before my own content, that seems to work well. However that isn't really practical for api calls and the like.
I'm curious if anyone has been able to devise a way to toggle thinking on/off using system prompts and/or chat templates with the gemma4 models?
submitted by /u/No_Information9314
[link] [comments]
