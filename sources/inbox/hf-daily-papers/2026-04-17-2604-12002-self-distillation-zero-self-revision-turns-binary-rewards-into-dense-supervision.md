---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reward-modeling, reasoning-behavior-shaping, llm-systems, self-distillation, binary-rewards, reasoning, sample-efficiency]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.12002
paper_id: 2604.12002
published: 2026-04-13T23:46:55+08:00
submitted_on_daily: 2026-04-17T01:59:16+08:00
decision: accept
score: 95
generator: scripts/update_hf_daily_papers.py
---

# Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision

## Summary

- one_sentence_summary: Self-Distillation Zero is a post-training method that uses a single model as both generator and reviser to turn binary reward signals into dense token-level supervision via on-policy self-distillation.
- why_relevant: This is directly relevant to reinforcement learning and post-training because it proposes a sample-efficient alternative to RLVR that uses reward signals to create dense supervision without an external teacher, and it also touches agent-like self-improvement dynamics.
- filter_reason: Directly advances post-training with binary rewards, self-distillation, and stronger reasoning performance.
- hugging_face_paper: https://huggingface.co/papers/2604.12002
- original_paper: https://arxiv.org/abs/2604.12002
- source_basis: `original abstract page`

## Key Points

- The method targets verifiable post-training settings where RLVR gives only sparse binary rewards and standard distillation needs costly external teachers or demonstrations.
- SD-Zero trains one model in two roles: a Generator that produces an initial answer and a Reviser that conditions on the answer plus its binary reward to produce an improved answer.
- The reviser's token distributions are then distilled back into the generator using on-policy self-distillation, converting reward feedback into dense token-level supervision.
- On math and code reasoning benchmarks with Qwen3-4B-Instruct and Olmo-3-7B-Instruct, the paper reports at least 10% improvement over the base models and better results than RFT, GRPO, and SDFT under the same question set and training budget.
- Ablations highlight token-level self-localization, where the reviser identifies which tokens need revision, and iterative self-evolution, where revision skill can be propagated back into generation through teacher synchronization.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.12002
- Hugging Face API entry: https://huggingface.co/api/papers/2604.12002
- arXiv abstract: https://arxiv.org/abs/2604.12002

## Paper Metadata

- authors: `Yinghui He`, `Simran Kaur`, `Adithya Bhaskar`, `Yongjin Yang`, `Jiarui Liu`, `Narutatsu Ri`, `Liam Fowl`, `Abhishek Panigrahi`, `Danqi Chen`, `Sanjeev Arora`
- organization: `Princeton University`
- ai_keywords: `reinforcement learning`, `distillation`, `self-distillation`, `binary rewards`, `token-level supervision`, `on-policy self-distillation`, `token-level self-localization`, `iterative self-evolution`, `teacher synchronization`
- upvotes: `5`
- num_comments: `3`
- abstract: Current post-training methods in verifiable settings fall into two categories. Reinforcement learning (RLVR) relies on binary rewards, which are broadly applicable and powerful, but provide only sparse supervision during training. Distillation provides dense token-level supervision, typically obtained from an external teacher or using high-quality demonstrations. Collecting such supervision can be costly or unavailable. We propose Self-Distillation Zero (SD-Zero), a method that is substantially more training sample-efficient than RL and does not require an external teacher or high-quality demonstrations. SD-Zero trains a single model to play two roles: a Generator, which produces an initial response, and a Reviser, which conditions on that response and its binary reward to produce an improved response. We then perform on-policy self-distillation to distill the reviser into the generator, using the reviser's token distributions conditioned on the generator's response and its reward as supervision. In effect, SD-Zero trains the model to transform binary rewards into dense token-level self-supervision. On math and code reasoning benchmarks with Qwen3-4B-Instruct and Olmo-3-7B-Instruct, SD-Zero improves performance by at least 10% over the base models and outperforms strong baselines, including Rejection Fine-Tuning (RFT), GRPO, and Self-Distillation Fine-Tuning (SDFT), under the same question set and training sample budget. Extensive ablation studies show two novel characteristics of our proposed algorithm: (a) token-level self-localization, where the reviser can identify the key tokens that need to be revised in the generator's response based on reward, and (b) iterative self-evolution, where the improving ability to revise answers can be distilled back into generation performance with regular teacher synchronization.
- hf_ai_summary: Self-Distillation Zero trains a model to transform binary rewards into dense token-level self-supervision through dual-role training and on-policy self-distillation, achieving superior performance in reasoning tasks with reduced sample efficiency requirements.

## Source Excerpt

Current post-training methods in verifiable settings fall into two categories. Reinforcement learning (RLVR) relies on binary rewards, which are broadly applicable and powerful, but provide only sparse supervision during training. Distillation provides dense token-level supervision, typically obtained from an external teacher or using high-quality demonstrations. Collecting such supervision can be costly or unavailable. We propose Self-Distillation Zero (SD-Zero), a method that is substantially more training sample-efficient than RL and does not require an external teacher or high-quality demonstrations. SD-Zero trains a single model to play two roles: a Generator, which produces an initial response, and a Reviser, which conditions on that response and its binary reward to produce an improved response. We then perform on-policy self-distillation to distill the reviser into the generator, using the reviser's token distributions conditioned on the generator's response and its reward as supervision. In effect, SD-Zero trains the model to transform binary rewards into dense token-level self-supervision. On math and code reasoning benchmarks with Qwen3-4B-Instruct and Olmo-3-7B-Instruct, SD-Zero improves performance by at least 10% over the base models and outperforms strong baselines, including Rejection Fine-Tuning (RFT), GRPO, and Self-Distillation Fine-Tuning (SDFT), under the same question set and training sample budget. Extensive ablation studies show two novel characteristics of our proposed algorithm: (a) token-level self-localization, where the reviser can identify the key tokens that need to be revised in the generator's response based on reward, and (b) iterative self-evolution, where the improving ability to revise answers can be distilled back into generation performance with regular teacher synchronization.

## Open Questions

- How does SD-Zero compare with the baselines across different benchmark types beyond math and code reasoning?
- What exact training details, synchronization schedule, and distillation objective are used to make the reviser-to-generator transfer work?
- How robust is the method when binary rewards are noisy or only weakly correlated with answer quality?
- Does the approach scale to larger models or to settings with tool use and multi-step agentic behavior?
