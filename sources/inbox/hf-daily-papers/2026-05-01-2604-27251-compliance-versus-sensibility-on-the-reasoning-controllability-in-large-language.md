---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, representation-analysis, reasoning-behavior-shaping, alignment, llm-systems, llm, reasoning, controllability, probes, instruction-following]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.27251
paper_id: 2604.27251
published: 2026-04-29T04:00:00+08:00
submitted_on_daily: 2026-05-01T16:26:41+08:00
decision: accept
score: 86
generator: scripts/update_hf_daily_papers.py
---

# Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models

## Summary

- one_sentence_summary: This paper studies reasoning controllability in LLMs by inducing conflicts between explicit logical schemata and task-appropriate reasoning, showing that models often favor sensibility over compliance but can be steered toward instruction following with activation-level interventions.
- why_relevant: It connects directly to reasoning control, mechanistic interpretability, and post-training-style intervention by showing that internal representations of reasoning types can be probed and manipulated to change instruction following.
- filter_reason: Strong fit for mechanistic interpretability and reasoning controllability, with probing and activation-level interventions.
- hugging_face_paper: https://huggingface.co/papers/2604.27251
- original_paper: https://arxiv.org/abs/2604.27251
- source_basis: `original abstract page`

## Key Points

- The paper frames controllability as a reasoning-conflict problem: the model is instructed to use a logical schema that conflicts with the schema normally expected for the task.
- Across evaluations, LLMs tend to prioritize sensibility over compliance, meaning they often use task-appropriate reasoning even when instructed otherwise.
- Task accuracy is not determined solely by whether the model follows the conflicting schema; models can keep high accuracy while relying on internalized parametric memory, and this tendency increases with model size.
- Reasoning conflicts are detectable internally because confidence scores drop during conflicting episodes.
- Probing results suggest reasoning types are linearly encoded in middle-to-late layers, and mechanistic interventions can increase instruction following by up to 29%.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27251
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27251
- arXiv abstract: https://arxiv.org/abs/2604.27251
- GitHub: https://github.com/Xingwei-Tan/compliance_sensibility

## Paper Metadata

- authors: `Xingwei Tan`, `Marco Valentino`, `Mahmud Elahi Akhter`, `Yuxiang Zhou`, `Maria Liakata`, `Nikolaos Aletras`
- ai_keywords: `Chain-of-Thought`, `parametric memory`, `logical schemata`, `reasoning conflicts`, `instruction following`, `activation-level controllability`, `internalized parametric memory`
- upvotes: `5`
- num_comments: `1`
- abstract: Large Language Models (LLMs) are known to acquire reasoning capabilities through shared inference patterns in pre-training data, which are further elicited via Chain-of-Thought (CoT) practices. However, whether fundamental reasoning patterns, such as induction, deduction, and abduction, can be decoupled from specific problem instances remains a critical challenge for model controllability, and for shedding light on reasoning controllability. In this paper, we present the first systematic investigation of this problem through the lens of reasoning conflicts: an explicit tension between parametric and contextual information induced by mandating logical schemata that deviate from those expected for a target task. Our evaluation reveals that LLMs consistently prioritize sensibility over compliance, favoring task-appropriate reasoning patterns despite conflicting instructions. Notably, task accuracy is not strictly determined by sensibility, with models often maintaining high performance even when using conflicting patterns, suggesting a reliance on internalized parametric memory that increases with model size. We further demonstrate that reasoning conflicts are internally detectable, as confidence scores significantly drop during conflicting episodes. Probing experiments confirm that reasoning types are linearly encoded from middle-to-late layers, indicating the potential for activation-level controllability. Leveraging these insights, we steer models towards compliance, increasing instruction following by up to 29%. Overall, our findings establish that while LLM reasoning is anchored to concrete instances, active mechanistic interventions can effectively decouple logical schemata from data, offering a path toward improved controllability, faithfulness, and generalizability.
- hf_ai_summary: Large language models exhibit reasoning conflicts where they prioritize task-appropriate patterns over explicit instructions, but these can be mitigated through mechanistic interventions that improve instruction following.

## Source Excerpt

Large Language Models (LLMs) are known to acquire reasoning capabilities through shared inference patterns in pre-training data, which are further elicited via Chain-of-Thought (CoT) practices. However, whether fundamental reasoning patterns, such as induction, deduction, and abduction, can be decoupled from specific problem instances remains a critical challenge for model controllability, and for shedding light on reasoning controllability. In this paper, we present the first systematic investigation of this problem through the lens of reasoning conflicts: an explicit tension between parametric and contextual information induced by mandating logical schemata that deviate from those expected for a target task. Our evaluation reveals that LLMs consistently prioritize sensibility over compliance, favoring task-appropriate reasoning patterns despite conflicting instructions. Notably, task accuracy is not strictly determined by sensibility, with models often maintaining high performance even when using conflicting patterns, suggesting a reliance on internalized parametric memory that increases with model size. We further demonstrate that reasoning conflicts are internally detectable, as confidence scores significantly drop during conflicting episodes. Probing experiments confirm that reasoning types are linearly encoded from middle-to-late layers, indicating the potential for activation-level controllability. Leveraging these insights, we steer models towards compliance, increasing instruction following by up to 29%. Overall, our findings establish that while LLM reasoning is anchored to concrete instances, active mechanistic interventions can effectively decouple logical schemata from data, offering a path toward improved controllability, faithfulness, and generalizability.

## Open Questions

- Which model families and sizes were evaluated, and how broadly do the results generalize?
- What specific logical schemata were used to create reasoning conflicts for induction, deduction, and abduction?
- What intervention method produced the reported increase in instruction following, and how invasive is it?
- Does improved compliance preserve accuracy across tasks, or does it trade off against task performance?
