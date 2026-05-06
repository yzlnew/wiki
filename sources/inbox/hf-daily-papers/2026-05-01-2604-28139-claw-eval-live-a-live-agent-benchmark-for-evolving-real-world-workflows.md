---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, benchmark, workflow-automation, evaluation]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.28139
paper_id: 2604.28139
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-01T12:32:04+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows

## Summary

- one_sentence_summary: Claw-Eval-Live is a live benchmark for workflow agents that combines refreshable demand signals with verifiable execution-based grading across controlled business and local workspace tasks.
- why_relevant: It is directly relevant to agent evaluation and tool-using systems because it tests end-to-end workflow execution with verifiable traces rather than only final answers, which also informs post-training priorities for agents.
- filter_reason: A live benchmark for workflow agents with execution-trace-based evaluation is directly useful for agent architectures and agent-evals.
- hugging_face_paper: https://huggingface.co/papers/2604.28139
- original_paper: https://arxiv.org/abs/2604.28139
- source_basis: `original abstract page`

## Key Points

- The benchmark separates a refreshable signal layer from a time-stamped release snapshot, so task selection can evolve with public workflow-demand signals while each release remains reproducible.
- Each release materializes controlled tasks with fixed fixtures, services, workspaces, and graders; the current release uses ClawHub Top-500 skills and contains 105 tasks.
- Grading uses execution traces, audit logs, service state, and post-run workspace artifacts, with deterministic checks when possible and structured LLM judging only for semantic dimensions.
- In evaluation of 13 frontier models, the best model passes 66.7% of tasks and no model reaches 70%, suggesting reliable workflow automation is still unsolved.
- Failures cluster by task family and execution surface: HR, management, and multi-system business workflows are persistent bottlenecks, while local workspace repair is easier but not saturated.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.28139
- Hugging Face API entry: https://huggingface.co/api/papers/2604.28139
- arXiv abstract: https://arxiv.org/abs/2604.28139
- GitHub: https://github.com/Claw-Eval-Live/Claw-Eval-Live
- Project page: https://claw-eval-live.github.io

## Paper Metadata

- authors: `Chenxin Li`, `Zhengyang Tang`, `Huangxin Lin`, `Yunlong Lin`, `Shijue Huang`, `Shengyuan Liu`, `Bowen Ye`, `Rang Li`, `Lei Li`, `Benyou Wang`, `Yixuan Yuan`
- ai_keywords: `workflow agents`, `live benchmark`, `execution traces`, `audit logs`, `structured LLM judging`, `task families`, `execution surface`, `workflow automation`
- upvotes: `17`
- num_comments: `2`
- abstract: LLM agents are expected to complete end-to-end units of work across software tools, business services, and local workspaces. Yet many agent benchmarks freeze a curated task set at release time and grade mainly the final response, making it difficult to evaluate agents against evolving workflow demand or verify whether a task was executed. We introduce Claw-Eval-Live, a live benchmark for workflow agents that separates a refreshable signal layer, updated across releases from public workflow-demand signals, from a reproducible, time-stamped release snapshot. Each release is constructed from public workflow-demand signals, with ClawHub Top-500 skills used in the current release, and materialized as controlled tasks with fixed fixtures, services, workspaces, and graders. For grading, Claw-Eval-Live records execution traces, audit logs, service state, and post-run workspace artifacts, using deterministic checks when evidence is sufficient and structured LLM judging only for semantic dimensions. The release contains 105 tasks spanning controlled business services and local workspace repair, and evaluates 13 frontier models under a shared public pass rule. Experiments reveal that reliable workflow automation remains far from solved: the leading model passes only 66.7% of tasks and no model reaches 70%. Failures are structured by task family and execution surface, with HR, management, and multi-system business workflows as persistent bottlenecks and local workspace repair comparatively easier but unsaturated. Leaderboard rank alone is insufficient because models with similar pass rates can diverge in overall completion, and task-level discrimination concentrates in a middle band of tasks. Claw-Eval-Live suggests that workflow-agent evaluation should be grounded twice, in fresh external demand and in verifiable agent action.
- hf_ai_summary: Claw-Eval-Live presents a dynamic benchmark for evaluating workflow agents that tracks evolving demands and verifies task execution through detailed logging and structured assessment methods.

## Source Excerpt

LLM agents are expected to complete end-to-end units of work across software tools, business services, and local workspaces. Yet many agent benchmarks freeze a curated task set at release time and grade mainly the final response, making it difficult to evaluate agents against evolving workflow demand or verify whether a task was executed. We introduce Claw-Eval-Live, a live benchmark for workflow agents that separates a refreshable signal layer, updated across releases from public workflow-demand signals, from a reproducible, time-stamped release snapshot. Each release is constructed from public workflow-demand signals, with ClawHub Top-500 skills used in the current release, and materialized as controlled tasks with fixed fixtures, services, workspaces, and graders. For grading, Claw-Eval-Live records execution traces, audit logs, service state, and post-run workspace artifacts, using deterministic checks when evidence is sufficient and structured LLM judging only for semantic dimensions. The release contains 105 tasks spanning controlled business services and local workspace repair, and evaluates 13 frontier models under a shared public pass rule. Experiments reveal that reliable workflow automation remains far from solved: the leading model passes only 66.7% of tasks and no model reaches 70%. Failures are structured by task family and execution surface, with HR, management, and multi-system business workflows as persistent bottlenecks and local workspace repair comparatively easier but unsaturated. Leaderboard rank alone is insufficient because models with similar pass rates can diverge in overall completion, and task-level discrimination concentrates in a middle band of tasks. Claw-Eval-Live suggests that workflow-agent evaluation should be grounded twice, in fresh external demand and in verifiable agent action.

## Open Questions

- How were the public workflow-demand signals collected and updated between releases?
- What specific criteria define the shared public pass rule used across models?
- How much of the score depends on deterministic checks versus structured LLM judging?
- Which model families were included among the 13 frontier models?
- What are the exact task-family definitions for HR, management, business workflows, and local workspace repair?
