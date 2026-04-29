---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, offline-rl, llm-post-training, optimal-transport, gradient-flow, behavior-regularization]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14265
paper_id: 2604.14265
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-18T03:12:38+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Reinforcement Learning via Value Gradient Flow

## Summary

- one_sentence_summary: Value Gradient Flow (VGF) reframes behavior-regularized reinforcement learning as an optimal transport problem solved by discrete gradient flow, using value gradients to move samples from a reference distribution toward higher-value policies without explicit policy parameterization.
- why_relevant: This is directly relevant to reinforcement learning post-training and LLM RL finetuning because it proposes a scalable alternative for constrained policy improvement, with an explicit mechanism for controlling how far updates move from the base model or dataset.
- filter_reason: A technically substantive RL/post-training method that directly targets behavior-regularized RL and LLM RL finetuning with benchmark gains.
- hugging_face_paper: https://huggingface.co/papers/2604.14265
- original_paper: https://arxiv.org/abs/2604.14265
- source_basis: `original abstract page`

## Key Points

- Targets behavior-regularized RL, where keeping updates close to a reference distribution is important to avoid value over-optimization from out-of-distribution extrapolation.
- Positions VGF as an alternative to reparameterized policy gradient methods, which the paper says are hard to scale to large generative models, and to reject sampling, which can be too conservative.
- Forms the problem as optimal transport from the reference distribution to the value-induced optimal policy distribution.
- Uses discrete gradient flow: particles initialized from the reference distribution are guided by value gradients, with regularization controlled implicitly through a transport budget.
- Claims adaptive test-time scaling is possible by changing the transport budget, and reports state-of-the-art results on D4RL, OGBench, and LLM RL tasks.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14265
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14265
- arXiv abstract: https://arxiv.org/abs/2604.14265
- GitHub: https://github.com/ryanxhr/vgf
- Project page: https://ryanxhr.github.io/vgf/

## Paper Metadata

- authors: `Haoran Xu`, `Kaiwen Hu`, `Somayeh Sojoudi`, `Amy Zhang`
- ai_keywords: `behavior-regularized reinforcement learning`, `reference distribution`, `value over-optimization`, `reparameterized policy gradient`, `reject sampling`, `optimal transport problem`, `discrete gradient flow`, `value gradients`, `transport budget`, `adaptive test-time scaling`
- upvotes: `5`
- num_comments: `2`
- abstract: We study behavior-regularized reinforcement learning (RL), where regularization toward a reference distribution (the dataset in offline RL or the base model in LLM RL finetuning) is essential to prevent value over-optimization caused by erroneous out-of-distribution extrapolation. Existing methods either rely on reparameterized policy gradient, which are difficult to scale to large generative models, or on reject sampling, which can be overly conservative when attempting to move beyond the behavior support. In this paper, we propose Value Gradient Flow (VGF), a scalable new paradigm for behavior-regularized RL. VGF casts behavior-regularized RL as an optimal transport problem that maps the reference distribution to the value-induced optimal policy distribution. We solve this transport problem via discrete gradient flow, where value gradients guide particles initialized from the reference distribution. Our analysis shows that VGF imposes regularization implicitly by controlling the transport budget. VGF eliminates explicit policy parameterization while remaining expressive and flexible, this enables adaptive test-time scaling by adjusting the transport budget. Extensive experiments demonstrate that VGF significantly outperforms prior methods, achieving state-of-the-art results on offline RL benchmarks (D4RL, OGBench) and LLM RL tasks. Code and runs can be found at https://ryanxhr.github.io/vgf.
- hf_ai_summary: Value Gradient Flow presents a scalable approach to behavior-regularized reinforcement learning by formulating it as an optimal transport problem solved through discrete gradient flow, enabling adaptive test-time scaling and outperforming existing methods on offline RL and LLM RL benchmarks.

## Source Excerpt

We study behavior-regularized reinforcement learning (RL), where regularization toward a reference distribution (the dataset in offline RL or the base model in LLM RL finetuning) is essential to prevent value over-optimization caused by erroneous out-of-distribution extrapolation. Existing methods either rely on reparameterized policy gradient, which are difficult to scale to large generative models, or on reject sampling, which can be overly conservative when attempting to move beyond the behavior support. In this paper, we propose Value Gradient Flow (VGF), a scalable new paradigm for behavior-regularized RL. VGF casts behavior-regularized RL as an optimal transport problem that maps the reference distribution to the value-induced optimal policy distribution. We solve this transport problem via discrete gradient flow, where value gradients guide particles initialized from the reference distribution. Our analysis shows that VGF imposes regularization implicitly by controlling the transport budget. VGF eliminates explicit policy parameterization while remaining expressive and flexible, this enables adaptive test-time scaling by adjusting the transport budget. Extensive experiments demonstrate that VGF significantly outperforms prior methods, achieving state-of-the-art results on offline RL benchmarks (D4RL, OGBench) and LLM RL tasks. Code and runs can be found at this https URL .

## Open Questions

- How is the transport budget chosen in practice, and how sensitive are results to it?
- What exact discrete gradient flow update rule does VGF use, and what are its compute costs relative to prior methods?
- How does VGF behave when the reference distribution is poor or when moving substantially beyond behavior support is necessary?
- What offline RL and LLM RL tasks were used for evaluation, and how large were the gains over the strongest baselines?
