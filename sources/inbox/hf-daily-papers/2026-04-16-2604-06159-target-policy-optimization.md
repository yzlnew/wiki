---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior-shaping, llm-systems, policy-optimization, llm-rl, sparse-reward]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.06159
paper_id: 2604.06159
published: 2026-04-07T21:55:59+08:00
submitted_on_daily: 2026-04-16T15:32:28+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Target Policy Optimization

## Summary

- one_sentence_summary: Target Policy Optimization (TPO) reframes RL policy updates as fitting a scored target distribution with cross-entropy, rather than directly pushing logits with a policy-gradient update.
- why_relevant: It is directly about reinforcement-learning post-training for LLMs and tool-like completion scoring, with a concrete alternative to standard policy-gradient optimization that is evaluated on sparse-reward settings.
- filter_reason: Directly targets RL post-training for LLMs with a concrete policy optimization method that improves sparse-reward optimization.
- hugging_face_paper: https://huggingface.co/papers/2604.06159
- original_paper: https://arxiv.org/abs/2604.06159
- source_basis: `original abstract page`

## Key Points

- The paper separates two coupled RL questions: which sampled completions should get more probability mass, and how the policy parameters should move to match that desired change.
- TPO constructs a target distribution from scored completions as q_i proportional to p_i^old exp(u_i), then fits the current policy to this target by cross-entropy.
- The sampled-completion logit gradient is p^theta - q, which goes to zero once the policy matches the target distribution.
- The authors argue this avoids the overshoot/undershoot behavior of standard policy-gradient methods that depends on learning rate, clipping, and optimizer settings.
- Across tabular bandits, transformer sequence tasks, and billion-parameter LLM RLVR, TPO matches PG/PPO/GRPO/DG on easy tasks and is substantially better under sparse reward.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.06159
- Hugging Face API entry: https://huggingface.co/api/papers/2604.06159
- arXiv abstract: https://arxiv.org/abs/2604.06159
- GitHub: https://github.com/JeanKaddour/tpo

## Paper Metadata

- authors: `Jean Kaddour`
- ai_keywords: `policy-gradient methods`, `policy optimization`, `target distribution`, `cross-entropy`, `policy matching`, `tabular bandits`, `transformer sequence tasks`, `LLM RLVR`, `sparse reward`
- upvotes: `19`
- num_comments: `2`
- abstract: In RL, given a prompt, we sample a group of completions from a model and score them. Two questions follow: which completions should gain probability mass, and how should the parameters move to realize that change? Standard policy-gradient methods answer both at once, so the update can overshoot or undershoot depending on the learning rate, clipping, and other optimizer choices. We introduce Target Policy Optimization (TPO), which separates the two questions. Given scored completions, TPO constructs a target distribution q_i propto p_i^{,old} exp(u_i) and fits the policy to it by cross-entropy. The loss gradient on sampled-completion logits is p^θ- q, which vanishes once the policy matches the target. On tabular bandits, transformer sequence tasks, and billion-parameter LLM RLVR, TPO matches PG, PPO, GRPO, and DG on easy tasks and substantially outperforms them under sparse reward. Code is available at https://github.com/JeanKaddour/tpo.
- hf_ai_summary: Target Policy Optimization separates policy update decisions from probability assignment in reinforcement learning, improving performance over standard policy gradient methods in sparse reward scenarios.

## Source Excerpt

In RL, given a prompt, we sample a group of completions from a model and score them. Two questions follow: which completions should gain probability mass, and how should the parameters move to realize that change? Standard policy-gradient methods answer both at once, so the update can overshoot or undershoot depending on the learning rate, clipping, and other optimizer choices. We introduce \emph{Target Policy Optimization} (TPO), which separates the two questions. Given scored completions, TPO constructs a target distribution $q_i \propto p_i^{\,\mathrm{old}} \exp(u_i)$ and fits the policy to it by cross-entropy. The loss gradient on sampled-completion logits is $p^\theta - q$, which vanishes once the policy matches the target. On tabular bandits, transformer sequence tasks, and billion-parameter LLM RLVR, TPO matches PG, PPO, GRPO, and DG on easy tasks and substantially outperforms them under sparse reward. Code is available at this https URL .

## Open Questions

- What exact scoring function u_i is used across the different benchmark settings?
- How sensitive is TPO to the choice of old-policy weights p_i^old in the target distribution?
- Does the paper report any failure modes or cases where TPO underperforms PPO/GRPO/DG?
- What implementation details are needed to scale the cross-entropy fitting objective to billion-parameter models?
