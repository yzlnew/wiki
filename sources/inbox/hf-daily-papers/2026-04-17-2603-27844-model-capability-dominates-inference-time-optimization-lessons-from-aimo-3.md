---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reasoning-behavior-shaping, llm-systems, agent-evals, inference-time-optimization, majority-vote, math-reasoning, model-capability, prompt-engineering, selection-loss]
source_count: 1
updated: 2026-04-18
source_url: https://arxiv.org/abs/2603.27844
paper_id: 2603.27844
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T11:38:23+08:00
decision: accept
score: 79
generator: scripts/update_hf_daily_papers.py
---

# Model Capability Dominates: Inference-Time Optimization Lessons from AIMO 3

## Summary

- one_sentence_summary: The paper reports that, on the AIMO 3 math benchmark, prompt-level diversity and other inference-time prompt interventions did not improve majority-vote performance, while base model capability dominated outcomes and the remaining gap was mainly due to selection loss.
- why_relevant: It is directly relevant to inference-time optimization for reasoning systems and shows a clear limit of prompt engineering versus model capability, with implications for post-training and tool-free selection methods.
- filter_reason: AIMO-style inference-time optimization and verifier-based selection are directly relevant to reasoning behavior shaping and evaluation.
- hugging_face_paper: https://huggingface.co/papers/2603.27844
- original_paper: https://arxiv.org/abs/2603.27844
- source_basis: `original abstract page`

## Key Points

- Majority voting helps mathematical reasoning, but correlated errors reduce the effective sample size.
- The authors test a prompt-diversity approach called Diverse Prompt Mixer on AIMO 3 with 3 models, 23+ experiments, 50 IMO-level problems, and a 5-hour H100 budget.
- Every prompt-level intervention fails in this setup; higher-temperature sampling already provides much of the useful error decorrelation.
- Weaker reasoning strategies tend to hurt accuracy more than they reduce correlation, so diversity alone does not recover performance.
- The best majority-vote score is 42/50 versus pass@20 of about 45.5, which the paper attributes to selection loss rather than prompt loss; a verifier-based selector is proposed as a possible fix.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2603.27844
- Hugging Face API entry: https://huggingface.co/api/papers/2603.27844
- arXiv abstract: https://arxiv.org/abs/2603.27844
- GitHub: https://github.com/nat-nischw/model-capability-dominates-lessons-aimo3
- Project page: https://www.kaggle.com/code/natnitarach/aimo-3-model-capability-dominate

## Paper Metadata

- authors: `Natapong Nitarach`
- ai_keywords: `majority voting`, `mathematical reasoning`, `correlated errors`, `reasoning strategies`, `Diverse Prompt Mixer`, `AIMO 3 competition`, `high-temperature sampling`, `model capability`, `selection loss`, `verifier-based selector`
- upvotes: `1`
- num_comments: `1`
- abstract: Majority voting over multiple LLM attempts improves mathematical reasoning, but correlated errors limit the effective sample size. A natural fix is to assign different reasoning strategies to different voters. The approach, Diverse Prompt Mixer, is tested on the AIMO 3 competition: 3 models, 23+ experiments, 50 IMO-level problems, one H100 80 GB, 5-hour limit. Every prompt-level intervention fails. High-temperature sampling already decorrelates errors; weaker strategies reduce accuracy more than they reduce correlation. Across an 8-point capability gap at equal N=8 and every optimization tested, model capability dominates. The gap between the best majority-vote score (42/50) and pass@20 (~45.5) is selection loss, not prompt loss. A verifier-based selector could close it. Prompt engineering cannot.
- hf_ai_summary: Majority voting improves mathematical reasoning but is limited by correlated errors; diverse reasoning strategies and model capability are more impactful than prompt engineering.

## Source Excerpt

Majority voting over multiple LLM attempts improves mathematical reasoning, but correlated errors limit the effective sample size. A natural fix is to assign different reasoning strategies to different voters. The approach, Diverse Prompt Mixer, is tested on the AIMO 3 competition: 3 models, 23+ experiments, 50 IMO-level problems, one H100 80 GB, 5-hour limit. Every prompt-level intervention fails. High-temperature sampling already decorrelates errors; weaker strategies reduce accuracy more than they reduce correlation. Across an 8-point capability gap at equal N=8 and every optimization tested, model capability dominates. The gap between the best majority-vote score (42/50) and pass@20 (~45.5) is selection loss, not prompt loss. A verifier-based selector could close it. Prompt engineering cannot.

## Open Questions

- What exact prompt-level interventions were tested, and how much did each change accuracy versus correlation?
- How was the pass@20 estimate computed, and on which models?
- What verifier-based selector is proposed, and would it generalize beyond this competition setting?
- Does the reported 8-point capability gap refer to a specific metric or model pair?
- Would similar conclusions hold on non-math or less competition-style tasks?
