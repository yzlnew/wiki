---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, llm-systems, vision-language, reasoning, hallucination, interpretability, multimodal]
source_count: 1
updated: 2026-05-06
source_url: https://arxiv.org/abs/2605.02730
paper_id: 2605.02730
published: 2026-05-04T04:00:00+08:00
submitted_on_daily: 2026-05-05T09:50:14+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# Perceptual Flow Network for Visually Grounded Reasoning

## Summary

- one_sentence_summary: PFlowNet is a visual reasoning method for large vision-language models that decouples perception from reasoning and uses variational reinforcement learning with multi-dimensional rewards to reduce language bias and hallucination.
- why_relevant: It is directly relevant to reinforcement-learning-based post-training for reasoning behavior shaping, especially in a multimodal agent setting where perception, reliability, and interpretability matter.
- filter_reason: Uses variational reinforcement learning and reward shaping to improve visually grounded reasoning in LVLMs.
- hugging_face_paper: https://huggingface.co/papers/2605.02730
- original_paper: https://arxiv.org/abs/2605.02730
- source_basis: `original abstract page`

## Key Points

- The paper argues that standard MLE training does not sufficiently constrain visual trajectories in LVLMs, which can produce language bias and hallucination.
- Existing methods that supervise models with geometric priors from visual experts are described as biased toward geometric precision and weak for reasoning utility.
- PFlowNet replaces rigid alignment to expert priors with a self-conditioned generation process that separates perception from reasoning.
- It combines multi-dimensional rewards with vicinal geometric shaping via variational reinforcement learning to encourage reasoning-oriented perceptual behavior while preserving visual reliability.
- The paper claims a provable performance guarantee and reports strong benchmark results, including new SOTA on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.02730
- Hugging Face API entry: https://huggingface.co/api/papers/2605.02730
- arXiv abstract: https://arxiv.org/abs/2605.02730

## Paper Metadata

- authors: `Yangfu Li`, `Yuning Gong`, `Hongjian Zhan`, `Teng Li`, `Yuanhuiyi Lyu`, `Tianyi Chen`, `Qi Liu`, `Ziyuan Huang`, `Zhihang Zhong`, `Dandan Zheng`, `Yue Lu`
- ai_keywords: `Large-Vision Language Models`, `geometric priors`, `visual trajectories`, `language bias`, `hallucination`, `perceptual flow network`, `self-conditioned generation`, `variational reinforcement learning`, `multi-dimensional rewards`, `visual reasoning`, `V* Bench`, `MME-RealWorld-lite`
- upvotes: `2`
- num_comments: `1`
- abstract: Despite the success of Large-Vision Language Models (LVLMs), general optimization objectives (e.g., standard MLE) fail to constrain visual trajectories, leading to language bias and hallucination. To mitigate this, current methods introduce geometric priors from visual experts as additional supervision. However, we observe that such supervision is typically suboptimal: it is biased toward geometric precision and offers limited reasoning utility. To bridge this gap, we propose Perceptual Flow Network (PFlowNet), which eschews rigid alignment with the expert priors and achieves interpretable yet more effective visual reasoning. Specifically, PFlowNet decouples perception from reasoning to establish a self-conditioned generation process. Based on this, it integrates multi-dimensional rewards with vicinal geometric shaping via variational reinforcement learning, thereby facilitating reasoning-oriented perceptual behaviors while preserving visual reliability. PFlowNet delivers a provable performance guarantee and competitive empirical results, particularly setting new SOTA records on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).
- hf_ai_summary: Perceptual Flow Network addresses limitations in vision-language models by decoupling perception from reasoning and using variational reinforcement learning with multi-dimensional rewards for improved visual reasoning.

## Source Excerpt

Despite the success of Large-Vision Language Models (LVLMs), general optimization objectives (e.g., standard MLE) fail to constrain visual trajectories, leading to language bias and hallucination. To mitigate this, current methods introduce geometric priors from visual experts as additional supervision. However, we observe that such supervision is typically suboptimal: it is biased toward geometric precision and offers limited reasoning utility. To bridge this gap, we propose Perceptual Flow Network (PFlowNet), which eschews rigid alignment with the expert priors and achieves interpretable yet more effective visual reasoning. Specifically, PFlowNet decouples perception from reasoning to establish a self-conditioned generation process. Based on this, it integrates multi-dimensional rewards with vicinal geometric shaping via variational reinforcement learning, thereby facilitating reasoning-oriented perceptual behaviors while preserving visual reliability. PFlowNet delivers a provable performance guarantee and competitive empirical results, particularly setting new SOTA records on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).

## Open Questions

- What are the exact reward dimensions used in the variational reinforcement learning objective?
- How is the self-conditioned generation process implemented in the model architecture or training loop?
- What does the provable performance guarantee formally state, and under what assumptions does it hold?
- How much of the gain comes from vicinal geometric shaping versus the perception-reasoning decoupling?
- How does PFlowNet compare against other LVLM post-training methods beyond the two highlighted benchmarks?
