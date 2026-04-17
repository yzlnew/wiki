---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, tool-use, llm-systems, benchmark, web-eval]
source_count: 1
updated: 2026-04-12
source_url: https://arxiv.org/abs/2604.08523
paper_id: 2604.08523
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T18:26:02+08:00
decision: accept
score: 95
generator: scripts/update_hf_daily_papers.py
---

# ClawBench: Can AI Agents Complete Everyday Online Tasks?

## Summary

- one_sentence_summary: ClawBench is a real-world web-agent benchmark with 153 everyday online tasks across 144 live platforms, designed to test whether AI agents can reliably handle multi-step, document-heavy workflows on production websites.
- why_relevant: This is directly relevant to agent evaluation and tool-using systems because it measures how current frontier models perform on realistic web tasks that require planning, browser interaction, and form completion.
- filter_reason: A strong real-world agent evaluation benchmark with production web tasks, multi-step workflows, and clear methodological value.
- hugging_face_paper: https://huggingface.co/papers/2604.08523
- original_paper: https://arxiv.org/abs/2604.08523
- source_basis: `original abstract page`

## Key Points

- Covers 153 tasks across 15 categories and 144 live platforms, including purchases, appointments, and job applications.
- Targets capabilities beyond static benchmark pages: extracting information from user-provided documents, navigating multi-step workflows, and completing write-heavy forms accurately.
- Runs on production websites instead of offline sandboxes, preserving dynamic real-world interaction complexity.
- Uses a lightweight interception layer that blocks only the final submission request, enabling safe evaluation without real-world side effects.
- Evaluations of 7 frontier models show that both proprietary and open-source agents complete only a small fraction of tasks; Claude Sonnet 4.6 reaches 33.3%.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08523
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08523
- arXiv abstract: https://arxiv.org/abs/2604.08523
- GitHub: https://github.com/reacher-z/ClawBench
- Project page: https://claw-bench.com

## Paper Metadata

- authors: `Yuxuan Zhang`, `Yubo Wang`, `Yipeng Zhu`, `Penghui Du`, `Junwen Miao`, `Xuan Lu`, `Wendong Xu`, `Yunzhuo Hao`, `Songcheng Cai`, `Xiaochen Wang`, `Huaisong Zhang`, `Xian Wu`, `Yi Lu`, `Minyi Lei`, `Kai Zou`, `Huifeng Yin`, `Ping Nie`, `Liang Chen`, `Dongfu Jiang`, `Wenhu Chen`, `Kelsey R. Allen`
- organization: `Natural and Artificial Intelligence Lab`
- ai_keywords: `AI agents`, `evaluation framework`, `online tasks`, `real-world web interaction`, `multi-step workflows`, `document processing`
- upvotes: `122`
- num_comments: `5`
- abstract: AI agents may be able to automate your inbox, but can they automate other routine aspects of your life? Everyday online tasks offer a realistic yet unsolved testbed for evaluating the next generation of AI agents. To this end, we introduce ClawBench, an evaluation framework of 153 simple tasks that people need to accomplish regularly in their lives and work, spanning 144 live platforms across 15 categories, from completing purchases and booking appointments to submitting job applications. These tasks require demanding capabilities beyond existing benchmarks, such as obtaining relevant information from user-provided documents, navigating multi-step workflows across diverse platforms, and write-heavy operations like filling in many detailed forms correctly. Unlike existing benchmarks that evaluate agents in offline sandboxes with static pages, ClawBench operates on production websites, preserving the full complexity, dynamic nature, and challenges of real-world web interaction. A lightweight interception layer captures and blocks only the final submission request, ensuring safe evaluation without real-world side effects. Our evaluations of 7 frontier models show that both proprietary and open-source models can complete only a small portion of these tasks. For example, Claude Sonnet 4.6 achieves only 33.3%. Progress on ClawBench brings us closer to AI agents that can function as reliable general-purpose assistants.
- hf_ai_summary: ClawBench presents a comprehensive evaluation framework with 153 real-world tasks across 144 platforms to test AI agents' ability to automate everyday online activities requiring complex multi-step workflows and document processing.

## Source Excerpt

AI agents may be able to automate your inbox, but can they automate other routine aspects of your life? Everyday online tasks offer a realistic yet unsolved testbed for evaluating the next generation of AI agents. To this end, we introduce ClawBench, an evaluation framework of 153 simple tasks that people need to accomplish regularly in their lives and work, spanning 144 live platforms across 15 categories, from completing purchases and booking appointments to submitting job applications. These tasks require demanding capabilities beyond existing benchmarks, such as obtaining relevant information from user-provided documents, navigating multi-step workflows across diverse platforms, and write-heavy operations like filling in many detailed forms correctly. Unlike existing benchmarks that evaluate agents in offline sandboxes with static pages, ClawBench operates on production websites, preserving the full complexity, dynamic nature, and challenges of real-world web interaction. A lightweight interception layer captures and blocks only the final submission request, ensuring safe evaluation without real-world side effects. Our evaluations of 7 frontier models show that both proprietary and open-source models can complete only a small portion of these tasks. For example, Claude Sonnet 4.6 achieves only 33.3%. Progress on ClawBench brings us closer to AI agents that can function as reliable general-purpose assistants.

## Open Questions

- What scoring metric is used to define task success across the 153 tasks?
- How are the 15 task categories distributed, and which categories are hardest?
- What kinds of failures dominate agent performance on ClawBench: planning, navigation, document reading, or form entry?
- Which of the 7 evaluated models were the strongest open-source systems, and how large was the gap to proprietary models?
