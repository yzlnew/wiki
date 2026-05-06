---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, reasoning, environment-interaction, gui-agents, benchmark, cross-application, desktop-automation, evaluation]
source_count: 1
updated: 2026-05-06
source_url: https://arxiv.org/abs/2604.27776
paper_id: 2604.27776
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-06T07:41:57+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments

## Summary

- one_sentence_summary: WindowsWorld is a cross-application GUI-agent benchmark for professional desktop workflows, built from 181 simulated tasks across 17 apps and showing that current computer-use agents struggle badly on multi-app reasoning and execution.
- why_relevant: It is directly relevant to agent evaluation and tool-using systems because it measures how well GUI agents handle realistic multi-application workflows, coordination, and execution efficiency.
- filter_reason: A strong GUI-agent benchmark for cross-application workflows with concrete evaluation of agent failures and multi-step reasoning.
- hugging_face_paper: https://huggingface.co/papers/2604.27776
- original_paper: https://arxiv.org/abs/2604.27776
- source_basis: `original abstract page`

## Key Points

- The benchmark targets a gap in existing GUI-agent evaluation: most prior benchmarks emphasize isolated, single-application tasks rather than coordinated cross-application workflows.
- Tasks were generated with a multi-agent framework guided by 16 occupations, then refined by human review and run in a simulated environment.
- WindowsWorld contains 181 tasks with an average of 5.0 sub-goals each, spanning 17 common desktop applications; 78% of tasks are inherently multi-application.
- Reported results show leading agents and large models perform poorly on multi-application tasks, with success rates below 21%, much worse than on single-app tasks.
- Failures are especially common when tasks require conditional judgment and reasoning across three or more applications, and many attempts waste steps far beyond human limits.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27776
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27776
- arXiv abstract: https://arxiv.org/abs/2604.27776
- GitHub: https://github.com/HITsz-TMG/WindowsWorld

## Paper Metadata

- authors: `Jinchao Li`, `Yunxin Li`, `Chenrui Zhao`, `Zhenran Xu`, `Baotian Hu`, `Min Zhang`
- ai_keywords: `GUI agents`, `cross-application workflows`, `multi-agent framework`, `desktop applications`, `multi-step tasks`, `conditional judgment`, `reasoning`, `execution efficiency`, `simulated environment`
- upvotes: `2`
- num_comments: `2`
- abstract: While GUI agents have shown impressive capabilities in common computer-use tasks such as OSWorld, current benchmarks mainly focus on isolated and single-application tasks. This overlooks a critical real-world requirement of coordinating across multiple applications to accomplish complex profession-specific workflows. To bridge this gap, we present a computer-use benchmark in cross-application workflows, named WindowsWorld, designed to systematically assess GUI Agents on complex multi-step tasks that mirror real-world professional activities. Our methodology uses a multi-agent framework steered by 16 occupations to generate four difficulty-level tasks with intermediate inspection, which are then refined by human review and executed in a simulated environment. The resulting benchmark contains 181 tasks with an average of 5.0 sub-goals across 17 common desktop applications, of which 78% are inherently multi-application. Experimental results of leading large models and agents show that: 1) All computer-use agents perform poorly on multi-application tasks (< 21% success rate), far below the performance of simple single-app tasks; 2) They largely fail at tasks requiring conditional judgment and reasoning across geq 3 applications, stalling at early sub-goals; 3) Low execution efficiency, where tasks often fail despite far exceeding human step limits. Code, benchmark data, and evaluation resources are available at github.com/HITsz-TMG/WindowsWorld.
- hf_ai_summary: A cross-application workflow benchmark named WindowsWorld was developed to evaluate GUI agents on complex multi-step tasks requiring coordination across multiple software applications, revealing significant performance gaps in current agents when handling real-world professional workflows.

## Source Excerpt

While GUI agents have shown impressive capabilities in common computer-use tasks such as OSWorld, current benchmarks mainly focus on isolated and single-application tasks. This overlooks a critical real-world requirement of coordinating across multiple applications to accomplish complex profession-specific workflows. To bridge this gap, we present a computer-use benchmark in cross-application workflows, named WindowsWorld, designed to systematically assess GUI Agents on complex multi-step tasks that mirror real-world professional activities. Our methodology uses a multi-agent framework steered by 16 occupations to generate four difficulty-level tasks with intermediate inspection, which are then refined by human review and executed in a simulated environment. The resulting benchmark contains 181 tasks with an average of 5.0 sub-goals across 17 common desktop applications, of which 78% are inherently multi-application. Experimental results of leading large models and agents show that: 1) All computer-use agents perform poorly on multi-application tasks (< 21% success rate), far below the performance of simple single-app tasks; 2) They largely fail at tasks requiring conditional judgment and reasoning across $\geq$ 3 applications, stalling at early sub-goals; 3) Low execution efficiency, where tasks often fail despite far exceeding human step limits. Code, benchmark data, and evaluation resources are available at this http URL .

## Open Questions

- Which specific models and agents were evaluated, and how did their scores differ by task difficulty?
- How is success defined in the benchmark and what metrics are used beyond task completion rate?
- What does the simulated environment include, and how closely does it match real Windows desktop behavior?
- How were the 16 occupations chosen, and do they cover the most important professional workflows?
