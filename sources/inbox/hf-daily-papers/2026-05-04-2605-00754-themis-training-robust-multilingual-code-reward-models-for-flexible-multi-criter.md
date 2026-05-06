---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reinforcement-learning, reward-modeling, llm-systems, code-generation, multilingual, multi-criteria, cross-lingual-transfer]
source_count: 1
updated: 2026-05-05
source_url: https://arxiv.org/abs/2605.00754
paper_id: 2605.00754
published: 2026-05-01T04:00:00+08:00
submitted_on_daily: 2026-05-04T08:30:58+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring

## Summary

- one_sentence_summary: Themis introduces multilingual code reward models and a large preference dataset to score code generation across multiple criteria, not just functional correctness.
- why_relevant: This is directly relevant to reward modeling and post-training because it extends code RMs beyond execution-only signals and studies how preference data, scaling, and multilingual transfer affect scoring quality.
- filter_reason: Directly on reward models and post-training, with concrete code-oriented evaluation and multilingual preference training.
- hugging_face_paper: https://huggingface.co/papers/2605.00754
- original_paper: https://arxiv.org/abs/2605.00754
- source_basis: `original abstract page`

## Key Points

- The paper argues that prior code reward model work has been too centered on execution feedback, which limits post-training to functional correctness on executable code.
- It introduces Themis-CodeRewardBench, a benchmark covering five preference dimensions across eight programming languages, and uses it to evaluate 50+ code, math, and general-purpose reward models.
- It releases Themis-CodePreference, described as the largest open-source code preference collection to date, with more than 350k preference pairs.
- It trains Themis-RM, a suite of multilingual code reward models ranging from 600M to 32B parameters for flexible multi-criteria scoring.
- Experiments and ablations report positive scaling trends, strong cross-lingual transfer from diverse preferences, and improved reliability from multi-criteria training.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.00754
- Hugging Face API entry: https://huggingface.co/api/papers/2605.00754
- arXiv abstract: https://arxiv.org/abs/2605.00754
- GitHub: https://github.com/iNeil77/Themis

## Paper Metadata

- authors: `Indraneil Paul`, `Glavaš Glavas`, `Iryna Gurevych`
- organization: `Themis`
- ai_keywords: `reward models`, `language models`, `code generation`, `functional correctness`, `multilingual`, `multi-criteria`, `preference dimensions`, `cross-lingual transfer`, `parameter-efficient fine-tuning`
- upvotes: `2`
- num_comments: `1`
- abstract: Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling. Research on the application of RMs in code generation, however, has been comparatively sparse, with existing work largely focusing on execution feedback. This choice constrains post-training to optimizing functional correctness over self-contained executable code. In this work, we examine the training and evaluation of multilingual, multi-criteria code RMs. To this end, we first compile Themis-CodeRewardBench, a benchmark to evaluate code RMs across five preference dimensions (i.e., criteria) and eight programming languages, on which we profile 50+ code, math, and general-purpose RMs. Observing the limited proficiency of current RMs beyond scoring for functional correctness, we develop Themis-CodePreference, the largest open-source collection of code preferences to date (more than 350k preference pairs), and use it to train Themis-RM, a suite of multilingual code reward models for flexible multi-criteria scoring, ranging in size from 600M to 32B parameters. Our experiments and ablations demonstrate positive scaling trends, strong cross-lingual transfer when training on diverse preferences, and the importance of multi-criteria training for reliable code reward modeling.
- hf_ai_summary: Researchers introduce Themis-RM, a suite of multilingual code reward models trained on a large preference dataset to enable flexible multi-criteria scoring for code generation tasks.

## Source Excerpt

Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling. Research on the application of RMs in code generation, however, has been comparatively sparse, with existing work largely focusing on execution feedback. This choice constrains post-training to optimizing functional correctness over self-contained executable code. In this work, we examine the training and evaluation of multilingual, multi-criteria code RMs. To this end, we first compile Themis-CodeRewardBench, a benchmark to evaluate code RMs across five preference dimensions (i.e., criteria) and eight programming languages, on which we profile 50+ code, math, and general-purpose RMs. Observing the limited proficiency of current RMs beyond scoring for functional correctness, we develop Themis-CodePreference, the largest open-source collection of code preferences to date (more than 350k preference pairs), and use it to train Themis-RM, a suite of multilingual code reward models for flexible multi-criteria scoring, ranging in size from 600M to 32B parameters. Our experiments and ablations demonstrate positive scaling trends, strong cross-lingual transfer when training on diverse preferences, and the importance of multi-criteria training for reliable code reward modeling.

## Open Questions

- What are the five preference dimensions used in Themis-CodeRewardBench?
- How is Themis-CodePreference constructed, and what sources or annotation process produced the 350k+ preference pairs?
- How much does performance vary across the eight programming languages and across model sizes?
- What specific ablation settings isolate the effect of multi-criteria training versus single-criterion training?
