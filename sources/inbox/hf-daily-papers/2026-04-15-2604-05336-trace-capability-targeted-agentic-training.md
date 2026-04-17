---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, reinforcement-learning, post-training, agent-evals, llm-systems, agentic-llms, tool-use, lora, trajectory-analysis, self-improvement]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.05336
paper_id: 2604.05336
published: 2026-04-07T04:00:00+08:00
submitted_on_daily: 2026-04-15T00:53:51+08:00
decision: accept
score: 96
generator: scripts/update_hf_daily_papers.py
---

# TRACE: Capability-Targeted Agentic Training

## Summary

- one_sentence_summary: TRACE is an environment-specific agent self-improvement system that infers missing capabilities from successful versus failed trajectories, builds synthetic training environments for those capabilities, and trains LoRA adapters with RL for routed inference.
- why_relevant: It is directly about post-training for agentic LLMs, combining trajectory-based analysis, RL, and adapter-based adaptation for tool-using systems.
- filter_reason: Directly targets agentic self-improvement with capability discovery, synthetic training environments, and RL-trained adapters.
- hugging_face_paper: https://huggingface.co/papers/2604.05336
- original_paper: https://arxiv.org/abs/2604.05336
- source_basis: `original abstract page`

## Key Points

- TRACE defines a capability as one or more actions in a trajectory that are necessary for solving a subset of tasks in an agentic environment.
- It contrasts successful and failed trajectories to identify likely capability gaps instead of training on untargeted synthetic data or only on the target environment.
- For each missing capability, TRACE synthesizes a training environment that rewards whether that capability was exercised, then trains a LoRA adapter via RL on that environment.
- At inference time, the system routes to the adapter relevant to the task/capability.
- The paper reports gains on customer-service and tool-use benchmarks, and says TRACE is more rollout-efficient than GRPO and GEPA under the same rollout budget.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.05336
- Hugging Face API entry: https://huggingface.co/api/papers/2604.05336
- arXiv abstract: https://arxiv.org/abs/2604.05336
- GitHub: https://github.com/ScalingIntelligence/TRACE
- Project page: https://scalingintelligence.stanford.edu/blogs/trace/

## Paper Metadata

- authors: `Hangoo Kang`, `Tarun Suresh`, `Jon Saad-Falcon`, `Azalia Mirhoseini`
- organization: `Stanford University`
- ai_keywords: `large language models`, `agentic environments`, `capabilities`, `trajectories`, `synthetic training data`, `LoRA adapter`, `reinforcement learning`, `environment-specific agent self-improvement`, `trajectory comparison`, `targeted training environments`
- upvotes: `11`
- num_comments: `1`
- abstract: Large Language Models (LLMs) deployed in agentic environments must exercise multiple capabilities across different task instances, where a capability is performing one or more actions in a trajectory that are necessary for successfully solving a subset of tasks in the environment. Many existing approaches either rely on synthetic training data that is not targeted to the model's actual capability deficits in the target environment or train directly on the target environment, where the model needs to implicitly learn the capabilities across tasks. We introduce TRACE (Turning Recurrent Agent failures into Capability-targeted training Environments), an end-to-end system for environment-specific agent self-improvement. TRACE contrasts successful and failed trajectories to automatically identify lacking capabilities, synthesizes a targeted training environment for each that rewards whether the capability was exercised, and trains a LoRA adapter via RL on each synthetic environment, routing to the relevant adapter at inference. Empirically, TRACE generalizes across different environments, improving over the base agent by +14.1 points on τ^2-bench (customer service) and +7 perfect scores on ToolSandbox (tool use), outperforming the strongest baseline by +7.4 points and +4 perfect scores, respectively. Given the same number of rollouts, TRACE scales more efficiently than baselines, outperforming GRPO and GEPA by +9.2 and +7.4 points on τ^2-bench.
- hf_ai_summary: TRACE enables LLM agents to improve in agentic environments by identifying capability gaps through trajectory comparison, creating targeted training environments, and using LoRA adapters for efficient, environment-specific self-improvement.

## Source Excerpt

Large Language Models (LLMs) deployed in agentic environments must exercise multiple capabilities across different task instances, where a capability is performing one or more actions in a trajectory that are necessary for successfully solving a subset of tasks in the environment. Many existing approaches either rely on synthetic training data that is not targeted to the model's actual capability deficits in the target environment or train directly on the target environment, where the model needs to implicitly learn the capabilities across tasks. We introduce TRACE (Turning Recurrent Agent failures into Capability-targeted training Environments), an end-to-end system for environment-specific agent self-improvement. TRACE contrasts successful and failed trajectories to automatically identify lacking capabilities, synthesizes a targeted training environment for each that rewards whether the capability was exercised, and trains a LoRA adapter via RL on each synthetic environment, routing to the relevant adapter at inference. Empirically, TRACE generalizes across different environments, improving over the base agent by +14.1 points on $\tau^2$-bench (customer service) and +7 perfect scores on ToolSandbox (tool use), outperforming the strongest baseline by +7.4 points and +4 perfect scores, respectively. Given the same number of rollouts, TRACE scales more efficiently than baselines, outperforming GRPO and GEPA by +9.2 and +7.4 points on $\tau^2$-bench.

## Open Questions

- How exactly does TRACE extract a capability label from paired successful and failed trajectories?
- What is the design of the synthetic training environment and reward signal for each capability?
- How are adapters selected or routed at inference time?
- How many capabilities or adapters are typically created per environment?
- How well does TRACE transfer to environments not covered by the reported benchmarks?
