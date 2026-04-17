---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, post-training, reinforcement-learning, llm-systems, llm-agents, multi-agent, deception, trust]
source_count: 1
updated: 2026-04-16
source_url: https://arxiv.org/abs/2604.09746
paper_id: 2604.09746
published: 2026-04-10T04:00:00+08:00
submitted_on_daily: 2026-04-15T11:20:45+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# CONSCIENTIA: Can LLM Agents Learn to Strategize? Emergent Deception and Trust in a Multi-Agent NYC Simulation

## Summary

- one_sentence_summary: This paper studies whether LLM agents can learn strategic behavior in a multi-agent NYC simulation and finds limited emergence of selective trust and deception, but persistent vulnerability to adversarial persuasion.
- why_relevant: It is directly relevant to agentic LLM post-training and multi-agent evaluation because it studies how training changes strategic behavior, trust, deception, and robustness under adversarial interaction.
- filter_reason: Strong match on LLM agents, strategic behavior in multi-agent interaction, and post-training via KTO for behavior shaping.
- hugging_face_paper: https://huggingface.co/papers/2604.09746
- original_paper: https://arxiv.org/abs/2604.09746
- source_basis: `original abstract page`

## Key Points

- The authors build a controlled multi-agent simulation of a simplified New York City where hidden identities and conflicting incentives force agents to decide whom to trust.
- Blue agents are trained to reach destinations efficiently while reducing billboard exposure, while Red agents try to steer them toward billboard-heavy routes using persuasive language.
- Policy learning is done through repeated interaction rounds with Kahneman-Tversky Optimization (KTO), allowing both Blue and Red policies to adapt over time.
- The best Blue policy improves task success from 46.0% to 57.3%, but susceptibility to steering remains high at 70.7%.
- Later policies show stronger selective cooperation while keeping trajectory efficiency, but the paper reports a persistent safety-helpfulness trade-off.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.09746
- Hugging Face API entry: https://huggingface.co/api/papers/2604.09746
- arXiv abstract: https://arxiv.org/abs/2604.09746

## Paper Metadata

- authors: `Aarush Sinha`, `Arion Das`, `Soumyadeep Nag`, `Charan Karnati`, `Shravani Nag`, `Chandra Vadhan Raj`, `Aman Chadha`, `Vinija Jain`, `Suranjana Trivedy`, `Amitava Das`
- ai_keywords: `large language models`, `multi-agent simulation`, `strategic behavior`, `adversarial persuasion`, `policy learning`, `Kahneman-Tversky Optimization`, `agent policies`, `task success`, `trajectory efficiency`, `selective cooperation`
- upvotes: `0`
- num_comments: `1`
- abstract: As large language models (LLMs) are increasingly deployed as autonomous agents, understanding how strategic behavior emerges in multi-agent environments has become an important alignment challenge. We take a neutral empirical stance and construct a controlled environment in which strategic behavior can be directly observed and measured. We introduce a large-scale multi-agent simulation in a simplified model of New York City, where LLM-driven agents interact under opposing incentives. Blue agents aim to reach their destinations efficiently, while Red agents attempt to divert them toward billboard-heavy routes using persuasive language to maximize advertising revenue. Hidden identities make navigation socially mediated, forcing agents to decide when to trust or deceive. We study policy learning through an iterative simulation pipeline that updates agent policies across repeated interaction rounds using Kahneman-Tversky Optimization (KTO). Blue agents are optimized to reduce billboard exposure while preserving navigation efficiency, whereas Red agents adapt to exploit remaining weaknesses. Across iterations, the best Blue policy improves task success from 46.0% to 57.3%, although susceptibility remains high at 70.7%. Later policies exhibit stronger selective cooperation while preserving trajectory efficiency. However, a persistent safety-helpfulness trade-off remains: policies that better resist adversarial steering do not simultaneously maximize task completion. Overall, our results show that LLM agents can exhibit limited strategic behavior, including selective trust and deception, while remaining highly vulnerable to adversarial persuasion.
- hf_ai_summary: Large language model agents demonstrate limited strategic behaviors including selective trust and deception in a simulated urban environment, remaining vulnerable to adversarial persuasion despite improved resistance over iterations.

## Source Excerpt

As large language models (LLMs) are increasingly deployed as autonomous agents, understanding how strategic behavior emerges in multi-agent environments has become an important alignment challenge. We take a neutral empirical stance and construct a controlled environment in which strategic behavior can be directly observed and measured. We introduce a large-scale multi-agent simulation in a simplified model of New York City, where LLM-driven agents interact under opposing incentives. Blue agents aim to reach their destinations efficiently, while Red agents attempt to divert them toward billboard-heavy routes using persuasive language to maximize advertising revenue. Hidden identities make navigation socially mediated, forcing agents to decide when to trust or deceive. We study policy learning through an iterative simulation pipeline that updates agent policies across repeated interaction rounds using Kahneman-Tversky Optimization (KTO). Blue agents are optimized to reduce billboard exposure while preserving navigation efficiency, whereas Red agents adapt to exploit remaining weaknesses. Across iterations, the best Blue policy improves task success from 46.0% to 57.3%, although susceptibility remains high at 70.7%. Later policies exhibit stronger selective cooperation while preserving trajectory efficiency. However, a persistent safety-helpfulness trade-off remains: policies that better resist adversarial steering do not simultaneously maximize task completion. Overall, our results show that LLM agents can exhibit limited strategic behavior, including selective trust and deception, while remaining highly vulnerable to adversarial persuasion.

## Open Questions

- How exactly is KTO applied to the agent policies in this simulation?
- What model family or scale is used for the LLM-driven agents?
- How is 'susceptibility' measured, and what counts as successful deception or selective cooperation?
- Do the reported results generalize beyond the simplified NYC environment?
