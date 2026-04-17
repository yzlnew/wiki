---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, reward-modeling, post-training, reasoning-behavior-shaping, llm-systems, visual-generation, rationalization, test-time-refinement]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.11626
paper_id: 2604.11626
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-16T09:46:38+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time

## Summary

- one_sentence_summary: RationalRewards trains an 8B reward model to generate structured critiques before scoring visual outputs, and uses those critiques both as richer RL rewards and in a test-time generate-critique-refine loop for text-to-image and image-editing systems.
- why_relevant: This is directly relevant to reinforcement learning and post-training because it studies reward modeling as a training signal and shows a critique-driven refinement loop that changes model behavior without additional weight updates.
- filter_reason: Strong reward-modeling and RL paper that uses structured critiques for training-time rewards and test-time refinement.
- hugging_face_paper: https://huggingface.co/papers/2604.11626
- original_paper: https://arxiv.org/abs/2604.11626
- source_basis: `original abstract page`

## Key Points

- The paper argues that scalar reward scores for visual generation throw away the reasoning behind preferences, while multi-dimensional critiques can serve as more informative supervision.
- It introduces Preference-Anchored Rationalization (PARROT), which reconstructs rationales from preference data using anchored generation, consistency filtering, and distillation, avoiding expensive rationale annotations.
- RationalRewards achieves state-of-the-art preference prediction among open-source reward models and is reported to be competitive with Gemini-2.5-Pro while using 10-20x less training data than comparable baselines.
- As an RL reward model, its structured rationales improve both text-to-image and image-editing generators beyond scalar reward alternatives.
- At test time, a Generate-Critique-Refine loop can improve outputs without parameter updates and is reported to match or exceed RL-based fine-tuning on several benchmarks.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11626
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11626
- arXiv abstract: https://arxiv.org/abs/2604.11626
- GitHub: https://github.com/TIGER-AI-Lab/RationalRewards
- Project page: https://tiger-ai-lab.github.io/RationalRewards/

## Paper Metadata

- authors: `Haozhe Wang`, `Cong Wei`, `Weiming Ren`, `Jiaming Liu`, `Fangzhen Lin`, `Wenhu Chen`
- ai_keywords: `reward models`, `visual generation`, `preference prediction`, `reinforcement learning`, `Generate-Critique-Refine loop`, `Preference-Anchored Rationalization`, `PARROT`, `rationalization`, `structured reasoning`, `text-to-image generation`, `image-editing generation`, `RL-based fine-tuning`
- upvotes: `95`
- num_comments: `3`
- abstract: Most reward models for visual generation reduce rich human judgments to a single unexplained score, discarding the reasoning that underlies preference. We show that teaching reward models to produce explicit, multi-dimensional critiques before scoring transforms them from passive evaluators into active optimization tools, improving generators in two complementary ways: at training time, structured rationales provide interpretable, fine-grained rewards for reinforcement learning; at test time, a Generate-Critique-Refine loop turns critiques into targeted prompt revisions that improve outputs without any parameter updates. To train such a reward model without costly rationale annotations, we introduce Preference-Anchored Rationalization (PARROT), a principled framework that recovers high-quality rationales from readily available preference data through anchored generation, consistency filtering, and distillation. The resulting model, RationalRewards (8B), achieves state-of-the-art preference prediction among open-source reward models, competitive with Gemini-2.5-Pro, while using 10-20x less training data than comparable baselines. As an RL reward, it consistently improves text-to-image and image-editing generators beyond scalar alternatives. Most strikingly, its test-time critique-and-refine loop matches or exceeds RL-based fine-tuning on several benchmarks, suggesting that structured reasoning can unlock latent capabilities in existing generators that suboptimal prompts fail to elicit.
- hf_ai_summary: Training reward models to generate multi-dimensional critiques improves visual generation through both enhanced reinforcement learning rewards and test-time refinement loops, achieving state-of-the-art performance with reduced training data requirements.

## Source Excerpt

Most reward models for visual generation reduce rich human judgments to a single unexplained score, discarding the reasoning that underlies preference. We show that teaching reward models to produce explicit, multi-dimensional critiques before scoring transforms them from passive evaluators into active optimization tools, improving generators in two complementary ways: at training time, structured rationales provide interpretable, fine-grained rewards for reinforcement learning; at test time, a Generate-Critique-Refine loop turns critiques into targeted prompt revisions that improve outputs without any parameter updates. To train such a reward model without costly rationale annotations, we introduce Preference-Anchored Rationalization (PARROT), a principled framework that recovers high-quality rationales from readily available preference data through anchored generation, consistency filtering, and distillation. The resulting model, RationalRewards (8B), achieves state-of-the-art preference prediction among open-source reward models, competitive with Gemini-2.5-Pro, while using 10-20x less training data than comparable baselines. As an RL reward, it consistently improves text-to-image and image-editing generators beyond scalar alternatives. Most strikingly, its test-time critique-and-refine loop matches or exceeds RL-based fine-tuning on several benchmarks, suggesting that structured reasoning can unlock latent capabilities in existing generators that suboptimal prompts fail to elicit.

## Open Questions

- How much of the reported gain comes from the critique structure itself versus the PARROT rationale reconstruction pipeline?
- Which benchmarks were used to compare the test-time refine loop against RL-based fine-tuning?
- How well do the recovered rationales align with human explanations, beyond improving downstream reward prediction?
- Does the approach transfer to other generation domains outside text-to-image and image editing?
