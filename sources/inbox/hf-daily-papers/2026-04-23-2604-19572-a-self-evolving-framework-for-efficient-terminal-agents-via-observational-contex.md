---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, reasoning-behavior-shaping, context-compression, terminal-agents, long-horizon, evaluation]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.19572
paper_id: 2604.19572
published: 2026-04-21T04:00:00+08:00
submitted_on_daily: 2026-04-23T15:26:52+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

## Summary

- one_sentence_summary: TACO is a plug-and-play terminal-agent compression framework that learns and refines observation-compression rules from interaction trajectories to cut token overhead while improving long-horizon agent performance.
- why_relevant: It is directly relevant to agent systems and post-training style behavior shaping because it changes how agents compress and retain context during tool-using, long-horizon execution.
- filter_reason: Directly targets terminal agents with a practical compression framework that improves agent performance and token efficiency.
- hugging_face_paper: https://huggingface.co/papers/2604.19572
- original_paper: https://arxiv.org/abs/2604.19572
- source_basis: `original abstract page`

## Key Points

- The paper targets terminal-centric agent tasks where preserving raw environment feedback in history causes redundant context growth and quadratic token cost over long horizons.
- TACO automatically discovers and refines compression rules from interaction trajectories, rather than relying on fixed heuristics or prompt templates.
- It is designed to work as a plug-and-play layer for existing terminal agents and across different agent frameworks and backbone models.
- Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional benchmarks show consistent performance gains and better token efficiency.
- With MiniMax-2.5, the framework reportedly reduces token overhead by about 10% while improving performance on most benchmarks; on TerminalBench it yields roughly 1%-4% gains and about 2%-3% higher accuracy under the same token budget.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.19572
- Hugging Face API entry: https://huggingface.co/api/papers/2604.19572
- arXiv abstract: https://arxiv.org/abs/2604.19572
- GitHub: https://github.com/multimodal-art-projection/TACO

## Paper Metadata

- authors: `Jincheng Ren`, `Siwei Wu`, `Yizhi Li`, `Kang Zhu`, `Shu Xu`, `Boyu Feng`, `Ruibin Yuan`, `Wei Zhang`, `Riza Batista-Navarro`, `Jian Yang`, `Chenghua Lin`
- organization: `Multimodal Art Projection`
- ai_keywords: `Terminal Agent Compression`, `interaction trajectories`, `observation compression`, `terminal-centric agentic tasks`, `token overhead`, `self-evolving framework`, `TerminalBench`, `agent frameworks`, `backbone models`
- upvotes: `15`
- num_comments: `1`
- abstract: As model capabilities advance, research has increasingly shifted toward long-horizon, multi-turn terminal-centric agentic tasks, where raw environment feedback is often preserved in the interaction history to support future decisions. However, repeatedly retaining such feedback introduces substantial redundancy and causes cumulative token cost to grow quadratically with the number of steps, hindering long-horizon reasoning. Although observation compression can mitigate this issue, the heterogeneity of terminal environments makes heuristic-based or fixed-prompt methods difficult to generalize. We propose TACO, a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks (i.e., SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench) show that TACO consistently improves performance across mainstream agent frameworks and strong backbone models. With MiniMax-2.5, it improves performance on most benchmarks while reducing token overhead by around 10%. On TerminalBench, it brings consistent gains of 1%-4% across strong agentic models, and further improves accuracy by around 2%-3% under the same token budget. These results demonstrate the effectiveness and generalization of self-evolving, task-aware compression for terminal agents.
- hf_ai_summary: TACO is a self-evolving compression framework that automatically discovers and refines compression rules from interaction trajectories to improve long-horizon agent performance while reducing token overhead.

## Source Excerpt

As model capabilities advance, research has increasingly shifted toward long-horizon, multi-turn terminal-centric agentic tasks, where raw environment feedback is often preserved in the interaction history to support future decisions. However, repeatedly retaining such feedback introduces substantial redundancy and causes cumulative token cost to grow quadratically with the number of steps, hindering long-horizon reasoning. Although observation compression can mitigate this issue, the heterogeneity of terminal environments makes heuristic-based or fixed-prompt methods difficult to generalize. We propose TACO, a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks (i.e., SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench) show that TACO consistently improves performance across mainstream agent frameworks and strong backbone models. With MiniMax-2.5, it improves performance on most benchmarks while reducing token overhead by around 10%. On TerminalBench, it brings consistent gains of 1%-4% across strong agentic models, and further improves accuracy by around 2%-3% under the same token budget. These results demonstrate the effectiveness and generalization of self-evolving, task-aware compression for terminal agents.

## Open Questions

- How are compression rules discovered and refined in TACO at a technical level?
- What signals from interaction trajectories are used to decide what to keep or discard?
- How much of the gain comes from better compression versus benchmark-specific tuning?
- Does the method generalize to non-terminal tool-using agents or only terminal environments?
