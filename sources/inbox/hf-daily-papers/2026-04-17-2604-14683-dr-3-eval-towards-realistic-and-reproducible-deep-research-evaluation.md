---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, tool-use, deep-research, agent-eval, benchmark, multimodal, report-generation, retrieval, hallucination]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14683
paper_id: 2604.14683
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T08:41:09+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation

## Summary

- one_sentence_summary: DR^{3}-Eval is a realistic, reproducible benchmark for deep research agents that evaluates multimodal, multi-file report generation with a static sandbox corpus and a multi-dimensional scoring framework.
- why_relevant: It is directly relevant to agents and tool-using systems because it benchmarks deep research workflows and surfaces retrieval and hallucination failures in multi-agent LLM systems.
- filter_reason: Strong fit for agent evaluation: it introduces a reproducible benchmark and metrics for deep research agents.
- hugging_face_paper: https://huggingface.co/papers/2604.14683
- original_paper: https://arxiv.org/abs/2604.14683
- source_basis: `original abstract page`

## Key Points

- Built for deep research agents that must handle planning, retrieval, multimodal understanding, and report generation over long-horizon tasks.
- Uses authentic user-provided materials plus a per-task static research sandbox corpus with supportive documents, distractors, and noise to simulate open-web complexity while staying verifiable.
- Introduces a multi-dimensional evaluation scheme covering Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality.
- Reports that the benchmark is challenging and exposes failure modes in retrieval robustness and hallucination control when tested with a multi-agent system using state-of-the-art language models.
- Claims alignment between the automated evaluation framework and human judgments, and states that code and data are publicly available.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14683
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14683
- arXiv abstract: https://arxiv.org/abs/2604.14683
- GitHub: https://github.com/NJU-LINK/DR3-Eval

## Paper Metadata

- authors: `Qianqian Xie`, `Qingheng Xiong`, `He Zhu`, `Tiantian Xia`, `Xueming Han`, `Fanyu Meng`, `Jiakai Wang`, `Zhiqi Bai`, `Chengkang Jiang`, `Zhaohui Wang`, `Yubin Guo`, `Yuqing Wen`, `Jiayang Mao`, `Zijie Zhang`, `Shihao Li`, `Yanghai Wang`, `Yuxiang Ren`, `Junlan Feng`, `Jiaheng Liu`
- ai_keywords: `deep research agents`, `multimodal understanding`, `report generation`, `research sandbox corpus`, `multi-dimensional evaluation framework`, `information recall`, `factual accuracy`, `citation coverage`, `instruction following`, `depth quality`, `hallucination control`, `multi-agent system`, `state-of-the-art language models`
- upvotes: `26`
- num_comments: `2`
- abstract: Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR^{3}-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR^{3}-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR^{3}-Agent based on multiple state-of-the-art language models demonstrate that DR^{3}-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.
- hf_ai_summary: DR$^{3}$-Eval is a benchmark for evaluating deep research agents on multimodal, multi-file report generation, featuring a realistic simulation of web environments and a comprehensive evaluation framework.

## Source Excerpt

Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

## Open Questions

- How large is the benchmark, and what kinds of tasks or domains does it cover beyond multimodal report generation?
- How is the static research sandbox corpus constructed and how are supportive documents, distractors, and noise balanced per task?
- What models or agent configurations were used in DR^{3}-Agent, and how strong were the results on each evaluation dimension?
- How is alignment with human judgments measured, and where does the automated framework diverge from human scoring?
