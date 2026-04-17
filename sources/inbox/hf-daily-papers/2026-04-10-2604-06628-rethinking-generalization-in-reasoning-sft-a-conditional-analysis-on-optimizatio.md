---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reinforcement-learning, reasoning-behavior-shaping, llm-systems, supervised-finetuning, reasoning, generalization, safety, chain-of-thought]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.06628
paper_id: 2604.06628
published: 2026-04-08T04:00:00+08:00
submitted_on_daily: 2026-04-10T11:14:36+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability

## Summary

- one_sentence_summary: The paper argues that reasoning SFT can generalize cross-domain, but only conditionally, with outcomes shaped by optimization length, training-data quality, and base-model capability, and with a tradeoff between reasoning gains and safety loss.
- why_relevant: It is directly relevant to post-training and reasoning-behavior shaping because it analyzes how supervised finetuning affects generalization, training dynamics, and safety tradeoffs in LLMs.
- filter_reason: Directly studies reasoning post-training generalization, optimization dynamics, and safety tradeoffs in SFT/RL-adjacent settings.
- hugging_face_paper: https://huggingface.co/papers/2604.06628
- original_paper: https://arxiv.org/abs/2604.06628
- source_basis: `original abstract page`

## Key Points

- Some apparent cross-domain failures are optimization artifacts: performance can dip early in training and recover with longer SFT, so short checkpoints can understate generalization.
- Data quality and trace structure matter: low-quality solutions hurt generalization, while verified long chain-of-thought traces produce more consistent cross-domain gains.
- Model capability changes what is learned: stronger models can internalize transferable procedures such as backtracking, while weaker models tend to mimic verbose surface form.
- Generalization is asymmetric: the same reasoning SFT that improves reasoning behavior can also degrade safety.
- The paper reframes the SFT-vs-RL generalization debate from a binary claim to a conditional question about when generalization appears and at what cost.

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
- upvotes: `189`
- num_comments: `6`
- abstract: A prevailing narrative in LLM post-training holds that supervised finetuning (SFT) memorizes while reinforcement learning (RL) generalizes. We revisit this claim for reasoning SFT with long chain-of-thought (CoT) supervision and find that cross-domain generalization is not absent but conditional, jointly shaped by optimization dynamics, training data, and base-model capability. Some reported failures are under-optimization artifacts: cross-domain performance first degrades before recovering and improving with extended training (a dip-and-recovery pattern), so shorttraining checkpoints can underestimate generalization. Data quality and structure both matter: low-quality solutions broadly hurt generalization,while verified long-CoT traces yield consistent cross-domain gains. Model capability is essential: stronger models internalize transferable procedural patterns (e.g., backtracking) even from a toy arithmetic game, while weaker ones imitate surface verbosity. This generalization is asymmetric, however: reasoning improves while safety degrades, reframing the question from whether reasoning SFT generalizes to under what conditions and at what cost.
- hf_ai_summary: Supervised finetuning and reinforcement learning exhibit conditional cross-domain generalization in reasoning tasks, influenced by optimization dynamics, data quality, and model capability, with asymmetric outcomes between reasoning improvement and safety degradation.

## Source Excerpt

A prevailing narrative in LLM post-training holds that supervised finetuning (SFT) memorizes while reinforcement learning (RL) generalizes. We revisit this claim for reasoning SFT with long chain-of-thought (CoT) supervision and find that cross-domain generalization is not absent but conditional, jointly shaped by optimization dynamics, training data, and base-model capability. Some reported failures are under-optimization artifacts: cross-domain performance first degrades before recovering and improving with extended training (a dip-and-recovery pattern), so shorttraining checkpoints can underestimate generalization. Data quality and structure both matter: low-quality solutions broadly hurt generalization,while verified long-CoT traces yield consistent cross-domain gains. Model capability is essential: stronger models internalize transferable procedural patterns (e.g., backtracking) even from a toy arithmetic game, while weaker ones imitate surface verbosity. This generalization is asymmetric, however: reasoning improves while safety degrades, reframing the question from whether reasoning SFT generalizes to under what conditions and at what cost.

## Open Questions

- Which model families and reasoning datasets were used to establish the dip-and-recovery pattern?
- How was cross-domain generalization measured, and across which target domains?
- What criteria defined low-quality versus verified long-CoT traces?
- How large was the reported safety degradation relative to the reasoning gains?
