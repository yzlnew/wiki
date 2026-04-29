---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, reinforcement-learning, post-training, agent-evals, llm-systems, tool-use, deep-research, benchmark]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.14518
paper_id: 2604.14518
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-21T07:47:32+08:00
decision: accept
score: 95
generator: scripts/update_hf_daily_papers.py
---

# Mind DeepResearch Technical Report

## Summary

- one_sentence_summary: Mind DeepResearch (MindDR) is a ~30B-parameter multi-agent deep research system that combines a three-agent workflow with a four-stage training pipeline to reach strong benchmark performance and product-level deployment.
- why_relevant: It is directly relevant to agents and post-training because it studies how multi-agent tool-using systems can be trained with RL and preference alignment to improve deep research performance.
- filter_reason: Multi-agent deep research system with Search-RL, Report-RL, preference alignment, and benchmarked agent evaluation is directly aligned with RL/post-training and agents.
- hugging_face_paper: https://huggingface.co/papers/2604.14518
- original_paper: https://arxiv.org/abs/2604.14518
- source_basis: `original abstract page`

## Key Points

- Uses a collaborative three-agent architecture: Planning Agent, DeepSearch Agent, and Report Agent.
- Trains the agents with a four-stage pipeline: SFT cold-start, Search-RL, Report-RL, and preference alignment.
- Reports competitive results at ~30B scale, including 45.7% on BrowseComp-ZH, 42.8% on BrowseComp, 46.5% on WideSearch, 75.0% on xbench-DS, and 52.5 on DeepResearch Bench.
- Introduces MindDR Bench, a 500-query benchmark drawn from internal real-world Chinese product user interactions.
- Evaluates MindDR Bench with a multi-dimensional rubric instead of a single RACE-style metric, and reports a state-of-the-art score of 51.8.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14518
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14518
- arXiv abstract: https://arxiv.org/abs/2604.14518

## Paper Metadata

- authors: `MindDR Team`, `Li Auto Inc`
- organization: `LiAuto`
- ai_keywords: `multi-agent deep research framework`, `data synthesis`, `multi-stage training pipeline`, `collaborative three-agent architecture`, `agent-specialized training pipeline`, `SFT cold-start`, `Search-RL`, `Report-RL`, `preference alignment`, `real-world Chinese queries`, `multi-dimensional rubric system`
- upvotes: `18`
- num_comments: `2`
- abstract: We present Mind DeepResearch (MindDR), an efficient multi-agent deep research framework that achieves leading performance with only ~30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with ~30B-scale models. Specifically, MindDR achieves 45.7% on BrowseComp-ZH, 42.8% on BrowseComp, 46.5% on WideSearch, 75.0% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce MindDR Bench, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.
- hf_ai_summary: MindDR is an efficient multi-agent deep research framework that achieves high performance through a collaborative three-agent architecture and specialized four-stage training pipeline, demonstrating strong results on multiple benchmarks.

## Source Excerpt

We present Mind DeepResearch (MindDR), an efficient multi-agent deep research framework that achieves leading performance with only ~30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with ~30B-scale models. Specifically, MindDR achieves 45.7% on BrowseComp-ZH, 42.8% on BrowseComp, 46.5% on WideSearch, 75.0% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce MindDR Bench, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

## Open Questions

- What are the exact roles, interfaces, and message flows between the three agents?
- How is Search-RL defined, including the reward signal and rollout setup?
- How is Report-RL defined, and what aspects of report quality does it optimize?
- What dimensions are included in the MindDR Bench rubric, and how are scores aggregated?
- How much does each training stage contribute in ablations, especially compared with SFT alone?
