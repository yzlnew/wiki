---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reinforcement-learning, reasoning-behavior-shaping, llm-systems, sft, reasoning, generalization, chain-of-thought, safety, optimization-dynamics]
source_count: 1
updated: 2026-04-10
source_url: https://arxiv.org/abs/2604.06628
paper_id: 2604.06628
published: 2026-04-08T04:00:00+08:00
submitted_on_daily: 2026-04-10T11:14:36+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability

## Summary

- one_sentence_summary: The paper argues that reasoning SFT can generalize cross-domain, but only under certain optimization, data, and model-capability conditions, and that gains in reasoning may come with safety regressions.
- why_relevant: It is directly relevant to post-training and RL-adjacent reasoning behavior shaping because it studies when supervised reasoning fine-tuning generalizes, and what tradeoffs it creates for safety.
- filter_reason: Directly studies reasoning post-training generalization, comparing SFT and RL with useful findings on optimization, data quality, and capability.
- hugging_face_paper: https://huggingface.co/papers/2604.06628
- original_paper: https://arxiv.org/abs/2604.06628
- source_basis: `original abstract page`

## Key Points

- Challenges the simple post-training narrative that SFT only memorizes while RL generalizes; for long-CoT reasoning SFT, cross-domain generalization is conditional rather than absent.
- Shows a dip-and-recovery training pattern: some cross-domain failures appear to be under-optimization artifacts, so short checkpoints can understate eventual generalization.
- Finds that data quality and structure matter: low-quality solutions broadly harm cross-domain generalization, while verified long-CoT traces produce consistent gains.
- Argues model capability is essential: stronger models can internalize transferable procedures such as backtracking, while weaker models mostly mimic surface verbosity.
- Reports asymmetric effects: reasoning performance improves, but safety degrades, so generalization should be evaluated with both capability and alignment costs in view.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.06628
- Hugging Face API entry: https://huggingface.co/api/papers/2604.06628
- arXiv abstract: https://arxiv.org/abs/2604.06628
- GitHub: https://github.com/Nebularaid2000/rethink_sft_generalization

## Paper Metadata

- authors: `Qihan Ren`, `Peng Wang`, `Ruikun Cai`, `Shuai Shao`, `Dadi Guo`, `Yuejin Xie`, `Yafu Li`, `Quanshi Zhang`, `Xia Hu`, `Jing Shao`, `Dongrui Liu`
- organization: `AI45Research`
- ai_keywords: `supervised finetuning`, `reinforcement learning`, `cross-domain generalization`, `optimization dynamics`, `long chain-of-thought`, `training data`, `base-model capability`, `dip-and-recovery pattern`, `data quality`, `model capability`, `reasoning tasks`, `safety degradation`
- upvotes: `49`
- num_comments: `1`
- abstract: A prevailing narrative in LLM post-training holds that supervised finetuning (SFT) memorizes while reinforcement learning (RL) generalizes. We revisit this claim for reasoning SFT with long chain-of-thought (CoT) supervision and find that cross-domain generalization is not absent but conditional, jointly shaped by optimization dynamics, training data, and base-model capability. Some reported failures are under-optimization artifacts: cross-domain performance first degrades before recovering and improving with extended training (a dip-and-recovery pattern), so shorttraining checkpoints can underestimate generalization. Data quality and structure both matter: low-quality solutions broadly hurt generalization,while verified long-CoT traces yield consistent cross-domain gains. Model capability is essential: stronger models internalize transferable procedural patterns (e.g., backtracking) even from a toy arithmetic game, while weaker ones imitate surface verbosity. This generalization is asymmetric, however: reasoning improves while safety degrades, reframing the question from whether reasoning SFT generalizes to under what conditions and at what cost.
- hf_ai_summary: Supervised finetuning and reinforcement learning exhibit conditional cross-domain generalization in reasoning tasks, influenced by optimization dynamics, data quality, and model capability, with asymmetric outcomes between reasoning improvement and safety degradation.

## Source Excerpt

A prevailing narrative in LLM post-training holds that supervised finetuning (SFT) memorizes while reinforcement learning (RL) generalizes. We revisit this claim for reasoning SFT with long chain-of-thought (CoT) supervision and find that cross-domain generalization is not absent but conditional, jointly shaped by optimization dynamics, training data, and base-model capability. Some reported failures are under-optimization artifacts: cross-domain performance first degrades before recovering and improving with extended training (a dip-and-recovery pattern), so shorttraining checkpoints can underestimate generalization. Data quality and structure both matter: low-quality solutions broadly hurt generalization,while verified long-CoT traces yield consistent cross-domain gains. Model capability is essential: stronger models internalize transferable procedural patterns (e.g., backtracking) even from a toy arithmetic game, while weaker ones imitate surface verbosity. This generalization is asymmetric, however: reasoning improves while safety degrades, reframing the question from whether reasoning SFT generalizes to under what conditions and at what cost.

## Open Questions

- Which specific cross-domain tasks were used to measure generalization?
- How much extended training was needed to observe the dip-and-recovery effect?
- What criteria defined low-quality versus verified long-CoT traces?
- How large and consistent was the reported safety degradation?
