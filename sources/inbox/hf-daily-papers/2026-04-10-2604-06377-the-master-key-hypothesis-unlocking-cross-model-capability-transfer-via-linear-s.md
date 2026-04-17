---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reasoning-behavior-shaping, mechanistic-interpretability, representation-analysis, reasoning, model-transfer, inference-time-intervention]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.06377
paper_id: 2604.06377
published: 2026-04-07T23:02:10+08:00
submitted_on_daily: 2026-04-10T21:52:19+08:00
decision: accept
score: 90
generator: scripts/update_hf_daily_papers.py
---

# The Master Key Hypothesis: Unlocking Cross-Model Capability Transfer via Linear Subspace Alignment

## Summary

- one_sentence_summary: The paper proposes that post-trained capabilities are encoded as transferable low-dimensional directions and presents UNLOCK, a training-free method for aligning and injecting those directions across models to elicit reasoning behaviors without retraining.
- why_relevant: It is directly relevant to post-training and reasoning-shaping because it studies how learned capabilities can be transferred or amplified across models through representation-level interventions rather than additional training.
- filter_reason: Strong fit on post-training, reasoning behavior shaping, and activation-space analysis with a concrete transfer method.
- hugging_face_paper: https://huggingface.co/papers/2604.06377
- original_paper: https://arxiv.org/abs/2604.06377
- source_basis: `original abstract page`

## Key Points

- Introduces the Master Key Hypothesis: capabilities correspond to directions in a low-dimensional latent subspace that can transfer across models via linear alignment.
- UNLOCK extracts a capability direction by contrasting activations from capability-present and capability-absent source variants, then aligns that direction to a target model with a low-rank linear transform.
- The method is training-free and label-free, and is applied at inference time to induce behaviors such as Chain-of-Thought and mathematical reasoning.
- Reported transfers improve reasoning accuracy across scales, including a 12.1% gain on MATH when moving CoT reasoning from Qwen1.5-14B to Qwen1.5-7B.
- The analysis suggests transfer works better when the relevant capability is already present from pre-training, and that the intervention sharpens output distributions toward successful reasoning trajectories.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.06377
- Hugging Face API entry: https://huggingface.co/api/papers/2604.06377
- arXiv abstract: https://arxiv.org/abs/2604.06377

## Paper Metadata

- authors: `Rishab Balasubramanian`, `Pin-Jie Lin`, `Rituraj Sharma`, `Anjie Fang`, `Fardin Abdi`, `Viktor Rozgic`, `Zheng Du`, `Mohit Bansal`, `Tu Vu`
- ai_keywords: `Master Key Hypothesis`, `capability direction`, `latent subspace`, `linear alignment`, `UNLOCK`, `source variants`, `target model`, `Chain-of-Thought`, `mathematical reasoning`, `pre-training`, `post-training`, `inference time`, `output distribution`
- upvotes: `3`
- num_comments: `2`
- abstract: We investigate whether post-trained capabilities can be transferred across models without retraining, with a focus on transfer across different model scales. We propose the Master Key Hypothesis, which states that model capabilities correspond to directions in a low-dimensional latent subspace that induce specific behaviors and are transferable across models through linear alignment. Based on this hypothesis, we introduce UNLOCK, a training-free and label-free framework that extracts a capability direction by contrasting activations between capability-present and capability-absent Source variants, aligns it with a Target model through a low-rank linear transformation, and applies it at inference time to elicit the behavior. Experiments on reasoning behaviors, including Chain-of-Thought (CoT) and mathematical reasoning, demonstrate substantial improvements across model scales without training. For example, transferring CoT reasoning from Qwen1.5-14B to Qwen1.5-7B yields an accuracy gain of 12.1% on MATH, and transferring a mathematical reasoning direction from Qwen3-4B-Base to Qwen3-14B-Base improves AGIEval Math accuracy from 61.1% to 71.3%, surpassing the 67.8% achieved by the 14B post-trained model. Our analysis shows that the success of transfer depends on the capabilities learned during pre-training, and that our intervention amplifies latent capabilities by sharpening the output distribution toward successful reasoning trajectories.
- hf_ai_summary: Post-trained model capabilities can be transferred across different model scales through linear alignment of latent subspace directions without requiring retraining.

## Source Excerpt

We investigate whether post-trained capabilities can be transferred across models without retraining, with a focus on transfer across different model scales. We propose the Master Key Hypothesis, which states that model capabilities correspond to directions in a low-dimensional latent subspace that induce specific behaviors and are transferable across models through linear alignment. Based on this hypothesis, we introduce UNLOCK, a training-free and label-free framework that extracts a capability direction by contrasting activations between capability-present and capability-absent Source variants, aligns it with a Target model through a low-rank linear transformation, and applies it at inference time to elicit the behavior. Experiments on reasoning behaviors, including Chain-of-Thought (CoT) and mathematical reasoning, demonstrate substantial improvements across model scales without training. For example, transferring CoT reasoning from Qwen1.5-14B to Qwen1.5-7B yields an accuracy gain of 12.1% on MATH, and transferring a mathematical reasoning direction from Qwen3-4B-Base to Qwen3-14B-Base improves AGIEval Math accuracy from 61.1% to 71.3%, surpassing the 67.8% achieved by the 14B post-trained model. Our analysis shows that the success of transfer depends on the capabilities learned during pre-training, and that our intervention amplifies latent capabilities by sharpening the output distribution toward successful reasoning trajectories.

## Open Questions

- Which specific layer or representation space is used to extract and apply the capability direction?
- How sensitive is UNLOCK to the choice of source variants and target-model architecture mismatch?
- Does the method generalize beyond reasoning tasks such as CoT and math to other post-trained behaviors?
- What are the limits of transfer when the target model lacks the relevant pre-trained capability?
