---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, post-training, llm-systems, agent-evals, vlm, ppo, long-horizon, game-playing]
source_count: 1
updated: 2026-05-05
source_url: https://arxiv.org/abs/2605.00347
paper_id: 2605.00347
published: 2026-05-01T04:00:00+08:00
submitted_on_daily: 2026-05-05T04:08:19+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning

## Summary

- one_sentence_summary: Odysseus studies reinforcement learning for long-horizon VLM decision-making in Super Mario Land and finds that an adapted PPO with a lightweight turn-level critic makes training more stable and sample-efficient than critic-free alternatives.
- why_relevant: It is directly about RL post-training for multimodal agents, with concrete evidence on how to stabilize long-horizon VLM training and improve agent performance in an interactive environment.
- filter_reason: Long-horizon RL training for VLM agents with PPO/GRPO comparisons and practical stability guidance is directly aligned with agents and post-training.
- hugging_face_paper: https://huggingface.co/papers/2605.00347
- original_paper: https://arxiv.org/abs/2605.00347
- source_basis: `original abstract page`

## Key Points

- Targets 100+ turn, visually grounded game play with coordinated perception, reasoning, and action, beyond the shorter horizons common in prior VLM RL work.
- Systematically studies algorithmic choices and proposes an adapted PPO variant with a lightweight turn-level critic.
- The critic-based approach improves training stability and sample efficiency relative to critic-free methods such as GRPO and Reinforce++.
- Pretrained VLMs act as strong action priors, reducing the need for manual action engineering compared with training classical deep RL agents from scratch.
- The resulting Odysseus framework shows substantial gains across game levels, at least 3x average game progress versus frontier models, and better in-game and cross-game generalization while preserving general-domain capabilities.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.00347
- Hugging Face API entry: https://huggingface.co/api/papers/2605.00347
- arXiv abstract: https://arxiv.org/abs/2605.00347
- Project page: https://odysseus-project.github.io

## Paper Metadata

- authors: `Chengshuai Shi`, `Wenzhe Li`, `Xinran Liang`, `Yizhou Lu`, `Wenjia Yang`, `Ruirong Feng`, `Seth Karten`, `Ziran Yang`, `Zihan Ding`, `Gabriel Sarch`, `Danqi Chen`, `Karthik Narasimhan`, `Chi Jin`
- organization: `Princeton University`
- upvotes: `7`
- num_comments: `1`
- abstract: Given the rapidly growing capabilities of vision-language models (VLMs), extending them to interactive decision-making tasks such as video games has emerged as a promising frontier. However, existing approaches either rely on large-scale supervised fine-tuning (SFT) on human trajectories or apply reinforcement learning (RL) only in relatively short-horizon settings (typically around 20--30 turns). In this work, we study RL-based training of VLMs for long-horizon decision-making in Super Mario Land, a visually grounded environment requiring 100+ turns of interaction with coordinated perception, reasoning, and action. We begin with a systematic investigation of key algorithmic components and propose an adapted variant of PPO with a lightweight turn-level critic, which substantially improves training stability and sample efficiency over critic-free methods such as GRPO and Reinforce++. We further show that pretrained VLMs provide strong action priors, significantly improving sample efficiency during RL training and reducing the need for manual design choices such as action engineering, compared to classical deep RL trained from scratch. Building on these insights, we introduce Odysseus, an open training framework for VLM agents, achieving substantial gains across multiple levels of the game and at least 3 times average game progresses than frontier models. Moreover, the trained models exhibit consistent improvements under both in-game and cross-game generalization settings, while maintaining general-domain capabilities. Overall, our results identify key ingredients for making RL stable and effective in long-horizon, multi-modal settings, and provide practical guidance for developing VLMs as embodied agents.

## Source Excerpt

Given the rapidly growing capabilities of vision-language models (VLMs), extending them to interactive decision-making tasks such as video games has emerged as a promising frontier. However, existing approaches either rely on large-scale supervised fine-tuning (SFT) on human trajectories or apply reinforcement learning (RL) only in relatively short-horizon settings (typically around 20--30 turns). In this work, we study RL-based training of VLMs for long-horizon decision-making in Super Mario Land, a visually grounded environment requiring 100+ turns of interaction with coordinated perception, reasoning, and action. We begin with a systematic investigation of key algorithmic components and propose an adapted variant of PPO with a lightweight turn-level critic, which substantially improves training stability and sample efficiency over critic-free methods such as GRPO and Reinforce++. We further show that pretrained VLMs provide strong action priors, significantly improving sample efficiency during RL training and reducing the need for manual design choices such as action engineering, compared to classical deep RL trained from scratch. Building on these insights, we introduce Odysseus, an open training framework for VLM agents, achieving substantial gains across multiple levels of the game and at least 3 times average game progresses than frontier models. Moreover, the trained models exhibit consistent improvements under both in-game and cross-game generalization settings, while maintaining general-domain capabilities. Overall, our results identify key ingredients for making RL stable and effective in long-horizon, multi-modal settings, and provide practical guidance for developing VLMs as embodied agents.

## Open Questions

- What exact environment setup, reward design, and evaluation protocol were used for the Super Mario Land experiments?
- How much of the reported gain comes from the PPO adaptation versus the pretrained VLM action priors?
- Does the lightweight turn-level critic generalize to other games or embodied decision-making tasks beyond Super Mario Land?
- What does 'maintaining general-domain capabilities' mean operationally, and how was it measured?
