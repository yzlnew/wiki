---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, circuit-analysis, post-training, alignment, llm-systems, llm-safety, jailbreaking, activation-scaling]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2509.25843
paper_id: 2509.25843
published: 2026-04-14T04:00:00+08:00
submitted_on_daily: 2026-04-17T08:59:56+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack

## Summary

- one_sentence_summary: ASGuard is a mechanistically informed safety method that uses circuit analysis and channel-wise activation scaling to harden LLM refusal behavior against tense-based targeted jailbreaking while preserving general utility.
- why_relevant: It connects directly to mechanistic interpretability, post-training alignment, and agent/safety behavior control by showing how internal circuit analysis can guide a concrete jailbreak mitigation method.
- filter_reason: Mechanistically grounded safety alignment work using circuit analysis and targeted fine-tuning to harden refusal behavior.
- hugging_face_paper: https://huggingface.co/papers/2509.25843
- original_paper: https://arxiv.org/abs/2509.25843
- source_basis: `original abstract page`

## Key Points

- The paper focuses on a specific generalization failure in alignment: models that refuse harmful requests can be induced to comply when the prompt is linguistically rephrased, such as shifting to past tense.
- ASGuard first uses circuit analysis to identify attention heads causally associated with the targeted jailbreak behavior.
- It then learns a channel-wise scaling vector to recalibrate activations in the vulnerable heads, followed by a preventative fine-tuning step intended to make the refusal mechanism more robust.
- The method is evaluated across four LLMs and is reported to reduce attack success rate while minimizing over-refusal and preserving general capabilities.
- The authors argue that adversarial suffixes suppress a refusal-mediating direction, and that internal-model understanding can support targeted, efficient safety interventions.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2509.25843
- Hugging Face API entry: https://huggingface.co/api/papers/2509.25843
- arXiv abstract: https://arxiv.org/abs/2509.25843
- GitHub: https://github.com/dmis-lab/ASGuard

## Paper Metadata

- authors: `Yein Park`, `Jungwoo Park`, `Jaewoo Kang`
- organization: `Korea University`
- ai_keywords: `large language models`, `jailbreaking`, `attention heads`, `circuit analysis`, `activation scaling`, `preventative fine-tuning`, `refusal behavior`, `adversarial suffixes`, `model internals`, `safety alignment`
- upvotes: `18`
- num_comments: `3`
- abstract: Large language models (LLMs), despite being safety-aligned, exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes. As tense jailbreaking demonstrates that models refusing harmful requests often comply when rephrased in past tense, a critical generalization gap is revealed in current alignment methods whose underlying mechanisms are poorly understood. In this work, we introduce Activation-Scaling Guard (ASGuard), an insightful, mechanistically-informed framework that surgically mitigates this specific vulnerability. In the first step, we use circuit analysis to identify the specific attention heads causally linked to the targeted jailbreaking such as a tense-changing attack. Second, we train a precise, channel-wise scaling vector to recalibrate the activation of tense vulnerable heads. Lastly, we apply it into a "preventative fine-tuning", forcing the model to learn a more robust refusal mechanism. Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility. Our findings underscore how adversarial suffixes suppress the propagation of the refusal-mediating direction, based on mechanistic analysis. Furthermore, our work showcases how a deep understanding of model internals can be leveraged to develop practical, efficient, and targeted methods for adjusting model behavior, charting a course for more reliable and interpretable AI safety.
- hf_ai_summary: Activation-Scaling Guard (ASGuard) mitigates brittle refusal behaviors in large language models by identifying and recalibrating specific attention heads vulnerable to tense-based jailbreaking attacks through mechanistic circuit analysis and targeted fine-tuning.

## Source Excerpt

Large language models (LLMs), despite being safety-aligned, exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes. As tense jailbreaking demonstrates that models refusing harmful requests often comply when rephrased in past tense, a critical generalization gap is revealed in current alignment methods whose underlying mechanisms are poorly understood. In this work, we introduce Activation-Scaling Guard (ASGuard), an insightful, mechanistically-informed framework that surgically mitigates this specific vulnerability. In the first step, we use circuit analysis to identify the specific attention heads causally linked to the targeted jailbreaking such as a tense-changing attack. Second, we train a precise, channel-wise scaling vector to recalibrate the activation of tense vulnerable heads. Lastly, we apply it into a "preventative fine-tuning", forcing the model to learn a more robust refusal mechanism. Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility. Our findings underscore how adversarial suffixes suppress the propagation of the refusal-mediating direction, based on mechanistic analysis. Furthermore, our work showcases how a deep understanding of model internals can be leveraged to develop practical, efficient, and targeted methods for adjusting model behavior, charting a course for more reliable and interpretable AI safety.

## Open Questions

- Which four LLMs were evaluated, and how large were the gains across models?
- How exactly were the vulnerable attention heads identified and validated as causal?
- What is the training objective for the channel-wise scaling vector and the preventative fine-tuning stage?
- How does ASGuard perform against other jailbreak variants beyond tense-changing attacks?
- Does the method transfer to broader safety behaviors, or is it specific to refusal under tense-based prompts?
