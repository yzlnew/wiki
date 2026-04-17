---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, tool-use, post-training, agent-evals, multimodal, rlhf, optimization]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.08545
paper_id: 2604.08545
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T09:28:42+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

## Summary

- one_sentence_summary: The paper proposes HDPO, a reinforcement learning framework for agentic multimodal models that decouples accuracy optimization from tool-efficiency optimization to reduce blind tool use while improving reasoning accuracy.
- why_relevant: It is directly relevant to reinforcement learning post-training for agents, especially tool-use control and training objectives for multimodal systems.
- filter_reason: Directly targets agentic tool-use post-training with a new RL objective that improves reasoning and tool efficiency.
- hugging_face_paper: https://huggingface.co/papers/2604.08545
- original_paper: https://arxiv.org/abs/2604.08545
- source_basis: `original abstract page`

## Key Points

- The problem is a meta-cognitive deficit in agents: they often invoke tools reflexively even when the answer is available from visual context alone.
- The authors argue that standard scalarized rewards for tool penalties create a tradeoff: strong penalties suppress necessary tool use, while weak penalties get washed out during advantage normalization.
- HDPO replaces reward scalarization with two separate optimization channels: one for task accuracy and one for tool efficiency.
- The efficiency objective is applied only within accurate trajectories via conditional advantage estimation, so the model learns to be economical without sacrificing correctness.
- The resulting model, Metis, is reported to cut tool invocations by orders of magnitude while also improving reasoning accuracy.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08545
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08545
- arXiv abstract: https://arxiv.org/abs/2604.08545
- GitHub: https://github.com/Accio-Lab/Metis
- Project page: https://Accio-Lab.github.io/Metis

## Paper Metadata

- authors: `Shilin Yan`, `Jintao Tong`, `Hongwei Xue`, `Xiaojun Tang`, `Yangyang Wang`, `Kunyu Shi`, `Guannan Zhang`, `Ruixuan Li`, `Yixiong Zou`
- organization: `Accio`
- ai_keywords: `agentic multimodal models`, `tool invocation`, `reinforcement learning`, `reward scalarization`, `advantage estimation`, `conditional advantage estimation`, `cognitive curriculum`, `Metis`
- upvotes: `31`
- num_comments: `2`
- abstract: The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.
- hf_ai_summary: Agents with meta-cognitive deficits struggle with tool usage decisions, leading to inefficiencies; a new framework called HDPO addresses this through decoupled optimization channels for accuracy and efficiency.

## Source Excerpt

The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.

## Open Questions

- What exact RL algorithm or training loop does HDPO build on?
- What tasks and benchmarks were used to evaluate tool usage reduction and reasoning accuracy?
- How is conditional advantage estimation implemented in practice?
- Does the approach generalize beyond multimodal visual agents to text-based tool-using agents?
