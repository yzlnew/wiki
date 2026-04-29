---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, reward-modeling, post-training, reasoning-behavior-shaping, preferences, rubrics, evaluation, rl]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.13618
paper_id: 2604.13618
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-17T09:02:08+08:00
decision: accept
score: 96
generator: scripts/update_hf_daily_papers.py
---

# C2: Scalable Rubric-Augmented Reward Modeling from Binary Preferences

## Summary

- one_sentence_summary: C2 is a rubric-augmented reward modeling framework that learns helpful rubrics from binary preferences and uses a critical verifier to reject misleading rubrics at inference time.
- why_relevant: This is directly relevant to reward modeling and post-training because it improves preference judgment quality with scalable rubric generation, and it touches agentic evaluation by making reward-model-based verification more reliable.
- filter_reason: Directly about reward modeling and scalable post-training with binary preferences, which is a top-priority area.
- hugging_face_paper: https://huggingface.co/papers/2604.13618
- original_paper: https://arxiv.org/abs/2604.13618
- source_basis: `original abstract page`

## Key Points

- The paper targets rubric-augmented verification for reward models, where explicit evaluation criteria can improve judgments but are usually expensive to annotate.
- It identifies a failure mode in rubric generation: low-quality rubrics can mislead reward models instead of helping them.
- C2 trains a cooperative rubric generator and a critical verifier using only binary preferences, without external rubric annotations.
- Training uses contrastive helpful-versus-misleading rubric pairs synthesized by measuring how each rubric shifts the reward model toward or away from the correct preference.
- Reported results include up to 6.5 points gain on RM-Bench and 6.0 points length-controlled win rate on AlpacaEval 2.0, with an 8B reward model matching a rubric-enabled 4x larger model.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.13618
- Hugging Face API entry: https://huggingface.co/api/papers/2604.13618
- arXiv abstract: https://arxiv.org/abs/2604.13618
- GitHub: https://github.com/asahi-research/C2

## Paper Metadata

- authors: `Akira Kawabata`, `Saku Sugawara`
- ai_keywords: `reward models`, `rubric generation`, `binary preferences`, `cooperative communication`, `critical verification`, `rubric augmentation`, `reward model judgments`, `RM-Bench`, `AlpacaEval 2.0`
- upvotes: `3`
- num_comments: `2`
- abstract: Rubric-augmented verification guides reward models with explicit evaluation criteria, yielding more reliable judgments than single-model verification. However, most existing methods require costly rubric annotations, limiting scalability. Moreover, we find that rubric generation is vulnerable to a failure of cooperation; low-quality rubrics actively mislead reward models rather than help. Inspired by the principle of cooperative communication, we propose Cooperative yet Critical reward modeling (C2), a framework that significantly improves reward model judgments by having the reward model critically collaborate with a rubric generator trained solely from binary preferences. In C2, we synthesize helpful and misleading rubric pairs by measuring how each rubric shifts the reward model toward or away from the correct preference. Using these contrastive pairs, we train a cooperative rubric generator to propose helpful rubrics, and a critical verifier to assess rubric validity before making its judgment, following only rubrics it deems helpful at inference time. C2 outperforms reasoning reward models trained on the same binary preferences, with gains of up to 6.5 points on RM-Bench and 6.0 points length-controlled win rate on AlpacaEval 2.0. Without external rubric annotations, C2 enables an 8B reward model to match performance achieved with rubrics from a 4times larger model. Overall, our work demonstrates that eliciting deliberate cooperation in rubric-augmented verification makes reward models more trustworthy in a scalable way.
- hf_ai_summary: Cooperative yet Critical reward modeling (C2) enhances reward model reliability by enabling critical collaboration between a reward model and a rubric generator trained exclusively from binary preferences, achieving superior performance without requiring costly rubric annotations.

## Source Excerpt

Rubric-augmented verification guides reward models with explicit evaluation criteria, yielding more reliable judgments than single-model verification. However, most existing methods require costly rubric annotations, limiting scalability. Moreover, we find that rubric generation is vulnerable to a failure of cooperation; low-quality rubrics actively mislead reward models rather than help. Inspired by the principle of cooperative communication, we propose Cooperative yet Critical reward modeling (C2), a framework that significantly improves reward model judgments by having the reward model critically collaborate with a rubric generator trained solely from binary preferences. In C2, we synthesize helpful and misleading rubric pairs by measuring how each rubric shifts the reward model toward or away from the correct preference. Using these contrastive pairs, we train a cooperative rubric generator to propose helpful rubrics, and a critical verifier to assess rubric validity before making its judgment, following only rubrics it deems helpful at inference time. C2 outperforms reasoning reward models trained on the same binary preferences, with gains of up to 6.5 points on RM-Bench and 6.0 points length-controlled win rate on AlpacaEval 2.0. Without external rubric annotations, C2 enables an 8B reward model to match performance achieved with rubrics from a 4$\times$ larger model. Overall, our work demonstrates that eliciting deliberate cooperation in rubric-augmented verification makes reward models more trustworthy in a scalable way.

## Open Questions

- What exact binary-preference datasets were used to train and evaluate C2?
- How is the helpful-versus-misleading rubric signal computed in practice?
- What is the runtime or inference overhead of the critical verifier?
- How does C2 compare with other rubric-free reward modeling approaches beyond the reported benchmarks?
