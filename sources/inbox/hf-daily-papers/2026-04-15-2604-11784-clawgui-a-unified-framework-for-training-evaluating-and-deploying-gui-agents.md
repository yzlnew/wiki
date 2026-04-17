---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, reinforcement-learning, post-training, agent-evals, llm-systems, gui-agents, evaluation, deployment, mobile, tool-use]
source_count: 1
updated: 2026-04-16
source_url: https://arxiv.org/abs/2604.11784
paper_id: 2604.11784
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-15T15:31:57+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents

## Summary

- one_sentence_summary: ClawGUI is an open-source end-to-end framework for GUI agents that unifies RL training, standardized evaluation, and cross-platform deployment across real devices and chat platforms.
- why_relevant: It is directly relevant to agents and post-training because it couples reinforcement learning, evaluation, and deployment into one infrastructure for GUI agents that operate on real devices.
- filter_reason: Directly targets GUI agents with RL training, standardized evaluation, and deployment infrastructure.
- hugging_face_paper: https://huggingface.co/papers/2604.11784
- original_paper: https://arxiv.org/abs/2604.11784
- source_basis: `original abstract page`

## Key Points

- The paper argues that GUI agent progress is limited less by model capacity than by infrastructure gaps: unstable RL environments, drifting evaluation protocols, and weak real-device deployment.
- ClawGUI-RL provides open-source GUI agent RL infrastructure with support for parallel virtual environments and real physical devices, combining GiGPO with a Process Reward Model for dense step-level supervision.
- ClawGUI-Eval standardizes evaluation across 6 benchmarks and 11+ models and reports 95.8% reproduction against official baselines.
- ClawGUI-Agent deploys trained agents to Android, HarmonyOS, and iOS through 12+ chat platforms using hybrid CLI-GUI control and persistent personalized memory.
- An end-to-end trained ClawGUI-2B model reaches 17.1% success rate on MobileWorld GUI-Only, beating the same-scale MAI-UI-2B baseline by 6.0%.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11784
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11784
- arXiv abstract: https://arxiv.org/abs/2604.11784
- GitHub: https://github.com/ZJU-REAL/ClawGUI
- Project page: https://zju-real.github.io/ClawGUI-Page/

## Paper Metadata

- authors: `Fei Tang`, `Zhiqiong Lu`, `Boxuan Zhang`, `Weiming Lu`, `Jun Xiao`, `Yueting Zhuang`, `Yongliang Shen`
- organization: `Zhejiang University`
- ai_keywords: `GUI agents`, `reinforcement learning`, `environment instability`, `closed pipelines`, `evaluation protocols`, `real-world deployment`, `mobile applications`, `GUI-only benchmark`, `success rate`, `hybrid CLI-GUI control`, `persistent memory`
- upvotes: `121`
- num_comments: `5`
- abstract: GUI agents drive applications through their visual interfaces instead of programmatic APIs, interacting with arbitrary software via taps, swipes, and keystrokes, reaching a long tail of applications that CLI-based agents cannot. Yet progress in this area is bottlenecked less by modeling capacity than by the absence of a coherent full-stack infrastructure: online RL training suffers from environment instability and closed pipelines, evaluation protocols drift silently across works, and trained agents rarely reach real users on real devices. We present ClawGUI, an open-source framework addressing these three gaps within a single harness. ClawGUI-RL provides the first open-source GUI agent RL infrastructure with validated support for both parallel virtual environments and real physical devices, integrating GiGPO with a Process Reward Model for dense step-level supervision. ClawGUI-Eval enforces a fully standardized evaluation pipeline across 6 benchmarks and 11+ models, achieving 95.8\% reproduction against official baselines. ClawGUI-Agent brings trained agents to Android, HarmonyOS, and iOS through 12+ chat platforms with hybrid CLI-GUI control and persistent personalized memory. Trained end to end within this pipeline, ClawGUI-2B achieves 17.1\% Success Rate on MobileWorld GUI-Only, outperforming the same-scale MAI-UI-2B baseline by 6.0\%.
- hf_ai_summary: ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

## Source Excerpt

GUI agents drive applications through their visual interfaces instead of programmatic APIs, interacting with arbitrary software via taps, swipes, and keystrokes, reaching a long tail of applications that CLI-based agents cannot. Yet progress in this area is bottlenecked less by modeling capacity than by the absence of a coherent full-stack infrastructure: online RL training suffers from environment instability and closed pipelines, evaluation protocols drift silently across works, and trained agents rarely reach real users on real devices. We present \textbf{ClawGUI}, an open-source framework addressing these three gaps within a single harness. \textbf{ClawGUI-RL} provides the first open-source GUI agent RL infrastructure with validated support for both parallel virtual environments and real physical devices, integrating GiGPO with a Process Reward Model for dense step-level supervision. \textbf{ClawGUI-Eval} enforces a fully standardized evaluation pipeline across 6 benchmarks and 11+ models, achieving 95.8\% reproduction against official baselines. \textbf{ClawGUI-Agent} brings trained agents to Android, HarmonyOS, and iOS through 12+ chat platforms with hybrid CLI-GUI control and persistent personalized memory. Trained end to end within this pipeline, \textbf{ClawGUI-2B} achieves 17.1\% Success Rate on MobileWorld GUI-Only, outperforming the same-scale MAI-UI-2B baseline by 6.0\%.

## Open Questions

- What specific tasks and environments are covered by the 6 benchmarks used in ClawGUI-Eval?
- How is the Process Reward Model trained and how are step-level rewards constructed?
- What aspects of environment instability are addressed in the parallel virtual and physical device setup?
- How does hybrid CLI-GUI control work in practice across the supported chat platforms?
- What is the size, architecture, and training recipe for ClawGUI-2B beyond the reported success rate?
