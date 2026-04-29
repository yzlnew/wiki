---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, evaluation, benchmark, data-visualization, tool-use]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.25914
paper_id: 2604.25914
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-04-29T08:39:07+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

## Summary

- one_sentence_summary: DV-World is a 260-task benchmark for evaluating real-world data visualization agents across spreadsheet manipulation, artifact adaptation, and user-simulator interaction, with a hybrid evaluation scheme for both numerical accuracy and semantic-visual quality.
- why_relevant: It is directly relevant to agentic tool use and evaluation, especially for systems that must operate in realistic environments, handle multi-step workflows, and align with imperfect user intent rather than solve isolated tasks.
- filter_reason: A strong agent-evaluation benchmark for real-world environment interaction and task alignment in a practical workflow domain.
- hugging_face_paper: https://huggingface.co/papers/2604.25914
- original_paper: https://arxiv.org/abs/2604.25914
- source_basis: `original abstract page`

## Key Points

- Covers three task families: DV-Sheet for native spreadsheet work including chart/dashboard creation and repair, DV-Evolution for adapting reference visual artifacts to new data, and DV-Interact for aligning with ambiguous user intent via a simulator.
- Targets gaps in prior benchmarks that rely on code-sandbox settings, single-language creation tasks, or perfect-intent assumptions.
- Uses a hybrid evaluation framework combining Table-value Alignment for numerical precision and MLLM-as-a-Judge with rubrics for semantic-visual assessment.
- Reports that state-of-the-art models achieve under 50% overall performance, suggesting substantial weakness on realistic visualization workflows.
- Positions the benchmark as a testbed for enterprise-oriented DV agent development across a more realistic professional lifecycle.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25914
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25914
- arXiv abstract: https://arxiv.org/abs/2604.25914
- Project page: https://dv-world-project.github.io/

## Paper Metadata

- authors: `Jinxiang Meng`, `Shaoping Huang`, `Fangyu Lei`, `Jingyu Guo`, `Haoxiang Liu`, `Jiahao Su`, `Sihan Wang`, `Yao Wang`, `Enrui Wang`, `Ye Yang`, `Hongze Chai`, `Jinming Lv`, `Anbang Yu`, `Huangjing Zhang`, `Yitong Zhang`, `Yiming Huang`, `Zeyao Ma`, `Shizhu He`, `Jun Zhao`, `Kang Liu`
- upvotes: `32`
- num_comments: `1`
- abstract: Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinement, single-language creation-only tasks, and assumption of perfect intent. To bridge these gaps, we introduce DV-World, a benchmark of 260 tasks designed to evaluate DV agents across real-world professional lifecycles. DV-World spans three domains: DV-Sheet for native spreadsheet manipulation including chart and dashboard creation as well as diagnostic repair; DV-Evolution for adapting and restructuring reference visual artifacts to fit new data across diverse programming paradigms and DV-Interact for proactive intent alignment with a user simulator that mimics real-world ambiguous requirements. Our hybrid evaluation framework integrates Table-value Alignment for numerical precision and MLLM-as-a-Judge with rubrics for semantic-visual assessment. Experiments reveal that state-of-the-art models achieve less than 50% overall performance, exposing critical deficits in handling the complex challenges of real-world data visualization. DV-World provides a realistic testbed to steer development toward the versatile expertise required in enterprise workflows. Our data and code are available at https://github.com/DA-Open/DV-World{this project page}.

## Source Excerpt

Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinement, single-language creation-only tasks, and assumption of perfect intent. To bridge these gaps, we introduce DV-World, a benchmark of 260 tasks designed to evaluate DV agents across real-world professional lifecycles. DV-World spans three domains: DV-Sheet for native spreadsheet manipulation including chart and dashboard creation as well as diagnostic repair; DV-Evolution for adapting and restructuring reference visual artifacts to fit new data across diverse programming paradigms and DV-Interact for proactive intent alignment with a user simulator that mimics real-world ambiguous requirements. Our hybrid evaluation framework integrates Table-value Alignment for numerical precision and MLLM-as-a-Judge with rubrics for semantic-visual assessment. Experiments reveal that state-of-the-art models achieve less than 50% overall performance, exposing critical deficits in handling the complex challenges of real-world data visualization. DV-World provides a realistic testbed to steer development toward the versatile expertise required in enterprise workflows. Our data and code are available at \href{ this https URL }{this project page}.

## Open Questions

- Which specific models were evaluated, and how were they prompted or tool-enabled?
- How many tasks are in each of the three DV-World sub-benchmarks?
- What exact criteria and scoring thresholds are used in Table-value Alignment and the MLLM-as-a-Judge rubric?
- How much does performance vary across spreadsheet, adaptation, and interaction settings?
