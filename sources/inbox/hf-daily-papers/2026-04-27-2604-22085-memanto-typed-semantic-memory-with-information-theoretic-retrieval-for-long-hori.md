---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-evals, reasoning-behavior-shaping, memory, retrieval, long-horizon, evaluation, semantic-search]
source_count: 1
updated: 2026-04-28
source_url: https://arxiv.org/abs/2604.22085
paper_id: 2604.22085
published: 2026-04-23T04:00:00+08:00
submitted_on_daily: 2026-04-27T19:33:50+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

## Summary

- one_sentence_summary: Memanto proposes a universal memory layer for persistent agents that uses a typed semantic schema plus information-theoretic search to deliver deterministic, low-latency retrieval without graph-style ingestion overhead.
- why_relevant: This is directly relevant to agent systems and post-training infrastructure because it focuses on persistent memory design for long-horizon agents and benchmarks a practical retrieval architecture for production use.
- filter_reason: A technical agent memory architecture paper with benchmarks and ablations directly relevant to long-horizon agent systems.
- hugging_face_paper: https://huggingface.co/papers/2604.22085
- original_paper: https://arxiv.org/abs/2604.22085
- source_basis: `original abstract page`

## Key Points

- It targets the memory bottleneck in persistent, multi-session autonomous agents, arguing that hybrid semantic graph approaches are too expensive to ingest and retrieve from.
- Memanto uses 13 predefined memory categories, automated conflict resolution, and temporal versioning as its core memory structure.
- The system is backed by Moorcheh's Information Theoretic Search engine, described as a no-index semantic database with deterministic retrieval under 90 ms and no ingestion delay.
- On LongMemEval and LoCoMo, the paper reports state-of-the-art accuracy of 89.8% and 87.1%, respectively, while using a single retrieval query and no ingestion cost.
- A five-stage ablation study is included to measure the contribution of each architectural component.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.22085
- Hugging Face API entry: https://huggingface.co/api/papers/2604.22085
- arXiv abstract: https://arxiv.org/abs/2604.22085
- GitHub: https://github.com/moorcheh-ai/memanto-evaluation
- Project page: https://memanto.ai/

## Paper Metadata

- authors: `Seyed Moein Abtahi`, `Rasa Rahnema`, `Hetkumar Patel`, `Neel Patel`, `Majid Fekri`, `Tara Khani`
- organization: `Moorcheh.ai`
- ai_keywords: `language model inference`, `persistent autonomous agents`, `memory architecture`, `semantic graph architectures`, `knowledge graph`, `entity extraction`, `graph schema maintenance`, `retrieval pipelines`, `typed semantic memory schema`, `conflict resolution mechanism`, `temporal versioning`, `information theoretic search engine`, `semantic database`, `deterministic retrieval`, `LongMemEval`, `LoCoMo`, `vector based systems`, `retrieval query`, `ingestion delay`, `operational complexity`
- upvotes: `6`
- num_comments: `3`
- abstract: The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems. Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval. These systems typically require large language model mediated entity extraction, explicit graph schema maintenance, and multi query retrieval pipelines. This paper introduces Memanto, a universal memory layer for agentic artificial intelligence that challenges the prevailing assumption that knowledge graph complexity is necessary to achieve high fidelity agent memory. Memanto integrates a typed semantic memory schema comprising thirteen predefined memory categories, an automated conflict resolution mechanism, and temporal versioning. These components are enabled by Moorcheh's Information Theoretic Search engine, a no indexing semantic database that provides deterministic retrieval within sub ninety millisecond latency while eliminating ingestion delay. Through systematic benchmarking on the LongMemEval and LoCoMo evaluation suites, Memanto achieves state of the art accuracy scores of 89.8 percent and 87.1 percent respectively. These results surpass all evaluated hybrid graph and vector based systems while requiring only a single retrieval query, incurring no ingestion cost, and maintaining substantially lower operational complexity. A five stage progressive ablation study is presented to quantify the contribution of each architectural component, followed by a discussion of the implications for scalable deployment of agentic memory systems.
- hf_ai_summary: Memanto presents a universal memory layer for agentic AI that eliminates computational overhead of hybrid semantic graph architectures through a typed semantic memory schema and information-theoretic search engine.

## Source Excerpt

The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems. Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval. These systems typically require large language model mediated entity extraction, explicit graph schema maintenance, and multi query retrieval pipelines. This paper introduces Memanto, a universal memory layer for agentic artificial intelligence that challenges the prevailing assumption that knowledge graph complexity is necessary to achieve high fidelity agent memory. Memanto integrates a typed semantic memory schema comprising thirteen predefined memory categories, an automated conflict resolution mechanism, and temporal versioning. These components are enabled by Moorcheh's Information Theoretic Search engine, a no indexing semantic database that provides deterministic retrieval within sub ninety millisecond latency while eliminating ingestion delay. Through systematic benchmarking on the LongMemEval and LoCoMo evaluation suites, Memanto achieves state of the art accuracy scores of 89.8 percent and 87.1 percent respectively. These results surpass all evaluated hybrid graph and vector based systems while requiring only a single retrieval query, incurring no ingestion cost, and maintaining substantially lower operational complexity. A five stage progressive ablation study is presented to quantify the contribution of each architectural component, followed by a discussion of the implications for scalable deployment of agentic memory systems.

## Open Questions

- What are the 13 memory categories, and how are they defined in the typed schema?
- How does the conflict resolution mechanism behave on contradictory or time-sensitive memories?
- What exactly does the 'information-theoretic search' retrieve and how is it implemented without indexing?
- How much of the reported gain comes from the schema versus the search engine versus temporal versioning?
- How does Memanto compare on latency and memory quality under longer, noisier real-world agent workloads beyond the reported benchmarks?
