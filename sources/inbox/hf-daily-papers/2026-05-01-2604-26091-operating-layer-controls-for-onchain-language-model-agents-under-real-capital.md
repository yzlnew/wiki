---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, agent-evals, llm-systems, post-training, rl, evaluation, onchain, reliability]
source_count: 1
updated: 2026-05-01
source_url: https://arxiv.org/abs/2604.26091
paper_id: 2604.26091
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-05-01T00:25:18+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital

## Summary

- one_sentence_summary: This paper reports a 21-day deployment of real-capital onchain language-model agents and argues that reliability came from the surrounding operating layer, not the base model alone.
- why_relevant: It is directly relevant to agentic tool use and post-training/evaluation because it studies how to make long-horizon language-model agents reliable when they must plan, validate, and execute actions under real constraints.
- filter_reason: Real-capital agent deployment with concrete operating-layer reliability, validation, and evaluation details is directly relevant to agents and agent systems.
- hugging_face_paper: https://huggingface.co/papers/2604.26091
- original_paper: https://arxiv.org/abs/2604.26091
- source_basis: `original abstract page`

## Key Points

- DX Terminal Pro deployed 3,505 user-funded agents in a bounded onchain market where agents handled normal buy/sell decisions under user-configured vault controls.
- The deployment generated large-scale traces: 7.5M agent invocations, about 300K onchain actions, about $20M in volume, more than 5,000 ETH deployed, and roughly 70B inference tokens.
- Policy-valid submitted transactions achieved 99.9% settlement success, suggesting the system was robust at the action-execution layer.
- Reliability depended on prompt compilation, typed controls, policy validation, execution guards, memory design, and trace-level observability rather than model capability alone.
- Pre-launch testing found failure modes that standard text benchmarks miss, including fabricated trading rules, fee paralysis, numeric anchoring, cadence trading, and misread tokenomics; targeted harness changes improved these behaviors materially.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.26091
- Hugging Face API entry: https://huggingface.co/api/papers/2604.26091
- arXiv abstract: https://arxiv.org/abs/2604.26091
- Project page: https://www.dxrg.ai/

## Paper Metadata

- authors: `T. J. Barton`, `Chris Constantakis`, `Patti Hauseman`, `Annie Mous`, `Alaska Hoffman`, `Brian Bergeron`, `Hunter Goodreau`
- organization: `DXRG AI Inc`
- ai_keywords: `language-model agents`, `tool actions`, `onchain market`, `agent invocations`, `inference tokens`, `settlement success`, `prompt compilation`, `policy validation`, `execution guards`, `memory design`, `trace-level observability`
- upvotes: `4`
- num_comments: `2`
- abstract: We study reliability in autonomous language-model agents that translate user mandates into validated tool actions under real capital. The setting is DX Terminal Pro, a 21-day deployment in which 3,505 user-funded agents traded real ETH in a bounded onchain market. Users configured vaults through structured controls and natural-language strategies, but only agents could choose normal buy/sell trades. The system produced 7.5M agent invocations, roughly 300K onchain actions, about $20M in volume, more than 5,000 ETH deployed, roughly 70B inference tokens, and 99.9% settlement success for policy-valid submitted transactions. Long-running agents accumulated thousands of sequential decisions, including 6,000+ prompt-state-action cycles for continuously active agents, yielding a large-scale trace from user mandate to rendered prompt, reasoning, validation, portfolio state, and settlement. Reliability did not come from the base model alone; it emerged from the operating layer around the model: prompt compilation, typed controls, policy validation, execution guards, memory design, and trace-level observability. Pre-launch testing exposed failures that text-only benchmarks rarely measure, including fabricated trading rules, fee paralysis, numeric anchoring, cadence trading, and misread tokenomics. Targeted harness changes reduced fabricated sell rules from 57% to 3%, reduced fee-led observations from 32.5% to below 10%, and increased capital deployment from 42.9% to 78.0% in an affected test population. We show that capital-managing agents should be evaluated across the full path from user mandate to prompt, validated action, and settlement.
- hf_ai_summary: Autonomous language-model agents managing real cryptocurrency trades demonstrated high reliability through comprehensive system design encompassing prompt compilation, policy validation, and execution safeguards rather than relying solely on base model performance.

## Source Excerpt

We study reliability in autonomous language-model agents that translate user mandates into validated tool actions under real capital. The setting is DX Terminal Pro, a 21-day deployment in which 3,505 user-funded agents traded real ETH in a bounded onchain market. Users configured vaults through structured controls and natural-language strategies, but only agents could choose normal buy/sell trades. The system produced 7.5M agent invocations, roughly 300K onchain actions, about $20M in volume, more than 5,000 ETH deployed, roughly 70B inference tokens, and 99.9% settlement success for policy-valid submitted transactions. Long-running agents accumulated thousands of sequential decisions, including 6,000+ prompt-state-action cycles for continuously active agents, yielding a large-scale trace from user mandate to rendered prompt, reasoning, validation, portfolio state, and settlement. Reliability did not come from the base model alone; it emerged from the operating layer around the model: prompt compilation, typed controls, policy validation, execution guards, memory design, and trace-level observability. Pre-launch testing exposed failures that text-only benchmarks rarely measure, including fabricated trading rules, fee paralysis, numeric anchoring, cadence trading, and misread tokenomics. Targeted harness changes reduced fabricated sell rules from 57% to 3%, reduced fee-led observations from 32.5% to below 10%, and increased capital deployment from 42.9% to 78.0% in an affected test population. We show that capital-managing agents should be evaluated across the full path from user mandate to prompt, validated action, and settlement.

## Open Questions

- What base model or models powered the agents, and were different model variants compared?
- How exactly were prompt compilation, typed controls, and execution guards implemented?
- What criteria defined a policy-valid transaction and what kinds of policy violations were observed before filtering?
- How representative is the bounded onchain market of other real-world agent deployment settings?
- Were the reported harness improvements measured on held-out scenarios or only on the affected test population?
