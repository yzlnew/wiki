---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, reasoning-behavior-shaping, llm-agents, tool-use, reasoning, post-training]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.17609
paper_id: 2604.17609
published: 2026-04-19T04:00:00+08:00
submitted_on_daily: 2026-04-21T19:58:04+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity

## Summary

- one_sentence_summary: The paper shows that current LLM-based agents often notice unexpected, highly relevant environmental information but frequently fail to use it, a behavior the authors call a lack of environmental curiosity.
- why_relevant: It directly concerns agent behavior, tool use, and post-training/test-time factors that shape whether LLM agents can adapt to new information during task execution.
- filter_reason: Directly studies LLM agent behavior, environment interaction, and agent evaluation with concrete benchmark evidence.
- hugging_face_paper: https://huggingface.co/papers/2604.17609
- original_paper: https://arxiv.org/abs/2604.17609
- source_basis: `original abstract page`

## Key Points

- The authors test whether agents can reflect on and exploit unexpected observations by injecting complete task solutions into environments across Terminal-Bench, SWE-Bench, and AppWorld.
- On Terminal-Bench, agents discovered the injected solutions in 79-81% of runs but exploited them only 37-50% of the time.
- The clearest failure appears in AppWorld, where agents saw documentation explicitly saying a command returns the complete solution in over 90% of attempts, yet used it in fewer than 7% of trials.
- The paper names this gap environmental curiosity: the ability to recognize and investigate unexpected but relevant stimuli, and argues current agents often fetch expected information without revising strategy.
- The authors identify three factors shaping curiosity: the agent scaffold's tools, test-time compute, and training data distribution; configurations that improve curiosity also improve benchmark performance, but even then agents still miss many discovered solutions.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.17609
- Hugging Face API entry: https://huggingface.co/api/papers/2604.17609
- arXiv abstract: https://arxiv.org/abs/2604.17609

## Paper Metadata

- authors: `Leon Engländer`, `Sophia Althammer`, `Ahmet Üstün`, `Matthias Gallé`, `Tom Sherborne`
- organization: `Cohere`
- ai_keywords: `LLM-based agents`, `environmental observations`, `reasoning`, `unexpected information`, `environmental curiosity`, `Terminal-Bench`, `SWE-Bench`, `AppWorld`, `task solutions`, `agent scaffolding`, `test-time compute`, `training data distribution`
- upvotes: `5`
- num_comments: `2`
- abstract: LLM-based agents are assumed to integrate environmental observations into their reasoning: discovering highly relevant but unexpected information should naturally lead to a model exploiting its own discoveries. We show that this assumption is false for current LLM-based agents, which struggle to reflect or react to unexpected information. Across three benchmarks (Terminal-Bench, SWE-Bench, AppWorld), we inject complete task solutions into the agent environments to deliberately expose a task's solution to a model. While agents discover these solutions on Terminal-Bench in 79-81% of runs, they interact, or exploit, them in only 37-50% of cases. This gap is starkest in AppWorld: agents see documentation stating that a command "returns the complete solution to this task" in over 90% of attempts but exploit this in fewer than 7% of trials. We show that agents lack what we call environmental curiosity: the capability to recognize and investigate unexpected but relevant observations in response to environmental stimuli. We identify three main factors influencing environmental curiosity: available tools in the agent scaffold, test-time compute, and training data distribution. Our findings identify configurations that maximize curiosity also achieve the best performance on the unmodified benchmarks. Yet even jointly optimized agents still ignore discovered solutions in the majority of trials: current agents use the environment to fetch expected information, but not to revise their strategy or maximally exploit useful stimuli.
- hf_ai_summary: LLM-based agents fail to exploit discovered unexpected information despite recognizing it, indicating a lack of environmental curiosity that depends on tools, compute, and training data distribution.

## Source Excerpt

LLM-based agents are assumed to integrate environmental observations into their reasoning: discovering highly relevant but unexpected information should naturally lead to a model exploiting its own discoveries. We show that this assumption is false for current LLM-based agents, which struggle to reflect or react to unexpected information. Across three benchmarks (Terminal-Bench, SWE-Bench, AppWorld), we inject complete task solutions into the agent environments to deliberately expose a task's solution to a model. While agents discover these solutions on Terminal-Bench in 79-81% of runs, they interact, or exploit, them in only 37-50% of cases. This gap is starkest in AppWorld: agents see documentation stating that a command "returns the complete solution to this task" in over 90% of attempts but exploit this in fewer than 7% of trials. We show that agents lack what we call environmental curiosity: the capability to recognize and investigate unexpected but relevant observations in response to environmental stimuli. We identify three main factors influencing environmental curiosity: available tools in the agent scaffold, test-time compute, and training data distribution. Our findings identify configurations that maximize curiosity also achieve the best performance on the unmodified benchmarks. Yet even jointly optimized agents still ignore discovered solutions in the majority of trials: current agents use the environment to fetch expected information, but not to revise their strategy or maximally exploit useful stimuli.

## Open Questions

- Which specific tool or scaffold changes most improve environmental curiosity?
- How much of the effect is driven by model training data versus test-time compute?
- Do the reported results generalize beyond the three benchmarks studied?
- What interventions would make agents reliably revise strategy after discovering a solution?
