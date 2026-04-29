---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, representation-analysis, internal-dynamics, llm-systems, representation-learning, fourier, numbers, transformers, rnn, lstm]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.20817
paper_id: 2604.20817
published: 2026-04-22T04:00:00+08:00
submitted_on_daily: 2026-04-23T09:42:29+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# Convergent Evolution: How Different Language Models Learn Similar Number Representations

## Summary

- one_sentence_summary: The paper shows that several model families learn periodic number representations with Fourier spikes at periods 2, 5, and 10, but only some of those features become geometrically separable enough for linear mod-T classification.
- why_relevant: It is directly relevant to mechanistic interpretability because it compares internal numerical representations across architectures and explains when periodic features become linearly usable, which also connects to representation learning in post-training and tool-using systems that rely on structured latent features.
- filter_reason: Strong representation-analysis paper on how language models encode numbers, with mechanistic structure and training-signal analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.20817
- original_paper: https://arxiv.org/abs/2604.20817
- source_basis: `original abstract page`

## Key Points

- Transformers, linear RNNs, LSTMs, and classical word embeddings all learn periodic numerical features in the Fourier domain.
- The authors distinguish Fourier sparsity from geometric separability: a model can show period-T spikes without supporting linear classification of numbers modulo T.
- They prove that Fourier-domain sparsity is necessary but not sufficient for mod-T geometric separability.
- Whether separable features emerge depends on training data, architecture, optimizer, and tokenizer.
- They identify two routes to separable features: general language co-occurrence signals, including text-number and cross-number interaction, or multi-token addition tasks.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.20817
- Hugging Face API entry: https://huggingface.co/api/papers/2604.20817
- arXiv abstract: https://arxiv.org/abs/2604.20817
- Project page: https://convergent-evolution.github.io/

## Paper Metadata

- authors: `Deqing Fu`, `Tianyi Zhou`, `Mikhail Belkin`, `Vatsal Sharan`, `Robin Jia`
- organization: `University of Southern California`
- ai_keywords: `Fourier domain`, `period-T spikes`, `geometric separability`, `linear classification`, `mod-T`, `Transformers`, `Linear RNNs`, `LSTMs`, `word embeddings`, `Fourier domain sparsity`, `convergent evolution`, `co-occurrence signals`, `text-number co-occurrence`, `cross-number interaction`, `multi-token addition problems`
- upvotes: `5`
- num_comments: `3`
- abstract: Language models trained on natural text learn to represent numbers using periodic features with dominant periods at T=2, 5, 10. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-T spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-T. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-T geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.
- hf_ai_summary: Transformers and other language models exhibit periodic numerical representations in their Fourier domains, with some models developing geometrically separable features for linear classification of numbers modulo T, though Fourier sparsity alone is insufficient for this separability.

## Source Excerpt

Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-$T$ spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-$T$. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-$T$ geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.

## Open Questions

- Which specific optimizer and tokenizer choices most strongly affect geometric separability?
- How general is the two-route explanation beyond the number-mod-T setting?
- Does the same hierarchy appear for other symbolic or algorithmic features besides numbers?
