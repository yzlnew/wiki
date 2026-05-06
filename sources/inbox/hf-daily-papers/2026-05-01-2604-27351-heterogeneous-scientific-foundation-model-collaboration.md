---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, llm-systems, reasoning, multi-agent, scientific-ml, foundation-models, orchestration]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.27351
paper_id: 2604.27351
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-01T08:30:02+08:00
decision: accept
score: 78
generator: scripts/update_hf_daily_papers.py
---

# Heterogeneous Scientific Foundation Model Collaboration

## Summary

- one_sentence_summary: Eywa is a heterogeneous agentic framework that lets language-model reasoning coordinate domain-specific scientific foundation models over non-linguistic data, improving performance on structured scientific tasks.
- why_relevant: This paper is directly relevant to agents and tool-using systems because it proposes an orchestration pattern for combining language reasoning with specialized foundation models, which is adjacent to post-training systems that expand agent capabilities beyond text.
- filter_reason: A technically grounded agent framework for orchestrating specialized models across modalities, directly relevant to agent architectures and tool-like collaboration.
- hugging_face_paper: https://huggingface.co/papers/2604.27351
- original_paper: https://arxiv.org/abs/2604.27351
- source_basis: `original abstract page`

## Key Points

- The core idea is to attach a language-model-based reasoning interface to domain-specific foundation models so they can participate in higher-level agentic decision-making.
- Eywa is designed to work in multiple settings: as a single-agent drop-in replacement (`EywaAgent`), as specialized agents inside multi-agent systems (`EywaMAS`), and in a planning-based orchestration setup (`EywaOrchestra`).
- The framework targets heterogeneous scientific data modalities rather than treating language as the universal interface.
- Evaluation spans scientific domains across physical, life, and social sciences.
- The reported result is improved performance on tasks involving structured and domain-specific data, with less dependence on language-only reasoning through collaboration with specialized models.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27351
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27351
- arXiv abstract: https://arxiv.org/abs/2604.27351
- GitHub: https://github.com/Violet24K/Eywa
- Project page: https://www.zihao.website/eywa.github.io/

## Paper Metadata

- authors: `Zihao Li`, `Jiaru Zou`, `Feihao Fang`, `Xuying Ning`, `Mengting Ai`, `Tianxin Wei`, `Sirui Chen`, `Xiyuan Yang`, `Jingrui He`
- organization: `University of Illinois at Urbana-Champaign`
- ai_keywords: `agentic framework`, `domain-specific foundation models`, `language-model-based reasoning`, `non-linguistic data modalities`, `predictive foundation models`, `multi-agent systems`, `planning-based orchestration`, `heterogeneous data modalities`
- upvotes: `176`
- num_comments: `1`
- abstract: Agentic large language model systems have demonstrated strong capabilities. However, their reliance on language as the universal interface fundamentally limits their applicability to many real-world problems, especially in scientific domains where domain-specific foundation models have been developed to address specialized tasks beyond natural language. In this work, we introduce Eywa, a heterogeneous agentic framework designed to extend language-centric systems to a broader class of scientific foundation models. The key idea of Eywa is to augment domain-specific foundation models with a language-model-based reasoning interface, enabling language models to guide inference over non-linguistic data modalities. This design allows predictive foundation models, which are typically optimized for specialized data and tasks, to participate in higher-level reasoning and decision-making processes within agentic systems. Eywa can serve as a drop-in replacement for a single-agent pipeline (EywaAgent) or be integrated into existing multi-agent systems by replacing traditional agents with specialized agents (EywaMAS). We further investigate a planning-based orchestration framework in which a planner dynamically coordinates traditional agents and Eywa agents to solve complex tasks across heterogeneous data modalities (EywaOrchestra). We evaluate Eywa across a diverse set of scientific domains spanning physical, life, and social sciences. Experimental results demonstrate that Eywa improves performance on tasks involving structured and domain-specific data, while reducing reliance on language-based reasoning through effective collaboration with specialized foundation models.
- hf_ai_summary: Eywa is a heterogeneous agentic framework that extends language-centric systems to scientific foundation models by integrating domain-specific models with language-based reasoning interfaces for improved performance across diverse scientific domains.

## Source Excerpt

Agentic large language model systems have demonstrated strong capabilities. However, their reliance on language as the universal interface fundamentally limits their applicability to many real-world problems, especially in scientific domains where domain-specific foundation models have been developed to address specialized tasks beyond natural language. In this work, we introduce Eywa, a heterogeneous agentic framework designed to extend language-centric systems to a broader class of scientific foundation models. The key idea of Eywa is to augment domain-specific foundation models with a language-model-based reasoning interface, enabling language models to guide inference over non-linguistic data modalities. This design allows predictive foundation models, which are typically optimized for specialized data and tasks, to participate in higher-level reasoning and decision-making processes within agentic systems. Eywa can serve as a drop-in replacement for a single-agent pipeline (EywaAgent) or be integrated into existing multi-agent systems by replacing traditional agents with specialized agents (EywaMAS). We further investigate a planning-based orchestration framework in which a planner dynamically coordinates traditional agents and Eywa agents to solve complex tasks across heterogeneous data modalities (EywaOrchestra). We evaluate Eywa across a diverse set of scientific domains spanning physical, life, and social sciences. Experimental results demonstrate that Eywa improves performance on tasks involving structured and domain-specific data, while reducing reliance on language-based reasoning through effective collaboration with specialized foundation models.

## Open Questions

- Which specific scientific foundation models were integrated, and what were their modalities?
- How much does Eywa improve over language-only agent baselines on each benchmark task?
- What planner/orchestration algorithm does EywaOrchestra use, and how does it choose between traditional and specialized agents?
- Does the paper report any failure modes or cases where the heterogeneous setup hurts performance?
