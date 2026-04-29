---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, agent-architectures, llm-systems, reasoning, spoken-dialogue, latency, post-training]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.15710
paper_id: 2604.15710
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-21T21:00:52+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# VoxMind: An End-to-End Agentic Spoken Dialogue System

## Summary

- one_sentence_summary: VoxMind is an end-to-end spoken dialogue framework that adds agentic tool use via structured reasoning and dynamic tool management to improve task completion without sacrificing conversational quality.
- why_relevant: This paper is directly relevant to agent architectures and tool-using systems, and it also touches post-training-style capability expansion through dataset-driven reasoning and tool orchestration.
- filter_reason: A technical agentic system paper with tool use, reasoning, and dynamic tool management that directly matches agents and environment interaction.
- hugging_face_paper: https://huggingface.co/papers/2604.15710
- original_paper: https://arxiv.org/abs/2604.15710
- source_basis: `original abstract page`

## Key Points

- It introduces a curated 470-hour AgentChat dataset to train end-to-end spoken dialogue models for agentic behavior.
- The proposed "Think-before-Speak" mechanism encourages structured internal reasoning before planning and response generation.
- A Multi-Agent Dynamic Tool Management architecture asynchronously delegates retrieval to an auxiliary agent, aiming to decouple inference latency from toolset size.
- Reported results show task completion rate rising from 34.88% to 74.57% against strong baselines, with spoken-agent performance surpassing Gemini-2.5-Pro while preserving general conversational quality.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.15710
- Hugging Face API entry: https://huggingface.co/api/papers/2604.15710
- arXiv abstract: https://arxiv.org/abs/2604.15710
- GitHub: https://github.com/MM-Speech/VoxMind

## Paper Metadata

- authors: `Tianle Liang`, `Yifu Chen`, `Shengpeng Ji`, `Yijun Chen`, `Zhiyang Jia`, `Jingyu Lu`, `Fan Zhuo`, `Xueyi Pu`, `Yangzhuo Li`, `Zhou Zhao`
- ai_keywords: `end-to-end spoken dialogue models`, `agentic capabilities`, `tool use`, `AgentChat dataset`, `Think-before-Speak mechanism`, `Multi-Agent Dynamic Tool Management`, `retrieval tasks`, `inference latency`, `task completion rate`, `conversational quality`
- upvotes: `6`
- num_comments: `1`
- abstract: Recent end-to-end spoken dialogue models enable natural interaction. However, as user demands become increasingly complex, models that rely solely on conversational abilities often struggle to cope. Incorporating agentic capabilities is therefore essential: by enabling tool use, these models can extend their knowledge boundaries and better solve real-world tasks. Yet, existing research has largely concentrated on core perception and generation, with comparatively limited exploration of such tool-augmented extensions. To bridge this gap, we present VoxMind, an integrated framework designed to equip end-to-end spoken dialogue models with comprehensive agentic abilities. Leveraging our curated 470-hour AgentChat dataset, we incorporate a "Think-before-Speak" mechanism, enabling the model to internalize structured reasoning as a critical prerequisite for planning and response generation. Furthermore, to mitigate latency bottlenecks caused by large-scale tool integration, we propose a Multi-Agent Dynamic Tool Management architecture. By asynchronously delegating retrieval tasks to an auxiliary agent aligned with the main model's reasoning trajectory, this system effectively decouples inference latency from toolset size. Experimental results confirm that VoxMind achieves significant improvements in agent performance: compared with strong baselines, the task completion rate increases from 34.88% to 74.57%, outperforming Gemini-2.5-Pro on spoken agent tasks while preserving general conversational quality. The source code and associated data are publicly available at https://github.com/MM-Speech/VoxMind.
- hf_ai_summary: VoxMind enhances spoken dialogue models with agentic capabilities through a "Think-before-Speak" mechanism and dynamic tool management to improve task completion rates while maintaining conversational quality.

## Source Excerpt

Recent end-to-end spoken dialogue models enable natural interaction. However, as user demands become increasingly complex, models that rely solely on conversational abilities often struggle to cope. Incorporating agentic capabilities is therefore essential: by enabling tool use, these models can extend their knowledge boundaries and better solve real-world tasks. Yet, existing research has largely concentrated on core perception and generation, with comparatively limited exploration of such tool-augmented extensions. To bridge this gap, we present VoxMind, an integrated framework designed to equip end-to-end spoken dialogue models with comprehensive agentic abilities. Leveraging our curated 470-hour AgentChat dataset, we incorporate a "Think-before-Speak" mechanism, enabling the model to internalize structured reasoning as a critical prerequisite for planning and response generation. Furthermore, to mitigate latency bottlenecks caused by large-scale tool integration, we propose a Multi-Agent Dynamic Tool Management architecture. By asynchronously delegating retrieval tasks to an auxiliary agent aligned with the main model's reasoning trajectory, this system effectively decouples inference latency from toolset size. Experimental results confirm that VoxMind achieves significant improvements in agent performance: compared with strong baselines, the task completion rate increases from 34.88% to 74.57%, outperforming Gemini-2.5-Pro on spoken agent tasks while preserving general conversational quality. The source code and associated data are publicly available at this https URL .

## Open Questions

- How is the 470-hour AgentChat dataset constructed and labeled?
- What exactly does the Think-before-Speak mechanism change in training or inference?
- What retrieval tasks are handled by the auxiliary agent, and how is alignment with the main model's reasoning trajectory enforced?
- What evaluation benchmarks were used to measure task completion rate and conversational quality?
- How large is the latency reduction from the dynamic tool management architecture as tool count grows?
