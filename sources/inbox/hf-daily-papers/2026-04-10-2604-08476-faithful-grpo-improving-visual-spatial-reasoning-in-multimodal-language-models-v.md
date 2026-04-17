---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, reward-modeling, llm-systems, multimodal, reasoning, grounding, constrained-optimization, grpo]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.08476
paper_id: 2604.08476
published: 2026-04-09T21:15:47+08:00
submitted_on_daily: 2026-04-10T17:09:54+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization

## Summary

- one_sentence_summary: Faithful GRPO is a constrained GRPO variant for multimodal reasoning models that improves spatial reasoning by enforcing logical consistency and visual grounding during RL post-training.
- why_relevant: This is directly relevant to RL post-training and agentic reasoning because it shows how constrained policy optimization can shape not just accuracy but also the faithfulness of intermediate reasoning in multimodal models.
- filter_reason: A concrete GRPO variant for RLVR that improves reasoning faithfulness and grounding fits post-training and reward-optimization priorities.
- hugging_face_paper: https://huggingface.co/papers/2604.08476
- original_paper: https://arxiv.org/abs/2604.08476
- source_basis: `original abstract page`

## Key Points

- The paper argues that RL with verifiable rewards can boost benchmark accuracy while degrading Chain-of-Thought quality, producing answers that are inconsistent or poorly grounded in the image.
- It studies this failure mode across seven real-world spatial reasoning benchmarks and reports that the issue affects existing MRMs including ViGoRL-Spatial, TreeVGR, and models trained with standard GRPO.
- It defines reasoning quality along two axes: logical consistency between the CoT and final answer, and visual grounding of reasoning steps to objects, attributes, and spatial relations in the image.
- Faithful GRPO (FGRPO) adds consistency and grounding as constraints via Lagrangian dual ascent, and folds batch-level constraint signals into group-level advantage computation with adaptive weighting.
- On Qwen2.5-VL-7B and 3B across seven spatial datasets, FGRPO reduces inconsistency from 24.5% to 1.7%, improves grounding by 13%, and also improves final answer accuracy over plain GRPO.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08476
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08476
- arXiv abstract: https://arxiv.org/abs/2604.08476

## Paper Metadata

- authors: `Sai Srinivas Kancheti`, `Aditya Kanade`, `Rohit Sinha`, `Vineeth N Balasubramanian`, `Tanuja Ganu`
- organization: `Microsoft`
- ai_keywords: `Multimodal reasoning models`, `reinforcement learning with verifiable rewards`, `Chain-of-Thought`, `visual reasoning benchmarks`, `Group Relative Policy Optimization`, `Lagrangian dual ascent`, `consistency constraints`, `grounding constraints`, `advantage computation`, `spatial reasoning benchmarks`, `Qwen2.5-VL`
- upvotes: `4`
- num_comments: `2`
- abstract: Multimodal reasoning models (MRMs) trained with reinforcement learning with verifiable rewards (RLVR) show improved accuracy on visual reasoning benchmarks. However, we observe that accuracy gains often come at the cost of reasoning quality: generated Chain-of-Thought (CoT) traces are frequently inconsistent with the final answer and poorly grounded in the visual evidence. We systematically study this phenomenon across seven challenging real-world spatial reasoning benchmarks and find that it affects contemporary MRMs such as ViGoRL-Spatial, TreeVGR as well as our own models trained with standard Group Relative Policy Optimization (GRPO). We characterize CoT reasoning quality along two complementary axes: "logical consistency" (does the CoT entail the final answer?) and "visual grounding" (does each reasoning step accurately describe objects, attributes, and spatial relationships in the image?). To address this, we propose Faithful GRPO (FGRPO), a variant of GRPO that enforces consistency and grounding as constraints via Lagrangian dual ascent. FGRPO incorporates batch-level consistency and grounding constraints into the advantage computation within a group, adaptively adjusting the relative importance of constraints during optimization. We evaluate FGRPO on Qwen2.5-VL-7B and 3B backbones across seven spatial datasets. Our results show that FGRPO substantially improves reasoning quality, reducing the inconsistency rate from 24.5% to 1.7% and improving visual grounding scores by +13%. It also improves final answer accuracy over simple GRPO, demonstrating that faithful reasoning enables better answers.
- hf_ai_summary: Researchers investigate how reinforcement learning with verifiable rewards can improve visual reasoning accuracy while maintaining logical consistency and visual grounding in multimodal reasoning models, proposing a constrained optimization method called Faithful GRPO that enhances both reasoning quality and final answer accuracy.

## Source Excerpt

Multimodal reasoning models (MRMs) trained with reinforcement learning with verifiable rewards (RLVR) show improved accuracy on visual reasoning benchmarks. However, we observe that accuracy gains often come at the cost of reasoning quality: generated Chain-of-Thought (CoT) traces are frequently inconsistent with the final answer and poorly grounded in the visual evidence. We systematically study this phenomenon across seven challenging real-world spatial reasoning benchmarks and find that it affects contemporary MRMs such as ViGoRL-Spatial, TreeVGR as well as our own models trained with standard Group Relative Policy Optimization (GRPO). We characterize CoT reasoning quality along two complementary axes: "logical consistency" (does the CoT entail the final answer?) and "visual grounding" (does each reasoning step accurately describe objects, attributes, and spatial relationships in the image?). To address this, we propose Faithful GRPO (FGRPO), a variant of GRPO that enforces consistency and grounding as constraints via Lagrangian dual ascent. FGRPO incorporates batch-level consistency and grounding constraints into the advantage computation within a group, adaptively adjusting the relative importance of constraints during optimization. We evaluate FGRPO on Qwen2.5-VL-7B and 3B backbones across seven spatial datasets. Our results show that FGRPO substantially improves reasoning quality, reducing the inconsistency rate from 24.5% to 1.7% and improving visual grounding scores by +13%. It also improves final answer accuracy over simple GRPO, demonstrating that faithful reasoning enables better answers.

## Open Questions

- How are the consistency and grounding constraints computed in practice for each batch?
- Does FGRPO generalize beyond spatial reasoning benchmarks to other multimodal tasks?
- What are the compute or stability tradeoffs of the Lagrangian dual ascent procedure versus standard GRPO?
