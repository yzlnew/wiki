---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, representation-analysis, internal-dynamics, llm-systems, pretraining, curriculum, capability-emergence, llm]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2604.08510
paper_id: 2604.08510
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-17T04:42:54+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# What do Language Models Learn and When? The Implicit Curriculum Hypothesis

## Summary

- one_sentence_summary: The paper argues that LLM pretraining follows a predictable compositional curriculum, where simpler skills tend to emerge before composite ones and the emergence order is reflected in internal representations.
- why_relevant: This is relevant to mechanistic interpretability and internal-dynamics work because it links training-time capability emergence to readable representation structure, with implications for analyzing and predicting model behavior during pretraining.
- filter_reason: Strong fit for representation analysis and internal dynamics of capability emergence during pretraining.
- hugging_face_paper: https://huggingface.co/papers/2604.08510
- original_paper: https://arxiv.org/abs/2604.08510
- source_basis: `original abstract page`

## Key Points

- Introduces the Implicit Curriculum Hypothesis: pretraining is not just monotonic loss reduction but an ordered emergence of skills.
- Measures emergence points for simple and compositional tasks spanning retrieval, morphology, coreference, logical reasoning, and math across four model families from 410M to 13B parameters.
- Finds highly consistent emergence orderings across models and data mixtures, with correlation rho = 0.81 across 45 model pairs.
- Reports that composite tasks usually appear after their component tasks, supporting a compositional progression of capability acquisition.
- Shows that function-vector-style representations are predictive of training trajectories, allowing held-out compositional task trajectories to be estimated with R^2 = 0.68 to 0.84 without evaluating them directly.
- Suggests that internal model representations encode information about what skills emerge when during pretraining.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08510
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08510
- arXiv abstract: https://arxiv.org/abs/2604.08510
- GitHub: https://github.com/KaiserWhoLearns/ElementalTask

## Paper Metadata

- authors: `Emmy Liu`, `Kaiser Sun`, `Millicent Li`, `Isabelle Lee`, `Lindia Tjuatja`, `Jen-tse Huang`, `Graham Neubig`
- ai_keywords: `large language models`, `pretraining`, `scaling laws`, `implicit curriculum hypothesis`, `compositional tasks`, `emergence points`, `model representations`, `function vector representations`, `training trajectories`
- upvotes: `1`
- num_comments: `1`
- abstract: Large language models (LLMs) can perform remarkably complex tasks, yet the fine-grained details of how these capabilities emerge during pretraining remain poorly understood. Scaling laws on validation loss tell us how much a model improves with additional compute, but not what skills it acquires in which order. To remedy this, we propose the Implicit Curriculum Hypothesis: pretraining follows a compositional and predictable curriculum across models and data mixtures. We test this by designing a suite of simple, composable tasks spanning retrieval, morphological transformations, coreference, logical reasoning, and mathematics. Using these tasks, we track emergence points across four model families spanning sizes from 410M-13B parameters. We find that emergence orderings of when models reach fixed accuracy thresholds are strikingly consistent (ρ= .81 across 45 model pairs), and that composite tasks most often emerge after their component tasks. Furthermore, we find that this structure is encoded in model representations: tasks with similar function vector representations also tend to follow similar trajectories in training. By using the space of representations derived from our task set, we can effectively predict the training trajectories of simple held-out compositional tasks throughout the course of pretraining (R^2 = .68-.84 across models) without previously evaluating them. Together, these results suggest that pretraining is more structured than loss curves reveal: skills emerge in a compositional order that is consistent across models and readable from their internals.
- hf_ai_summary: Pretraining follows a structured, compositional curriculum where model capabilities emerge consistently across different architectures and can be predicted from internal representations.

## Source Excerpt

Large language models (LLMs) can perform remarkably complex tasks, yet the fine-grained details of how these capabilities emerge during pretraining remain poorly understood. Scaling laws on validation loss tell us how much a model improves with additional compute, but not what skills it acquires in which order. To remedy this, we propose the Implicit Curriculum Hypothesis: pretraining follows a compositional and predictable curriculum across models and data mixtures. We test this by designing a suite of simple, composable tasks spanning retrieval, morphological transformations, coreference, logical reasoning, and mathematics. Using these tasks, we track emergence points across four model families spanning sizes from 410M-13B parameters. We find that emergence orderings of when models reach fixed accuracy thresholds are strikingly consistent ($\rho = .81$ across 45 model pairs), and that composite tasks most often emerge after their component tasks. Furthermore, we find that this structure is encoded in model representations: tasks with similar function vector representations also tend to follow similar trajectories in training. By using the space of representations derived from our task set, we can effectively predict the training trajectories of simple held-out compositional tasks throughout the course of pretraining ($R^2 = .68$-$.84$ across models) without previously evaluating them. Together, these results suggest that pretraining is more structured than loss curves reveal: skills emerge in a compositional order that is consistent across models and readable from their internals.

## Open Questions

- How robust are the emergence orderings to different training datasets, optimization settings, or task definitions?
- What exactly are the function vector representations used, and how interpretable are they mechanistically?
- Do the predictive relationships hold for larger frontier models or only for the model families studied here?
- How early in training can the held-out task trajectories be predicted reliably?
