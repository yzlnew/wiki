---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-evals, reasoning, agent-memory, retrieval, forgetting, local-first]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.04514
paper_id: 2604.04514
published: 2026-04-06T04:00:00+08:00
submitted_on_daily: 2026-04-17T11:33:44+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# SuperLocalMemory V3.3: The Living Brain -- Biologically-Inspired Forgetting, Cognitive Quantization, and Multi-Channel Retrieval for Zero-LLM Agent Memory Systems

## Summary

- one_sentence_summary: SuperLocalMemory V3.3 is a local-first memory system for coding agents that adds new retrieval metrics, adaptive forgetting, multi-channel recall, and soft-prompt-based long-term implicit memory, with reported gains on LoCoMo in zero-LLM mode.
- why_relevant: This is directly relevant to agent systems and post-training memory design because it focuses on local-first retrieval, memory consolidation/forgetting, and evaluation on an agent benchmark rather than only parametric model changes.
- filter_reason: Directly targets agent memory architecture with concrete retrieval/forgetting methods and benchmark results.
- hugging_face_paper: https://huggingface.co/papers/2604.04514
- original_paper: https://arxiv.org/abs/2604.04514
- source_basis: `original abstract page`

## Key Points

- The paper frames agent memory as a limitation of current coding agents: they retain parametric knowledge but cannot reliably remember prior conversation context, and many existing systems depend on cloud LLMs and single-channel vector retrieval.
- It introduces Fisher-Rao Quantization-Aware Distance (FRQAD), a metric on the Gaussian statistical manifold that the abstract says prefers high-fidelity embeddings over quantized ones with 100% precision, compared with 85.6% for cosine.
- It proposes Ebbinghaus Adaptive Forgetting with lifecycle-aware quantization, described as a mathematical forgetting curve coupled to progressive embedding compression, with a reported 6.7x discriminative power.
- It uses 7 retrieval channels: semantic, keyword, entity graph, temporal, spreading activation, consolidation, and Hopfield associative retrieval, and reports 70.4% on LoCoMo in zero-LLM Mode A.
- It adds memory parameterization for Long-Term Implicit memory via soft prompts and a zero-friction auto-cognitive pipeline that automates the memory lifecycle.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.04514
- Hugging Face API entry: https://huggingface.co/api/papers/2604.04514
- arXiv abstract: https://arxiv.org/abs/2604.04514
- Project page: https://superlocalmemory.com/

## Paper Metadata

- authors: `Varun Pratap Bhardwaj`
- organization: `Qualixar`
- ai_keywords: `Fisher-Rao Quantization-Aware Distance`, `Ebbinghaus Adaptive Forgetting`, `cognitive retrieval`, `semantic retrieval`, `keyword retrieval`, `entity graph retrieval`, `temporal retrieval`, `spreading activation`, `consolidation`, `Hopfield associative memory`, `Long-Term Implicit memory`, `soft prompts`, `auto-cognitive pipeline`, `Gaussian statistical manifold`, `quantization-aware distance`, `progressive embedding compression`, `memory parameterization`
- upvotes: `5`
- num_comments: `2`
- abstract: AI coding agents operate in a paradox: they possess vast parametric knowledge yet cannot remember a conversation from an hour ago. Existing memory systems store text in vector databases with single-channel retrieval, require cloud LLMs for core operations, and implement none of the cognitive processes that make human memory effective. We present SuperLocalMemory V3.3 ("The Living Brain"), a local-first agent memory system implementing the full cognitive memory taxonomy with mathematical lifecycle dynamics. Building on the information-geometric foundations of V3.2 (arXiv:2603.14588), we introduce five contributions: (1) Fisher-Rao Quantization-Aware Distance (FRQAD) -- a new metric on the Gaussian statistical manifold achieving 100% precision at preferring high-fidelity embeddings over quantized ones (vs 85.6% for cosine), with zero prior art; (2) Ebbinghaus Adaptive Forgetting with lifecycle-aware quantization -- the first mathematical forgetting curve in local agent memory coupled to progressive embedding compression, achieving 6.7x discriminative power; (3) 7-channel cognitive retrieval spanning semantic, keyword, entity graph, temporal, spreading activation, consolidation, and Hopfield associative channels, achieving 70.4% on LoCoMo in zero-LLM Mode A; (4) memory parameterization implementing Long-Term Implicit memory via soft prompts; (5) zero-friction auto-cognitive pipeline automating the complete memory lifecycle. On LoCoMo, V3.3 achieves 70.4% in Mode A (zero-LLM), with +23.8pp on multi-hop and +12.7pp on adversarial. V3.2 achieved 74.8% Mode A and 87.7% Mode C; the 4.4pp gap reflects a deliberate architectural trade-off. SLM V3.3 is open source under the Elastic License 2.0, runs entirely on CPU, with over 5,000 monthly downloads.
- hf_ai_summary: A new local-first agent memory system implements comprehensive cognitive memory processes with enhanced retrieval and forgetting mechanisms, achieving superior performance in zero-LLM settings.

## Source Excerpt

AI coding agents operate in a paradox: they possess vast parametric knowledge yet cannot remember a conversation from an hour ago. Existing memory systems store text in vector databases with single-channel retrieval, require cloud LLMs for core operations, and implement none of the cognitive processes that make human memory effective. We present SuperLocalMemory V3.3 ("The Living Brain"), a local-first agent memory system implementing the full cognitive memory taxonomy with mathematical lifecycle dynamics. Building on the information-geometric foundations of V3.2 ( arXiv:2603.14588 ), we introduce five contributions: (1) Fisher-Rao Quantization-Aware Distance (FRQAD) -- a new metric on the Gaussian statistical manifold achieving 100% precision at preferring high-fidelity embeddings over quantized ones (vs 85.6% for cosine), with zero prior art; (2) Ebbinghaus Adaptive Forgetting with lifecycle-aware quantization -- the first mathematical forgetting curve in local agent memory coupled to progressive embedding compression, achieving 6.7x discriminative power; (3) 7-channel cognitive retrieval spanning semantic, keyword, entity graph, temporal, spreading activation, consolidation, and Hopfield associative channels, achieving 70.4% on LoCoMo in zero-LLM Mode A; (4) memory parameterization implementing Long-Term Implicit memory via soft prompts; (5) zero-friction auto-cognitive pipeline automating the complete memory lifecycle. On LoCoMo, V3.3 achieves 70.4% in Mode A (zero-LLM), with +23.8pp on multi-hop and +12.7pp on adversarial. V3.2 achieved 74.8% Mode A and 87.7% Mode C; the 4.4pp gap reflects a deliberate architectural trade-off. SLM V3.3 is open source under the Elastic License 2.0, runs entirely on CPU, with over 5,000 monthly downloads.

## Open Questions

- What exact LoCoMo task setup and scoring protocol were used for the 70.4% result?
- How were FRQAD and the forgetting curve evaluated beyond the headline precision and discriminative-power claims?
- What is the implementation detail of the 7-channel retrieval stack and how much each channel contributes individually?
- How does Mode A differ operationally from V3.2 Mode C, and what architectural trade-off explains the reported gap?
