---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, post-training, web-agents, supervised-learning, synthetic-data, distillation, benchmarking]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.07776
paper_id: 2604.07776
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T10:25:55+08:00
decision: accept
score: 96
generator: scripts/update_hf_daily_papers.py
---

# Structured Distillation of Web Agent Capabilities Enables Generalization

## Summary

- one_sentence_summary: The paper proposes Agent-as-Annotators, a supervised data-generation pipeline for web agents that uses a frontier teacher model to synthesize and filter trajectories, enabling a 9B open-weight student to outperform prior open and some closed web-agent baselines.
- why_relevant: It is directly relevant to agents and post-training because it shows how structured synthetic supervision from a strong teacher can produce competitive web agents and transfer to unseen environments without RL.
- filter_reason: A strong web-agent post-training method with structured synthetic data generation, clear ablations, and cross-environment evaluation.
- hugging_face_paper: https://huggingface.co/papers/2604.07776
- original_paper: https://arxiv.org/abs/2604.07776
- source_basis: `original abstract page`

## Key Points

- Introduces Agent-as-Annotators, which maps web-trajectory synthesis onto annotation roles: Task Designer, Annotator, and Supervisor.
- Uses Gemini 3 Pro as the teacher to generate 3,000 trajectories across six web environments, then fine-tunes a 9B student on the 2,322 trajectories that pass quality filtering.
- Training is pure supervised learning, not RL, making the method a post-training/data-distillation approach for web agents.
- Reports 41.5% on WebArena, above Claude 3.5 Sonnet (36.0%), GPT-4o (31.5%), and the previous open-weight best Go-Browse (21.7%) under the same protocol.
- Shows transfer to unseen settings, including an 18.2 percentage point gain on WorkArena L1 and consistent improvements on three other benchmarks; ablations indicate filtering, evaluation hints, and reasoning traces each help.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.07776
- Hugging Face API entry: https://huggingface.co/api/papers/2604.07776
- arXiv abstract: https://arxiv.org/abs/2604.07776
- GitHub: https://github.com/McGill-NLP/agent-as-annotators
- Project page: https://agent-as-annotators.github.io/

## Paper Metadata

- authors: `Xing Han Lù`, `Siva Reddy`
- organization: `McGill NLP Group`
- ai_keywords: `web agents`, `synthetic trajectory generation`, `supervised learning`, `web environments`, `agent-as-annotators`, `task designer`, `annotator`, `supervisor`, `gemini 3 pro`, `webarena`, `workarena l1`, `go-browse`, `ablation studies`, `judge filtering`, `evaluation hints`, `reasoning traces`
- upvotes: `15`
- num_comments: `2`
- abstract: Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: https://agent-as-annotators.github.io
- hf_ai_summary: Structured synthetic trajectory generation using a frontier LLM as teacher enables open-weight web agents with superior performance and cross-environment capabilities.

## Source Excerpt

Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: this https URL

## Open Questions

- What exact model architecture and prompting setup were used for the 9B student?
- How much of the gain comes from each pipeline component individually versus their combination?
- How were the quality filters and evaluation hints implemented in detail?
- Are the reported gains stable across different teacher models or only with Gemini 3 Pro?
