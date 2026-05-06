---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, reinforcement-learning, post-training, llm-systems, synthetic-data, tool-use, long-horizon, productivity]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.28181
paper_id: 2604.28181
published: 2026-04-30T04:00:00+08:00
submitted_on_daily: 2026-05-01T08:16:59+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# Synthetic Computers at Scale for Long-Horizon Productivity Simulation

## Summary

- one_sentence_summary: The paper proposes Synthetic Computers at Scale, a method for generating realistic user computer environments and running long-horizon agent simulations to produce experiential learning signals that improve productivity-task performance.
- why_relevant: It is directly relevant to agents, post-training, and reinforcement learning because it frames large-scale simulated work environments as a source of training signal for improving long-horizon tool-using productivity agents.
- filter_reason: Directly targets agentic reinforcement learning and long-horizon agent evaluation with concrete simulation infrastructure.
- hugging_face_paper: https://huggingface.co/papers/2604.28181
- original_paper: https://arxiv.org/abs/2604.28181
- source_basis: `original abstract page`

## Key Points

- It creates synthetic computer worlds with realistic folder hierarchies and content-rich artifacts such as documents, spreadsheets, and presentations.
- For each synthetic computer, one agent generates user-specific productivity objectives, and another agent acts as the user across the computer until the objectives are completed.
- The simulations are long-horizon: the paper reports 1,000 synthetic computers, more than 8 hours of agent runtime per run, and over 2,000 turns on average.
- The resulting experiential learning signals are said to improve agent performance on both in-domain and out-of-domain productivity evaluations.
- The authors position this as a scalable substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity settings.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.28181
- Hugging Face API entry: https://huggingface.co/api/papers/2604.28181
- arXiv abstract: https://arxiv.org/abs/2604.28181
- Project page: https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale

## Paper Metadata

- authors: `Tao Ge`, `Baolin Peng`, `Hao Cheng`, `Jianfeng Gao`
- organization: `Microsoft`
- ai_keywords: `synthetic data creation`, `long-horizon simulations`, `agent-based modeling`, `experiential learning`, `agent self-improvement`, `agentic reinforcement learning`
- upvotes: `8`
- num_comments: `2`
- abstract: Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content-rich artifacts. To scale synthetic data creation for such productivity scenarios, we introduce Synthetic Computers at Scale, a scalable methodology for creating such environments with realistic folder hierarchies and content-rich artifacts (e.g., documents, spreadsheets, and presentations). Conditioned on each synthetic computer, we run long-horizon simulations: one agent creates productivity objectives that are specific to the computer's user and require multiple professional deliverables and about a month of human work; another agent then acts as that user and keeps working across the computer -- for example, navigating the filesystem for grounding, coordinating with simulated collaborators, and producing professional artifacts -- until these objectives are completed. In preliminary experiments, we create 1,000 synthetic computers and run long-horizon simulations on them; each run requires over 8 hours of agent runtime and spans more than 2,000 turns on average. These simulations produce rich experiential learning signals, whose effectiveness is validated by significant improvements in agent performance on both in-domain and out-of-domain productivity evaluations. Given that personas are abundant at billion scale, this methodology can in principle scale to millions or even billions of synthetic user worlds with sufficient compute, enabling broader coverage of diverse professions, roles, contexts, environments, and productivity needs. We argue that scalable synthetic computer creation, together with at-scale simulations, is highly promising as a foundational substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity scenarios.
- hf_ai_summary: Synthetic computers with realistic folder structures and artifacts enable long-horizon productivity simulations that improve agent performance through extensive experiential learning.

## Source Excerpt

Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content-rich artifacts. To scale synthetic data creation for such productivity scenarios, we introduce Synthetic Computers at Scale, a scalable methodology for creating such environments with realistic folder hierarchies and content-rich artifacts (e.g., documents, spreadsheets, and presentations). Conditioned on each synthetic computer, we run long-horizon simulations: one agent creates productivity objectives that are specific to the computer's user and require multiple professional deliverables and about a month of human work; another agent then acts as that user and keeps working across the computer -- for example, navigating the filesystem for grounding, coordinating with simulated collaborators, and producing professional artifacts -- until these objectives are completed. In preliminary experiments, we create 1,000 synthetic computers and run long-horizon simulations on them; each run requires over 8 hours of agent runtime and spans more than 2,000 turns on average. These simulations produce rich experiential learning signals, whose effectiveness is validated by significant improvements in agent performance on both in-domain and out-of-domain productivity evaluations. Given that personas are abundant at billion scale, this methodology can in principle scale to millions or even billions of synthetic user worlds with sufficient compute, enabling broader coverage of diverse professions, roles, contexts, environments, and productivity needs. We argue that scalable synthetic computer creation, together with at-scale simulations, is highly promising as a foundational substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity scenarios.

## Open Questions

- What specific productivity benchmarks were used for the in-domain and out-of-domain evaluations?
- How much of the performance gain comes from the synthetic computer environments versus the long-horizon simulation procedure itself?
- What generation pipeline is used to ensure the synthetic folder structures and artifacts are realistic?
- How are productivity objectives sampled to match a user's context and a month of human work?
- What failures or limitations were observed in the long-horizon simulations?
