---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, agent-architectures, llm-systems, benchmark, lifelong-learning, skills, tool-use, post-training]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.17308
paper_id: 2604.17308
published: 2026-04-19T04:00:00+08:00
submitted_on_daily: 2026-04-21T11:39:20+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents

## Summary

- one_sentence_summary: SkillFlow is a benchmark for lifelong skill discovery and evolution in autonomous agents, evaluating whether agents can discover, patch, transfer, and retain external skills across sequential tasks.
- why_relevant: This is directly relevant to agent systems and post-training because it benchmarks how autonomous agents learn, update, and reuse skills over time rather than only whether they can invoke tools once.
- filter_reason: A strong agents benchmark for lifelong skill discovery, patching, transfer, and evaluation under sequential interaction.
- hugging_face_paper: https://huggingface.co/papers/2604.17308
- original_paper: https://arxiv.org/abs/2604.17308
- source_basis: `original abstract page`

## Key Points

- It defines 166 tasks across 20 families using a Domain-Agnostic Execution Flow (DAEF) so tasks in each family share a consistent workflow.
- Agents are evaluated under an Agentic Lifelong Learning protocol: they start without skills, solve tasks sequentially, externalize lessons into skill patches, and carry the updated skill library forward.
- The benchmark targets gaps that standard skill-use benchmarks miss, especially whether agents can discover skills from experience, repair failed skills, and maintain a coherent skill library over time.
- Results show a substantial gap between skill usage and actual utility: Claude Opus 4.6 improves from 62.65% to 71.08% with lifelong skill evolution, while Kimi K2.5 shows only +0.60 points despite 66.87% skill usage.
- Qwen-Coder-Next still performs poorly at 44.58% task completion and regresses relative to the vanilla setting, indicating that skill-heavy setups can fail without real capability gains.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.17308
- Hugging Face API entry: https://huggingface.co/api/papers/2604.17308
- arXiv abstract: https://arxiv.org/abs/2604.17308
- GitHub: https://github.com/ZhangZi-a/SkillFlow
- Project page: https://zhangzi-a.github.io/SkillFlow-project-page/

## Paper Metadata

- authors: `Ziao Zhang`, `Kou Shi`, `Shiting Huang`, `Avery Nie`, `Yu Zeng`, `Yiming Zhao`, `Zhen Fang`, `Qishen Su`, `Haibo Qiu`, `Wei Yang`, `Qingnan Ren`, `Shun Zou`, `Wenxuan Huang`, `Lin Chen`, `Zehui Chen`, `Feng Zhao`
- ai_keywords: `autonomous agents`, `plug-and-play external skills`, `Domain-Agnostic Execution Flow`, `Agentic Lifelong Learning`, `skill discovery`, `skill patching`, `skill transfer`, `lifelong learning protocol`
- upvotes: `15`
- num_comments: `1`
- abstract: As the capability frontier of autonomous agents continues to expand, they are increasingly able to complete specialized tasks through plug-and-play external skills. Yet current benchmarks mostly test whether models can use provided skills, leaving open whether they can discover skills from experience, repair them after failure, and maintain a coherent library over time. We introduce SkillFlow, a benchmark of 166 tasks across 20 families in which task construction within each family follows a Domain-Agnostic Execution Flow (DAEF) that defines an agent workflow framework, allowing these tasks to share a consistent workflow. Agents are evaluated under an Agentic Lifelong Learning protocol in which they begin without skills, solve tasks sequentially within each family, externalize lessons through trajectory- and rubric-driven skill patches, and carry the updated library forward. Experiments reveal a substantial capability gap. For Claude Opus 4.6, lifelong skill evolution improves task success from 62.65% to 71.08% (+8.43 points). However, high skill usage does not necessarily imply high utility: Kimi K2.5 gains only +0.60 points despite 66.87% skill usage, while Qwen-Coder-Next reaches only a 44.58% task completion rate and still regresses relative to the vanilla setting. SkillFlow contributes a structured testbed for this direction and an in-depth empirical analysis of skill discovery, patching, transfer, and their failure modes under lifelong evaluation.
- hf_ai_summary: SkillFlow presents a benchmark for evaluating autonomous agents' ability to discover, repair, and maintain skills over time through a structured lifelong learning protocol.

## Source Excerpt

As the capability frontier of autonomous agents continues to expand, they are increasingly able to complete specialized tasks through plug-and-play external skills. Yet current benchmarks mostly test whether models can use provided skills, leaving open whether they can discover skills from experience, repair them after failure, and maintain a coherent library over time. We introduce SkillFlow, a benchmark of 166 tasks across 20 families in which task construction within each family follows a Domain-Agnostic Execution Flow (DAEF) that defines an agent workflow framework, allowing these tasks to share a consistent workflow. Agents are evaluated under an Agentic Lifelong Learning protocol in which they begin without skills, solve tasks sequentially within each family, externalize lessons through trajectory- and rubric-driven skill patches, and carry the updated library forward. Experiments reveal a substantial capability gap. For Claude Opus 4.6, lifelong skill evolution improves task success from 62.65% to 71.08% (+8.43 points). However, high skill usage does not necessarily imply high utility: Kimi K2.5 gains only +0.60 points despite 66.87% skill usage, while Qwen-Coder-Next reaches only a 44.58% task completion rate and still regresses relative to the vanilla setting. SkillFlow contributes a structured testbed for this direction and an in-depth empirical analysis of skill discovery, patching, transfer, and their failure modes under lifelong evaluation.

## Open Questions

- How are trajectory-driven skill patches generated and validated in practice?
- What rubric is used to decide whether a skill patch is correct or useful?
- Which task families are hardest for skill discovery versus skill transfer?
- What failure modes dominate when skill usage is high but utility is low?
