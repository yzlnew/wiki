---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior, reward-modeling, llm-systems, llm-reasoning, reward-optimization, policy-update, mechanism]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.14142
paper_id: 2604.14142
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-16T09:56:11+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# From P(y|x) to P(y): Investigating Reinforcement Learning in Pre-train Space

## Summary

- one_sentence_summary: The paper proposes PreRL, a reinforcement-learning method that updates the marginal output distribution P(y) in pre-train space, and combines it with standard RL in a two-stage Dual Space RL strategy to improve reasoning.
- why_relevant: It is directly about reinforcement learning post-training for LLM reasoning and introduces a mechanism-level view of how reward updates shape internal reasoning behavior.
- filter_reason: Directly studies reinforcement learning for reasoning behavior shaping and post-training with a new RL formulation and mechanism analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.14142
- original_paper: https://arxiv.org/abs/2604.14142
- source_basis: `original abstract page`

## Key Points

- The core claim is that RLVR over P(y|x) is bounded by the base model's existing output distribution, so directly optimizing the marginal P(y) may better expand reasoning capacity.
- PreRL performs reward-driven online updates in pre-train space rather than relying only on static pre-training corpora.
- The authors report strong gradient alignment between log P(y) and log P(y|x), arguing that PreRL can act as a surrogate for standard RL.
- Negative Sample Reinforcement (NSR) is presented as a key mechanism: it prunes incorrect reasoning spaces and increases reflective behaviors, including reported 14.89x more transition thoughts and 6.54x more reflection thoughts.
- Dual Space RL (DSRL) uses a Policy Reincarnation strategy: first NSR-PreRL to broaden the reasoning horizon, then standard RL for finer optimization, and it is reported to outperform strong baselines.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14142
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14142
- arXiv abstract: https://arxiv.org/abs/2604.14142
- GitHub: https://github.com/Trae1ounG/Pretrain_Space_RLVR

## Paper Metadata

- authors: `Yuqiao Tan`, `Minzheng Wang`, `Bo Liu`, `Zichen Liu`, `Tian Liang`, `Shizhu He`, `Jun Zhao`, `Kang Liu`
- organization: `Chinese Academic of Science Institute of Automation`
- ai_keywords: `reinforcement learning with verifiable rewards`, `conditional distribution`, `marginal distribution`, `pre-train space`, `reward-driven online updates`, `gradient alignment`, `negative sample reinforcement`, `policy reincarnation`, `reasoning horizon`, `standard RL`
- upvotes: `23`
- num_comments: `2`
- abstract: While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.
- hf_ai_summary: PreRL applies reward-driven online updates to the marginal distribution in pre-train space, while DSRL uses NSR-PreRL to expand reasoning horizons before standard RL fine-tuning.

## Source Excerpt

While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.

## Open Questions

- How is P(y) optimized operationally in PreRL, and what exact reward signals or update rules are used?
- What tasks, benchmarks, and model sizes were used to evaluate DSRL against the strong baselines?
- How general is the reported gradient alignment between log P(y) and log P(y|x) across models and training regimes?
- Does NSR improve final answer accuracy, or mainly change intermediate reasoning traces and reflection frequency?
