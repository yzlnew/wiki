---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-evals, tool-use, multi-agent, web-search, agent-coordination]
source_count: 1
updated: 2026-05-05
source_url: https://arxiv.org/abs/2604.27221
paper_id: 2604.27221
published: 2026-04-29T04:00:00+08:00
submitted_on_daily: 2026-05-04T16:27:29+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction

## Summary

- one_sentence_summary: Web2BigTable is a bi-level multi-agent web search system that decomposes search into parallel subproblems, coordinates workers through shared state, and iteratively improves decomposition and execution via a run-verify-reflect loop.
- why_relevant: It is directly relevant to agentic tool use and multi-agent coordination, and its evaluation on web search tasks connects to post-training-style iterative improvement for LLM systems.
- filter_reason: A technically detailed multi-agent web-search/extraction system with coordinated agents, decomposition, and verification fits the agents and LLM-systems priorities.
- hugging_face_paper: https://huggingface.co/papers/2604.27221
- original_paper: https://arxiv.org/abs/2604.27221
- source_basis: `original abstract page`

## Key Points

- The paper targets two web-search regimes: breadth-oriented aggregation across many entities/sources and depth-oriented reasoning over long search trajectories.
- Web2BigTable uses an upper-level orchestrator to split tasks into subproblems and lower-level worker agents to execute them in parallel.
- A closed-loop run-verify-reflect process updates both task decomposition and agent execution over time using persistent, human-readable external memory.
- Workers share a workspace so partial findings are visible, which helps reduce redundant search, reconcile conflicting evidence, and close coverage gaps.
- The system reports strong results on WideSearch and also generalizes to XBench-DeepSearch, suggesting the design supports both table-style aggregation and deeper agentic search.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27221
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27221
- arXiv abstract: https://arxiv.org/abs/2604.27221
- GitHub: https://github.com/web2bigtable/web2bigtable

## Paper Metadata

- authors: `Yuxuan Huang`, `Yihang Chen`, `Zhiyuan He`, `Yuxiang Chen`, `Ka Yiu Lee`, `Huichi Zhou`, `Weilin Luo`, `Meng Fang`, `Jun Wang`
- ai_keywords: `multi-agent framework`, `bi-level architecture`, `task decomposition`, `parallel execution`, `closed-loop run--verify--reflect process`, `external memory`, `shared workspace`, `coordinated agents`, `iterative improvement`
- upvotes: `27`
- num_comments: `4`
- abstract: Agentic web search increasingly faces two distinct demands: deep reasoning over a single target, and structured aggregation across many entities and heterogeneous sources. Current systems struggle on both fronts. Breadth-oriented tasks demand schema-aligned outputs with wide coverage and cross-entity consistency, while depth-oriented tasks require coherent reasoning over long, branching search trajectories. We introduce Web2BigTable, a multi-agent framework for web-to-table search that supports both regimes. Web2BigTable adopts a bi-level architecture in which an upper-level orchestrator decomposes the task into sub-problems and lower-level worker agents solve them in parallel. Through a closed-loop run--verify--reflect process, the framework jointly improves decomposition and execution over time via persistent, human-readable external memory, with self-evolving updates to each single-agent. During execution, workers coordinate through a shared workspace that makes partial findings visible, allowing them to reduce redundant exploration, reconcile conflicting evidence, and adapt to emerging coverage gaps. Web2BigTable sets a new state of the art on WideSearch, reaching an Avg@4 Success Rate of 38.50 (7.5times the second best at 5.10), Row F1 of 63.53 (+25.03 over the second best), and Item F1 of 80.12 (+14.42 over the second best). It also generalises to depth-oriented search on XBench-DeepSearch, achieving 73.0 accuracy. Code is available at https://github.com/web2bigtable/web2bigtable.
- hf_ai_summary: Web2BigTable is a multi-agent framework that addresses both broad and deep web search challenges through a bi-level architecture with coordinated agents and iterative improvement mechanisms.

## Source Excerpt

Agentic web search increasingly faces two distinct demands: deep reasoning over a single target, and structured aggregation across many entities and heterogeneous sources. Current systems struggle on both fronts. Breadth-oriented tasks demand schema-aligned outputs with wide coverage and cross-entity consistency, while depth-oriented tasks require coherent reasoning over long, branching search trajectories. We introduce \textbf{Web2BigTable}, a multi-agent framework for web-to-table search that supports both regimes. Web2BigTable adopts a bi-level architecture in which an upper-level orchestrator decomposes the task into sub-problems and lower-level worker agents solve them in parallel. Through a closed-loop run--verify--reflect process, the framework jointly improves decomposition and execution over time via persistent, human-readable external memory, with self-evolving updates to each single-agent. During execution, workers coordinate through a shared workspace that makes partial findings visible, allowing them to reduce redundant exploration, reconcile conflicting evidence, and adapt to emerging coverage gaps. Web2BigTable sets a new state of the art on WideSearch, reaching an Avg@4 Success Rate of \textbf{38.50} ($7.5\times$ the second best at 5.10), Row F1 of \textbf{63.53} (+25.03 over the second best), and Item F1 of \textbf{80.12} (+14.42 over the second best). It also generalises to depth-oriented search on XBench-DeepSearch, achieving 73.0 accuracy. Code is available at this https URL .

## Open Questions

- How exactly is the run-verify-reflect loop implemented, and what triggers memory updates?
- What is stored in the external memory, and how much of it is human-readable versus learned?
- What are the task decomposition heuristics or policies used by the upper-level orchestrator?
- How are conflicts between worker findings resolved in the shared workspace?
- Does the paper report ablations isolating the gains from parallelism, shared workspace, and reflective updates?
