---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, environment-interaction, mobile-agents, gui-agents, evaluation, robustness, benchmark]
source_count: 1
updated: 2026-04-17
source_url: https://arxiv.org/abs/2507.04227
paper_id: 2507.04227
published: 2026-04-14T04:00:00+08:00
submitted_on_daily: 2026-04-16T14:46:26+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# Mobile GUI Agents under Real-world Threats: Are We There Yet?

## Summary

- one_sentence_summary: The paper argues that mobile GUI agents need pre-deployment validation against real-world third-party content, and shows that such content can substantially degrade both open-source and commercial agents.
- why_relevant: It is directly about agent evaluation under environment shift and adversarially misleading content, which matters for tool-using systems and post-training robustness rather than RL optimization itself.
- filter_reason: Directly evaluates mobile GUI agents in realistic environments with a benchmark and threat-focused failure analysis.
- hugging_face_paper: https://huggingface.co/papers/2507.04227
- original_paper: https://arxiv.org/abs/2507.04227
- source_basis: `original abstract page`

## Key Points

- Introduces a scalable app content instrumentation framework for targeted content modification inside existing applications.
- Builds a benchmark with two parts: a dynamic task-execution environment and a static dataset of challenging GUI states.
- The dynamic environment includes 122 reproducible tasks; the static dataset contains over 3,000 scenarios derived from commercial apps.
- Experiments show all examined agents are significantly misled by third-party content, with average misleading rates of 42.0% in the dynamic setting and 36.1% in the static setting.
- Positions real-world content robustness as a missing pre-deployment check for mobile GUI agents beyond standard static benchmarks.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2507.04227
- Hugging Face API entry: https://huggingface.co/api/papers/2507.04227
- arXiv abstract: https://arxiv.org/abs/2507.04227
- GitHub: https://github.com/Zsbyqx20/AgentHazard
- Project page: https://agenthazard.github.io

## Paper Metadata

- authors: `Guohong Liu`, `Jialei Ye`, `Jiacheng Liu`, `Yuanchun Li`, `Wei Liu`, `Pengzhi Gao`, `Jian Luan`, `Yunxin Liu`
- organization: `Tsinghua University`
- ai_keywords: `mobile GUI agents`, `large language models`, `device-control tasks`, `natural language instructions`, `benchmarking`, `app content instrumentation`, `GUI states`, `dynamic environment`, `static dataset`
- upvotes: `2`
- num_comments: `2`
- abstract: Recent years have witnessed a rapid development of mobile GUI agents powered by large language models (LLMs), which can autonomously execute diverse device-control tasks based on natural language instructions. The increasing accuracy of these agents on standard benchmarks has raised expectations for large-scale real-world deployment, and there are already several commercial agents released and used by early adopters. However, are we really ready for GUI agents integrated into our daily devices as system building blocks? We argue that an important pre-deployment validation is missing to examine whether the agents can maintain their performance under real-world threats. Specifically, unlike existing common benchmarks that are based on simple static app contents (they have to do so to ensure environment consistency between different tests), real-world apps are filled with contents from untrustworthy third parties, such as advertisement emails, user-generated posts and medias, etc. ... To this end, we introduce a scalable app content instrumentation framework to enable flexible and targeted content modifications within existing applications. Leveraging this framework, we create a test suite comprising both a dynamic task execution environment and a static dataset of challenging GUI states. The dynamic environment encompasses 122 reproducible tasks, and the static dataset consists of over 3,000 scenarios constructed from commercial apps. We perform experiments on both open-source and commercial GUI agents. Our findings reveal that all examined agents can be significantly degraded due to third-party contents, with an average misleading rate of 42.0% and 36.1% in dynamic and static environments respectively. The framework and benchmark has been released at https://agenthazard.github.io.
- hf_ai_summary: Mobile GUI agents powered by large language models show significant performance degradation when exposed to real-world third-party content in commercial applications.

## Source Excerpt

Recent years have witnessed a rapid development of mobile GUI agents powered by large language models (LLMs), which can autonomously execute diverse device-control tasks based on natural language instructions. The increasing accuracy of these agents on standard benchmarks has raised expectations for large-scale real-world deployment, and there are already several commercial agents released and used by early adopters. However, are we really ready for GUI agents integrated into our daily devices as system building blocks? We argue that an important pre-deployment validation is missing to examine whether the agents can maintain their performance under real-world threats. Specifically, unlike existing common benchmarks that are based on simple static app contents (they have to do so to ensure environment consistency between different tests), real-world apps are filled with contents from untrustworthy third parties, such as advertisement emails, user-generated posts and medias, etc. ... To this end, we introduce a scalable app content instrumentation framework to enable flexible and targeted content modifications within existing applications. Leveraging this framework, we create a test suite comprising both a dynamic task execution environment and a static dataset of challenging GUI states. The dynamic environment encompasses 122 reproducible tasks, and the static dataset consists of over 3,000 scenarios constructed from commercial apps. We perform experiments on both open-source and commercial GUI agents. Our findings reveal that all examined agents can be significantly degraded due to third-party contents, with an average misleading rate of 42.0% and 36.1% in dynamic and static environments respectively. The framework and benchmark has been released at this https URL .

## Open Questions

- Which open-source and commercial GUI agents were evaluated, and how did their failure modes differ?
- What kinds of third-party content were most misleading in the dynamic versus static settings?
- How exactly does the app content instrumentation framework modify app content while preserving task reproducibility?
- Does the benchmark measure only task success, or also intermediate action quality and recovery behavior?
