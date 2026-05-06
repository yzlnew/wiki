---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, post-training, agent-evals, multi-turn, exploration, uncertainty, stability, evaluation]
source_count: 1
updated: 2026-05-06
source_url: https://arxiv.org/abs/2605.02178
paper_id: 2605.02178
published: 2026-05-04T04:00:00+08:00
submitted_on_daily: 2026-05-05T09:35:45+08:00
decision: accept
score: 96
generator: scripts/update_hf_daily_papers.py
---

# T^2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning

## Summary

- one_sentence_summary: T^2PO is an uncertainty-aware multi-turn RL method that controls exploration at both token and turn levels to reduce instability and improve agent training performance.
- why_relevant: It is directly relevant to reinforcement learning for agents and post-training because it proposes a concrete stability mechanism for multi-turn tool- and environment-interacting policies.
- filter_reason: Directly targets multi-turn agentic reinforcement learning with exploration control and training stability improvements.
- hugging_face_paper: https://huggingface.co/papers/2605.02178
- original_paper: https://arxiv.org/abs/2605.02178
- source_basis: `original abstract page`

## Key Points

- The paper argues that multi-turn RL instability often comes from inefficient exploration: policies keep producing low-information actions that do not reduce uncertainty or advance task progress.
- At the token level, T^2PO monitors uncertainty dynamics and triggers a thinking intervention when marginal uncertainty reduction falls below a threshold.
- At the turn level, T^2PO detects interactions with negligible exploration progress and dynamically resamples them to avoid wasted rollouts.
- The method is evaluated on WebShop, ALFWorld, and Search QA, where it improves training stability, performance, and exploration efficiency.
- The paper positions T^2PO as a stabilization approach for post-training / agentic RL settings beyond existing credit-assignment and trajectory-filtering tricks.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.02178
- Hugging Face API entry: https://huggingface.co/api/papers/2605.02178
- arXiv abstract: https://arxiv.org/abs/2605.02178
- GitHub: https://github.com/WillDreamer/T2PO

## Paper Metadata

- authors: `Haixin Wang`, `Hejie Cui`, `Chenwei Zhang`, `Xin Liu`, `Shuowei Jin`, `Shijie Geng`, `Xinyang Zhang`, `Nasser Zalmout`, `Zhenyu Shi`, `Yizhou Sun`
- ai_keywords: `multi-turn reinforcement learning`, `policy optimization`, `uncertainty awareness`, `fine-grained exploration`, `trajectory filtering`, `credit assignment`, `training stability`, `reinforcement learning`
- upvotes: `4`
- num_comments: `2`
- abstract: Recent progress in multi-turn reinforcement learning (RL) has significantly improved reasoning LLMs' performances on complex interactive tasks. Despite advances in stabilization techniques such as fine-grained credit assignment and trajectory filtering, instability remains pervasive and often leads to training collapse. We argue that this instability stems from inefficient exploration in multi-turn settings, where policies continue to generate low-information actions that neither reduce uncertainty nor advance task progress. To address this issue, we propose Token- and Turn-level Policy Optimization (T^2PO), an uncertainty-aware framework that explicitly controls exploration at fine-grained levels. At the token level, T^2PO monitors uncertainty dynamics and triggers a thinking intervention once the marginal uncertainty change falls below a threshold. At the turn level, T^2PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts. We evaluate T^2PO in diverse environments, including WebShop, ALFWorld, and Search QA, demonstrating substantial gains in training stability and performance improvements with better exploration efficiency. Code is available at: https://github.com/WillDreamer/T2PO.
- hf_ai_summary: Token- and Turn-level Policy Optimization (T²PO) addresses multi-turn RL instability by controlling exploration at fine-grained levels through uncertainty monitoring and dynamic resampling.

## Source Excerpt

Recent progress in multi-turn reinforcement learning (RL) has significantly improved reasoning LLMs' performances on complex interactive tasks. Despite advances in stabilization techniques such as fine-grained credit assignment and trajectory filtering, instability remains pervasive and often leads to training collapse. We argue that this instability stems from inefficient exploration in multi-turn settings, where policies continue to generate low-information actions that neither reduce uncertainty nor advance task progress. To address this issue, we propose Token- and Turn-level Policy Optimization (T$^2$PO), an uncertainty-aware framework that explicitly controls exploration at fine-grained levels. At the token level, T$^2$PO monitors uncertainty dynamics and triggers a thinking intervention once the marginal uncertainty change falls below a threshold. At the turn level, T$^2$PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts. We evaluate T$^2$PO in diverse environments, including WebShop, ALFWorld, and Search QA, demonstrating substantial gains in training stability and performance improvements with better exploration efficiency. Code is available at: this https URL .

## Open Questions

- How exactly is uncertainty measured at the token level, and what thresholding rule is used in practice?
- What does the dynamic resampling procedure change in the training loop, and how often does it trigger?
- How large are the reported gains on each benchmark, and do they hold across different model backbones?
- Does T^2PO add meaningful training overhead compared with standard multi-turn RL baselines?
