---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, agent-evals, llm-systems, personalization, memory, benchmark, evaluation]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.17886
paper_id: 2604.17886
published: 2026-04-20T04:00:00+08:00
submitted_on_daily: 2026-04-21T14:33:05+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# Latent Preference Modeling for Cross-Session Personalized Tool Calling

## Summary

- one_sentence_summary: This paper introduces MPT, a 265-dialogue benchmark for personalized tool calling across multiple sessions, and PRefine, a test-time memory method that improves tool execution by turning user history into evolving preference hypotheses.
- why_relevant: It directly targets agent tool-use and evaluation for personalized, memory-based action selection, which is central to post-training and agentic systems that must infer user preferences over time.
- filter_reason: Directly studies tool-augmented agents, memory for personalization, and evaluates a new benchmark with a concrete test-time method.
- hugging_face_paper: https://huggingface.co/papers/2604.17886
- original_paper: https://arxiv.org/abs/2604.17886
- source_basis: `original abstract page`

## Key Points

- The core problem is under-specified user requests in tool-augmented agents, where API calls often need missing arguments inferred from prior interactions.
- MPT is a benchmark of 265 multi-session dialogues designed around three tasks: Preference Recall, Preference Induction, and Preference Transfer.
- PRefine is a test-time memory-augmented approach that models user preferences as evolving hypotheses rather than fixed facts.
- PRefine uses a generate--verify--refine loop to extract reusable constraints from history and improve tool-calling accuracy.
- The method reportedly uses only 1.24% of the tokens required by full-history prompting while still improving performance.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.17886
- Hugging Face API entry: https://huggingface.co/api/papers/2604.17886
- arXiv abstract: https://arxiv.org/abs/2604.17886
- Project page: https://still-with-you.github.io/pages/prefine/

## Paper Metadata

- authors: `Yejin Yoon`, `Minseo Kim`, `Taeuk Kim`
- organization: `HYU NLP Lab.`
- ai_keywords: `tool-augmented agents`, `API execution`, `personalized tool calling`, `MPT benchmark`, `PRefine`, `test-time memory augmentation`, `generate--verify--refine loop`, `user preferences`, `multi-session dialogues`, `preference recall`, `preference induction`, `preference transfer`
- upvotes: `0`
- num_comments: `1`
- abstract: Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use. This poses a fundamental challenge for tool-augmented agents, as API execution typically requires complete arguments, highlighting the need for personalized tool calling. To study this problem, we introduce MPT, a benchmark comprising 265 multi-session dialogues that cover three challenges: Preference Recall, Preference Induction, and Preference Transfer. We also propose PRefine, a test-time memory-augmented method that represents user preferences as evolving hypotheses. Through a generate--verify--refine loop, it extracts reusable constraints from history and improves tool-calling accuracy while using only 1.24% of the tokens required by full-history prompting. These results indicate that robust personalization in agentic systems depends on memory that captures the reasons behind user choices, not just the choices themselves.
- hf_ai_summary: Personalized tool calling in LLM-based agents is improved through memory-augmented methods that capture user choice reasoning rather than just choices, using minimal token overhead.

## Source Excerpt

Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use. This poses a fundamental challenge for tool-augmented agents, as API execution typically requires complete arguments, highlighting the need for personalized tool calling. To study this problem, we introduce MPT, a benchmark comprising 265 multi-session dialogues that cover three challenges: Preference Recall, Preference Induction, and Preference Transfer. We also propose PRefine, a test-time memory-augmented method that represents user preferences as evolving hypotheses. Through a generate--verify--refine loop, it extracts reusable constraints from history and improves tool-calling accuracy while using only 1.24% of the tokens required by full-history prompting. These results indicate that robust personalization in agentic systems depends on memory that captures the reasons behind user choices, not just the choices themselves.

## Open Questions

- How does PRefine compare against other memory or retrieval baselines beyond full-history prompting?
- What are the absolute accuracy gains on each of the three MPT challenge types?
- How robust is the method when user preferences change or conflict across sessions?
- Does the benchmark or method generalize beyond the specific tool domains covered in MPT?
