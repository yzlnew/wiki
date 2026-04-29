---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, alignment, mechanistic-interpretability, representation-analysis, llm-systems, audio-llm, safety]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.16659
paper_id: 2604.16659
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-23T20:56:12+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs

## Summary

- one_sentence_summary: This paper shows that benign fine-tuning can sharply erode safety alignment in Audio LLMs, with jailbreak success rising to 87.12% and the failure mode depending on model architecture and how audio is encoded.
- why_relevant: It directly connects post-training and alignment robustness with representation analysis, and the mechanistic result about a suppressed late-layer refusal circuit is relevant to internal model analysis.
- filter_reason: Directly studies post-training safety degradation and includes mechanistic analysis of refusal circuitry in aligned models.
- hugging_face_paper: https://huggingface.co/papers/2604.16659
- original_paper: https://arxiv.org/abs/2604.16659
- source_basis: `original abstract page`

## Key Points

- The authors study benign fine-tuning safety in three state-of-the-art Audio LLMs and use a proximity-based filtering framework to select benign audio near harmful content in embedding space.
- They decompose proximity into semantic, acoustic, and mixed axes using external reference encoders plus each model's internal encoder, rather than treating representation space as undifferentiated.
- Benign fine-tuning can raise Jailbreak Success Rate from single digits to as high as 87.12%.
- The main vulnerability axis, and whether audio or text fine-tuning is riskier, depends on architecture and on how the encoder and projector map audio into the LLM input space.
- They report two defenses: filtering training data to stay far from harmful embeddings and adding a textual system prompt at inference; both reduce JSR to near-zero without changing the architecture.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.16659
- Hugging Face API entry: https://huggingface.co/api/papers/2604.16659
- arXiv abstract: https://arxiv.org/abs/2604.16659

## Paper Metadata

- authors: `Jaechul Roh`, `Amir Houmansadr`
- ai_keywords: `Audio LLMs`, `embedding space`, `harmful content`, `Jailbreak Success Rate`, `fine-tuning`, `proximity-based filtering`, `semantic axis`, `acoustic axis`, `mixed axis`, `external reference encoders`, `internal encoder`, `encoder`, `projector`, `late-layer refusal circuit`, `frozen encoder`
- upvotes: `0`
- num_comments: `1`
- abstract: Prior work shows that fine-tuning aligned models on benign data degrades safety in text and vision modalities, and that proximity to harmful content in representation space predicts which samples cause the most damage. However, existing analyses operate within a single, undifferentiated embedding space -- leaving open whether distinct input properties drive the vulnerability differently. Audio introduces a structurally richer problem: a benign sample can neighbor harmful content not only through what is said but through how it sounds, even when its words are entirely innocuous. We present the first systematic study of benign fine-tuning safety in Audio LLMs, evaluating three state-of-the-art models with a proximity-based filtering framework that selects benign audio by embedding-space distance to harmful content. By decomposing proximity into semantic, acoustic, and mixed axes using external reference encoders alongside each model's own internal encoder, we show that benign fine-tuning elevates Jailbreak Success Rate (JSR) from single digits to as high as 87.12%. Crucially, the dominant vulnerability axis and the relative risk of audio versus text fine-tuning are both architecture-conditioned -- determined by how each model's encoder and projector transform audio into the LLM's input space. We propose two defenses: filtering training data to maximize distance from harmful embeddings, and a textual system prompt at inference, both reducing JSR to near-zero without architectural modification. Our mechanistic analysis on two architectures reveals that fine-tuning selectively suppresses the late-layer refusal circuit while the frozen encoder preserves representations, and that even the suppression pattern is architecture-conditioned, mirroring the behavioral asymmetries across modalities. Safety degradation from benign fine-tuning is a qualitatively distinct risk in Audio LLMs.
- hf_ai_summary: Audio LLM safety degradation through benign fine-tuning occurs due to proximity to harmful content in embedding space, with vulnerability patterns varying by model architecture and modality.

## Source Excerpt

Prior work shows that fine-tuning aligned models on benign data degrades safety in text and vision modalities, and that proximity to harmful content in representation space predicts which samples cause the most damage. However, existing analyses operate within a single, undifferentiated embedding space -- leaving open whether distinct input properties drive the vulnerability differently. Audio introduces a structurally richer problem: a benign sample can neighbor harmful content not only through what is said but through how it sounds, even when its words are entirely innocuous. We present the first systematic study of benign fine-tuning safety in Audio LLMs, evaluating three state-of-the-art models with a proximity-based filtering framework that selects benign audio by embedding-space distance to harmful content. By decomposing proximity into semantic, acoustic, and mixed axes using external reference encoders alongside each model's own internal encoder, we show that benign fine-tuning elevates Jailbreak Success Rate (JSR) from single digits to as high as 87.12%. Crucially, the dominant vulnerability axis and the relative risk of audio versus text fine-tuning are both architecture-conditioned -- determined by how each model's encoder and projector transform audio into the LLM's input space. We propose two defenses: filtering training data to maximize distance from harmful embeddings, and a textual system prompt at inference, both reducing JSR to near-zero without architectural modification. Our mechanistic analysis on two architectures reveals that fine-tuning selectively suppresses the late-layer refusal circuit while the frozen encoder preserves representations, and that even the suppression pattern is architecture-conditioned, mirroring the behavioral asymmetries across modalities. Safety degradation from benign fine-tuning is a qualitatively distinct risk in Audio LLMs.

## Open Questions

- Which three Audio LLM architectures were evaluated, and how different were their vulnerability patterns?
- How exactly were the semantic, acoustic, and mixed axes defined operationally?
- Does the near-zero JSR defense result hold across all evaluated models and datasets, or only under the paper's test conditions?
- What evidence shows the late-layer refusal circuit is selectively suppressed rather than simply bypassed?
