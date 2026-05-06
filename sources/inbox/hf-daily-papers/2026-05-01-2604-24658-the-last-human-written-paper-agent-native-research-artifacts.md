---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, coding-agents, research-artifacts, reproducibility, evaluation, tool-using-systems]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.24658
paper_id: 2604.24658
published: 2026-04-29T04:00:00+08:00
submitted_on_daily: 2026-05-01T09:25:42+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# The Last Human-Written Paper: Agent-Native Research Artifacts

## Summary

- one_sentence_summary: The paper proposes Agent-Native Research Artifacts (ARA), a machine-executable research package designed to preserve research process, implementation details, and evidence for AI agents that need to read, reproduce, and extend prior work.
- why_relevant: This is directly relevant to agents and tool-using systems because it treats research artifacts as machine-executable inputs for AI agents, and it also touches post-training/evaluation infrastructure for agent performance.
- filter_reason: Directly about agent-native research artifacts, review automation, and benchmarked agent evaluation with concrete system design details.
- hugging_face_paper: https://huggingface.co/papers/2604.24658
- original_paper: https://arxiv.org/abs/2604.24658
- source_basis: `original abstract page`

## Key Points

- It argues that conventional papers impose a "storytelling tax" by omitting failed experiments and branching exploration, and an "engineering tax" by leaving out details needed for agents to reproduce code.
- ARA is structured into four layers: scientific logic, executable code with full specifications, an exploration graph that preserves discarded branches, and evidence tying claims to raw outputs.
- The proposed ecosystem includes a Live Research Manager for capturing decisions and dead ends, an ARA Compiler for converting legacy PDFs and repos into ARA format, and an ARA-native review system for objective checks.
- In evaluation, ARA improves PaperBench and RE-Bench question-answering accuracy from 72.4% to 93.7%, and reproduction success from 57.4% to 64.4%.
- The paper reports a tradeoff on open-ended extension tasks: preserved failure traces can help progress, but may also constrain capable agents depending on their ability to explore beyond prior work.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.24658
- Hugging Face API entry: https://huggingface.co/api/papers/2604.24658
- arXiv abstract: https://arxiv.org/abs/2604.24658
- GitHub: https://github.com/Orchestra-Research/Agent-Native-Research-Artifact
- Project page: https://www.orchestra-research.com/ara

## Paper Metadata

- authors: `Jiachen Liu`, `Jiaxin Pei`, `Jintao Huang`, `Chenglei Si`, `Ao Qu`, `Xiangru Tang`, `Runyu Lu`, `Lichang Chen`, `Xiaoyan Bai`, `Haizhong Zheng`, `Carl Chen`, `Zhiyang Chen`, `Haojie Ye`, `Yujuan Fu`, `Zexue He`, `Zijian Jin`, `Zhenyu Zhang`, `Shangquan Sun`, `Maestro Harmon`, `John Dianzhuo Wang`, `Jianqiao Zeng`, `Jiachen Sun`, `Mingyuan Wu`, `Baoyu Zhou`, `Chenyu You`, `Shijian Lu`, `Yiming Qiu`, `Fan Lai`, `Yuan Yuan`, `Yao Li`, `Junyuan Hong`, `Ruihao Zhu`, `Beidi Chen`, `Alex Pentland`, `Ang Chen`, `Mosharaf Chowdhury`, `Zechen Zhang`
- organization: `Stanford University`
- upvotes: `6`
- num_comments: `2`
- abstract: Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way. This compilation imposes two structural costs: a Storytelling Tax, where failed experiments, rejected hypotheses, and the branching exploration process are discarded to fit a linear narrative; and an Engineering Tax, where the gap between reviewer-sufficient prose and agent-sufficient specification leaves critical implementation details unwritten. Tolerable for human readers, these costs become critical when AI agents must understand, reproduce, and extend published work. We introduce the Agent-Native Research Artifact (ARA), a protocol that replaces the narrative paper with a machine-executable research package structured around four layers: scientific logic, executable code with full specifications, an exploration graph that preserves the failures compilation discards, and evidence grounding every claim in raw outputs. Three mechanisms support the ecosystem: a Live Research Manager that captures decisions and dead ends during ordinary development; an ARA Compiler that translates legacy PDFs and repos into ARAs; and an ARA-native review system that automates objective checks so human reviewers can focus on significance, novelty, and taste. On PaperBench and RE-Bench, ARA raises question-answering accuracy from 72.4% to 93.7% and reproduction success from 57.4% to 64.4%. On RE-Bench's five open-ended extension tasks, preserved failure traces in ARA accelerate progress, but can also constrain a capable agent from stepping outside the prior-run box depending on the agent's capabilities.

## Source Excerpt

Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way. This compilation imposes two structural costs: a Storytelling Tax, where failed experiments, rejected hypotheses, and the branching exploration process are discarded to fit a linear narrative; and an Engineering Tax, where the gap between reviewer-sufficient prose and agent-sufficient specification leaves critical implementation details unwritten. Tolerable for human readers, these costs become critical when AI agents must understand, reproduce, and extend published work. We introduce the Agent-Native Research Artifact (ARA), a protocol that replaces the narrative paper with a machine-executable research package structured around four layers: scientific logic, executable code with full specifications, an exploration graph that preserves the failures compilation discards, and evidence grounding every claim in raw outputs. Three mechanisms support the ecosystem: a Live Research Manager that captures decisions and dead ends during ordinary development; an ARA Compiler that translates legacy PDFs and repos into ARAs; and an ARA-native review system that automates objective checks so human reviewers can focus on significance, novelty, and taste. On PaperBench and RE-Bench, ARA raises question-answering accuracy from 72.4% to 93.7% and reproduction success from 57.4% to 64.4%. On RE-Bench's five open-ended extension tasks, preserved failure traces in ARA accelerate progress, but can also constrain a capable agent from stepping outside the prior-run box depending on the agent's capabilities.

## Open Questions

- How is the exploration graph represented in practice, and what data does the compiler extract automatically versus require human input?
- How much of the reported gain comes from better retrieval of evidence versus better reproducibility of code and specifications?
- What are the objective checks used in the ARA-native review system, and how do they compare to standard peer review criteria?
- How well does the approach generalize beyond PaperBench and RE-Bench to other research domains or longer-horizon agent tasks?
