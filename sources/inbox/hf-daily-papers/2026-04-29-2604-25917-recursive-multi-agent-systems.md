---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, reasoning, llm-systems, agent-evals, multi-agent-systems, recursive-computation, latent-space, credit-assignment, efficiency]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.25917
paper_id: 2604.25917
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-04-29T08:12:09+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Recursive Multi-Agent Systems

## Summary

- one_sentence_summary: RecursiveMAS extends recursive or looped model computation from single-model reasoning to multi-agent collaboration by treating heterogeneous agents as a latent-space recursive system with shared credit assignment.
- why_relevant: This is directly relevant to agent architectures and post-training because it studies how to scale agent collaboration, optimize multi-agent learning end-to-end, and reduce inference cost through recursive latent computation.
- filter_reason: A technically grounded multi-agent architecture paper with recursive reasoning, credit assignment, and evaluation across code and reasoning benchmarks.
- hugging_face_paper: https://huggingface.co/papers/2604.25917
- original_paper: https://arxiv.org/abs/2604.25917
- source_basis: `original abstract page`

## Key Points

- Introduces RecursiveMAS, a recursive multi-agent framework that represents the whole agent system as unified latent-space recursive computation rather than text-only interaction.
- Uses a lightweight RecursiveLink module to connect heterogeneous agents in a collaboration loop, supporting latent thought generation and cross-agent latent state transfer.
- Proposes an inner-outer loop learning algorithm for whole-system co-optimization with shared gradient-based credit assignment across recursion rounds.
- The paper claims theoretical results on runtime complexity and learning dynamics, arguing RecursiveMAS is more efficient than standard text-based multi-agent systems and has stable gradients during recursive training.
- Evaluates 4 collaboration patterns on 9 benchmarks across math, science, medicine, search, and code generation, reporting 8.3% average accuracy gain, 1.2x-2.4x inference speedup, and 34.6%-75.6% token reduction versus baselines.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25917
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25917
- arXiv abstract: https://arxiv.org/abs/2604.25917
- GitHub: https://github.com/RecursiveMAS/RecursiveMAS
- Project page: https://recursivemas.github.io

## Paper Metadata

- authors: `Xiyuan Yang`, `Jiaru Zou`, `Rui Pan`, `Ruizhong Qiu`, `Pan Lu`, `Shizhe Diao`, `Jindong Jiang`, `Hanghang Tong`, `Tong Zhang`, `Markus J. Buehler`, `Jingrui He`, `James Zou`
- organization: `Stanford University`
- ai_keywords: `recursive language models`, `multi-agent systems`, `latent-space recursive computation`, `RecursiveLink module`, `inner-outer loop learning`, `gradient-based credit assignment`, `runtime complexity`, `learning dynamics`, `agent collaboration patterns`, `end-to-end inference speedup`, `token usage reduction`
- upvotes: `53`
- num_comments: `2`
- abstract: Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. To optimize our framework, we develop an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses of runtime complexity and learning dynamics establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Empirically, we instantiate RecursiveMAS under 4 representative agent collaboration patterns and evaluate across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2times-2.4times end-to-end inference speedup, and 34.6%-75.6% token usage reduction. Code and Data are provided in https://recursivemas.github.io.
- hf_ai_summary: RecursiveMAS extends recursive scaling principles from single models to multi-agent systems, enabling collaborative reasoning through iterative latent-space computations with improved efficiency and accuracy.

## Source Excerpt

Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. To optimize our framework, we develop an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses of runtime complexity and learning dynamics establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Empirically, we instantiate RecursiveMAS under 4 representative agent collaboration patterns and evaluate across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2$\times$-2.4$\times$ end-to-end inference speedup, and 34.6%-75.6% token usage reduction. Code and Data are provided in this https URL .

## Open Questions

- What exactly are the 4 representative agent collaboration patterns instantiated in RecursiveMAS?
- How does RecursiveLink implement cross-agent latent state transfer in practice?
- What baselines were used for the multi-agent and recursive computation comparisons?
- Does the abstract indicate whether the speedup and token reductions hold across all benchmarks or only on average?
