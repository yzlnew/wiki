---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, llm-systems, rlvr, llm, exploration-exploitation, perplexity, reward-allocation, function-calling, reasoning]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.13902
paper_id: 2604.13902
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-20T18:02:53+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off

## Summary

- one_sentence_summary: DiPO is an RLVR method for LLM post-training that separates samples by perplexity into exploration and exploitation subspaces, then uses bidirectional reward allocation to stabilize optimization and improve performance.
- why_relevant: This is directly relevant to reinforcement-learning post-training for LLMs and to agent/tool-use settings because it proposes a training-time mechanism for improving reasoning and function-calling behavior.
- filter_reason: A concrete RLVR post-training method for LLM reasoning and function calling with a new exploration-exploitation optimization mechanism.
- hugging_face_paper: https://huggingface.co/papers/2604.13902
- original_paper: https://arxiv.org/abs/2604.13902
- source_basis: `original abstract page`

## Key Points

- The paper targets a central RLVR problem: balancing exploration and exploitation during LLM reasoning training, especially across very hard and very easy samples.
- It introduces a perplexity-space disentangling strategy that partitions training samples into high-perplexity exploration subspaces and low-perplexity exploitation subspaces.
- It adds a bidirectional reward allocation mechanism designed to guide exploration and exploitation while minimizing disruption to verification rewards.
- The method is evaluated on two tasks: mathematical reasoning and function calling.
- The reported result is improved LLM performance, with the authors attributing gains to a finer-grained exploration-exploitation trade-off.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.13902
- Hugging Face API entry: https://huggingface.co/api/papers/2604.13902
- arXiv abstract: https://arxiv.org/abs/2604.13902

## Paper Metadata

- authors: `Xiaofan Li`, `Ming Yang`, `Zhiyuan Ma`, `Shichao Ma`, `Jintao Du`, `Yu Cheng`, `Weiqiang Wang`, `Zhizhong Zhang`, `Xin Tan`, `Yanyun Qu`, `Lizhuang Ma`, `Yuan Xie`
- organization: `East China Normal University`
- ai_keywords: `reinforcement learning`, `large language models`, `exploration-exploitation trade-off`, `perplexity space`, `disentangling strategy`, `bidirectional reward allocation`, `policy optimization`, `mathematical reasoning`, `function calling`
- upvotes: `1`
- num_comments: `2`
- abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant advances in the reasoning capabilities of Large Language Models (LLMs). However, effectively managing the exploration and exploitation trade-off remains a critical challenge. In this paper, we fully analyze the exploration and exploitation dilemma of extremely hard and easy samples during the training and propose a new fine-grained trade-off mechanism. Concretely, we introduce a perplexity space disentangling strategy that divides the sample space into distinct exploration (high perplexity) and exploitation (low perplexity) subspaces, thereby mining fine-grained samples requiring exploration-exploitation trade-off. Subsequently, we propose a bidirectional reward allocation mechanism with a minimum impact on verification rewards to implement perplexity-guided exploration and exploitation, enabling more stable policy optimization. Finally, we have evaluated our method on two mainstream tasks: mathematical reasoning and function calling, and experimental results demonstrate the superiority of the proposed method, confirming its effectiveness in enhancing LLM performance by fine-grained exploration-exploitation trade-off.
- hf_ai_summary: A novel reinforcement learning approach for large language models that addresses the exploration-exploitation trade-off through perplexity-based sample partitioning and bidirectional reward allocation mechanisms.

## Source Excerpt

Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant advances in the reasoning capabilities of Large Language Models (LLMs). However, effectively managing the exploration and exploitation trade-off remains a critical challenge. In this paper, we fully analyze the exploration and exploitation dilemma of extremely hard and easy samples during the training and propose a new fine-grained trade-off mechanism. Concretely, we introduce a perplexity space disentangling strategy that divides the sample space into distinct exploration (high perplexity) and exploitation (low perplexity) subspaces, thereby mining fine-grained samples requiring exploration-exploitation trade-off. Subsequently, we propose a bidirectional reward allocation mechanism with a minimum impact on verification rewards to implement perplexity-guided exploration and exploitation, enabling more stable policy optimization. Finally, we have evaluated our method on two mainstream tasks: mathematical reasoning and function calling, and experimental results demonstrate the superiority of the proposed method, confirming its effectiveness in enhancing LLM performance by fine-grained exploration-exploitation trade-off.

## Open Questions

- How exactly is perplexity computed and used to define the exploration versus exploitation partitions?
- What is the precise form of the bidirectional reward allocation mechanism?
- Which baseline RLVR methods does DiPO outperform, and by how much on each benchmark?
- Does the method generalize beyond mathematical reasoning and function calling?
