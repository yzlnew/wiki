---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, llm-systems, agent-evals, failure-analysis, multi-turn]
source_count: 1
updated: 2026-05-01
source_url: https://arxiv.org/abs/2604.25135
paper_id: 2604.25135
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-05-01T00:26:59+08:00
decision: accept
score: 90
generator: scripts/update_hf_daily_papers.py
---

# FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments

## Summary

- one_sentence_summary: FAMA is a failure-aware meta-agentic framework that analyzes baseline agent failures and injects targeted context from specialized agents to improve open-source LLM tool-use performance in multi-turn conversational tasks.
- why_relevant: It is directly relevant to agentic tool use and post-training/system design because it proposes a concrete orchestration method for improving LLM decision-making in interactive environments.
- filter_reason: Directly targets agentic tool use reliability with a failure-aware orchestration framework and evaluation on open-source LLM agents.
- hugging_face_paper: https://huggingface.co/papers/2604.25135
- original_paper: https://arxiv.org/abs/2604.25135
- source_basis: `original abstract page`

## Key Points

- The paper targets error accumulation in autonomous tool-using agents, especially for open-source LLMs with smaller context windows and constrained inference budgets.
- FAMA works in two stages: it first analyzes failure trajectories from baseline agents to find the most common errors, then orchestrates a minimal subset of specialized agents to address those failures.
- The specialized agents provide targeted context to the tool-use agent before the decision-making step, rather than broadly expanding the agent pipeline.
- Experiments on open-source LLMs report gains of up to 27% across evaluation modes compared with standard baselines.
- The authors argue that curating context around recurring failure modes is a useful design principle for reliable multi-turn conversational agents.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25135
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25135
- arXiv abstract: https://arxiv.org/abs/2604.25135

## Paper Metadata

- authors: `Amir Saeidi`, `Venkatesh Mishra`, `Souradeep Mukhopadhyay`, `Gaowen Liu`, `Ali Payani`, `Jayanth Srinivasa`, `Chitta Baral`
- ai_keywords: `large language models`, `autonomous agents`, `decision-making`, `failure trajectories`, `orchestration mechanism`, `specialized agents`, `tool-use agents`, `context injection`, `error accumulation`, `multi-turn conversations`
- upvotes: `6`
- num_comments: `2`
- abstract: Large Language Models are being increasingly deployed as the decision-making core of autonomous agents capable of effecting change in external environments. Yet, in conversational benchmarks, which simulate real-world customer-centric issue resolution scenarios, these agents frequently fail due to the cascading effects of incorrect decision-making. These challenges are particularly pronounced for open-source LLMs with smaller parameter sizes, limited context windows, and constrained inference budgets, which contribute to increased error accumulation in agentic settings. To tackle these challenges, we present the Failure-Aware Meta-Agentic (FAMA) framework. FAMA operates in two stages: first, it analyzes failure trajectories from baseline agents to identify the most prevalent errors; second, it employs an orchestration mechanism that activates a minimal subset of specialized agents tailored to address these failures by injecting a targeted context for the tool-use agent before the decision-making step. Experiments across open-source LLMs demonstrate performance gains up to 27% across evaluation modes over standard baselines. These results highlight that targeted curation of context through specialized agents to address common failures is a valuable design principle for building reliable, multi-turn tool-use LLM agents that simulate real-world conversational scenarios.
- hf_ai_summary: Failure-Aware Meta-Agentic framework improves open-source LLM performance in conversational scenarios by identifying common errors and deploying specialized agents to correct them.

## Source Excerpt

Large Language Models are being increasingly deployed as the decision-making core of autonomous agents capable of effecting change in external environments. Yet, in conversational benchmarks, which simulate real-world customer-centric issue resolution scenarios, these agents frequently fail due to the cascading effects of incorrect decision-making. These challenges are particularly pronounced for open-source LLMs with smaller parameter sizes, limited context windows, and constrained inference budgets, which contribute to increased error accumulation in agentic settings. To tackle these challenges, we present the Failure-Aware Meta-Agentic (FAMA) framework. FAMA operates in two stages: first, it analyzes failure trajectories from baseline agents to identify the most prevalent errors; second, it employs an orchestration mechanism that activates a minimal subset of specialized agents tailored to address these failures by injecting a targeted context for the tool-use agent before the decision-making step. Experiments across open-source LLMs demonstrate performance gains up to 27% across evaluation modes over standard baselines. These results highlight that targeted curation of context through specialized agents to address common failures is a valuable design principle for building reliable, multi-turn tool-use LLM agents that simulate real-world conversational scenarios.

## Open Questions

- Which open-source LLMs and conversational benchmarks were used in the experiments?
- What exact failure categories were most common in the analyzed trajectories?
- How are the specialized agents implemented and selected at runtime?
- What does the reported 27% improvement measure, and how consistent is it across tasks or modes?
