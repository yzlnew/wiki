---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, llm-systems, mechanistic-interpretability, reasoning-behavior-shaping, mixture-of-experts, activation-steering, llm-safety, routing]
source_count: 1
updated: 2026-05-05
source_url: https://arxiv.org/abs/2604.27818
paper_id: 2604.27818
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-05T02:07:50+08:00
decision: accept
score: 86
generator: scripts/update_hf_daily_papers.py
---

# MASCing: Configurable Mixture-of-Experts Behavior via Activation Steering Masks

## Summary

- one_sentence_summary: MASCing is a no-retraining framework for reconfiguring Mixture-of-Experts LLM behavior by learning routing-dependent steering masks that override expert selection at inference time.
- why_relevant: The paper is relevant to post-training and mechanistic interpretability because it manipulates internal MoE routing behavior directly, using router-level analysis to shape model behavior without retraining.
- filter_reason: Technically detailed MoE behavior steering for safety reconfiguration without retraining, which is useful for post-training and model control work.
- hugging_face_paper: https://huggingface.co/papers/2604.27818
- original_paper: https://arxiv.org/abs/2604.27818
- source_basis: `original abstract page`

## Key Points

- Uses an LSTM-based surrogate model to capture cross-layer routing dependencies and map routing logits to downstream behaviors.
- Optimizes a steering matrix to identify behavior-relevant expert circuits in the MoE router.
- Applies steering masks to routing gates at inference time to enhance or suppress targeted behaviors without full fine-tuning or retraining.
- Reports consistent gains across seven open-source MoE models with negligible overhead.
- Evaluates two safety-oriented objectives: multi-turn jailbreak defense and adult-content generation.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27818
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27818
- arXiv abstract: https://arxiv.org/abs/2604.27818
- GitHub: https://github.com/jonatelintelo/MASCing

## Paper Metadata

- authors: `Jona te Lintelo`, `Lichao Wu`, `Marina Krček`, `Sengim Karayalçin`, `Stjepan Picek`
- ai_keywords: `Mixture-of-Experts`, `Large Language Models`, `sparse activation`, `routing decisions`, `LSTM-based surrogate model`, `routing logits`, `steering matrix`, `steering masks`, `expert circuits`, `jailbreak defense`, `adult-content generation`
- upvotes: `2`
- num_comments: `1`
- abstract: Mixture-of-Experts (MoE) architectures in Large Language Models (LLMs) have significantly reduced inference costs through sparse activation. However, this sparse activation paradigm also introduces new safety challenges. Since only a subset of experts is engaged for each input, model behavior becomes coupled to routing decisions, yielding a difficult-to-control mechanism that can vary across safety-relevant scenarios. At the same time, adapting model behavior through full fine-tuning or retraining is costly, especially when developers need to rapidly configure the same model for different safety objectives. We present MASCing (MoE Activation Steering Configuration), the first framework that enables flexible reconfiguration of MoE behavior across diverse safety scenarios without retraining. MASCing uses an LSTM-based surrogate model to capture cross-layer routing dependencies and map routing logits to downstream behaviors. It then optimizes a steering matrix to identify behavior-relevant expert circuits and, at inference time, applies steering masks to the routing gates to override expert selection. This enables targeted enhancement or suppression of specific behaviors while preserving general language utility. To demonstrate its reconfigurability, we apply MASCing to two different safety-related objectives and observe consistent gains with negligible overhead across seven open-source MoE models. For multi-turn jailbreak defense, it improves the average defense success rate from 52.5% to 83.9%, with gains of up to 89.2%. For adult-content generation, MASCing enables models to comply with such requests that would otherwise be refused, increasing the average generation success rate from 52.6% to 82.0%, with gains of up to 93.0%. These results establish MASCing as a practical, lightweight, and flexible framework for scenario-specific safety reconfiguration in MoE models.
- hf_ai_summary: MASCing is a framework that enables flexible reconfiguration of Mixture-of-Experts model behavior for safety objectives through steering matrices and routing gate modifications without requiring retraining.

## Source Excerpt

Mixture-of-Experts (MoE) architectures in Large Language Models (LLMs) have significantly reduced inference costs through sparse activation. However, this sparse activation paradigm also introduces new safety challenges. Since only a subset of experts is engaged for each input, model behavior becomes coupled to routing decisions, yielding a difficult-to-control mechanism that can vary across safety-relevant scenarios. At the same time, adapting model behavior through full fine-tuning or retraining is costly, especially when developers need to rapidly configure the same model for different safety objectives. We present MASCing (MoE Activation Steering Configuration), the first framework that enables flexible reconfiguration of MoE behavior across diverse safety scenarios without retraining. MASCing uses an LSTM-based surrogate model to capture cross-layer routing dependencies and map routing logits to downstream behaviors. It then optimizes a steering matrix to identify behavior-relevant expert circuits and, at inference time, applies steering masks to the routing gates to override expert selection. This enables targeted enhancement or suppression of specific behaviors while preserving general language utility. To demonstrate its reconfigurability, we apply MASCing to two different safety-related objectives and observe consistent gains with negligible overhead across seven open-source MoE models. For multi-turn jailbreak defense, it improves the average defense success rate from 52.5% to 83.9%, with gains of up to 89.2%. For adult-content generation, MASCing enables models to comply with such requests that would otherwise be refused, increasing the average generation success rate from 52.6% to 82.0%, with gains of up to 93.0%. These results establish MASCing as a practical, lightweight, and flexible framework for scenario-specific safety reconfiguration in MoE models.

## Open Questions

- How general is the steering matrix across tasks, prompts, and model families beyond the seven MoE models tested?
- What are the failure modes or safety tradeoffs when steering masks override routing decisions?
- How much data is needed to fit the surrogate model and identify behavior-relevant expert circuits?
- Does the method preserve performance on non-safety tasks or degrade general utility in subtle ways?
