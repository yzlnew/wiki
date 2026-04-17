---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, coding-agents, llm-systems, agent-evals, memory, transfer-learning, post-training, evaluation]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.14004
paper_id: 2604.14004
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-16T12:03:22+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

## Summary

- one_sentence_summary: This paper studies memory transfer learning for coding agents, showing that a unified cross-domain memory pool can improve performance by transferring abstract meta-knowledge rather than task-specific traces.
- why_relevant: It is directly relevant to coding agents and post-training because it studies how persistent memory can improve agent performance across domains and identifies which kinds of stored experience actually transfer.
- filter_reason: Strongly relevant coding-agent work on memory sharing, cross-domain transfer, and benchmarked system design principles.
- hugging_face_paper: https://huggingface.co/papers/2604.14004
- original_paper: https://arxiv.org/abs/2604.14004
- source_basis: `original abstract page`

## Key Points

- It proposes Memory Transfer Learning (MTL), which reuses a unified memory pool across heterogeneous coding domains instead of keeping memory siloed by task type.
- The evaluation covers 6 coding benchmarks and 4 memory representations, ranging from concrete traces to abstract insights.
- Cross-domain memory improves average performance by 3.7%, with the gains mainly coming from transferred meta-knowledge such as validation routines.
- Abstraction level matters: high-level insights transfer better, while low-level traces can cause negative transfer because they are too specific.
- Transfer effectiveness increases as the memory pool grows, and memory transfer can work even across different models.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14004
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14004
- arXiv abstract: https://arxiv.org/abs/2604.14004
- GitHub: https://github.com/KangsanKim07/MemoryTransferLearning
- Project page: https://memorytransfer.github.io/

## Paper Metadata

- authors: `Kangsan Kim`, `Minki Kang`, `Taeil Kim`, `Yanlai Yang`, `Mengye Ren`, `Sung Ju Hwang`
- organization: `KAIST AI`
- ai_keywords: `Memory Transfer Learning`, `memory pool`, `cross-domain transfer`, `meta-knowledge`, `abstraction`, `memory representation`, `validation routines`, `negative transfer`
- upvotes: `24`
- num_comments: `2`
- abstract: Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate Memory Transfer Learning (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: https://memorytransfer.github.io/
- hf_ai_summary: Memory transfer learning enables cross-domain code generation by leveraging unified memory pools, with performance improvements achieved through high-level abstraction rather than low-level code traces.

## Source Excerpt

Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: this https URL

## Open Questions

- Which six coding benchmarks were used, and how did results vary by benchmark?
- How were the four memory representations defined and operationalized?
- What mechanism was used to store, retrieve, and select memories from the unified pool?
- How large was the effect of transfer between different models compared with within-model transfer?
- What kinds of negative transfer cases were observed for low-level traces?
