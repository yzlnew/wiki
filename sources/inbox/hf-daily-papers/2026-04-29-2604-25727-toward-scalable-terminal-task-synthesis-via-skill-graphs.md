---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, environment-interaction, post-training, terminal-agents, task-synthesis, skill-graphs]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.25727
paper_id: 2604.25727
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-04-29T08:45:15+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Toward Scalable Terminal Task Synthesis via Skill Graphs

## Summary

- one_sentence_summary: SkillSynth is an automated terminal-task synthesis framework that uses a scenario-mediated skill graph to generate executable tasks with more explicit control over the diversity of execution trajectories used for training terminal agents.
- why_relevant: This is directly relevant to agents, environment interaction, and post-training because it proposes a scalable task-synthesis method for training terminal agents with better trajectory diversity.
- filter_reason: Directly targets terminal agents, trajectory synthesis, and benchmark-driven training for agentic system improvement.
- hugging_face_paper: https://huggingface.co/papers/2604.25727
- original_paper: https://arxiv.org/abs/2604.25727
- source_basis: `original abstract page`

## Key Points

- It addresses a training bottleneck for terminal agents: the lack of high-quality and diverse execution trajectories.
- SkillSynth builds a large-scale skill graph in which scenarios act as intermediate transition nodes connecting command-line skills.
- It samples workflow paths from the graph as abstractions of real-world terminal workflows, then uses a multi-agent harness to turn those paths into executable task instances.
- The core design goal is to control the diversity of the minimal trajectories agents must take to solve the synthesized tasks, rather than only increasing task count.
- The paper reports experiments on Terminal-Bench and says SkillSynth-generated tasks were used to train Hy3 Preview, improving its agentic terminal performance.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25727
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25727
- arXiv abstract: https://arxiv.org/abs/2604.25727

## Paper Metadata

- authors: `Zhiyuan Fan`, `Tinghao Yu`, `Yuanjun Cai`, `Jiangtao Guan`, `Yun Yang`, `Dingxin Hu`, `Jiang Zhou`, `Xing Wu`, `Zhuo Han`, `Feng Zhang`, `Lilin Wang`
- organization: `Tencent Hunyuan`
- ai_keywords: `skill graph`, `scenario-mediated`, `terminal task synthesis`, `execution trajectories`, `multi-agent harness`, `workflow paths`, `terminal-based settings`
- upvotes: `5`
- num_comments: `0`
- abstract: Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality and diverse execution trajectories. Existing approaches mitigate this bottleneck by synthesizing large-scale terminal task instances for trajectory sampling. However, they primarily focus on scaling the number of tasks while providing limited control over the diversity of execution trajectories that agents actually experience during training. In this paper, we present SkillSynth, an automated framework for terminal task synthesis built on a scenario-mediated skill graph. SkillSynth first constructs a large-scale skill graph, where scenarios serve as intermediate transition nodes that connect diverse command-line skills. It then samples paths from this graph as abstractions of real-world workflows, and uses a multi-agent harness to instantiate them into executable task instances. By grounding task synthesis in graph-sampled workflow paths, SkillSynth explicitly controls the diversity of minimal execution trajectories required to solve the synthesized tasks. Experiments on Terminal-Bench demonstrate the effectiveness of SkillSynth. Moreover, task instances synthesized by SkillSynth have been adopted to train Hy3 Preview, contributing to its enhanced agentic capabilities in terminal-based settings.
- hf_ai_summary: SkillSynth is an automated framework for terminal task synthesis that uses scenario-mediated skill graphs to control execution trajectory diversity during training.

## Source Excerpt

Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality and diverse execution trajectories. Existing approaches mitigate this bottleneck by synthesizing large-scale terminal task instances for trajectory sampling. However, they primarily focus on scaling the number of tasks while providing limited control over the diversity of execution trajectories that agents actually experience during training. In this paper, we present SkillSynth, an automated framework for terminal task synthesis built on a scenario-mediated skill graph. SkillSynth first constructs a large-scale skill graph, where scenarios serve as intermediate transition nodes that connect diverse command-line skills. It then samples paths from this graph as abstractions of real-world workflows, and uses a multi-agent harness to instantiate them into executable task instances. By grounding task synthesis in graph-sampled workflow paths, SkillSynth explicitly controls the diversity of minimal execution trajectories required to solve the synthesized tasks. Experiments on Terminal-Bench demonstrate the effectiveness of SkillSynth. Moreover, task instances synthesized by SkillSynth have been adopted to train Hy3 Preview, contributing to its enhanced agentic capabilities in terminal-based settings.

## Open Questions

- How is the skill graph constructed in practice, and what data sources define the scenario nodes and command-line skills?
- What metrics does Terminal-Bench use to quantify the claimed diversity gains in execution trajectories?
- How much performance improvement does SkillSynth provide over prior task-synthesis baselines?
- What parts of the multi-agent harness are responsible for instantiating graph paths into executable tasks?
- Does the method generalize beyond terminal settings to other agent environments?
