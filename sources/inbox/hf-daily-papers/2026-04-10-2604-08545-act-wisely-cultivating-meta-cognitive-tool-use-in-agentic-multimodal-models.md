---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, reinforcement-learning, post-training, agent-evals, multimodal, reward-design]
source_count: 1
updated: 2026-04-10
source_url: https://arxiv.org/abs/2604.08545
paper_id: 2604.08545
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T09:28:42+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

## Summary

- one_sentence_summary: The paper proposes HDPO, a reinforcement-learning framework for agentic multimodal models that separates task accuracy from tool-efficiency optimization to reduce unnecessary tool use while improving reasoning accuracy.
- why_relevant: It is directly relevant to reinforcement learning post-training for agents, especially tool-using multimodal systems, because it proposes a concrete RL objective design for better tool arbitration.
- filter_reason: Directly targets agentic tool-use training with a new RL/post-training objective that improves reasoning and reduces tool overuse.
- hugging_face_paper: https://huggingface.co/papers/2604.08545
- original_paper: https://arxiv.org/abs/2604.08545
- source_basis: `original abstract page`

## Key Points

- The paper argues that many agentic multimodal models have a meta-cognitive deficit: they invoke tools reflexively even when the answer is available from visual context.
- It criticizes scalarized rewards that penalize tool use, claiming they either suppress necessary tool use too strongly or become ineffective after advantage normalization.
- HDPO replaces reward scalarization with two decoupled optimization channels: one for accuracy and one for efficiency.
- The efficiency objective is applied only to accurate trajectories through conditional advantage estimation, so tool economy is encouraged without directly competing with correctness on all samples.
- The authors describe this as inducing a cognitive curriculum: first learn to solve the task, then learn to rely less on tools.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
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
- upvotes: `22`
- num_comments: `1`
- abstract: The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.
- hf_ai_summary: Agents with meta-cognitive deficits struggle with tool usage decisions, leading to inefficiencies; a new framework called HDPO addresses this through decoupled optimization channels for accuracy and efficiency.

## Source Excerpt

The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.

## Open Questions

- What exact benchmark tasks and tool-usage settings were used in the evaluations?
- How much did tool invocations drop numerically, and on which metrics did accuracy improve?
- How is conditional advantage estimation implemented in detail compared with standard PPO-style advantage normalization?
- Does HDPO generalize beyond multimodal visual agents to text-only or other tool-using agents?
