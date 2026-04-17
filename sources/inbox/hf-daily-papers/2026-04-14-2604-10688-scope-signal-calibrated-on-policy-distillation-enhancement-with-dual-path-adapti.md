---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, reward-modeling, on-policy-distillation, reasoning, kl-distillation, mle, credit-assignment]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.10688
paper_id: 2604.10688
published: 2026-04-12T04:00:00+08:00
submitted_on_daily: 2026-04-14T19:11:57+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting

## Summary

- one_sentence_summary: SCOPE is a dual-path on-policy distillation method that routes rollouts by correctness and adapts the supervision signal to improve reasoning alignment in large language models.
- why_relevant: It is directly relevant to post-training and reinforcement-learning-based reasoning alignment because it proposes a concrete way to reshape supervision for better training signal quality in on-policy systems.
- filter_reason: Directly targets on-policy reinforcement learning and reasoning alignment with a concrete adaptive post-training method.
- hugging_face_paper: https://huggingface.co/papers/2604.10688
- original_paper: https://arxiv.org/abs/2604.10688
- source_basis: `original abstract page`

## Key Points

- It targets the token-level credit assignment problem in on-policy reinforcement learning by adding dense supervision on top of outcome-level rewards.
- Incorrect trajectories are trained with teacher-perplexity-weighted KL distillation so the method emphasizes teacher guidance where the teacher appears most corrective and down-weights unreliable signals.
- Correct trajectories are trained with student-perplexity-weighted MLE so reinforcement is focused on low-confidence samples near the capability boundary rather than already-mastered ones.
- Both supervision paths use group-level normalization to adjust weight distributions for prompt difficulty variation.
- On six reasoning benchmarks, the paper reports average relative gains of 11.42% in Avg@32 and 7.30% in Pass@32 over competitive baselines.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.10688
- Hugging Face API entry: https://huggingface.co/api/papers/2604.10688
- arXiv abstract: https://arxiv.org/abs/2604.10688

## Paper Metadata

- authors: `Binbin Zheng`, `Xing Ma`, `Yiheng Liang`, `Jingqing Ruan`, `Xiaoliang Fu`, `Kepeng Lin`, `Benchang Zhu`, `Ke Zeng`, `Xunliang Cai`
- ai_keywords: `on-policy reinforcement learning`, `token-level credit assignment`, `on-policy distillation`, `KL divergence`, `teacher-perplexity-weighted KL distillation`, `student-perplexity-weighted MLE`, `group-level normalization`, `reasoning alignment`, `reinforcement learning`
- upvotes: `5`
- num_comments: `1`
- abstract: On-policy reinforcement learning has become the dominant paradigm for reasoning alignment in large language models, yet its sparse, outcome-level rewards make token-level credit assignment notoriously difficult. On-Policy Distillation (OPD) alleviates this by introducing dense, token-level KL supervision from a teacher model, but typically applies this supervision uniformly across all rollouts, ignoring fundamental differences in signal quality. We propose Signal-Calibrated On-Policy Distillation Enhancement (SCOPE), a dual-path adaptive training framework that routes on-policy rollouts by correctness into two complementary supervision paths. For incorrect trajectories, SCOPE performs teacher-perplexity-weighted KL distillation to prioritize instances where the teacher demonstrates genuine corrective capability, while down-weighting unreliable guidance. For correct trajectories, it applies student-perplexity-weighted MLE to concentrate reinforcement on low-confidence samples at the capability boundary rather than over-reinforcing already mastered ones. Both paths employ a group-level normalization to adaptively calibrate weight distributions, accounting for the intrinsic difficulty variance across prompts. Extensive experiments on six reasoning benchmarks show that SCOPE achieves an average relative improvement of 11.42% in Avg@32 and 7.30% in Pass@32 over competitive baselines, demonstrating its consistent effectiveness.
- hf_ai_summary: SCOPE enhances on-policy distillation by adapting supervision paths based on trajectory correctness, using teacher-perplexity-weighted KL distillation for incorrect trajectories and student-perplexity-weighted MLE for correct ones, achieving superior reasoning performance.

## Source Excerpt

On-policy reinforcement learning has become the dominant paradigm for reasoning alignment in large language models, yet its sparse, outcome-level rewards make token-level credit assignment notoriously difficult. On-Policy Distillation (OPD) alleviates this by introducing dense, token-level KL supervision from a teacher model, but typically applies this supervision uniformly across all rollouts, ignoring fundamental differences in signal quality. We propose Signal-Calibrated On-Policy Distillation Enhancement (SCOPE), a dual-path adaptive training framework that routes on-policy rollouts by correctness into two complementary supervision paths. For incorrect trajectories, SCOPE performs teacher-perplexity-weighted KL distillation to prioritize instances where the teacher demonstrates genuine corrective capability, while down-weighting unreliable guidance. For correct trajectories, it applies student-perplexity-weighted MLE to concentrate reinforcement on low-confidence samples at the capability boundary rather than over-reinforcing already mastered ones. Both paths employ a group-level normalization to adaptively calibrate weight distributions, accounting for the intrinsic difficulty variance across prompts. Extensive experiments on six reasoning benchmarks show that SCOPE achieves an average relative improvement of 11.42% in Avg@32 and 7.30% in Pass@32 over competitive baselines, demonstrating its consistent effectiveness.

## Open Questions

- Which teacher and student models were used in the experiments?
- How is trajectory correctness determined during training?
- What exact baselines were compared against, and how large were the improvements on each benchmark?
- How sensitive is SCOPE to the choice of perplexity weighting and group-level normalization?
- Does the method generalize beyond reasoning benchmarks to other post-training tasks?
