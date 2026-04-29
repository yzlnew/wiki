---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, post-training, mobile-agents, imitation-learning, task-synthesis, trajectory-rollout, vision-language-models, androidworld, open-source]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.15093
paper_id: 2604.15093
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-23T20:50:33+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis

## Summary

- one_sentence_summary: OpenMobile is an open-source framework for training mobile agents that synthesizes grounded task instructions and trajectories via environment-memory-based task generation and learner-expert policy switching during rollout.
- why_relevant: It is directly about agent training and post-training data synthesis for vision-language mobile agents, which aligns with agent systems and RL-style trajectory collection interests.
- filter_reason: Open-source mobile agent training with task/trajectory synthesis, policy switching, and benchmark evaluation is directly relevant to agents and environment interaction.
- hugging_face_paper: https://huggingface.co/papers/2604.15093
- original_paper: https://arxiv.org/abs/2604.15093
- source_basis: `original abstract page`

## Key Points

- It builds a scalable task synthesis pipeline that first constructs a global environment memory from exploration, then uses that memory to generate diverse, grounded instructions.
- It uses a policy-switching rollout strategy that alternates between learner and expert models to collect error-recovery trajectories that standard imitation learning often misses.
- The paper reports competitive results on three dynamic mobile-agent benchmarks; fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld.
- The authors analyze overlap between synthetic instructions and benchmark test sets and argue the gains come from broad functionality coverage rather than benchmark overfitting.
- The main contribution is data and recipe transparency for mobile agent post-training, with released code and data intended to reduce the open-data gap.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.15093
- Hugging Face API entry: https://huggingface.co/api/papers/2604.15093
- arXiv abstract: https://arxiv.org/abs/2604.15093
- GitHub: https://github.com/njucckevin/OpenMobile-Code
- Project page: https://njucckevin.github.io/openmobile/

## Paper Metadata

- authors: `Kanzhi Cheng`, `Zehao Li`, `Zheng Ma`, `Nuo Chen`, `Jialin Cao`, `Qiushi Sun`, `Zichen Ding`, `Fangzhi Xu`, `Hang Yan`, `Jiajun Chen`, `Anh Tuan Luu`, `Jianbing Zhang`, `Lewei Lu`, `Dahua Lin`
- ai_keywords: `vision-language models`, `mobile agents`, `task synthesis pipeline`, `global environment memory`, `policy-switching strategy`, `trajectory rollout`, `imitation learning`, `AndroidWorld`, `Qwen2.5-VL`, `Qwen3-VL`
- upvotes: `23`
- num_comments: `1`
- abstract: Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at https://njucckevin.github.io/openmobile/ to bridge the data gap and facilitate broader mobile agent research.
- hf_ai_summary: An open-source framework for mobile agent training that synthesizes task instructions and trajectories through scalable pipelines and policy-switching strategies, achieving superior performance on AndroidWorld benchmarks.

## Source Excerpt

Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at this https URL to bridge the data gap and facilitate broader mobile agent research.

## Open Questions

- How much of the improvement comes from the task synthesis pipeline versus the policy-switching rollout strategy individually?
- What is the exact composition and scale of the generated training data?
- How does the approach perform on tasks requiring longer-horizon recovery or more complex multi-app workflows?
- What does the overlap analysis show quantitatively for each benchmark?
