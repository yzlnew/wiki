---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, llm-systems, long-context, llm, mechanistic, sparse-updates, activation-patterns]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14922
paper_id: 2604.14922
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T09:00:45+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# LongAct: Harnessing Intrinsic Activation Patterns for Long-Context Reinforcement Learning

## Summary

- one_sentence_summary: LongAct is a post-training RL method for long-context LLMs that uses high-magnitude query/key activations to drive saliency-guided sparse weight updates instead of uniform updates.
- why_relevant: It connects mechanistic activation analysis with RL post-training for LLM reasoning, which is directly relevant to long-context agents and training methods that exploit internal model structure.
- filter_reason: Directly targets RL post-training for long-context reasoning with a concrete sparse-update method that works across GRPO and DAPO.
- hugging_face_paper: https://huggingface.co/papers/2604.14922
- original_paper: https://arxiv.org/abs/2604.14922
- source_basis: `original abstract page`

## Key Points

- The paper reports an empirical pattern: long-context processing produces high-magnitude activations in query and key vectors.
- It turns that observation into a training rule, updating only weights tied to these salient activations rather than applying uniform updates everywhere.
- The method is motivated by two ideas from the paper: quantization-style criticality of large activations and the sparse structure of long-context reasoning.
- LongAct is reported to improve performance by about 8% on LongBench v2 and to generalize better on the RULER benchmark.
- The approach is described as broadly compatible with multiple RL algorithms, including GRPO and DAPO.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14922
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14922
- arXiv abstract: https://arxiv.org/abs/2604.14922

## Paper Metadata

- authors: `Bowen Ping`, `Zijun Chen`, `Tingfeng Hui`, `Qize Yu`, `Chenxuan Li`, `Junchi Yan`, `Baobao Chang`
- ai_keywords: `reinforcement learning`, `large language models`, `long-context reasoning`, `query vectors`, `key vectors`, `model quantization`, `sparse updates`, `LongBench v2`, `RULER benchmark`, `GRPO`, `DAPO`
- upvotes: `5`
- num_comments: `2`
- abstract: Reinforcement Learning (RL) has emerged as a critical driver for enhancing the reasoning capabilities of Large Language Models (LLMs). While recent advancements have focused on reward engineering or data synthesis, few studies exploit the model's intrinsic representation characteristics to guide the training process. In this paper, we first observe the presence of high-magnitude activations within the query and key vectors when processing long contexts. Drawing inspiration from model quantization -- which establishes the criticality of such high-magnitude activations -- and the insight that long-context reasoning inherently exhibits a sparse structure, we hypothesize that these weights serve as the pivotal drivers for effective model optimization. Based on this insight, we propose LongAct, a strategy that shifts from uniform to saliency-guided sparse updates. By selectively updating only the weights associated with these significant activations, LongAct achieves an approximate 8% improvement on LongBench v2 and enhances generalization on the RULER benchmark. Furthermore, our method exhibits remarkable universality, consistently boosting performance across diverse RL algorithms such as GRPO and DAPO. Extensive ablation studies suggest that focusing on these salient features is key to unlocking long-context potential.
- hf_ai_summary: LongAct improves long-context reasoning in LLMs by implementing saliency-guided sparse updates based on high-magnitude activation patterns in query and key vectors.

## Source Excerpt

Reinforcement Learning (RL) has emerged as a critical driver for enhancing the reasoning capabilities of Large Language Models (LLMs). While recent advancements have focused on reward engineering or data synthesis, few studies exploit the model's intrinsic representation characteristics to guide the training process. In this paper, we first observe the presence of high-magnitude activations within the query and key vectors when processing long contexts. Drawing inspiration from model quantization -- which establishes the criticality of such high-magnitude activations -- and the insight that long-context reasoning inherently exhibits a sparse structure, we hypothesize that these weights serve as the pivotal drivers for effective model optimization. Based on this insight, we propose LongAct, a strategy that shifts from uniform to saliency-guided sparse updates. By selectively updating only the weights associated with these significant activations, LongAct achieves an approximate 8% improvement on LongBench v2 and enhances generalization on the RULER benchmark. Furthermore, our method exhibits remarkable universality, consistently boosting performance across diverse RL algorithms such as GRPO and DAPO. Extensive ablation studies suggest that focusing on these salient features is key to unlocking long-context potential.

## Open Questions

- Which model sizes and architectures were used in the LongBench v2 and RULER evaluations?
- How are the salient query/key weights selected in practice, and what sparsity level is used?
- What is the exact baseline for the reported 8% improvement?
- Does LongAct affect training cost, stability, or sample efficiency compared with uniform updates?
- Which ablations most strongly support the claim that high-magnitude activations are the key driver?
