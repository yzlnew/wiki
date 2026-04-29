---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, agent-evals, llm-systems, benchmark, evaluation, workflow]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.15715
paper_id: 2604.15715
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-20T09:42:51+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows

## Summary

- one_sentence_summary: GTA-2 is a hierarchical benchmark for general tool agents that tests both atomic tool-use precision and long-horizon open-ended workflows using real queries, deployed tools, and multimodal contexts.
- why_relevant: This paper is directly relevant to tool-using agents and post-training because it benchmarks real workflow execution, exposes the limits of current models, and shows that harness design can matter as much as underlying model capability.
- filter_reason: This is a technically useful tool-use and agent evaluation benchmark with open-ended workflow execution and harness design analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.15715
- original_paper: https://arxiv.org/abs/2604.15715
- source_basis: `original abstract page`

## Key Points

- The benchmark is split into GTA-Atomic for short-horizon, closed-ended tool use and GTA-Workflow for long-horizon, open-ended end-to-end tasks.
- It is built around real-world authenticity, using real user queries, deployed tools, and multimodal contexts rather than AI-generated prompts or dummy tools.
- For open-ended workflows, the paper proposes a recursive checkpoint-based evaluation that breaks objectives into verifiable sub-goals.
- The evaluation is designed to measure both model capability and the quality of agent execution frameworks or harnesses.
- Experiments show a steep capability cliff: frontier models score below 50% on atomic tasks and top models reach only 14.39% on workflow completion.
- Checkpoint-guided feedback improves performance, and stronger frameworks such as Manus and OpenClaw materially improve workflow completion.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.15715
- Hugging Face API entry: https://huggingface.co/api/papers/2604.15715
- arXiv abstract: https://arxiv.org/abs/2604.15715

## Paper Metadata

- authors: `Jize Wang`, `Xuanxuan Liu`, `Yining Li`, `Songyang Zhang`, `Yijun Wang`, `Zifei Shan`, `Xinyi Le`, `Cailian Chen`, `Xinping Guan`, `Dacheng Tao`
- ai_keywords: `tool-use benchmarks`, `general-purpose agents`, `real-world authenticity`, `atomic tool use`, `open-ended workflows`, `recursive checkpoint-based evaluation`, `execution harnesses`, `model capabilities`, `agent execution frameworks`
- upvotes: `3`
- num_comments: `2`
- abstract: The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at https://github.com/open-compass/GTA.
- hf_ai_summary: General Tool Agents face significant challenges in real-world workflow completion, with performance dropping sharply from atomic tasks to complex, open-ended workflows, highlighting the need for improved execution frameworks beyond model capacity.

## Source Excerpt

The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at this https URL .

## Open Questions

- What exact tasks, tools, and multimodal inputs are included in GTA-Workflow?
- How are recursive checkpoints defined and scored in the evaluation protocol?
- Which frontier models were tested, and what were their per-benchmark results beyond the reported aggregate rates?
- How much of the performance gain comes from checkpoint-guided feedback versus the choice of execution framework?
- Will the dataset, code, and evaluation harness be available in a form that supports replication?
