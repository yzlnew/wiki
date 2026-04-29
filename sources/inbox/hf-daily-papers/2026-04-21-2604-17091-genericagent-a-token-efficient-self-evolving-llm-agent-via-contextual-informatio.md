---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, tool-use, llm-systems, agent-evals, post-training, llm-agents, memory, self-evolution, context-compression]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.17091
paper_id: 2604.17091
published: 2026-04-18T04:00:00+08:00
submitted_on_daily: 2026-04-21T20:16:25+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)

## Summary

- one_sentence_summary: GenericAgent is a self-evolving LLM agent that tries to improve long-horizon performance by maximizing decision-relevant information per token through compact tools, hierarchical memory, reusable SOPs/code, and context compression.
- why_relevant: It is directly relevant to agent architectures, tool use, and post-training-style self-improvement because it proposes a concrete mechanism for making long-horizon agents more token-efficient and persistent.
- filter_reason: A technically detailed LLM agent system focused on long-horizon tool use, memory, self-evolution, and token-efficient execution.
- hugging_face_paper: https://huggingface.co/papers/2604.17091
- original_paper: https://arxiv.org/abs/2604.17091
- source_basis: `original abstract page`

## Key Points

- The paper frames long-horizon agent failure as a context-density problem: performance depends on how much decision-relevant information can be retained within a finite context budget, not just raw context length.
- GenericAgent uses a minimal atomic tool set to keep the agent interface simple and reduce context overhead from tool descriptions and usage complexity.
- It adds hierarchical on-demand memory that exposes only a small high-level view by default, instead of dumping full retrieved memory into context.
- A self-evolution mechanism converts verified past trajectories into reusable SOPs and executable code, so experience can persist across episodes.
- A context truncation and compression layer is used during long executions to preserve information density; the abstract claims gains across task completion, tool use efficiency, memory effectiveness, self-evolution, and web browsing with fewer tokens and interactions.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.17091
- Hugging Face API entry: https://huggingface.co/api/papers/2604.17091
- arXiv abstract: https://arxiv.org/abs/2604.17091
- GitHub: https://github.com/lsdefine/GenericAgent

## Paper Metadata

- authors: `Jiaqing Liang`, `Jinyi Han`, `Weijia Li`, `Xinyi Wang`, `Zhoujia Zhang`, `Zishang Jiang`, `Ying Liao`, `Tingyun Li`, `Ying Huang`, `Hao Shen`, `Hanyu Wu`, `Fang Guo`, `Keyi Wang`, `Zhonghua Hong`, `Zhiyu Lu`, `Lipeng Ma`, `Sihang Jiang`, `Yanghua Xiao`
- organization: `Fudan University`
- ai_keywords: `large language model agents`, `context length`, `decision-relevant information`, `context information density maximization`, `hierarchical on-demand memory`, `self-evolution mechanism`, `reusable SOPs`, `context truncation`, `context compression`
- upvotes: `6`
- num_comments: `1`
- abstract: Long-horizon large language model (LLM) agents are fundamentally limited by context. As interactions become longer, tool descriptions, retrieved memories, and raw environmental feedback accumulate and push out the information needed for decision-making. At the same time, useful experience gained from tasks is often lost across episodes. We argue that long-horizon performance is determined not by context length, but by how much decision-relevant information is maintained within a finite context budget. We present GenericAgent (GA), a general-purpose, self-evolving LLM agent system built around a single principle: context information density maximization. GA implements this through four closely connected components: a minimal atomic tool set that keeps the interface simple, a hierarchical on-demand memory that only shows a small high-level view by default, a self-evolution mechanism that turns verified past trajectories into reusable SOPs and executable code, and a context truncation and compression layer that maintains information density during long executions. Across task completion, tool use efficiency, memory effectiveness, self-evolution, and web browsing, GA consistently outperforms leading agent systems while using significantly fewer tokens and interactions, and it continues to evolve over time. Project: https://github.com/lsdefine/GenericAgent
- hf_ai_summary: GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

## Source Excerpt

Long-horizon large language model (LLM) agents are fundamentally limited by context. As interactions become longer, tool descriptions, retrieved memories, and raw environmental feedback accumulate and push out the information needed for decision-making. At the same time, useful experience gained from tasks is often lost across episodes. We argue that long-horizon performance is determined not by context length, but by how much decision-relevant information is maintained within a finite context budget. We present GenericAgent (GA), a general-purpose, self-evolving LLM agent system built around a single principle: context information density maximization. GA implements this through four closely connected components: a minimal atomic tool set that keeps the interface simple, a hierarchical on-demand memory that only shows a small high-level view by default, a self-evolution mechanism that turns verified past trajectories into reusable SOPs and executable code, and a context truncation and compression layer that maintains information density during long executions. Across task completion, tool use efficiency, memory effectiveness, self-evolution, and web browsing, GA consistently outperforms leading agent systems while using significantly fewer tokens and interactions, and it continues to evolve over time. Project: this https URL

## Open Questions

- What benchmarks and task suites were used to support the claimed gains?
- How are 'verified past trajectories' selected and converted into SOPs or code?
- What is the exact truncation/compression policy, and how much performance is lost versus saved?
- How does the minimal atomic tool set compare to richer tool libraries in capability and robustness?
