---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, post-training, reinforcement-learning, agent-evals, llm-systems, on-policy-distillation, curriculum-learning, multi-turn, rl]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.24005
paper_id: 2604.24005
published: 2026-04-27T04:00:00+08:00
submitted_on_daily: 2026-04-29T10:05:06+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents

## Summary

- one_sentence_summary: TCOD is a temporal-curriculum version of on-policy distillation that stabilizes multi-turn agent training by gradually increasing trajectory depth, reducing KL instability and improving performance over vanilla OPD.
- why_relevant: It is directly about post-training for agents, showing how curriculum design can stabilize on-policy distillation in multi-turn tool- and environment-driven settings.
- filter_reason: Strong match on agent training and post-training: it studies on-policy distillation stability for multi-turn autonomous agents with benchmark gains.
- hugging_face_paper: https://huggingface.co/papers/2604.24005
- original_paper: https://arxiv.org/abs/2604.24005
- source_basis: `original abstract page`

## Key Points

- The paper identifies a multi-turn failure mode for vanilla on-policy distillation called trajectory-level KL instability, where KL divergence rises as success rate falls and remains high even after convergence.
- The proposed cause is inter-turn error compounding: accumulated mistakes push the student beyond the teacher's effective support, making the supervision signal unreliable.
- TCOD addresses this by exposing the student to short trajectories first and then progressively expanding to longer trajectories with a curriculum schedule.
- Across four student-teacher pairs and three benchmarks, ALFWorld, WebShop, and ScienceWorld, TCOD improves KL stability and yields up to an 18-point gain over vanilla OPD.
- The paper reports that TCOD can sometimes outperform the teacher and generalize to tasks the teacher fails on.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.24005
- Hugging Face API entry: https://huggingface.co/api/papers/2604.24005
- arXiv abstract: https://arxiv.org/abs/2604.24005
- GitHub: https://github.com/kokolerk/TCOD

## Paper Metadata

- authors: `Jiaqi Wang`, `Wenhao Zhang`, `Weijie Shi`, `Yaliang Li`, `James Cheng`
- ai_keywords: `on-policy distillation`, `trajectory-level KL instability`, `inter-turn error compounding`, `TCOD`, `temporal curriculum`, `multi-turn agent settings`, `KL divergence`, `student-teacher pairs`, `ALFWorld`, `WebShop`, `ScienceWorld`
- upvotes: `5`
- num_comments: `1`
- abstract: On-policy distillation (OPD) has shown strong potential for transferring reasoning ability from frontier or domain-specific models to smaller students. While effective on static single-turn tasks, its behavior in multi-turn agent settings remains underexplored. In this work, we identify a key limitation of vanilla OPD in such settings, which we term Trajectory-Level KL Instability. Specifically, we observe that KL divergence increases together with a drop in success rate, and even after convergence, the KL remains high, leading to unstable training. This instability arises from inter-turn error compounding: as errors accumulate, the student is driven beyond the teacher's effective support, rendering the supervision signal unreliable. To address this, we propose TCOD (Temporal Curriculum On-Policy Distillation), a simple yet effective framework that controls the trajectory depth exposed to the student and progressively expands it from short to long with a curriculum schedule.Experimental results across four student-teacher pairs on three multi-turn agent benchmarks (ALFWorld, WebShop, ScienceWorld) show that TCOD mitigates KL escalation and enhances KL stability throughout training, improving agent performance by up to 18 points over vanilla OPD. Further evaluations show that TCOD can even surpass the teacher's performance and generalize to tasks on which the teacher fails.
- hf_ai_summary: On-policy distillation faces instability in multi-turn settings due to trajectory-level KL divergence issues, which are addressed through a temporal curriculum approach that gradually increases trajectory depth for improved agent performance.

## Source Excerpt

On-policy distillation (OPD) has shown strong potential for transferring reasoning ability from frontier or domain-specific models to smaller students. While effective on static single-turn tasks, its behavior in multi-turn agent settings remains underexplored. In this work, we identify a key limitation of vanilla OPD in such settings, which we term Trajectory-Level KL Instability. Specifically, we observe that KL divergence increases together with a drop in success rate, and even after convergence, the KL remains high, leading to unstable training. This instability arises from inter-turn error compounding: as errors accumulate, the student is driven beyond the teacher's effective support, rendering the supervision signal unreliable. To address this, we propose TCOD (Temporal Curriculum On-Policy Distillation), a simple yet effective framework that controls the trajectory depth exposed to the student and progressively expands it from short to long with a curriculum schedule. Experimental results across four student-teacher pairs on three multi-turn agent benchmarks (ALFWorld, WebShop, ScienceWorld) show that TCOD mitigates KL escalation and enhances KL stability throughout training, improving agent performance by up to 18 points over vanilla OPD. Further evaluations show that TCOD can even surpass the teacher's performance and generalize to tasks on which the teacher fails.

## Open Questions

- How is trajectory depth scheduled in TCOD, and does the paper specify a fixed or adaptive curriculum?
- What student and teacher model families were used in the four pairs?
- How exactly is trajectory-level KL measured across turns during training?
- Does TCOD require any changes to the distillation objective beyond the curriculum schedule?
