---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, agent-evals, llm-systems, software-engineering, context-management, cot, swe-bench, reasoning]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.11716
paper_id: 2604.11716
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-14T12:01:22+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context

## Summary

- one_sentence_summary: SWE-AGILE is a software agent framework for multi-turn SWE tasks that manages reasoning context with a sliding window plus compressed reasoning digests to reduce context explosion while preserving continuity.
- why_relevant: It is directly relevant to agents and tool-using systems because it proposes a concrete context-management mechanism for long-horizon reasoning in software engineering agents, with benchmark evidence.
- filter_reason: A technically focused software-agent framework for SWE with context management and SWE-Bench-Verified evaluation fits the agents and agent-evals priorities.
- hugging_face_paper: https://huggingface.co/papers/2604.11716
- original_paper: https://arxiv.org/abs/2604.11716
- source_basis: `original abstract page`

## Key Points

- The paper argues that ReAct-style SWE agents often lack explicit System-2 reasoning, which hurts deep analysis and edge-case handling.
- It identifies a core tradeoff in multi-turn software engineering tasks: keeping full reasoning history causes context explosion and lost-in-the-middle degradation, while discarding history forces repeated re-reasoning.
- SWE-AGILE's Dynamic Reasoning Context strategy keeps detailed recent reasoning in a sliding window and compresses older reasoning into concise Reasoning Digests.
- The framework is reported to set a new standard for 7B-8B models on SWE-Bench-Verified, using 2.2k trajectories over 896 tasks.
- The contribution is primarily an agent-system design for long-horizon reasoning management rather than a new base model or algorithmic RL method.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11716
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11716
- arXiv abstract: https://arxiv.org/abs/2604.11716
- GitHub: https://github.com/KDEGroup/SWE-AGILE

## Paper Metadata

- authors: `Shuquan Lian`, `Juncheng Liu`, `Yazhe Chen`, `Yuhong Chen`, `Hui Li`
- organization: `Knowledge and Data Engineering Group at Xiamen University`
- ai_keywords: `ReAct-style approaches`, `System-2 reasoning`, `Chain-of-Thought`, `multi-turn SWE task`, `context explosion`, `Lost-in-the-Middle degradation`, `dynamic reasoning context`, `sliding window`, `reasoning digests`, `SWE-Bench-Verified`
- upvotes: `3`
- num_comments: `1`
- abstract: Prior representative ReAct-style approaches in autonomous Software Engineering (SWE) typically lack the explicit System-2 reasoning required for deep analysis and handling complex edge cases. While recent reasoning models demonstrate the potential of extended Chain-of-Thought (CoT), applying them to the multi-turn SWE task creates a fundamental dilemma: retaining full reasoning history leads to context explosion and ``Lost-in-the-Middle'' degradation, while discarding it would force the agent to redundantly re-reason at every step. To address these challenges, we propose SWE-AGILE, a novel software agent framework designed to bridge the gap between reasoning depth, efficiency, and context constraints. SWE-AGILE introduces a Dynamic Reasoning Context strategy, maintaining a ``sliding window'' of detailed reasoning for immediate continuity to prevent redundant re-analyzing, while compressing historical reasoning content into concise Reasoning Digests. Empirically, SWE-AGILE sets a new standard for 7B-8B models on SWE-Bench-Verified using only 2.2k trajectories and 896 tasks. Code is available at https://github.com/KDEGroup/SWE-AGILE.
- hf_ai_summary: SWE-AGILE addresses reasoning limitations in software engineering by using dynamic context management to balance detailed analysis with computational efficiency.

## Source Excerpt

Prior representative ReAct-style approaches in autonomous Software Engineering (SWE) typically lack the explicit System-2 reasoning required for deep analysis and handling complex edge cases. While recent reasoning models demonstrate the potential of extended Chain-of-Thought (CoT), applying them to the multi-turn SWE task creates a fundamental dilemma: retaining full reasoning history leads to context explosion and ``Lost-in-the-Middle'' degradation, while discarding it would force the agent to redundantly re-reason at every step. To address these challenges, we propose SWE-AGILE, a novel software agent framework designed to bridge the gap between reasoning depth, efficiency, and context constraints. SWE-AGILE introduces a Dynamic Reasoning Context strategy, maintaining a ``sliding window'' of detailed reasoning for immediate continuity to prevent redundant re-analyzing, while compressing historical reasoning content into concise Reasoning Digests. Empirically, SWE-AGILE sets a new standard for 7B-8B models on SWE-Bench-Verified using only 2.2k trajectories and 896 tasks. Code is available at this https URL .

## Open Questions

- How are Reasoning Digests constructed and updated during a trajectory?
- What exact SWE-Bench-Verified metrics improved, and by how much over baselines?
- How much of the gain comes from the sliding window versus the digest compression?
- Does the approach generalize beyond SWE-Bench-Verified or beyond 7B-8B models?
