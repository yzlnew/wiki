---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, reinforcement-learning, llm-systems, post-training, evaluation, synthetic-data, tool-use]
source_count: 1
updated: 2026-05-01
source_url: https://arxiv.org/abs/2604.26904
paper_id: 2604.26904
published: 2026-04-29T04:00:00+08:00
submitted_on_daily: 2026-04-30T08:41:21+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# ClawGym: A Scalable Framework for Building Effective Claw Agents

## Summary

- one_sentence_summary: ClawGym is a framework for building and evaluating Claw-style personal agents using synthetic verifiable tasks, supervised fine-tuning on rollout trajectories, and a benchmark for diagnostic evaluation.
- why_relevant: The paper is directly relevant to agents and post-training because it focuses on scalable agent training data, supervised fine-tuning, reinforcement learning, and evaluation for tool-using workspace agents.
- filter_reason: Directly targets agent training, rollout-based RL, and benchmarked evaluation for Claw-style agents.
- hugging_face_paper: https://huggingface.co/papers/2604.26904
- original_paper: https://arxiv.org/abs/2604.26904
- source_basis: `original abstract page`

## Key Points

- ClawGym-SynData contains 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations.
- The synthetic tasks are paired with realistic mock workspaces and hybrid verification mechanisms to make training data more verifiable.
- ClawGym-Agents are trained with supervised fine-tuning on black-box rollout trajectories.
- The paper also explores reinforcement learning with a lightweight pipeline that parallelizes rollouts across per-task sandboxes.
- ClawGym-Bench provides 200 evaluation instances, calibrated with automated filtering plus human-LLM review.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.26904
- Hugging Face API entry: https://huggingface.co/api/papers/2604.26904
- arXiv abstract: https://arxiv.org/abs/2604.26904
- Project page: https://github.com/ClawGym

## Paper Metadata

- authors: `Fei Bai`, `Huatong Song`, `Shuang Sun`, `Daixuan Cheng`, `Yike Yang`, `Chuan Hao`, `Renyuan Li`, `Feng Chang`, `Yuan Wei`, `Ran Tao`, `Bryan Dai`, `Jian Yang`, `Wayne Xin Zhao`
- ai_keywords: `Claw-style environments`, `multi-step workflows`, `scalable development`, `verifiable training data`, `agent training`, `diagnostic evaluation`, `ClawGym-SynData`, `persona-driven intents`, `skill-grounded operations`, `mock workspaces`, `hybrid verification mechanisms`, `ClawGym-Agents`, `supervised fine-tuning`, `black-box rollout trajectories`, `reinforcement learning`, `lightweight pipeline`, `per-task sandboxes`, `ClawGym-Bench`, `automated filtering`, `human-LLM review`
- upvotes: `38`
- num_comments: `3`
- abstract: Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task sandboxes.To support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at https://github.com/ClawGym.
- hf_ai_summary: ClawGym presents a scalable framework for developing Claw-style personal agents with synthetic training data, verified workspaces, and benchmark evaluation.

## Source Excerpt

Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task this http URL support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at this https URL .

## Open Questions

- How much do ClawGym-Agents improve over baseline models on ClawGym-Bench and other benchmarks?
- What exact verification signals are used in the hybrid verification mechanisms?
- How does the lightweight reinforcement learning pipeline compare to supervised fine-tuning in effectiveness and cost?
- What types of tasks and tools are covered by the 200 benchmark instances?
