---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, post-training, agent-evals, llm-systems, agentic-search, experience-reuse, reasoning]
source_count: 1
updated: 2026-04-10
source_url: https://arxiv.org/abs/2604.08124
paper_id: 2604.08124
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T09:05:46+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search

## Summary

- one_sentence_summary: HiExp is an RL post-training framework for search-using LLM agents that converts raw reasoning trajectories into hierarchical experience knowledge to improve search strategy, training stability, and generalization.
- why_relevant: It sits directly at the intersection of reinforcement learning post-training and agentic systems, with a concrete technique for improving search agents through structured experience extracted from trajectories.
- filter_reason: Directly targets RL-based agentic search with a new training framework for reasoning trajectories and stability.
- hugging_face_paper: https://huggingface.co/papers/2604.08124
- original_paper: https://arxiv.org/abs/2604.08124
- source_basis: `original abstract page`

## Key Points

- The paper targets RL-based search agents that currently depend on stochastic exploration plus outcome rewards, which can produce inefficient trajectories and unstable training.
- HiExp extracts empirical knowledge from trajectories using contrastive analysis and a multi-level clustering mechanism, producing hierarchical experience knowledge.
- The method then uses experience-aligned training to regularize exploration, shifting behavior from random search toward more strategic, experience-driven search.
- Evaluations on multiple agentic search and mathematical reasoning benchmarks show substantial performance gains.
- The reported gains generalize across tasks and across algorithms, suggesting the experience representation is reusable rather than benchmark-specific.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08124
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08124
- arXiv abstract: https://arxiv.org/abs/2604.08124

## Paper Metadata

- authors: `Chuzhan Hao`, `Wenfeng Feng`, `Guochao Jiang`, `Guofeng Quan`, `Guohua Liu`, `Yuewei Zhang`
- ai_keywords: `reinforcement learning`, `large language models`, `external search engines`, `stochastic exploration`, `outcome rewards`, `hierarchical experience`, `contrastive analysis`, `multi-level clustering`, `reasoning trajectories`, `experience-aligned training`, `agentic search`, `mathematical reasoning`
- upvotes: `2`
- num_comments: `0`
- abstract: Reinforcement learning (RL) has become an effective approach for advancing the reasoning capabilities of large language models (LLMs) through the strategic integration of external search engines. However, current RL-based search agents often rely on a process of stochastic exploration guided by carefully crafted outcome rewards, leading to inefficient reasoning trajectories and unstable training. To address these issues, we propose a novel framework, Hierarchical Experience (HiExp), to enhance the performance and training stability of search agents. Specifically, we extract empirical knowledge through contrastive analysis and a multi-level clustering mechanism, transforming raw reasoning trajectories into hierarchical experience knowledge. By leveraging experience-aligned training, we effectively regularize stochastic exploration, evolving it into a strategic and experience-driven search process. Extensive evaluations on multiple complex agentic search and mathematical reasoning benchmarks demonstrate that our approach not only achieves substantial performance gains but also exhibits strong cross-task and cross-algorithm generalization.
- hf_ai_summary: A novel hierarchical experience framework improves reinforcement learning-based search agents by transforming raw reasoning trajectories into structured knowledge, enhancing both performance and training stability in complex reasoning tasks.

## Source Excerpt

Reinforcement learning (RL) has become an effective approach for advancing the reasoning capabilities of large language models (LLMs) through the strategic integration of external search engines. However, current RL-based search agents often rely on a process of stochastic exploration guided by carefully crafted outcome rewards, leading to inefficient reasoning trajectories and unstable training. To address these issues, we propose a novel framework, Hierarchical Experience (HiExp), to enhance the performance and training stability of search agents. Specifically, we extract empirical knowledge through contrastive analysis and a multi-level clustering mechanism, transforming raw reasoning trajectories into hierarchical experience knowledge. By leveraging experience-aligned training, we effectively regularize stochastic exploration, evolving it into a strategic and experience-driven search process. Extensive evaluations on multiple complex agentic search and mathematical reasoning benchmarks demonstrate that our approach not only achieves substantial performance gains but also exhibits strong cross-task and cross-algorithm generalization.

## Open Questions

- What exact contrastive signals are used to define useful versus useless trajectories?
- How is the multi-level clustering structured, and what hierarchy levels are retained at training time?
- Which agentic search and mathematical reasoning benchmarks were used, and how large were the gains?
- How does HiExp compare to simpler trajectory filtering or retrieval-based experience reuse baselines?
