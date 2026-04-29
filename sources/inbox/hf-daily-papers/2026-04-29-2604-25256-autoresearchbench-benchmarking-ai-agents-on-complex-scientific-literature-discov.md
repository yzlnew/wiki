---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, benchmark, scientific-research, literature-discovery, web-browsing]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.25256
paper_id: 2604.25256
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-04-29T12:35:39+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery

## Summary

- one_sentence_summary: AutoResearchBench is a benchmark for autonomous scientific literature discovery that tests AI agents on deep paper-tracking and wide paper-collection tasks, and finds that strong LLM agents still perform poorly.
- why_relevant: It is directly relevant to agents and tool-using systems because it evaluates autonomous research behavior, and it is adjacent to post-training only insofar as it provides a demanding benchmark for agent capability rather than a training method.
- filter_reason: A strong agent-evaluation benchmark for autonomous scientific literature discovery, directly relevant to agent architectures and evaluation.
- hugging_face_paper: https://huggingface.co/papers/2604.25256
- original_paper: https://arxiv.org/abs/2604.25256
- source_basis: `original abstract page`

## Key Points

- Introduces two task types: Deep Research, which tracks down a specific target paper through multi-step probing, and Wide Research, which collects all papers matching given conditions.
- The benchmark is designed around scientific literature discovery rather than generic web browsing, so tasks require understanding scientific concepts and fine-grained details in papers.
- The authors frame the tasks as open-ended and search-intensive, because the number of valid papers may be unknown and deliberate reasoning is needed throughout.
- Reported results are low even for strong models: 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research for the best LLMs mentioned, with many baselines below 5%.
- The paper releases the dataset, evaluation pipeline, and code for follow-up work on autonomous research agents.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25256
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25256
- arXiv abstract: https://arxiv.org/abs/2604.25256
- GitHub: https://github.com/CherYou/AutoResearchBench
- Project page: https://cheryou.github.io/autoresearchbench.github.io/

## Paper Metadata

- authors: `Lei Xiong`, `Kun Luo`, `Ziyi Xia`, `Wenbo Zhang`, `Jin-Ge Yao`, `Zheng Liu`, `Jingying Shao`, `Jianlyu Chen`, `Hongjin Qian`, `Xi Yang`, `Qian Yu`, `Hao Li`, `Chen Yue`, `Xiaan Du`, `Yuyang Wang`, `Yesheng Liu`, `Haiyu Xu`, `Zhicheng Dou`
- organization: `Beijing Academy of Artificial Intelligence`
- ai_keywords: `autonomous scientific research`, `AI agents`, `scientific literature discovery`, `AutoResearchBench`, `Deep Research`, `Wide Research`, `agentic web browsing`, `LLMs`, `benchmark evaluation`
- upvotes: `21`
- num_comments: `1`
- abstract: Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a research problem, or to acquire evidence for verifying assumptions and supporting claims. To assess AI agents' capability in driving this process, we present AutoResearchBench, a dedicated benchmark for autonomous scientific literature discovery. AutoResearchBench consists of two complementary task types: (1) Deep Research, which requires tracking down a specific target paper through a progressive, multi-step probing process, and (2) Wide Research, which requires comprehensively collecting a set of papers satisfying given conditions. Compared to previous benchmarks on agentic web browsing, AutoResearchBench is distinguished along three dimensions: it is research-oriented, calling for in-depth comprehension of scientific concepts; literature-focused, demanding fine-grained utilization of detailed information; and open-ended, involving an unknown number of qualified papers and thus requiring deliberate reasoning and search throughout. These properties make AutoResearchBench uniquely suited for evaluating autonomous research capabilities, and extraordinarily challenging. Even the most powerful LLMs, despite having largely conquered general agentic web-browsing benchmarks such as BrowseComp, achieve only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, while many other strong baselines fall below 5%. We publicly release the dataset and evaluation pipeline to facilitate future research in this direction. We publicly release the dataset, evaluation pipeline, and code at https://github.com/CherYou/AutoResearchBench.
- hf_ai_summary: AutoResearchBench is a benchmark for autonomous scientific literature discovery that evaluates AI agents' ability to conduct deep and wide research tasks with high difficulty, achieving low accuracy rates even among powerful LLMs.

## Source Excerpt

Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a research problem, or to acquire evidence for verifying assumptions and supporting claims. To assess AI agents' capability in driving this process, we present AutoResearchBench, a dedicated benchmark for autonomous scientific literature discovery. AutoResearchBench consists of two complementary task types: (1) Deep Research, which requires tracking down a specific target paper through a progressive, multi-step probing process, and (2) Wide Research, which requires comprehensively collecting a set of papers satisfying given conditions. Compared to previous benchmarks on agentic web browsing, AutoResearchBench is distinguished along three dimensions: it is research-oriented, calling for in-depth comprehension of scientific concepts; literature-focused, demanding fine-grained utilization of detailed information; and open-ended, involving an unknown number of qualified papers and thus requiring deliberate reasoning and search throughout. These properties make AutoResearchBench uniquely suited for evaluating autonomous research capabilities, and extraordinarily challenging. Even the most powerful LLMs, despite having largely conquered general agentic web-browsing benchmarks such as BrowseComp, achieve only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, while many other strong baselines fall below 5%. We publicly release the dataset and evaluation pipeline to facilitate future research in this direction. We publicly release the dataset, evaluation pipeline, and code at this https URL .

## Open Questions

- What specific agentic search strategies or tools are used in the benchmark evaluations?
- How are Deep Research and Wide Research scored in detail beyond the reported accuracy and IoU numbers?
- What paper conditions define a valid match in Wide Research?
- Which model families were compared, and how much performance varied across them?
