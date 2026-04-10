---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, post-training, web-agents, synthetic-data, supervised-finetuning, generalization]
source_count: 1
updated: 2026-04-10
source_url: https://arxiv.org/abs/2604.07776
paper_id: 2604.07776
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T10:25:55+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Structured Distillation of Web Agent Capabilities Enables Generalization

## Summary

- one_sentence_summary: Agent-as-Annotators turns synthetic web-agent trajectory generation into a structured annotation pipeline and uses it to fine-tune a 9B student that generalizes well across web benchmarks.
- why_relevant: This paper is directly relevant to agent training and post-training because it shows how structured synthetic supervision can produce a competitive open-weight web agent with strong transfer to new environments.
- filter_reason: Strongly relevant web-agent training work with synthetic trajectories, transfer, and evaluation across environments.
- hugging_face_paper: https://huggingface.co/papers/2604.07776
- original_paper: https://arxiv.org/abs/2604.07776
- source_basis: `original abstract page`

## Key Points

- The method replaces human annotation roles with modular LLM components: Task Designer, Annotator, and Supervisor, all used to generate synthetic trajectories for web agents.
- Using Gemini 3 Pro as teacher, the authors generate 3,000 trajectories across six web environments and retain 2,322 after quality filtering for supervised fine-tuning.
- A 9B-parameter student trained with pure supervised learning reaches 41.5% on WebArena under the same protocol, beating Claude 3.5 Sonnet, GPT-4o, and the previous best open-weight result, Go-Browse.
- The trained agent transfers to unseen environments, including an 18.2 percentage point gain on WorkArena L1, and improves on three additional benchmarks.
- Ablations show that Judge filtering, evaluation hints, and reasoning traces each contribute measurable gains, supporting the value of structured trajectory synthesis.

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
- upvotes: `1`
- num_comments: `1`
- abstract: Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: https://agent-as-annotators.github.io
- hf_ai_summary: Structured synthetic trajectory generation using a frontier LLM as teacher enables open-weight web agents with superior performance and cross-environment capabilities.

## Source Excerpt

Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: this https URL

## Open Questions

- What exact model architecture and training recipe were used for the 9B student?
- How much each ablation contributed quantitatively to final performance is not specified in the abstract.
- What are the six training environments and the three additional benchmarks?
- How does the quality filtering criterion work in detail?
- Does the approach rely on any environment-specific prompting or evaluation hints that might limit reproducibility?
