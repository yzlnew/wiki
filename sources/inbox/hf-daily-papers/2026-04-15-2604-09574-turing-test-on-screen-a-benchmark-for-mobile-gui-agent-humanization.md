---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, gui-agents, evaluation, humanization, adversarial, mobile, benchmark]
source_count: 1
updated: 2026-04-16
source_url: https://arxiv.org/abs/2604.09574
paper_id: 2604.09574
published: 2026-02-24T03:00:00+08:00
submitted_on_daily: 2026-04-15T15:30:28+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# Turing Test on Screen: A Benchmark for Mobile GUI Agent Humanization

## Summary

- one_sentence_summary: This paper proposes “Turing Test on Screen,” a benchmark and optimization framing for making mobile GUI agents less detectable by matching human touch behavior while preserving task performance.
- why_relevant: It is directly relevant to agentic systems and evaluation because it studies how autonomous GUI agents should behave under adversarial detection, not just whether they complete tasks.
- filter_reason: A concrete benchmark and evaluation framework for mobile GUI agents, with technical details on behavior matching and performance trade-offs.
- hugging_face_paper: https://huggingface.co/papers/2604.09574
- original_paper: https://arxiv.org/abs/2604.09574
- source_basis: `original abstract page`

## Key Points

- Models agent-vs-detector interaction as a MinMax problem where the agent minimizes behavioral divergence from human behavior.
- Introduces a new high-fidelity dataset of mobile touch dynamics to analyze and compare agent behavior.
- Finds that vanilla LMM-based GUI agents are easy to detect because their kinematics look unnatural.
- Defines the Agent Humanization Benchmark (AHB) and detection metrics to measure the trade-off between imitability and utility.
- Reports that heuristic noise and data-driven behavioral matching can improve human-likeness without sacrificing performance, at least in the paper's experiments.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.09574
- Hugging Face API entry: https://huggingface.co/api/papers/2604.09574
- arXiv abstract: https://arxiv.org/abs/2604.09574

## Paper Metadata

- authors: `Jiachen Zhu`, `Lingyu Yang`, `Rong Shan`, `Congmin Zheng`, `Zeyu Zheng`, `Weiwen Liu`, `Yong Yu`, `Weinan Zhang`, `Jianghao Lin`
- organization: `Shanghai Jiao Tong University`
- ai_keywords: `autonomous GUI agents`, `adversarial countermeasures`, `human-centric ecosystems`, `Turing Test on Screen`, `MinMax optimization`, `LMM-based agents`, `behavioral divergence`, `Agent Humanization Benchmark`, `imitability`, `task performance`
- upvotes: `27`
- num_comments: `2`
- abstract: The rise of autonomous GUI agents has triggered adversarial countermeasures from digital platforms, yet existing research prioritizes utility and robustness over the critical dimension of anti-detection. We argue that for agents to survive in human-centric ecosystems, they must evolve Humanization capabilities. We introduce the ``Turing Test on Screen,'' formally modeling the interaction as a MinMax optimization problem between a detector and an agent aiming to minimize behavioral divergence. We then collect a new high-fidelity dataset of mobile touch dynamics, and conduct our analysis that vanilla LMM-based agents are easily detectable due to unnatural kinematics. Consequently, we establish the Agent Humanization Benchmark (AHB) and detection metrics to quantify the trade-off between imitability and utility. Finally, we propose methods ranging from heuristic noise to data-driven behavioral matching, demonstrating that agents can achieve high imitability theoretically and empirically without sacrificing performance. This work shifts the paradigm from whether an agent can perform a task to how it performs it within a human-centric ecosystem, laying the groundwork for seamless coexistence in adversarial digital environments.
- hf_ai_summary: Researchers propose humanization capabilities for autonomous GUI agents to avoid detection by digital platforms, introducing a benchmark and methods to balance imitability with task performance.

## Source Excerpt

The rise of autonomous GUI agents has triggered adversarial countermeasures from digital platforms, yet existing research prioritizes utility and robustness over the critical dimension of anti-detection. We argue that for agents to survive in human-centric ecosystems, they must evolve Humanization capabilities. We introduce the ``Turing Test on Screen,'' formally modeling the interaction as a MinMax optimization problem between a detector and an agent aiming to minimize behavioral divergence. We then collect a new high-fidelity dataset of mobile touch dynamics, and conduct our analysis that vanilla LMM-based agents are easily detectable due to unnatural kinematics. Consequently, we establish the Agent Humanization Benchmark (AHB) and detection metrics to quantify the trade-off between imitability and utility. Finally, we propose methods ranging from heuristic noise to data-driven behavioral matching, demonstrating that agents can achieve high imitability theoretically and empirically without sacrificing performance. This work shifts the paradigm from whether an agent can perform a task to how it performs it within a human-centric ecosystem, laying the groundwork for seamless coexistence in adversarial digital environments.

## Open Questions

- What exact detector models and evaluation protocol were used in AHB?
- How large and diverse is the mobile touch dynamics dataset?
- Which behavioral matching method performed best, and on what tasks or devices?
- How much performance trade-off remains under stronger detectors or more realistic platform defenses?
