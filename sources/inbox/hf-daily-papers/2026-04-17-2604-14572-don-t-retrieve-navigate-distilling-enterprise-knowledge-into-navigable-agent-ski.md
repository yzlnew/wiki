---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-evals, rag, retrieval, navigation, hierarchical-summaries, enterprise-qa]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14572
paper_id: 2604.14572
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T16:03:22+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG

## Summary

- one_sentence_summary: Corpus2Skill converts a document corpus into a hierarchical, navigable skill directory so an LLM agent can inspect structure, backtrack, and retrieve full documents by ID during QA.
- why_relevant: It is directly relevant to agents and tool-using systems because it reframes retrieval as navigation over an explicit structure, and it also matters for post-training-style system design around better evidence access.
- filter_reason: Directly relevant agentic RAG work that turns corpus structure into navigable skills for better query-time reasoning and evidence retrieval.
- hugging_face_paper: https://huggingface.co/papers/2604.14572
- original_paper: https://arxiv.org/abs/2604.14572
- source_basis: `original abstract page`

## Key Points

- The paper argues that standard RAG makes the model a passive consumer of search results and hides corpus structure, which limits backtracking and cross-branch evidence combination.
- Corpus2Skill compiles a corpus offline by iteratively clustering documents, generating LLM-written summaries at each level, and turning the result into a tree of navigable skill files.
- At serve time, the agent sees a bird's-eye view of the corpus, drills down through progressively finer summaries, and fetches full documents by ID.
- The explicit hierarchy is intended to support reasoning about where to look, recovering from unproductive paths, and combining evidence across branches.
- On the WixQA enterprise customer-support benchmark, it reportedly outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14572
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14572
- arXiv abstract: https://arxiv.org/abs/2604.14572
- GitHub: https://github.com/dukesun99/Corpus2Skill

## Paper Metadata

- authors: `Yiqun Sun`, `Pengfei Wei`, `Lawrence B. Hsieh`
- ai_keywords: `Retrieval-Augmented Generation`, `LLM agent`, `hierarchical skill directory`, `document clustering`, `tree of navigable skill files`, `dense retrieval`, `RAPTOR`, `agentic RAG`
- upvotes: `4`
- num_comments: `2`
- abstract: Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, limiting its ability to backtrack or combine scattered evidence. We present Corpus2Skill, which distills a document corpus into a hierarchical skill directory offline and lets an LLM agent navigate it at serve time. The compilation pipeline iteratively clusters documents, generates LLM-written summaries at each level, and materializes the result as a tree of navigable skill files. At serve time, the agent receives a bird's-eye view of the corpus, drills into topic branches via progressively finer summaries, and retrieves full documents by ID. Because the hierarchy is explicitly visible, the agent can reason about where to look, backtrack from unproductive paths, and combine evidence across branches. On WixQA, an enterprise customer-support benchmark for RAG, Corpus2Skill outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics.
- hf_ai_summary: Corpus2Skill enhances retrieval-augmented generation by structuring document corpora into hierarchical skill directories that enable language model agents to navigate and reason about information organization during query processing.

## Source Excerpt

Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, limiting its ability to backtrack or combine scattered evidence. We present Corpus2Skill, which distills a document corpus into a hierarchical skill directory offline and lets an LLM agent navigate it at serve time. The compilation pipeline iteratively clusters documents, generates LLM-written summaries at each level, and materializes the result as a tree of navigable skill files. At serve time, the agent receives a bird's-eye view of the corpus, drills into topic branches via progressively finer summaries, and retrieves full documents by ID. Because the hierarchy is explicitly visible, the agent can reason about where to look, backtrack from unproductive paths, and combine evidence across branches. On WixQA, an enterprise customer-support benchmark for RAG, Corpus2Skill outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics.

## Open Questions

- How is the hierarchical skill directory constructed in detail, and what clustering and summarization settings are used?
- What are the exact quality metrics on WixQA, and how large are the gains over each baseline?
- What is the runtime or storage overhead of compiling and serving the navigable corpus compared with dense retrieval?
- Does the approach generalize beyond enterprise support corpora to other document collections?
