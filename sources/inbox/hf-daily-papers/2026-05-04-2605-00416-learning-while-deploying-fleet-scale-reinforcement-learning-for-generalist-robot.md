---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, agent-environment-interaction, robotics, vla, online-rl, fleet-learning, human-interventions, value-learning]
source_count: 1
updated: 2026-05-05
source_url: https://arxiv.org/abs/2605.00416
paper_id: 2605.00416
published: 2026-05-01T04:00:00+08:00
submitted_on_daily: 2026-05-04T09:54:53+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

## Summary

- one_sentence_summary: Learning While Deploying (LWD) is a fleet-scale offline-to-online RL framework that continually post-trains a pretrained Vision-Language-Action robot policy from deployment data, autonomous rollouts, and human interventions.
- why_relevant: This paper is directly relevant to reinforcement learning post-training and agentic tool-use because it studies continual policy improvement from live deployment experience in real robot systems.
- filter_reason: Strongly relevant fleet-scale reinforcement learning post-training for embodied policies with deployment-time learning and real-world evaluation.
- hugging_face_paper: https://huggingface.co/papers/2605.00416
- original_paper: https://arxiv.org/abs/2605.00416
- source_basis: `original abstract page`

## Key Points

- LWD closes the loop between real-world deployment, shared fleet experience, policy improvement, and redeployment for generalist VLA policies.
- The framework is designed for heterogeneous, sparse-reward robot data and combines Distributional Implicit Value Learning (DIVL) with Q-learning via Adjoint Matching (QAM).
- The learning setup uses autonomous rollouts and human corrections collected across a fleet, rather than relying only on fixed demonstration datasets.
- The paper evaluates LWD on 16 dual-arm robots across eight real-world manipulation tasks, including semantic grocery restocking and 3 to 5 minute long-horizon tasks.
- The reported result is a single generalist policy reaching 95% average success rate, with the largest gains on long-horizon tasks.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.00416
- Hugging Face API entry: https://huggingface.co/api/papers/2605.00416
- arXiv abstract: https://arxiv.org/abs/2605.00416

## Paper Metadata

- authors: `Yi Wang`, `Xinchen Li`, `Pengwei Xie`, `Pu Yang`, `Buqing Nie`, `Yunuo Cai`, `Qinglin Zhang`, `Chendi Qu`, `Jeffrey Wu`, `Jianheng Song`, `Xinlin Ren`, `Jingshun Huang`, `Mingjie Pan`, `Siyuan Feng`, `Zhi Chen`, `Jianlan Luo`
- ai_keywords: `Vision-Language-Action`, `reinforcement learning`, `policy improvement`, `autonomous rollouts`, `human interventions`, `Distributional Implicit Value Learning`, `Q-learning`, `Adjoint Matching`, `flow-based action generators`
- upvotes: `10`
- num_comments: `2`
- abstract: Generalist robot policies increasingly benefit from large-scale pretraining, but offline data alone is insufficient for robust real-world deployment. Deployed robots encounter distribution shifts, long-tail failures, task variations, and human correction opportunities that fixed demonstration datasets cannot fully capture. We present Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning framework for continual post-training of generalist Vision-Language-Action (VLA) policies. Starting from a pretrained VLA policy, LWD closes the loop between deployment, shared physical experience, policy improvement, and redeployment by using autonomous rollouts and human interventions collected across a robot fleet. To stabilize learning from heterogeneous, sparse-reward fleet data, LWD combines Distributional Implicit Value Learning (DIVL) for robust value estimation with Q-learning via Adjoint Matching (QAM) for policy extraction in flow-based VLA action generators. We validate LWD on a fleet of 16 dual-arm robots across eight real-world manipulation tasks, including semantic grocery restocking and 3--5 minute long-horizon tasks. A single generalist policy improves as fleet experience accumulates, reaching an average success rate of 95%, with the largest gains on long-horizon tasks.
- hf_ai_summary: Learning While Deploying framework enables continuous improvement of Vision-Language-Action policies through fleet-scale offline-to-online reinforcement learning with distributed robot experience and human interventions.

## Source Excerpt

Generalist robot policies increasingly benefit from large-scale pretraining, but offline data alone is insufficient for robust real-world deployment. Deployed robots encounter distribution shifts, long-tail failures, task variations, and human correction opportunities that fixed demonstration datasets cannot fully capture. We present Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning framework for continual post-training of generalist Vision-Language-Action (VLA) policies. Starting from a pretrained VLA policy, LWD closes the loop between deployment, shared physical experience, policy improvement, and redeployment by using autonomous rollouts and human interventions collected across a robot fleet. To stabilize learning from heterogeneous, sparse-reward fleet data, LWD combines Distributional Implicit Value Learning (DIVL) for robust value estimation with Q-learning via Adjoint Matching (QAM) for policy extraction in flow-based VLA action generators. We validate LWD on a fleet of 16 dual-arm robots across eight real-world manipulation tasks, including semantic grocery restocking and 3--5 minute long-horizon tasks. A single generalist policy improves as fleet experience accumulates, reaching an average success rate of 95%, with the largest gains on long-horizon tasks.

## Open Questions

- How much of the improvement comes from autonomous rollouts versus human interventions?
- What are the per-task success rates and failure modes across the eight manipulation tasks?
- How does LWD compare against offline-only post-training or other online RL baselines?
- What exact properties of DIVL and QAM make training stable on sparse fleet data?
- How often is the policy redeployed during the learning loop, and what is the update cadence?
