---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, reasoning-behavior, llm-systems, llm-agents, scientific-reasoning, evaluation, epistemics, behavior-analysis]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.18805
paper_id: 2604.18805
published: 2026-04-20T04:00:00+08:00
submitted_on_daily: 2026-04-23T14:27:03+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# AI scientists produce results without reasoning scientifically

## Summary

- one_sentence_summary: This paper evaluates LLM-based scientific agents across eight domains and finds that they can execute workflows but usually do not follow the epistemic patterns associated with scientific reasoning.
- why_relevant: It is directly about LLM agents, their reasoning behavior, and evaluation limits, making it relevant to agent systems research and to questions about whether post-training or scaffolding can improve scientific reasoning.
- filter_reason: Directly studies LLM scientific agents, their reasoning behavior, and evaluation limits across workflows.
- hugging_face_paper: https://huggingface.co/papers/2604.18805
- original_paper: https://arxiv.org/abs/2604.18805
- source_basis: `original abstract page`

## Key Points

- Evaluates LLM-based scientific agents in eight domains with more than 25,000 runs, covering both workflow execution and hypothesis-driven inquiry.
- Uses two lenses: performance decomposition between base model and scaffold, and behavioral analysis of the epistemic structure of agent reasoning.
- Finds the base model dominates outcomes and behavior, explaining 41.4% of variance versus 1.5% for the scaffold.
- Reports that evidence is ignored in 68% of traces, refutation-driven belief revision appears in 26%, and convergent multi-test evidence is rare.
- Shows the same weak reasoning pattern persists even when agents are given near-complete successful trajectories as context, suggesting scaffold engineering alone is insufficient.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.18805
- Hugging Face API entry: https://huggingface.co/api/papers/2604.18805
- arXiv abstract: https://arxiv.org/abs/2604.18805
- Project page: https://lamalab-org.github.io/corral/

## Paper Metadata

- authors: `Martiño Ríos-García`, `Nawaf Alampara`, `Chandan Gupta`, `Indrajeet Mandal`, `Sajid Mannan`, `Ali Asghar Aghajani`, `N. M. Anoop Krishnan`, `Kevin Maik Jablonka`
- organization: `Lab of Kevin Jablonka at Uni Jena`
- ai_keywords: `large language model`, `scientific agents`, `epistemic norms`, `reasoning patterns`, `hypothesis-driven inquiry`, `computational workflow`, `belief revision`, `scientific reasoning`
- upvotes: `2`
- num_comments: `2`
- abstract: Large language model (LLM)-based systems are increasingly deployed to conduct scientific research autonomously, yet whether their reasoning adheres to the epistemic norms that make scientific inquiry self-correcting is poorly understood. Here, we evaluate LLM-based scientific agents across eight domains, spanning workflow execution to hypothesis-driven inquiry, through more than 25,000 agent runs and two complementary lenses: (i) a systematic performance analysis that decomposes the contributions of the base model and the agent scaffold, and (ii) a behavioral analysis of the epistemological structure of agent reasoning. We observe that the base model is the primary determinant of both performance and behavior, accounting for 41.4% of explained variance versus 1.5% for the scaffold. Across all configurations, evidence is ignored in 68% of traces, refutation-driven belief revision occurs in 26%, and convergent multi-test evidence is rare. The same reasoning pattern appears whether the agent executes a computational workflow or conducts hypothesis-driven inquiry. They persist even when agents receive near-complete successful reasoning trajectories as context, and the resulting unreliability compounds across repeated trials in epistemically demanding domains. Thus, current LLM-based agents execute scientific workflows but do not exhibit the epistemic patterns that characterize scientific reasoning. Outcome-based evaluation cannot detect these failures, and scaffold engineering alone cannot repair them. Until reasoning itself becomes a training target, the scientific knowledge produced by such agents cannot be justified by the process that generated it.
- hf_ai_summary: Large language model-based scientific agents demonstrate consistent reasoning patterns that lack key epistemic features of scientific inquiry, regardless of task type or successful context, indicating fundamental limitations in their ability to replicate genuine scientific reasoning processes.

## Source Excerpt

Large language model (LLM)-based systems are increasingly deployed to conduct scientific research autonomously, yet whether their reasoning adheres to the epistemic norms that make scientific inquiry self-correcting is poorly understood. Here, we evaluate LLM-based scientific agents across eight domains, spanning workflow execution to hypothesis-driven inquiry, through more than 25,000 agent runs and two complementary lenses: (i) a systematic performance analysis that decomposes the contributions of the base model and the agent scaffold, and (ii) a behavioral analysis of the epistemological structure of agent reasoning. We observe that the base model is the primary determinant of both performance and behavior, accounting for 41.4% of explained variance versus 1.5% for the scaffold. Across all configurations, evidence is ignored in 68% of traces, refutation-driven belief revision occurs in 26%, and convergent multi-test evidence is rare. The same reasoning pattern appears whether the agent executes a computational workflow or conducts hypothesis-driven inquiry. They persist even when agents receive near-complete successful reasoning trajectories as context, and the resulting unreliability compounds across repeated trials in epistemically demanding domains. Thus, current LLM-based agents execute scientific workflows but do not exhibit the epistemic patterns that characterize scientific reasoning. Outcome-based evaluation cannot detect these failures, and scaffold engineering alone cannot repair them. Until reasoning itself becomes a training target, the scientific knowledge produced by such agents cannot be justified by the process that generated it.

## Open Questions

- Which eight domains were evaluated, and how differently did the agents behave across them?
- How were 'evidence ignored,' 'belief revision,' and 'convergent multi-test evidence' operationalized in the analysis?
- What kinds of scaffolds were tested, and which ones had the most effect, if any?
- Did the paper identify any specific failure modes where outcome-based evaluation looked good despite poor reasoning?
