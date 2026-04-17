---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, llm-post-training, experience-replay, replay-buffer, compute-efficiency]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.08706
paper_id: 2604.08706
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-14T23:47:01+08:00
decision: accept
score: 95
generator: scripts/update_hf_daily_papers.py
---

# Efficient RL Training for LLMs with Experience Replay

## Summary

- one_sentence_summary: The paper argues that experience replay is useful for LLM post-training and shows that a well-designed replay buffer can cut generation cost substantially without hurting, and sometimes improving, final performance.
- why_relevant: It is directly relevant to reinforcement learning and post-training because it targets the data-efficiency and compute tradeoffs of rollout reuse in LLM training.
- filter_reason: Directly relevant post-training RL method that studies replay buffers and inference-compute tradeoffs for LLM training.
- hugging_face_paper: https://huggingface.co/papers/2604.08706
- original_paper: https://arxiv.org/abs/2604.08706
- source_basis: `original abstract page`

## Key Points

- The work challenges the assumption that LLM post-training must rely on fresh on-policy samples.
- It studies replay buffers systematically for LLM post-training and frames their design as a trade-off between staleness-induced variance, sample diversity, and generation cost.
- The authors claim strict on-policy sampling is suboptimal when rollouts are expensive to generate.
- Empirically, a well-designed replay buffer can reduce inference compute without degrading final model performance, and can sometimes improve it.
- The method is reported to preserve policy entropy, suggesting replay need not collapse exploration behavior.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08706
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08706
- arXiv abstract: https://arxiv.org/abs/2604.08706

## Paper Metadata

- authors: `Charles Arnal`, `Vivien Cabannes`, `Taco Cohen`, `Julia Kempe`, `Remi Munos`
- organization: `Meta Llama`
- ai_keywords: `Experience Replay`, `rollouts`, `reinforcement learning`, `LLM post-training`, `on-policy sampling`, `replay buffers`, `staleness-induced variance`, `sample diversity`, `inference compute`, `policy entropy`
- upvotes: `9`
- num_comments: `1`
- abstract: While Experience Replay - the practice of storing rollouts and reusing them multiple times during training - is a foundational technique in general RL, it remains largely unexplored in LLM post-training due to the prevailing belief that fresh, on-policy data is essential for high performance. In this work, we challenge this assumption. We present a systematic study of replay buffers for LLM post-training, formalizing the optimal design as a trade-off between staleness-induced variance, sample diversity and the high computational cost of generation. We show that strict on-policy sampling is suboptimal when generation is expensive. Empirically, we show that a well-designed replay buffer can drastically reduce inference compute without degrading - and in some cases even improving - final model performance, while preserving policy entropy.
- hf_ai_summary: Experience replay techniques for large language model post-training balance staleness variance and computational costs while maintaining performance and policy entropy.

## Source Excerpt

While Experience Replay - the practice of storing rollouts and reusing them multiple times during training - is a foundational technique in general RL, it remains largely unexplored in LLM post-training due to the prevailing belief that fresh, on-policy data is essential for high performance. In this work, we challenge this assumption. We present a systematic study of replay buffers for LLM post-training, formalizing the optimal design as a trade-off between staleness-induced variance, sample diversity and the high computational cost of generation. We show that strict on-policy sampling is suboptimal when generation is expensive. Empirically, we show that a well-designed replay buffer can drastically reduce inference compute without degrading - and in some cases even improving - final model performance, while preserving policy entropy.

## Open Questions

- What specific replay buffer design choices are used to manage staleness versus diversity?
- Which tasks or benchmarks were used to evaluate performance and compute savings?
- How large were the gains in inference compute and final accuracy or reward?
- Does the method depend on a particular RL objective or model class?
- What does preserving policy entropy mean operationally in their setup?
