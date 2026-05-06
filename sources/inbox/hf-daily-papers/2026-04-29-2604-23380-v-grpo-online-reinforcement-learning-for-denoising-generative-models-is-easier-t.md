---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, rlhf, grpo, reward-modeling, llm-systems, diffusion, generative-models, text-to-image, alignment]
source_count: 1
updated: 2026-04-30
source_url: https://arxiv.org/abs/2604.23380
paper_id: 2604.23380
published: 2026-04-25T04:00:00+08:00
submitted_on_daily: 2026-04-29T18:07:03+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# V-GRPO: Online Reinforcement Learning for Denoising Generative Models Is Easier than You Think

## Summary

- one_sentence_summary: V-GRPO is an online reinforcement learning method for post-training denoising generative models that makes ELBO-based policy-gradient optimization stable and efficient enough to outperform prior MDP-based approaches in text-to-image synthesis.
- why_relevant: It is directly relevant to reinforcement-learning post-training and agent-style optimization because it proposes a practical RL method for aligning generative models, with a concrete optimization mechanism and efficiency gains.
- filter_reason: Directly targets post-training RL with GRPO and proposes an implementable alignment method for generative models.
- hugging_face_paper: https://huggingface.co/papers/2604.23380
- original_paper: https://arxiv.org/abs/2604.23380
- source_basis: `original abstract page`

## Key Points

- The paper targets online RL alignment of denoising generative models with human preferences or verifiable rewards, where direct policy-gradient training is difficult because likelihoods are intractable.
- Prior work split between MDP-over-trajectory methods, which are stable but inefficient, and ELBO-based likelihood surrogates, which had underperformed on visual generation.
- The central claim is that ELBO-based surrogates can work well if surrogate variance is reduced and gradient steps are controlled.
- V-GRPO combines ELBO-based surrogates with Group Relative Policy Optimization (GRPO) and adds simple implementation techniques to improve stability and efficiency.
- The method reports state-of-the-art text-to-image synthesis performance and faster training than MixGRPO and DiffusionNFT.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.23380
- Hugging Face API entry: https://huggingface.co/api/papers/2604.23380
- arXiv abstract: https://arxiv.org/abs/2604.23380
- GitHub: https://github.com/tang-bd/v-grpo

## Paper Metadata

- authors: `Bingda Tang`, `Yuhui Zhang`, `Xiaohan Wang`, `Jiayuan Mao`, `Ludwig Schmidt`, `Serena Yeung-Levy`
- organization: `Stanford University`
- ai_keywords: `denoising generative models`, `policy-gradient`, `reinforcement learning`, `Markov decision process`, `diffusion evidence lower bound`, `variational inference`, `Group Relative Policy Optimization`, `text-to-image synthesis`, `surrogate variance`, `gradient steps`
- upvotes: `2`
- num_comments: `1`
- abstract: Aligning denoising generative models with human preferences or verifiable rewards remains a key challenge. While policy-gradient online reinforcement learning (RL) offers a principled post-training framework, its direct application is hindered by the intractable likelihoods of these models. Prior work therefore either optimizes an induced Markov decision process (MDP) over sampling trajectories, which is stable but inefficient, or uses likelihood surrogates based on the diffusion evidence lower bound (ELBO), which have so far underperformed on visual generation. Our key insight is that the ELBO-based approach can, in fact, be made both stable and efficient. By reducing surrogate variance and controlling gradient steps, we show that this approach can beat MDP-based methods. To this end, we introduce Variational GRPO (V-GRPO), a method that integrates ELBO-based surrogates with the Group Relative Policy Optimization (GRPO) algorithm, alongside a set of simple yet essential techniques. Our method is easy to implement, aligns with pretraining objectives, and avoids the limitations of MDP-based methods. V-GRPO achieves state-of-the-art performance in text-to-image synthesis, while delivering a 2times speedup over MixGRPO and a 3times speedup over DiffusionNFT.
- hf_ai_summary: Researchers developed a novel method called Variational GRPO that improves text-to-image synthesis by combining ELBO-based surrogates with Group Relative Policy Optimization, achieving faster and more efficient alignment of generative models with human preferences compared to existing approaches.

## Source Excerpt

Aligning denoising generative models with human preferences or verifiable rewards remains a key challenge. While policy-gradient online reinforcement learning (RL) offers a principled post-training framework, its direct application is hindered by the intractable likelihoods of these models. Prior work therefore either optimizes an induced Markov decision process (MDP) over sampling trajectories, which is stable but inefficient, or uses likelihood surrogates based on the diffusion evidence lower bound (ELBO), which have so far underperformed on visual generation. Our key insight is that the ELBO-based approach can, in fact, be made both stable and efficient. By reducing surrogate variance and controlling gradient steps, we show that this approach can beat MDP-based methods. To this end, we introduce Variational GRPO (V-GRPO), a method that integrates ELBO-based surrogates with the Group Relative Policy Optimization (GRPO) algorithm, alongside a set of simple yet essential techniques. Our method is easy to implement, aligns with pretraining objectives, and avoids the limitations of MDP-based methods. V-GRPO achieves state-of-the-art performance in text-to-image synthesis, while delivering a $2\times$ speedup over MixGRPO and a $3\times$ speedup over DiffusionNFT.

## Open Questions

- What specific variance-reduction techniques does V-GRPO use?
- How are gradient steps controlled in practice?
- Which text-to-image benchmarks or reward setups were used to establish state-of-the-art performance?
- Does the method generalize beyond text-to-image synthesis to other denoising generative models or reward types?
