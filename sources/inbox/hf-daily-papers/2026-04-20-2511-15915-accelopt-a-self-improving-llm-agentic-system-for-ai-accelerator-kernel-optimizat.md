---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, llm-systems, agent-architectures, benchmarks, kernel-optimization, benchmark, trainium, self-improvement]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2511.15915
paper_id: 2511.15915
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-20T11:45:34+08:00
decision: accept
score: 86
generator: scripts/update_hf_daily_papers.py
---

# AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization

## Summary

- one_sentence_summary: AccelOpt is a self-improving LLM agentic system that optimizes accelerator kernels by iteratively generating candidates and using an optimization memory of prior slow-fast kernel pairs to guide search.
- why_relevant: This is directly relevant to agentic systems and post-training-style self-improvement loops, with a concrete evaluation on tool-like optimization for accelerator kernels rather than language tasks.
- filter_reason: A technically detailed agentic LLM system with benchmarked self-improvement for kernel optimization, directly relevant to agents and LLM systems.
- hugging_face_paper: https://huggingface.co/papers/2511.15915
- original_paper: https://arxiv.org/abs/2511.15915
- source_basis: `original abstract page`

## Key Points

- The system targets kernel optimization for emerging AI accelerators and is designed to remove the need for expert-provided hardware-specific optimization knowledge.
- AccelOpt uses iterative generation plus an optimization memory that stores experiences and insights from previously observed slow-fast kernel pairs.
- The paper introduces NKIBench, a benchmark suite of AWS Trainium kernels with varying complexity extracted from real-world LLM workloads.
- On NKIBench, average peak throughput improved from 49% to 61% on Trainium 1 and from 45% to 59% on Trainium 2 as the system improved over time.
- Using open-source models, AccelOpt matched the kernel improvements of Claude Sonnet 4 while being 26x cheaper.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2511.15915
- Hugging Face API entry: https://huggingface.co/api/papers/2511.15915
- arXiv abstract: https://arxiv.org/abs/2511.15915
- GitHub: https://github.com/zhang677/AccelOpt
- Project page: https://ppl.stanford.edu/accelopt.html

## Paper Metadata

- authors: `Genghan Zhang`, `Shaowei Zhu`, `Anjiang Wei`, `Zhenyu Song`, `Allen Nie`, `Zhen Jia`, `Nandita Vijaykumar`, `Yida Wang`, `Kunle Olukotun`
- organization: `Stanford University`
- ai_keywords: `large language model`, `agentic system`, `kernel optimization`, `optimization memory`, `AWS Trainium accelerator`, `NKIBench`, `throughput improvement`, `cost-effectiveness`
- upvotes: `2`
- num_comments: `2`
- abstract: We present AccelOpt, a self-improving large language model (LLM) agentic system that autonomously optimizes kernels for emerging AI acclerators, eliminating the need for expert-provided hardware-specific optimization knowledge. AccelOpt explores the kernel optimization space through iterative generation, informed by an optimization memory that curates experiences and insights from previously encountered slow-fast kernel pairs. We build NKIBench, a new benchmark suite of AWS Trainium accelerator kernels with varying complexity extracted from real-world LLM workloads to evaluate the effectiveness of AccelOpt. Our evaluation confirms that AccelOpt's capability improves over time, boosting the average percentage of peak throughput from 49% to 61% on Trainium 1 and from 45% to 59% on Trainium 2 for NKIBench kernels. Moreover, AccelOpt is highly cost-effective: using open-source models, it matches the kernel improvements of Claude Sonnet 4 while being 26times cheaper. The code is open-sourced at https://github.com/zhang677/AccelOpt.
- hf_ai_summary: AccelOpt is a self-improving LLM agentic system that autonomously optimizes kernels for AI accelerators using iterative generation and optimization memory, achieving significant throughput improvements at reduced costs.

## Source Excerpt

We present AccelOpt, a self-improving large language model (LLM) agentic system that autonomously optimizes kernels for emerging AI acclerators, eliminating the need for expert-provided hardware-specific optimization knowledge. AccelOpt explores the kernel optimization space through iterative generation, informed by an optimization memory that curates experiences and insights from previously encountered slow-fast kernel pairs. We build NKIBench, a new benchmark suite of AWS Trainium accelerator kernels with varying complexity extracted from real-world LLM workloads to evaluate the effectiveness of AccelOpt. Our evaluation confirms that AccelOpt's capability improves over time, boosting the average percentage of peak throughput from $49\%$ to $61\%$ on Trainium 1 and from $45\%$ to $59\%$ on Trainium 2 for NKIBench kernels. Moreover, AccelOpt is highly cost-effective: using open-source models, it matches the kernel improvements of Claude Sonnet 4 while being $26\times$ cheaper. The code is open-sourced at this https URL .

## Open Questions

- What model and prompting/setup details are used for the iterative kernel generation loop?
- How is the optimization memory represented and updated across runs?
- How much of the improvement comes from memory versus repeated search alone?
- What exact kernels and task splits are included in NKIBench?
- How does performance vary across individual kernels and not just the averages reported?
