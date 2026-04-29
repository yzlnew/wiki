---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, mixture-of-experts, options-framework]
source_count: 1
updated: 2026-04-25
source_url: https://arxiv.org/abs/2604.20156
paper_id: 2604.20156
published: 2026-04-22T04:00:00+08:00
submitted_on_daily: 2026-04-25T00:13:18+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Temporally Extended Mixture-of-Experts Models

## Summary

- one_sentence_summary: The paper proposes temporally extended mixture-of-experts layers by adding an RL-style controller that learns when to switch expert sets and which experts to load, reducing expert churn while preserving much of the base model's accuracy.
- why_relevant: It directly combines reinforcement learning ideas with post-training of an LLM system to control expert routing and memory behavior, which is relevant to both RL/post-training and agentic model infrastructure.
- filter_reason: Uses the RL options framework to reshape MoE expert switching for practical serving and accuracy tradeoffs.
- hugging_face_paper: https://huggingface.co/papers/2604.20156
- original_paper: https://arxiv.org/abs/2604.20156
- source_basis: `original abstract page`

## Key Points

- Builds on the options framework and option-critic with deliberation costs to make expert switching temporally extended rather than token-by-token.
- Adds a controller at each layer that learns both switching timing and expert loading decisions.
- Uses low-rank adapters plus a self-distillation reward to convert gpt-oss-20b into a temporally extended MoE.
- Reports a drop in expert switch rates from over 50% to below 5% while retaining up to 90% of base-model accuracy on MATH, MMLU, and MMMLU.
- Motivates the method as a path toward memory-efficient serving and continual learning for large MoE models where churn breaks offloading and prefetching optimizations.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.20156
- Hugging Face API entry: https://huggingface.co/api/papers/2604.20156
- arXiv abstract: https://arxiv.org/abs/2604.20156
- GitHub: https://github.com/princeton-polaris-lab/rl_moe
- Project page: https://princeton-polaris-lab.github.io/moe_webpage/

## Paper Metadata

- authors: `Zeyu Shen`, `Peter Henderson`
- organization: `Princeton University`
- ai_keywords: `mixture-of-experts`, `reinforcement learning`, `options framework`, `option-critic framework`, `deliberation costs`, `self-distillation`, `low-rank adapters`, `GPT-oss-20b`
- upvotes: `1`
- num_comments: `2`
- abstract: Mixture-of-Experts models, now popular for scaling capacity at fixed inference speed, switch experts at nearly every token. Once a model outgrows available GPU memory, this churn can render optimizations like offloading and pre-fetching ineffective. We make the case that the options framework in reinforcement learning is a perfect match to tackle this problem, and argue for temporally extended mixture-of-experts layers. Building on the option-critic framework with deliberation costs, we add a controller to each layer that learns when to switch expert sets and which to load. By applying this to gpt-oss-20b with low-rank adapters and a self-distillation reward, our method reduces switch rates from over 50% to below 5% while retaining up to 90% of base-model accuracy on MATH, MMLU, and MMMLU. This shows that even existing pre-trained models can be converted to temporally extended MoEs with lightweight training, with the deliberation cost allowing model trainers to trade off switching rates against capability. We hope this opens a principled path, grounded in the options framework, for memory-efficient serving and continual learning in ever-growing MoE models.
- hf_ai_summary: Temporal extension of mixture-of-experts layers using reinforcement learning options framework reduces expert switching rates while maintaining model accuracy.

## Source Excerpt

Mixture-of-Experts models, now popular for scaling capacity at fixed inference speed, switch experts at nearly every token. Once a model outgrows available GPU memory, this churn can render optimizations like offloading and pre-fetching ineffective. We make the case that the options framework in reinforcement learning is a perfect match to tackle this problem, and argue for temporally extended mixture-of-experts layers. Building on the option-critic framework with deliberation costs, we add a controller to each layer that learns when to switch expert sets and which to load. By applying this to gpt-oss-20b with low-rank adapters and a self-distillation reward, our method reduces switch rates from over 50% to below 5% while retaining up to 90% of base-model accuracy on MATH, MMLU, and MMMLU. This shows that even existing pre-trained models can be converted to temporally extended MoEs with lightweight training, with the deliberation cost allowing model trainers to trade off switching rates against capability. We hope this opens a principled path, grounded in the options framework, for memory-efficient serving and continual learning in ever-growing MoE models.

## Open Questions

- How exactly is the deliberation cost defined and tuned during training?
- What is the controller architecture used at each layer?
- How does performance change across different expert budgets or memory constraints?
- Does the method generalize beyond gpt-oss-20b and the reported benchmarks?
- What does self-distillation reward mean operationally in this setup?
