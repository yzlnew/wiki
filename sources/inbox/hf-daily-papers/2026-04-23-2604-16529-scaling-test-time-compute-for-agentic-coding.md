---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, coding-agents, agentic-coding, test-time-scaling, trajectory-summaries, recursive-voting, post-training, swe-bench, terminal-bench]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.16529
paper_id: 2604.16529
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-23T13:11:23+08:00
decision: accept
score: 95
generator: scripts/update_hf_daily_papers.py
---

# Scaling Test-Time Compute for Agentic Coding

## Summary

- one_sentence_summary: The paper proposes a test-time scaling framework for long-horizon coding agents that compresses rollout trajectories into structured summaries and uses them for selection and refinement.
- why_relevant: It is directly relevant to agentic systems and post-training/test-time scaling because it studies how to improve coding agents by reusing structured traces rather than just sampling more trajectories.
- filter_reason: Directly targets agentic coding, test-time scaling, and evaluation on SWE-Bench and Terminal-Bench with concrete inference-time methods.
- hugging_face_paper: https://huggingface.co/papers/2604.16529
- original_paper: https://arxiv.org/abs/2604.16529
- source_basis: `original abstract page`

## Key Points

- Each agent rollout is converted into a structured summary that keeps salient hypotheses, progress, and failure modes while dropping low-signal trace details.
- For parallel scaling, the paper introduces Recursive Tournament Voting (RTV), which recursively filters a population of rollout summaries through small-group comparisons.
- For sequential scaling, it adapts Parallel-Distill-Refine (PDR) so new rollouts are conditioned on summaries distilled from prior attempts.
- The method improves frontier coding agents on SWE-Bench Verified and Terminal-Bench v2.0, with reported gains for Claude-4.5-Opus from 70.9% to 77.6% and from 46.9% to 59.1%, respectively.
- The main claim is that test-time scaling for long-horizon agents is less about generating more attempts and more about representation, selection, and reuse.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.16529
- Hugging Face API entry: https://huggingface.co/api/papers/2604.16529
- arXiv abstract: https://arxiv.org/abs/2604.16529

## Paper Metadata

- authors: `Joongwon Kim`, `Wannan Yang`, `Kelvin Niu`, `Hongming Zhang`, `Yun Zhu`, `Eryk Helenowski`, `Ruan Silva`, `Zhengxing Chen`, `Srinivasan Iyer`, `Manzil Zaheer`, `Daniel Fried`, `Hannaneh Hajishirzi`, `Sanjeev Arora`, `Gabriel Synnaeve`, `Ruslan Salakhutdinov`, `Anirudh Goyal`
- organization: `AI at Meta`
- ai_keywords: `test-time scaling`, `agentic coding`, `rollout trajectories`, `structured summaries`, `Recursive Tournament Voting`, `Parallel-Distill-Refine`, `SWE-Bench Verified`, `Terminal-Bench v2.0`
- upvotes: `6`
- num_comments: `1`
- abstract: Test-time scaling has become a powerful way to improve large language models. However, existing methods are best suited to short, bounded outputs that can be directly compared, ranked or refined. Long-horizon coding agents violate this premise: each attempt produces an extended trajectory of actions, observations, errors, and partial progress taken by the agent. In this setting, the main challenge is no longer generating more attempts, but representing prior experience in a form that can be effectively selected from and reused. We propose a test-time scaling framework for agentic coding based on compact representations of rollout trajectories. Our framework converts each rollout into a structured summary that preserves its salient hypotheses, progress, and failure modes while discarding low-signal trace details. This representation enables two complementary forms of inference-time scaling. For parallel scaling, we introduce Recursive Tournament Voting (RTV), which recursively narrows a population of rollout summaries through small-group comparisons. For sequential scaling, we adapt Parallel-Distill-Refine (PDR) to the agentic setting by conditioning new rollouts on summaries distilled from prior attempts. Our method consistently improves the performance of frontier coding agents across SWE-Bench Verified and Terminal-Bench v2.0. For example, by using our method Claude-4.5-Opus improves from 70.9% to 77.6% on SWE-Bench Verified (mini-SWE-agent) and 46.9% to 59.1% on Terminal-Bench v2.0 (Terminus 1). Our results suggest that test-time scaling for long-horizon agents is fundamentally a problem of representation, selection, and reuse.
- hf_ai_summary: Test-time scaling framework for agentic coding uses compact trajectory representations and recursive voting/parallel-distill-refine methods to improve long-horizon task performance.

## Source Excerpt

Test-time scaling has become a powerful way to improve large language models. However, existing methods are best suited to short, bounded outputs that can be directly compared, ranked or refined. Long-horizon coding agents violate this premise: each attempt produces an extended trajectory of actions, observations, errors, and partial progress taken by the agent. In this setting, the main challenge is no longer generating more attempts, but representing prior experience in a form that can be effectively selected from and reused. We propose a test-time scaling framework for agentic coding based on compact representations of rollout trajectories. Our framework converts each rollout into a structured summary that preserves its salient hypotheses, progress, and failure modes while discarding low-signal trace details. This representation enables two complementary forms of inference-time scaling. For parallel scaling, we introduce Recursive Tournament Voting (RTV), which recursively narrows a population of rollout summaries through small-group comparisons. For sequential scaling, we adapt Parallel-Distill-Refine (PDR) to the agentic setting by conditioning new rollouts on summaries distilled from prior attempts. Our method consistently improves the performance of frontier coding agents across SWE-Bench Verified and Terminal-Bench v2.0. For example, by using our method Claude-4.5-Opus improves from 70.9% to 77.6% on SWE-Bench Verified (mini-SWE-agent) and 46.9% to 59.1% on Terminal-Bench v2.0 (Terminus 1). Our results suggest that test-time scaling for long-horizon agents is fundamentally a problem of representation, selection, and reuse.

## Open Questions

- What exact summarization format is used for rollout trajectories, and how sensitive are results to summary quality?
- How much of the gain comes from RTV versus PDR individually?
- Does the approach generalize beyond coding benchmarks to other long-horizon agent tasks?
- What comparison baselines were used for test-time scaling and agent improvement?
