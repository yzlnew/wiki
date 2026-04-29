---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reward-modeling, reasoning-behavior-shaping, llm-systems, llm, supervised-finetuning, policy-gradient, stability]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.14258
paper_id: 2604.14258
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-21T13:47:29+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification

## Summary

- one_sentence_summary: GFT reframes supervised fine-tuning as a problematic special case of policy gradient optimization and introduces group-based contrastive supervision plus adaptive weight rectification to make post-training more stable and RL-friendly.
- why_relevant: It directly targets post-training for LLMs and connects supervised fine-tuning to reinforcement-learning dynamics, which is relevant to RL post-training and agent-training pipelines.
- filter_reason: Directly targets post-training and reward fine-tuning with a policy-gradient view of SFT plus a stabilizing method.
- hugging_face_paper: https://huggingface.co/papers/2604.14258
- original_paper: https://arxiv.org/abs/2604.14258
- source_basis: `original abstract page`

## Key Points

- The paper argues that SFT can be viewed as policy-gradient optimization with extremely sparse implicit rewards and unstable inverse-probability weighting.
- This interpretation is used to explain three failure modes: single-path dependency, entropy collapse, and gradient explosion.
- Group Fine-Tuning (GFT) adds Group Advantage Learning, which builds diverse response groups and uses normalized contrastive supervision to reduce reward sparsity.
- GFT also adds Dynamic Coefficient Rectification, which adaptively bounds inverse-probability weights to stabilize optimization while keeping efficient knowledge injection.
- The reported experiments show GFT outperforming SFT-based methods and producing policies that work more smoothly with later RL training.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14258
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14258
- arXiv abstract: https://arxiv.org/abs/2604.14258
- GitHub: https://github.com/ZJU-OmniAI/GFT
- Project page: https://arxiv.org/abs/2604.14258

## Paper Metadata

- authors: `Wangjie Gan`, `Miao Pan`, `Linbo Xi`, `Wenqi Zhang`, `Jintao Chen`, `Jianwei Yin`, `Xuhong Zhang`
- organization: `ZJU-OmniAI`
- ai_keywords: `supervised fine-tuning`, `reinforcement learning`, `policy gradient optimization`, `implicit reward`, `inverse-probability weighting`, `single-path dependency`, `entropy collapse`, `gradient explosion`, `Group Fine-Tuning`, `Group Advantage Learning`, `Dynamic Coefficient Rectification`
- upvotes: `19`
- num_comments: `2`
- abstract: Large language models are typically post-trained using supervised fine-tuning (SFT) and reinforcement learning (RL), yet effectively unifying efficient knowledge injection with robust generalization remains challenging. In this work, we provide a training-dynamics analysis showing that SFT can be interpreted as a special case of policy gradient optimization with an extremely sparse implicit reward and unstable inverse-probability weighting, which together lead to single-path dependency, entropy collapse, and gradient explosion. Motivated by this diagnosis, we propose Group Fine-Tuning (GFT), a unified post-training framework that addresses these intrinsic limitations through two mechanisms: Group Advantage Learning, which constructs diverse response groups and derives normalized contrastive supervision to alleviate reward sparsity, and Dynamic Coefficient Rectification, which adaptively bounds inverse-probability weights to stabilize optimization while preserving efficient knowledge injection. Experiments demonstrate that GFT consistently surpasses SFT-based methods and yields policies that integrate more smoothly with subsequent RL training.
- hf_ai_summary: Group Fine-Tuning addresses limitations in supervised fine-tuning by using diverse response groups and adaptive weight bounding to improve training stability and efficiency.

## Source Excerpt

Large language models are typically post-trained using supervised fine-tuning (SFT) and reinforcement learning (RL), yet effectively unifying efficient knowledge injection with robust generalization remains challenging. In this work, we provide a training-dynamics analysis showing that SFT can be interpreted as a special case of policy gradient optimization with an extremely sparse implicit reward and unstable inverse-probability weighting, which together lead to single-path dependency, entropy collapse, and gradient explosion. Motivated by this diagnosis, we propose Group Fine-Tuning (GFT), a unified post-training framework that addresses these intrinsic limitations through two mechanisms: Group Advantage Learning, which constructs diverse response groups and derives normalized contrastive supervision to alleviate reward sparsity, and Dynamic Coefficient Rectification, which adaptively bounds inverse-probability weights to stabilize optimization while preserving efficient knowledge injection. Experiments demonstrate that GFT consistently surpasses SFT-based methods and yields policies that integrate more smoothly with subsequent RL training.

## Open Questions

- What benchmarks and model scales were used to evaluate GFT?
- How much does GFT improve downstream RL performance relative to standard SFT baselines?
- What exact form does the normalized contrastive supervision take in Group Advantage Learning?
- How is the inverse-probability bound chosen or scheduled in Dynamic Coefficient Rectification?
