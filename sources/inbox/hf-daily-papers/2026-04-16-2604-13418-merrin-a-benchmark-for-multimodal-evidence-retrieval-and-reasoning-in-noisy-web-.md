---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, tool-use, reasoning, llm-systems, benchmark, multimodal, web-search, evaluation]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.13418
paper_id: 2604.13418
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-16T09:18:53+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments

## Summary

- one_sentence_summary: MERRIN is a human-annotated benchmark for evaluating search-augmented agents on multimodal evidence retrieval and multi-hop reasoning in noisy web environments, and it shows current agents struggle badly on this task.
- why_relevant: This is directly relevant to agentic tool use and evaluation because it tests search-augmented reasoning under realistic web noise and multimodal evidence constraints, which are central to robust post-training and agent design.
- filter_reason: A strong benchmark for search-augmented agents and multimodal reasoning, directly aligned with agent evaluation and tool-use behavior.
- hugging_face_paper: https://huggingface.co/papers/2604.13418
- original_paper: https://arxiv.org/abs/2604.13418
- source_basis: `original abstract page`

## Key Points

- The benchmark targets underspecified search queries where the relevant evidence may span text, video, and audio, and where web results can be noisy or conflicting.
- MERRIN evaluates whether agents can identify relevant modalities, retrieve multimodal evidence, and reason across multiple hops over web sources.
- It differs from prior work by removing explicit modality cues from queries, including underexplored modalities, and requiring evidence retrieval from complex web environments.
- Across ten models and three settings (no search, native search, agentic search), the average accuracy was 22.3%, with the best agent reaching 40.1%.
- Stronger agents improved somewhat, but gains were limited by over-exploration, inefficient source selection, and overreliance on text despite multimodal evidence being available.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.13418
- Hugging Face API entry: https://huggingface.co/api/papers/2604.13418
- arXiv abstract: https://arxiv.org/abs/2604.13418
- GitHub: https://github.com/HanNight/MERRIN
- Project page: https://merrin-benchmark.github.io

## Paper Metadata

- authors: `Han Wang`, `David Wan`, `Hyunji Lee`, `Thinh Pham`, `Mikaela Cankosyan`, `Weiyuan Chen`, `Elias Stengel-Eskin`, `Tu Vu`, `Mohit Bansal`
- ai_keywords: `search-augmented agents`, `multimodal evidence retrieval`, `multi-hop reasoning`, `noisy web environments`, `human-annotated benchmark`, `web search`, `multimodal evidence`, `search agents`, `artificial intelligence agents`, `web retrieval`
- upvotes: `5`
- num_comments: `2`
- abstract: Motivated by the underspecified, multi-hop nature of search queries and the multimodal, heterogeneous, and often conflicting nature of real-world web results, we introduce MERRIN (Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments), a human-annotated benchmark for evaluating search-augmented agents. MERRIN measures AI agents' ability to identify relevant modalities, retrieve multimodal evidence, and perform multi-hop reasoning over noisy web sources. It differs from prior work in three important aspects: (1) using natural language queries without explicit modality cues, (2) incorporating underexplored modalities such as video and audio, and (3) requiring the retrieval of complex, often noisy or conflicting multimodal evidence during web search. We evaluate diverse search agents powered by ten models, including strong closed-source models (e.g., GPT-5.4-mini, Gemini 3/3.1 Flash/Pro) and open-weight models (Qwen3-4B/30B/235B), across three search settings (no search, native search, and agentic search). Our results show that MERRIN is highly challenging: the average accuracy across all agents is 22.3%, with the best-performing agent reaching only 40.1%. We further observe that while stronger agents like Gemini Deep Research achieve higher performance, gains are modest due to over-exploration; they take more steps and use more tools, but are often distracted by conflicting or partially relevant web content, leading to incorrect answers. Compared to humans, these agents consume more resources yet achieve lower accuracy, largely due to inefficient source selection and an overreliance on text modalities. These findings highlight the need for search agents capable of robust search and reasoning across diverse modalities in noisy web environments, making MERRIN a valuable testbed for evaluating such capabilities.
- hf_ai_summary: MERRIN is a human-annotated benchmark for evaluating search-augmented agents in multimodal, noisy web environments, demonstrating significant challenges in retrieving and reasoning over diverse evidence types.

## Source Excerpt

Motivated by the underspecified, multi-hop nature of search queries and the multimodal, heterogeneous, and often conflicting nature of real-world web results, we introduce MERRIN (Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments), a human-annotated benchmark for evaluating search-augmented agents. MERRIN measures AI agents' ability to identify relevant modalities, retrieve multimodal evidence, and perform multi-hop reasoning over noisy web sources. It differs from prior work in three important aspects: (1) using natural language queries without explicit modality cues, (2) incorporating underexplored modalities such as video and audio, and (3) requiring the retrieval of complex, often noisy or conflicting multimodal evidence during web search. We evaluate diverse search agents powered by ten models, including strong closed-source models (e.g., GPT-5.4-mini, Gemini 3/3.1 Flash/Pro) and open-weight models (Qwen3-4B/30B/235B), across three search settings (no search, native search, and agentic search). Our results show that MERRIN is highly challenging: the average accuracy across all agents is 22.3%, with the best-performing agent reaching only 40.1%. We further observe that while stronger agents like Gemini Deep Research achieve higher performance, gains are modest due to over-exploration; they take more steps and use more tools, but are often distracted by conflicting or partially relevant web content, leading to incorrect answers. Compared to humans, these agents consume more resources yet achieve lower accuracy, largely due to inefficient source selection and an overreliance on text modalities. These findings highlight the need for search agents capable of robust search and reasoning across diverse modalities in noisy web environments, making MERRIN a valuable testbed for evaluating such capabilities.

## Open Questions

- What kinds of questions or task categories are included in MERRIN?
- How large is the benchmark and how is the human annotation structured?
- What exact scoring protocol is used across the three search settings?
- Which models or agent configurations performed best and why?
- How much of the failure mode comes from retrieval versus reasoning?
