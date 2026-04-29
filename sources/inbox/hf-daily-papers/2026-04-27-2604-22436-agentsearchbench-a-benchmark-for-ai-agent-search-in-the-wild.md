---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, tool-use, benchmarks, retrieval, reranking, evaluation]
source_count: 1
updated: 2026-04-28
source_url: https://arxiv.org/abs/2604.22436
paper_id: 2604.22436
published: 2026-04-24T04:00:00+08:00
submitted_on_daily: 2026-04-27T08:15:49+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# AgentSearchBench: A Benchmark for AI Agent Search in the Wild

## Summary

- one_sentence_summary: AgentSearchBench is a large-scale benchmark for finding suitable AI agents in the wild, framing agent discovery as retrieval and reranking over nearly 10,000 real-world agents and evaluating matches with execution-grounded performance signals.
- why_relevant: It is directly relevant to agentic systems and tool-use because it studies how to search, rank, and evaluate AI agents using behavior and execution signals rather than only metadata or text.
- filter_reason: A technically useful benchmark for agent search and execution-grounded ranking that directly supports agent evaluation and discovery.
- hugging_face_paper: https://huggingface.co/papers/2604.22436
- original_paper: https://arxiv.org/abs/2604.22436
- source_basis: `original abstract page`

## Key Points

- The benchmark targets realistic agent search scenarios where agent capabilities are compositional and execution-dependent, so textual descriptions are not enough to judge usefulness.
- It includes nearly 10,000 real-world agents from multiple providers and supports both executable task queries and high-level task descriptions.
- Relevance is measured using execution-grounded performance signals rather than semantic similarity alone.
- The paper reports a consistent gap between description-based similarity and actual agent performance, showing limitations of standard retrieval and reranking methods.
- Lightweight behavioral signals, including execution-aware probing, improve ranking quality and suggest that agent discovery should use execution evidence.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.22436
- Hugging Face API entry: https://huggingface.co/api/papers/2604.22436
- arXiv abstract: https://arxiv.org/abs/2604.22436
- GitHub: https://github.com/Bingo-W/AgentSearchBench
- Project page: https://bingo-w.github.io/AgentSearchBench/

## Paper Metadata

- authors: `Bin Wu`, `Arastun Mammadli`, `Xiaoyu Zhang`, `Emine Yilmaz`
- organization: `University College London`
- ai_keywords: `agent search`, `retrieval`, `reranking`, `execution-grounded performance signals`, `behavioral signals`, `execution-aware probing`
- upvotes: `9`
- num_comments: `1`
- abstract: The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at https://github.com/Bingo-W/AgentSearchBench.
- hf_ai_summary: AgentSearchBench presents a large-scale benchmark for agent search that addresses the challenge of identifying suitable AI agents for complex tasks by evaluating performance through execution-grounded signals rather than textual descriptions alone.

## Source Excerpt

The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at this https URL .

## Open Questions

- What exact execution-grounded signals are used to define relevance?
- How are the nearly 10,000 agents sourced and normalized across providers?
- Which retrieval and reranking baselines are compared in the benchmark?
- How much do behavioral signals improve ranking quality on each query type?
