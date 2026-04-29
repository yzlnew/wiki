---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, llm-systems, alignment, safety, guard-models, llm-internals, linear-probing]
source_count: 1
updated: 2026-04-28
source_url: https://arxiv.org/abs/2604.18519
paper_id: 2604.18519
published: 2026-04-20T04:00:00+08:00
submitted_on_daily: 2026-04-27T08:16:57+08:00
decision: accept
score: 78
generator: scripts/update_hf_daily_papers.py
---

# LLM Safety From Within: Detecting Harmful Content with Internal Representations

## Summary

- one_sentence_summary: SIREN is a lightweight harmful-content guard model that detects safety signals from internal LLM layers using linear probing and adaptive layer weighting instead of relying only on terminal-layer representations.
- why_relevant: This is relevant to mechanistic interpretability and LLM systems because it uses internal representations to build a practical safety detector, with implications for efficient post-training-era alignment tooling.
- filter_reason: Uses internal LLM representations and probing to build a practical harmfulness detector, which is directly relevant to mechanistic interpretability and LLM safety systems.
- hugging_face_paper: https://huggingface.co/papers/2604.18519
- original_paper: https://arxiv.org/abs/2604.18519
- source_basis: `original abstract page`

## Key Points

- The paper argues that standard guard models miss safety-relevant features because they use only terminal-layer representations.
- SIREN identifies "safety neurons" with linear probing and combines signals across layers using an adaptive layer-weighted strategy.
- The model is built from LLM internals without modifying the underlying model.
- In evaluation, SIREN reportedly outperforms open-source guard models across multiple benchmarks while using 250 times fewer trainable parameters.
- The authors also report better generalization to unseen benchmarks, real-time streaming detection, and improved inference efficiency versus generative guard models.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.18519
- Hugging Face API entry: https://huggingface.co/api/papers/2604.18519
- arXiv abstract: https://arxiv.org/abs/2604.18519
- GitHub: https://github.com/CSSLab/SIREN

## Paper Metadata

- authors: `Difan Jiao`, `Yilun Liu`, `Ye Yuan`, `Zhenwei Tang`, `Linfeng Du`, `Haolun Wu`, `Ashton Anderson`
- organization: `University of Toronto CSSLab`
- ai_keywords: `guard models`, `terminal-layer representations`, `internal layers`, `safety neurons`, `linear probing`, `adaptive layer-weighted strategy`, `harmfulness detector`, `LLM internals`, `trainable parameters`, `real-time streaming detection`, `inference efficiency`, `generative guard models`
- upvotes: `21`
- num_comments: `1`
- abstract: Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM internals without modifying the underlying model. Our comprehensive evaluation shows that SIREN substantially outperforms state-of-the-art open-source guard models across multiple benchmarks while using 250 times fewer trainable parameters. Moreover, SIREN exhibits superior generalization to unseen benchmarks, naturally enables real-time streaming detection, and significantly improves inference efficiency compared to generative guard models. Overall, our results highlight LLM internal states as a promising foundation for practical, high-performance harmfulness detection.
- hf_ai_summary: SIREN is a lightweight guard model that leverages internal layer features from LLMs to improve harmful content detection efficiency and performance.

## Source Excerpt

Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM internals without modifying the underlying model. Our comprehensive evaluation shows that SIREN substantially outperforms state-of-the-art open-source guard models across multiple benchmarks while using 250 times fewer trainable parameters. Moreover, SIREN exhibits superior generalization to unseen benchmarks, naturally enables real-time streaming detection, and significantly improves inference efficiency compared to generative guard models. Overall, our results highlight LLM internal states as a promising foundation for practical, high-performance harmfulness detection.

## Open Questions

- Which base LLMs were used to extract internal representations for SIREN?
- How many benchmarks were included, and what kinds of harmful-content settings did they cover?
- What exactly counts as a "safety neuron," and how stable are these neurons across models or prompts?
- How does the adaptive layer-weighted strategy perform compared with simpler pooling across layers?
- Does the streaming detection behavior introduce latency, calibration, or false-positive tradeoffs?
