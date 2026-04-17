---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reward-modeling, llm-systems, reasoning-behavior-shaping, llm, reward-shaping, diversity, sampling, clustering, memory]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.11297
paper_id: 2604.11297
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-14T17:48:46+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# The Past Is Not Past: Memory-Enhanced Dynamic Reward Shaping

## Summary

- one_sentence_summary: MEDS is a memory-enhanced reward shaping method for RL-trained LLMs that uses historical rollout representations to detect recurring error clusters and penalize them to improve diversity and performance.
- why_relevant: This is directly relevant to reinforcement learning post-training for LLMs because it changes reward design to shape generation behavior and reduce repeated failure modes during sampling.
- filter_reason: Directly relevant RL-for-LLMs work on dynamic reward shaping that targets repeated failure patterns and sampling diversity.
- hugging_face_paper: https://huggingface.co/papers/2604.11297
- original_paper: https://arxiv.org/abs/2604.11297
- source_basis: `original abstract page`

## Key Points

- The paper targets a specific RL failure mode for LLMs: reduced sampling diversity, where similar erroneous behaviors keep repeating across rollouts.
- MEDS stores intermediate model representations from past rollouts and uses density-based clustering to identify recurring error patterns.
- Rollouts that fall into more prevalent error clusters receive stronger penalties, which is meant to push the policy toward broader exploration rather than repeated mistakes.
- The method is evaluated across five datasets and three base models, with reported gains of up to 4.13 pass@1 and 4.37 pass@128 over baselines.
- The authors report that both LLM-based annotations and quantitative diversity metrics indicate increased behavioral diversity during sampling.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11297
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11297
- arXiv abstract: https://arxiv.org/abs/2604.11297
- GitHub: https://github.com/Linxi000/MEDS

## Paper Metadata

- authors: `Yang Liu`, `Enxi Wang`, `Yufei Gao`, `Weixin Zhang`, `Bo Wang`, `Zhiyuan Zeng`, `Yikai Zhang`, `Yining Zheng`, `Xipeng Qiu`
- ai_keywords: `reinforcement learning`, `large language models`, `sampling diversity`, `entropy regularization`, `reward shaping`, `memory-enhanced dynamic reward shaping`, `historical behavioral signals`, `intermediate model representations`, `density-based clustering`, `error patterns`, `behavioral diversity`
- upvotes: `81`
- num_comments: `1`
- abstract: Despite the success of reinforcement learning for large language models, a common failure mode is reduced sampling diversity, where the policy repeatedly generates similar erroneous behaviors. Classical entropy regularization encourages randomness under the current policy, but does not explicitly discourage recurrent failure patterns across rollouts. We propose MEDS, a Memory-Enhanced Dynamic reward Shaping framework that incorporates historical behavioral signals into reward design. By storing and leveraging intermediate model representations, we capture features of past rollouts and use density-based clustering to identify frequently recurring error patterns. Rollouts assigned to more prevalent error clusters are penalized more heavily, encouraging broader exploration while reducing repeated mistakes. Across five datasets and three base models, MEDS consistently improves average performance over existing baselines, achieving gains of up to 4.13 pass@1 points and 4.37 pass@128 points. Additional analyses using both LLM-based annotations and quantitative diversity metrics show that MEDS increases behavioral diversity during sampling.
- hf_ai_summary: MEDS is a memory-enhanced dynamic reward shaping framework that improves sampling diversity in reinforcement learning for large language models by identifying and penalizing recurrent error patterns through clustering of historical behavioral signals.

## Source Excerpt

Despite the success of reinforcement learning for large language models, a common failure mode is reduced sampling diversity, where the policy repeatedly generates similar erroneous behaviors. Classical entropy regularization encourages randomness under the current policy, but does not explicitly discourage recurrent failure patterns across rollouts. We propose MEDS, a Memory-Enhanced Dynamic reward Shaping framework that incorporates historical behavioral signals into reward design. By storing and leveraging intermediate model representations, we capture features of past rollouts and use density-based clustering to identify frequently recurring error patterns. Rollouts assigned to more prevalent error clusters are penalized more heavily, encouraging broader exploration while reducing repeated mistakes. Across five datasets and three base models, MEDS consistently improves average performance over existing baselines, achieving gains of up to 4.13 pass@1 points and 4.37 pass@128 points. Additional analyses using both LLM-based annotations and quantitative diversity metrics show that MEDS increases behavioral diversity during sampling.

## Open Questions

- How does MEDS compare to standard entropy regularization when matched for compute and sampling budget?
- What intermediate representations are stored, and how sensitive is the method to the choice of representation layer or model state?
- Which five datasets and three base models were used, and do the gains hold uniformly across them?
- How costly is the clustering and memory mechanism during training or rollout collection?
- Does the diversity improvement come with any degradation in calibration, stability, or final-answer quality on harder tasks?
