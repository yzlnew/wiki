---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, tool-use, llm-systems, evaluation, reliability, osworld, computer-use]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.17849
paper_id: 2604.17849
published: 2026-04-20T04:00:00+08:00
submitted_on_daily: 2026-04-21T22:14:34+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# On the Reliability of Computer Use Agents

## Summary

- one_sentence_summary: The paper argues that computer-use agents can be unreliable even on repeated runs of the same task, and studies how execution stochasticity, task ambiguity, and behavioral variability affect reliability on OSWorld.
- why_relevant: It is directly relevant to agent evaluation and tool-using systems because it studies why computer-use agents fail to behave reliably across runs, which matters for deployment and post-training evaluation.
- filter_reason: Directly studies reliability and evaluation of computer-use agents, with concrete OSWorld methodology and repeated-execution analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.17849
- original_paper: https://arxiv.org/abs/2604.17849
- source_basis: `original abstract page`

## Key Points

- The authors focus on reliability rather than one-shot success: an agent that completes a task once may still fail when rerun on the same task and model.
- They analyze three sources of unreliability: stochasticity during execution, ambiguity in task specification, and variability in agent behavior.
- The study uses repeated executions of the same OSWorld task and paired statistical tests to detect task-level changes across settings.
- Their analysis suggests reliability depends both on how tasks are specified and on how stable the agent's behavior is across runs.
- The paper recommends evaluating agents under repeated execution, supporting interaction to resolve ambiguity, and preferring strategies that remain stable across runs.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.17849
- Hugging Face API entry: https://huggingface.co/api/papers/2604.17849
- arXiv abstract: https://arxiv.org/abs/2604.17849
- GitHub: https://github.com/simular-ai/cua_reliability

## Paper Metadata

- authors: `Gonzalo Gonzalez-Pumariega`, `Saaket Agashe`, `Jiachen Yang`, `Ang Li`, `Xin Eric Wang`
- organization: `Simular`
- upvotes: `8`
- num_comments: `1`
- abstract: Computer-use agents have rapidly improved on real-world tasks such as web navigation, desktop automation, and software interaction, in some cases surpassing human performance. Yet even when the task and model are unchanged, an agent that succeeds once may fail on a repeated execution of the same task. This raises a fundamental question: if an agent can succeed at a task once, what prevents it from doing so reliably? In this work, we study the sources of unreliability in computer-use agents through three factors: stochasticity during execution, ambiguity in task specification, and variability in agent behavior. We analyze these factors on OSWorld using repeated executions of the same task together with paired statistical tests that capture task-level changes across settings. Our analysis shows that reliability depends on both how tasks are specified and how agent behavior varies across executions. These findings suggest the need to evaluate agents under repeated execution, to allow agents to resolve task ambiguity through interaction, and to favor strategies that remain stable across runs.
- hf_ai_summary: Computer-use agents exhibit unreliable performance due to execution stochasticity, task specification ambiguity, and behavioral variability, necessitating repeated evaluation and stable strategies for consistent task completion.

## Source Excerpt

Computer-use agents have rapidly improved on real-world tasks such as web navigation, desktop automation, and software interaction, in some cases surpassing human performance. Yet even when the task and model are unchanged, an agent that succeeds once may fail on a repeated execution of the same task. This raises a fundamental question: if an agent can succeed at a task once, what prevents it from doing so reliably? In this work, we study the sources of unreliability in computer-use agents through three factors: stochasticity during execution, ambiguity in task specification, and variability in agent behavior. We analyze these factors on OSWorld using repeated executions of the same task together with paired statistical tests that capture task-level changes across settings. Our analysis shows that reliability depends on both how tasks are specified and how agent behavior varies across executions. These findings suggest the need to evaluate agents under repeated execution, to allow agents to resolve task ambiguity through interaction, and to favor strategies that remain stable across runs.

## Open Questions

- Which specific agent strategies were compared in OSWorld?
- How large were the reliability differences across the three sources of unreliability?
- Which task types were most sensitive to specification ambiguity or behavioral variability?
- What paired statistical tests were used, and what were the main significant effects?
- Did the paper propose any concrete method to reduce run-to-run variability?
