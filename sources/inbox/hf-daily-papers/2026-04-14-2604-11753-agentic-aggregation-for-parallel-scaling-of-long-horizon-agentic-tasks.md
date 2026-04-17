---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, agent-architectures, agent-evals, llm-systems, test-time-scaling, aggregation, deep-research, benchmarking]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.11753
paper_id: 2604.11753
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-14T22:53:42+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks

## Summary

- one_sentence_summary: AggAgent is an aggregation agent for parallel test-time scaling on long-horizon agentic tasks that synthesizes multiple tool-augmented rollouts with lightweight inspection/search tools instead of concatenating full trajectories or keeping only final answers.
- why_relevant: It is directly about agentic systems and tool-using post-training/test-time scaling behavior, with an evaluation setup centered on long-horizon tasks rather than simple reasoning benchmarks.
- filter_reason: A strong agents paper on parallel test-time scaling with a concrete aggregation-agent mechanism and broad benchmark gains.
- hugging_face_paper: https://huggingface.co/papers/2604.11753
- original_paper: https://arxiv.org/abs/2604.11753
- source_basis: `original abstract page`

## Key Points

- The paper targets agentic search and deep research settings where multiple parallel rollouts must be merged into one response.
- It argues that naive aggregation is hard because trajectories are long, multi-turn, tool-augmented, and open-ended, while full concatenation exceeds context limits.
- AggAgent treats the set of trajectories as an environment and uses lightweight tools to inspect candidate solutions and search across trajectories on demand.
- Across six benchmarks and three model families, the method beats existing aggregation approaches by up to 5.3% absolute on average and 10.3% on two deep research tasks.
- The aggregation overhead is kept low, with cost bounded by a single agentic rollout.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11753
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11753
- arXiv abstract: https://arxiv.org/abs/2604.11753

## Paper Metadata

- authors: `Yoonsang Lee`, `Howard Yen`, `Xi Ye`, `Danqi Chen`
- ai_keywords: `parallel test-time scaling`, `agentic tasks`, `rollouts`, `trajectory aggregation`, `chain-of-thought reasoning`, `tool-augmented`, `context window`, `aggregation agent`, `candidate solutions`, `information synthesis`
- upvotes: `10`
- num_comments: `1`
- abstract: We study parallel test-time scaling for long-horizon agentic tasks such as agentic search and deep research, where multiple rollouts are generated in parallel and aggregated into a final response. While such scaling has proven effective for chain-of-thought reasoning, agentic tasks pose unique challenges: trajectories are long, multi-turn, and tool-augmented, and outputs are often open-ended. Aggregating only final answers discards rich information from trajectories, while concatenating all trajectories exceeds the model's context window. To address this, we propose AggAgent, an aggregation agent that treats parallel trajectories as an environment. We equip it with lightweight tools to inspect candidate solutions and search across trajectories, enabling it to navigate and synthesize information on demand. Across six benchmarks and three model families (GLM-4.7, Qwen3.5, MiniMax-M2.5), AggAgent outperforms all existing aggregation methods-by up to 5.3% absolute on average and 10.3% on two deep research tasks-while adding minimal overhead, as the aggregation cost remains bounded by a single agentic rollout. Our findings establish agentic aggregation as an effective and cost-efficient approach to parallel test-time scaling.
- hf_ai_summary: AggAgent enables efficient parallel test-time scaling for long-horizon agentic tasks by aggregating trajectories through a lightweight agent that navigates and synthesizes information on demand.

## Source Excerpt

We study parallel test-time scaling for long-horizon agentic tasks such as agentic search and deep research, where multiple rollouts are generated in parallel and aggregated into a final response. While such scaling has proven effective for chain-of-thought reasoning, agentic tasks pose unique challenges: trajectories are long, multi-turn, and tool-augmented, and outputs are often open-ended. Aggregating only final answers discards rich information from trajectories, while concatenating all trajectories exceeds the model's context window. To address this, we propose AggAgent, an aggregation agent that treats parallel trajectories as an environment. We equip it with lightweight tools to inspect candidate solutions and search across trajectories, enabling it to navigate and synthesize information on demand. Across six benchmarks and three model families (GLM-4.7, Qwen3.5, MiniMax-M2.5), AggAgent outperforms all existing aggregation methods-by up to 5.3% absolute on average and 10.3% on two deep research tasks-while adding minimal overhead, as the aggregation cost remains bounded by a single agentic rollout. Our findings establish agentic aggregation as an effective and cost-efficient approach to parallel test-time scaling.

## Open Questions

- What exact lightweight tools does AggAgent use to inspect and search trajectories?
- How is the aggregation agent trained or prompted, if at all?
- Which six benchmarks were used, and how were the two deep research tasks defined?
- What are the specific baseline aggregation methods it outperforms?
- Does the approach generalize equally well across the three model families or depend on model-specific behavior?
