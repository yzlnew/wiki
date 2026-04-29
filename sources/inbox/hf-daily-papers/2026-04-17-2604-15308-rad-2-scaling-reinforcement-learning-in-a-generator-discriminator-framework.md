---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, generator-discriminator, autonomous-driving, planning, closed-loop]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.15308
paper_id: 2604.15308
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T08:55:21+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework

## Summary

- one_sentence_summary: RAD-2 is a unified generator-discriminator framework for closed-loop autonomous driving planning that combines diffusion-based trajectory generation with RL-based reranking and generator optimization to improve stability and safety.
- why_relevant: This paper is relevant to reinforcement learning and post-training because it studies how to stabilize RL-style optimization in a generative planner, with an architecture and training scheme that may transfer conceptually to other agentic systems.
- filter_reason: Concrete RL framework with GRPO-style optimization and on-policy training for closed-loop planning, which is methodologically useful beyond driving.
- hugging_face_paper: https://huggingface.co/papers/2604.15308
- original_paper: https://arxiv.org/abs/2604.15308
- source_basis: `original abstract page`

## Key Points

- A diffusion-based generator produces diverse trajectory candidates, while an RL-optimized discriminator reranks them by long-term driving quality.
- The generator-discriminator split is meant to avoid applying sparse scalar rewards directly to a high-dimensional trajectory space, which the paper argues improves optimization stability.
- Temporally Consistent Group Relative Policy Optimization uses temporal coherence to reduce credit assignment difficulty.
- On-policy Generator Optimization turns closed-loop feedback into structured longitudinal optimization signals and shifts the generator toward higher-reward trajectory manifolds.
- BEV-Warp is a high-throughput closed-loop simulation environment that evaluates planning in Bird's-Eye View feature space via spatial warping.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.15308
- Hugging Face API entry: https://huggingface.co/api/papers/2604.15308
- arXiv abstract: https://arxiv.org/abs/2604.15308
- GitHub: https://github.com/hustvl/RAD
- Project page: https://hgao-cv.github.io/RAD-2/

## Paper Metadata

- authors: `Hao Gao`, `Shaoyu Chen`, `Yifan Zhu`, `Yuehao Song`, `Wenyu Liu`, `Qian Zhang`, `Xinggang Wang`
- organization: `Huazhong University of Science and Technology`
- ai_keywords: `diffusion-based planners`, `imitation learning`, `generator-discriminator framework`, `trajectory candidates`, `reinforcement learning`, `temporal consistency`, `policy optimization`, `closed-loop planning`, `Bird's-Eye View`, `spatial warping`, `collision rate reduction`
- upvotes: `25`
- num_comments: `4`
- abstract: High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.
- hf_ai_summary: A unified generator-discriminator framework for autonomous driving motion planning that improves stability and performance through diffusion-based trajectory generation and reinforcement learning optimization.

## Source Excerpt

High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.

## Open Questions

- What exact reward or quality signals does the discriminator use during reranking?
- How is Temporally Consistent Group Relative Policy Optimization implemented in detail?
- What are the main ablations separating gains from the discriminator, the generator optimization, and BEV-Warp?
- How well does the approach generalize beyond the reported urban driving scenarios?
