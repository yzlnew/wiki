---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-architectures, agent-evals, coding-agents, architecture, mcp, plugins, tool-use, infrastructure]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.11045
paper_id: 2604.11045
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-16T11:55:28+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Sema Code: Decoupling AI Coding Agents into Programmable, Embeddable Infrastructure

## Summary

- one_sentence_summary: Sema Code proposes an embeddable, framework-first AI coding agent architecture that separates a shared core reasoning engine from client interfaces and exposes it as a standalone npm library.
- why_relevant: It is directly relevant to agent systems and post-training-adjacent infrastructure work because it focuses on the architecture needed to make tool-using coding agents reusable, embeddable, and operable across multiple interfaces.
- filter_reason: Strong systems-focused paper on coding agents with programmable architecture, multi-agent scheduling, and runtime isolation.
- hugging_face_paper: https://huggingface.co/papers/2604.11045
- original_paper: https://arxiv.org/abs/2604.11045
- source_basis: `original abstract page`

## Key Points

- The paper argues that existing coding agents are too tightly bound to one delivery form, such as a CLI, IDE plugin, or web app, which makes reuse across heterogeneous enterprise environments difficult.
- Sema Code decouples the core agent engine from client layers so any runtime can drive it programmatically through a standalone npm library.
- The framework is organized around eight mechanisms: multi-tenant engine isolation, FIFO input queuing with safe session reconstruction, adaptive context compression, multi-agent collaborative scheduling, Todo-based process management, asynchronous permission control, MCP/Skills/Plugins integration, and a background task framework with separated execution and observation privileges.
- The same Sema Core engine powers both a VSCode extension and a multi-channel messaging gateway, showing that different product surfaces can share the same reasoning kernel.
- The main contribution is architectural: it turns a coding agent into shared infrastructure rather than a single-purpose app.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11045
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11045
- arXiv abstract: https://arxiv.org/abs/2604.11045
- GitHub: https://github.com/midea-ai/sema-code-core

## Paper Metadata

- authors: `Huacan Wang`, `Jie Zhou`, `Ningyan Zhu`, `Shuo Zhang`, `Feiyu Chen`, `Jiarou Wu`, `Ge Chen`, `Chen Liu`, `Wangyi Chen`, `Xiaofeng Mou`, `Yi Xu`
- organization: `Midea AI Research Center`
- ai_keywords: `AI coding agents`, `embeddable framework`, `pluggable architecture`, `multi-tenant engine isolation`, `FIFO input queuing`, `adaptive context compression`, `multi-agent collaborative scheduling`, `intelligent Todo-based process management`, `asynchronous permission control`, `ecosystem integration`, `MCP`, `Skills`, `Plugins`, `background task framework`
- upvotes: `18`
- num_comments: `2`
- abstract: AI coding agents have become central to developer workflows, yet every existing solution locks its reasoning capabilities within a specific delivery form, such as a CLI, IDE plugin, or web application. This limitation creates systemic barriers when enterprises attempt to reuse these capabilities across heterogeneous engineering environments. To address this challenge, we present Sema Code, an open AI coding framework built on the principle of being embeddable, pluggable, and framework-first. Sema Code completely decouples the core agent engine from all client layers, publishing it as a standalone npm library that any runtime can drive programmatically. Built around this architecture, we designed eight key mechanisms: multi-tenant engine isolation, FIFO input queuing with safe session reconstruction, adaptive context compression, multi-agent collaborative scheduling, intelligent Todo-based process management, four-layer asynchronous permission control, three-tier ecosystem integration spanning MCP, Skills, and Plugins, and a background task framework with separated execution and observation privileges. These mechanisms collectively address the engineering challenges of transforming a complex agent engine into a shared, programmable core. Demonstrating its architectural versatility, the same Sema Core engine simultaneously powers a VSCode extension and a multi-channel messaging gateway, which we name SemaClaw, to unify agent interactions across platforms such as Telegram and Feishu. These represent two fundamentally different product forms sharing an identical reasoning kernel, differing only at the client layer.
- hf_ai_summary: Sema Code presents an open AI coding framework that decouples the core agent engine from client interfaces, enabling shared reasoning capabilities across diverse development environments through a standalone npm library and modular architecture.

## Source Excerpt

AI coding agents have become central to developer workflows, yet every existing solution locks its reasoning capabilities within a specific delivery form, such as a CLI, IDE plugin, or web application. This limitation creates systemic barriers when enterprises attempt to reuse these capabilities across heterogeneous engineering environments. To address this challenge, we present Sema Code, an open AI coding framework built on the principle of being embeddable, pluggable, and framework-first. Sema Code completely decouples the core agent engine from all client layers, publishing it as a standalone npm library that any runtime can drive programmatically. Built around this architecture, we designed eight key mechanisms: multi-tenant engine isolation, FIFO input queuing with safe session reconstruction, adaptive context compression, multi-agent collaborative scheduling, intelligent Todo-based process management, four-layer asynchronous permission control, three-tier ecosystem integration spanning MCP, Skills, and Plugins, and a background task framework with separated execution and observation privileges. These mechanisms collectively address the engineering challenges of transforming a complex agent engine into a shared, programmable core. Demonstrating its architectural versatility, the same Sema Core engine simultaneously powers a VSCode extension and a multi-channel messaging gateway, which we name SemaClaw, to unify agent interactions across platforms such as Telegram and Feishu. These represent two fundamentally different product forms sharing an identical reasoning kernel, differing only at the client layer.

## Open Questions

- What empirical evaluation shows that the eight mechanisms improve reliability, latency, or task success?
- How does safe session reconstruction work in detail when queued inputs arrive out of order or after interruptions?
- What permission model is used for the four-layer asynchronous control path?
- How do MCP, Skills, and Plugins interact in practice, and what is the boundary between them?
- Does the paper report any limitations or overhead from making the engine multi-tenant and background-task capable?
