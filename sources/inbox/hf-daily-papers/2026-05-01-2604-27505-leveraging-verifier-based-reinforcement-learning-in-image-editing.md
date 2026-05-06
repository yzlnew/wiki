---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, reward-modeling, post-training, grpo, reasoning-behavior-shaping, rlhf, image-editing, verifier]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.27505
paper_id: 2604.27505
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-01T10:43:05+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Leveraging Verifier-Based Reinforcement Learning in Image Editing

## Summary

- one_sentence_summary: Edit-R1 turns image-editing reward modeling from a coarse scorer into a chain-of-thought reasoning verifier, then uses reinforcement learning to improve both the reward model and downstream editing models.
- why_relevant: It is directly relevant to post-training and reward modeling because it combines verifier-style reasoning, preference optimization, and GRPO to shape model behavior through a learned reward signal.
- filter_reason: Directly relevant RLHF/reward-modeling work using verifier-based reasoning and GRPO for post-training.
- hugging_face_paper: https://huggingface.co/papers/2604.27505
- original_paper: https://arxiv.org/abs/2604.27505
- source_basis: `original abstract page`

## Key Points

- The paper argues that image-editing RLHF is bottlenecked by the lack of a robust general reward model that can check multiple instruction requirements separately.
- Edit-R1 introduces an Edit-RRM that decomposes an editing instruction into distinct principles, verifies the edited image against each principle, and aggregates the checks into an interpretable fine-grained reward.
- To build the reward model, the authors use supervised fine-tuning as a cold start to generate CoT reward trajectories, then apply Group Contrastive Preference Optimization (GCPO) with human pairwise preferences to strengthen the pointwise reward model.
- The downstream editing model is trained with GRPO using the resulting reward model, even though the reward is non-differentiable.
- Reported results claim the reward model outperforms strong VLMs such as Seed-1.5-VL and Seed-1.6-VL for editing-specific reward modeling, and that scaling from 3B to 7B parameters improves performance.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27505
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27505
- arXiv abstract: https://arxiv.org/abs/2604.27505

## Paper Metadata

- authors: `Hanzhong Guo`, `Jie Wu`, `Jie Liu`, `Yu Gao`, `Zilyu Ye`, `Linxiao Yuan`, `Xionghui Wang`, `Yizhou Yu`, `Weilin Huang`
- organization: `ByteDance Seed`
- ai_keywords: `Reinforcement Learning from Human Feedback`, `image editing`, `reward model`, `chain-of-thought`, `reasoning verifier`, `supervised fine-tuning`, `Group Contrastive Preference Optimization`, `reinforcement learning`, `non-differentiable reward model`, `GRPO`
- upvotes: `15`
- num_comments: `1`
- abstract: While Reinforcement Learning from Human Feedback (RLHF) has become a pivotal paradigm for text-to-image generation, its application to image editing remains largely unexplored. A key bottleneck is the lack of a robust general reward model for all editing tasks. Existing edit reward models usually give overall scores without detailed checks, ignoring different instruction requirements and causing biased rewards. To address this, we argue that the key is to move from a simple scorer to a reasoning verifier. We introduce Edit-R1, a framework that builds a chain-of-thought (CoT) verifier-based reasoning reward model (RRM) and then leverages it for downstream image editing. The Edit-RRM breaks instructions into distinct principles, evaluates the edited image against each principle, and aggregates these checks into an interpretable, fine-grained reward. To build such an RRM, we first apply supervised fine-tuning (SFT) as a ``cold-start'' to generate CoT reward trajectories. Then, we introduce Group Contrastive Preference Optimization (GCPO), a reinforcement learning algorithm that leverages human pairwise preference data to reinforce our pointwise RRM. After building the RRM, we use GRPO to train editing models with this non-differentiable yet powerful reward model. Extensive experiments demonstrate that our Edit-RRM surpasses powerful VLMs such as Seed-1.5-VL and Seed-1.6-VL as an editing-specific reward model, and we observe a clear scaling trend, with performance consistently improving from 3B to 7B parameters. Moreover, Edit-R1 delivers gains to editing models like FLUX.1-kontext, highlighting its effectiveness in enhancing image editing.
- hf_ai_summary: RLHF-based image editing framework introduces a chain-of-thought verification reward model that improves editing performance through fine-grained reward evaluation and reinforcement learning.

## Source Excerpt

While Reinforcement Learning from Human Feedback (RLHF) has become a pivotal paradigm for text-to-image generation, its application to image editing remains largely unexplored. A key bottleneck is the lack of a robust general reward model for all editing tasks. Existing edit reward models usually give overall scores without detailed checks, ignoring different instruction requirements and causing biased rewards. To address this, we argue that the key is to move from a simple scorer to a reasoning verifier. We introduce Edit-R1, a framework that builds a chain-of-thought (CoT) verifier-based reasoning reward model (RRM) and then leverages it for downstream image editing. The Edit-RRM breaks instructions into distinct principles, evaluates the edited image against each principle, and aggregates these checks into an interpretable, fine-grained reward. To build such an RRM, we first apply supervised fine-tuning (SFT) as a ``cold-start'' to generate CoT reward trajectories. Then, we introduce Group Contrastive Preference Optimization (GCPO), a reinforcement learning algorithm that leverages human pairwise preference data to reinforce our pointwise RRM. After building the RRM, we use GRPO to train editing models with this non-differentiable yet powerful reward model. Extensive experiments demonstrate that our Edit-RRM surpasses powerful VLMs such as Seed-1.5-VL and Seed-1.6-VL as an editing-specific reward model, and we observe a clear scaling trend, with performance consistently improving from 3B to 7B parameters. Moreover, Edit-R1 delivers gains to editing models like FLUX.1-kontext, highlighting its effectiveness in enhancing image editing.

## Open Questions

- What editing benchmarks and human evaluation protocols were used to compare Edit-RRM against Seed-1.5-VL and Seed-1.6-VL?
- How is the instruction decomposed into principles, and who or what defines those principles during training?
- How much of the downstream gain comes from the reward model quality versus the GRPO training setup itself?
- Does the method generalize across different classes of editing instructions, or only the tasks covered in the paper's evaluation set?
