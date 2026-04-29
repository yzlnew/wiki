---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reinforcement-learning, mechanistic-interpretability, llm-systems, supervised-fine-tuning, hallucination, continual-learning, self-distillation, mechanistic]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.15574
paper_id: 2604.15574
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-29T03:46:10+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Why Fine-Tuning Encourages Hallucinations and How to Fix It

## Summary

- one_sentence_summary: The paper argues that supervised fine-tuning can increase factual hallucinations by degrading pre-trained knowledge, and proposes continual-learning-inspired fixes such as self-distillation and parameter freezing.
- why_relevant: It is directly relevant to post-training because it studies how SFT changes model behavior, and it also connects to mechanistic interpretability by proposing and testing an internal-interference explanation for hallucinations.
- filter_reason: Directly addresses post-training hallucination mitigation with continual-learning methods and a mechanism analysis of interference.
- hugging_face_paper: https://huggingface.co/papers/2604.15574
- original_paper: https://arxiv.org/abs/2604.15574
- source_basis: `original abstract page`

## Key Points

- SFT can worsen hallucinations relative to knowledge learned during pre-training, even when it improves factual learning on new data.
- The main proposed mitigation is a self-distillation-based SFT objective that regularizes output-distribution drift while preserving factual acquisition.
- When new knowledge acquisition is not needed, freezing parameter groups can reduce factual plasticity and preserve task performance while lowering hallucinations.
- The authors test three explanations for SFT-induced hallucinations: capacity limits, behavior cloning, and localized interference.
- Their experiments support interference between overlapping semantic representations as a key mechanism, and suggest self-distillation helps by reducing that interference.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.15574
- Hugging Face API entry: https://huggingface.co/api/papers/2604.15574
- arXiv abstract: https://arxiv.org/abs/2604.15574

## Paper Metadata

- authors: `Guy Kaplan`, `Zorik Gekhman`, `Zhen Zhu`, `Lotem Rozner`, `Yuval Reif`, `Swabha Swayamdipta`, `Derek Hoiem`, `Roy Schwartz`
- ai_keywords: `supervised fine-tuning`, `hallucinations`, `continual learning`, `self-distillation`, `output-distribution drift`, `parameter-efficient fine-tuning`, `knowledge degradation`, `semantic representations`, `interference`
- upvotes: `13`
- num_comments: `2`
- abstract: Large language models are prone to hallucinating factually incorrect statements. A key source of these errors is exposure to new factual information through supervised fine-tuning (SFT), which can increase hallucinations w.r.t. knowledge acquired during pre-training. In this work, we explore whether SFT-induced hallucinations can be mitigated using established tools from the continual learning literature, since they arise as a by-product of knowledge degradation during training. We propose a self-distillation-based SFT method that facilitates effective factual learning while minimizing hallucinations w.r.t. pre-existing knowledge by regularizing output-distribution drift. We also show that, in settings where new knowledge acquisition is unnecessary, suppressing factual plasticity by freezing parameter groups, can preserve task performance while reducing hallucinations. Lastly, we investigate the mechanism behind SFT-induced hallucinations through three hypotheses: capacity limitations, behavior cloning, and localized interference. Our experiments show that a main driver is interference among overlapping semantic representations, and that self-distillation succeeds by mitigating this interference.
- hf_ai_summary: Supervised fine-tuning in large language models can cause factual hallucinations due to knowledge degradation, which can be reduced through self-distillation regularization and parameter freezing techniques.

## Source Excerpt

Large language models are prone to hallucinating factually incorrect statements. A key source of these errors is exposure to new factual information through supervised fine-tuning (SFT), which can increase hallucinations w.r.t. knowledge acquired during pre-training. In this work, we explore whether SFT-induced hallucinations can be mitigated using established tools from the continual learning literature, since they arise as a by-product of knowledge degradation during training. We propose a self-distillation-based SFT method that facilitates effective factual learning while minimizing hallucinations w.r.t. pre-existing knowledge by regularizing output-distribution drift. We also show that, in settings where new knowledge acquisition is unnecessary, suppressing factual plasticity by freezing parameter groups, can preserve task performance while reducing hallucinations. Lastly, we investigate the mechanism behind SFT-induced hallucinations through three hypotheses: capacity limitations, behavior cloning, and localized interference. Our experiments show that a main driver is interference among overlapping semantic representations, and that self-distillation succeeds by mitigating this interference.

## Open Questions

- How does the self-distillation method compare against standard SFT across different model sizes and domains?
- Which parameter groups are frozen in the freezing variant, and how sensitive are results to that choice?
- What evaluation benchmarks were used to measure factual retention versus hallucination reduction?
- Does the interference explanation generalize beyond the specific SFT settings tested in the paper?
