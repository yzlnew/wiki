---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, coding-agents, agent-evals, llm-systems, multimodal, benchmark, website-generation, tool-use, interactive-eval]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.27419
paper_id: 2604.27419
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-01T09:31:26+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?

## Summary

- one_sentence_summary: InteractWeb-Bench is a multimodal interactive benchmark for website generation that tests whether coding agents can handle ambiguous non-expert instructions through clarification, implementation, verification, and submission steps.
- why_relevant: This paper is directly relevant to agents and tool-using systems because it evaluates how multimodal coding agents behave in interactive, user-facing workflows rather than static benchmark settings.
- filter_reason: A technically grounded benchmark for interactive coding agents and multimodal website-generation workflows, with clear evaluation of intent recognition and adaptive interaction.
- hugging_face_paper: https://huggingface.co/papers/2604.27419
- original_paper: https://arxiv.org/abs/2604.27419
- source_basis: `original abstract page`

## Key Points

- The paper targets a real failure mode in agentic website development: blind execution, where agents proceed without resolving semantic mismatches in user instructions.
- InteractWeb-Bench is presented as the first multimodal interactive benchmark for website generation under non-expert, low-code user conditions.
- It uses four user-agent types plus persona-driven instruction perturbations to simulate ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies.
- The benchmark includes an interactive execution environment with a unified action space: Clarify, Implement, Verify, and Submit.
- Experiments reportedly show that frontier MLLM-based agents still get trapped in blind execution, suggesting weaknesses in intent recognition and adaptive interaction.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27419
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27419
- arXiv abstract: https://arxiv.org/abs/2604.27419
- GitHub: https://github.com/AIforIP/InteractWeb-Bench
- Project page: https://interactweb-bench.wangqiyao.me/

## Paper Metadata

- authors: `Qiyao Wang`, `Haoran Hu`, `Longze Chen`, `Hongbo Wang`, `Hamid Alinejad-Rokny`, `Yuan Lin`, `Min Yang`
- organization: `IP Intelligence`
- ai_keywords: `multimodal large language models`, `coding agents`, `website generation`, `interactive benchmark`, `user agents`, `persona-driven instruction perturbations`, `requirement engineering defect taxonomies`, `interactive execution environment`, `unified action space`, `blind execution`, `intent recognition`, `adaptive interaction`
- upvotes: `8`
- num_comments: `2`
- abstract: With the advancement of multimodal large language models (MLLMs) and coding agents, the website development has shifted from manual programming to agent-based project-level code synthesis. Existing benchmarks rely on idealized assumptions, especially for well-structured, information-rich inputs and static execution settings. In contrast, real-world development is constrained by a critical bottleneck: the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution. To address this gap, we introduce InteractWeb-Bench, the first multimodal interactive benchmark for website generation under non-expert low-code user conditions. InteractWeb-Bench introduces four types of user agents and persona-driven instruction perturbations to systematically simulate diverse user behaviors, including ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies. We develop an interactive execution environment for agents, featuring a unified action space comprising Clarify, Implement, Verify, and Submit, enabling iterative intent refinement, code synthesis, and visual feedback-based validation. Extensive experiments and analysis reveal that frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction.
- hf_ai_summary: InteractWeb-Bench presents the first multimodal interactive benchmark for website generation under non-expert low-code conditions, addressing semantic misalignment through diverse user agents and interactive execution environments.

## Source Excerpt

With the advancement of multimodal large language models (MLLMs) and coding agents, the website development has shifted from manual programming to agent-based project-level code synthesis. Existing benchmarks rely on idealized assumptions, especially for well-structured, information-rich inputs and static execution settings. In contrast, real-world development is constrained by a critical bottleneck: the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution. To address this gap, we introduce InteractWeb-Bench, the first multimodal interactive benchmark for website generation under non-expert low-code user conditions. InteractWeb-Bench introduces four types of user agents and persona-driven instruction perturbations to systematically simulate diverse user behaviors, including ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies. We develop an interactive execution environment for agents, featuring a unified action space comprising Clarify, Implement, Verify, and Submit, enabling iterative intent refinement, code synthesis, and visual feedback-based validation. Extensive experiments and analysis reveal that frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction.

## Open Questions

- What models and baselines were evaluated on InteractWeb-Bench?
- How is performance measured across Clarify, Implement, Verify, and Submit actions?
- What are the four user-agent types, and how do they differ operationally?
- Does the benchmark include any quantitative results showing how much clarification improves outcomes?
