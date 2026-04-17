---
type: source-summary
status: active
tags: [freshrss, rss, inbox]
source_count: 1
updated: 2026-04-11
source_url: https://old.reddit.com/r/LocalLLaMA/comments/1shzjwx/turboquant_triattention_chip_68_total_kv_cache/
feed_source: LocalLlama
published: 2026-04-11T05:18:28+08:00
decision: accept
score: 96
generator: scripts/update_freshrss.py
---

# TurboQuant + TriAttention (C/HIP): ~6.8× total KV cache reduction in llama.cpp

## Summary

- source_feed: `LocalLlama`
- original_url: https://old.reddit.com/r/LocalLLaMA/comments/1shzjwx/turboquant_triattention_chip_68_total_kv_cache/
- published: `2026-04-11T05:18:28+08:00`
- filter_reason: Strong fit for agent-workflows with useful signal in source/title.

## Feed Metadata

- source_home: https://old.reddit.com/r/LocalLlama/
- categories: `user/-/state/com.google/reading-list`, `user/-/label/未分类`, `user/-/state/org.freshrss/main`, `r/LocalLLaMA`
- feed_summary: Edit (2026-04-11): Correction — my NIAH 28/28 results are TurboQuant-only, not the TriAttention combo. The ~6.8× figure is an arithmetic stack estimate (5.12× × 1.33×), not a validated end-to-end retrieval claim. TriAttention integration is promising on the PPL path but not yet validated for retrieval, especially on...
- fetched_page_title: TurboQuant + TriAttention (C/HIP): ~6.8× total KV cache reduction in llama.cpp : LocalLLaMA
- fetched_page_description: **Edit (2026-04-11):** Correction — my NIAH 28/28 results are TurboQuant-only, not the TriAttention combo. The ~6.8× figure is an arithmetic...

## Full Text

Edit (2026-04-11): Correction — my NIAH 28/28 results are TurboQuant-only, not the TriAttention combo. The ~6.8× figure is an arithmetic stack estimate (5.12× × 1.33×), not a validated end-to-end retrieval claim. TriAttention integration is promising on the PPL path but not yet validated for retrieval, especially on hybrid architectures. See TheTom's V3 analysis for rigorous testing.
Results from combining two KV-cache reduction methods in llama.cpp on AMD/HIP:
TurboQuant KV cache compression (turbo3): ~5.1× reduction
TriAttention KV cache pruning (75% retention): ~1.33× reduction
Combined: ~6.8× total KV reduction
At 131K context: f16 KV = 8.2 GiB → combo ≈ 1.2 GiB.
TurboQuant numbers (Qwen3.5-27B, RX 7900 XTX): - GSM8K: 72.0% on 1319 problems (vs 66% f16) - NIAH: 28/28 up to 64K context - Tool calling: 26/26 - PPL: +0.02% at 4K, -0.9% at 16K - Speed overhead: ~1-2%
TriAttention is based on the recent NVIDIA/MIT paper (arXiv:2604.04921). My implementation is in C/ggml — no Python needed at runtime. Pre-built calibration stats for Qwen3 family included.
As far as I know, this is currently the only HIP/ROCm TurboQuant implementation for llama.cpp and the only C/ggml implementation of TriAttention.
Repos: - TurboQuant (HIP): llama.cpp-turboquant-hip - TriAttention (C/ggml): triattention-ggml - llama.cpp discussion: #20969
3 users currently testing on Strix Halo (gfx1201) and RDNA3 (gfx1100). Feedback and testing results welcome.
submitted by /u/Acrobatic_Bee_6660
[link] [comments]
