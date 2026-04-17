---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, agent-evals, post-training, theory-of-mind, adversarial-interaction, evaluation]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.11666
paper_id: 2604.11666
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-14T13:14:49+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Playing Along: Learning a Double-Agent Defender for Belief Steering via Theory of Mind

## Summary

- one_sentence_summary: The paper introduces ToM-SB, a privacy-themed theory-of-mind benchmark where a defender must mislead an attacker about extracting sensitive information, and shows that reinforcement learning can train AI double agents that improve both belief-steering and theory-of-mind performance.
- why_relevant: It directly connects reinforcement learning, agentic interaction, and post-training behavior shaping, while also providing an evaluation setup for belief modeling in adversarial dialogue systems.
- filter_reason: Strongly aligned with RL for agent behavior shaping and adversarial agent interaction, with a concrete ToM-based training method and evaluation.
- hugging_face_paper: https://huggingface.co/papers/2604.11666
- original_paper: https://arxiv.org/abs/2604.11666
- source_basis: `original abstract page`

## Key Points

- ToM-SB is a shared-universe adversarial dialogue task in which the defender acts as a double agent and must steer the attacker’s beliefs under partial attacker prior knowledge.
- The task is designed to test whether a model can form and use a theory of mind in a security- or privacy-flavored setting.
- Strong frontier models such as Gemini3-Pro and GPT-5.4 struggle on hard ToM-SB scenarios, including when prompted to reason about the attacker’s beliefs.
- The authors train defender models with reinforcement learning using fooling rewards, theory-of-mind rewards, or both, and find a bidirectional relationship: optimizing one objective improves the other.
- Across four attackers, six defender methods, in-distribution and out-of-distribution evaluation, combined ToM plus fooling rewards give the strongest results and outperform prompted frontier models on hard scenarios.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.11666
- Hugging Face API entry: https://huggingface.co/api/papers/2604.11666
- arXiv abstract: https://arxiv.org/abs/2604.11666
- GitHub: https://github.com/The-Inscrutable-X/AIDoubleAgentDefenders

## Paper Metadata

- authors: `Hanqi Xiao`, `Vaidehi Patil`, `Zaid Khan`, `Hyunji Lee`, `Elias Stengel-Eskin`, `Mohit Bansal`
- ai_keywords: `large language models`, `theory-of-mind`, `adversarial interaction`, `reinforcement learning`, `AI double agents`, `belief manipulation`, `reward optimization`, `ToM prompting`
- upvotes: `3`
- num_comments: `2`
- abstract: As large language models (LLMs) become the engine behind conversational systems, their ability to reason about the intentions and states of their dialogue partners (i.e., form and use a theory-of-mind, or ToM) becomes increasingly critical for safe interaction with potentially adversarial partners. We propose a novel privacy-themed ToM challenge, ToM for Steering Beliefs (ToM-SB), in which a defender must act as a Double Agent to steer the beliefs of an attacker with partial prior knowledge within a shared universe. To succeed on ToM-SB, the defender must engage with and form a ToM of the attacker, with a goal of fooling the attacker into believing they have succeeded in extracting sensitive information. We find that strong frontier models like Gemini3-Pro and GPT-5.4 struggle on ToM-SB, often failing to fool attackers in hard scenarios with partial attacker prior knowledge, even when prompted to reason about the attacker's beliefs (ToM prompting). To close this gap, we train models on ToM-SB to act as AI Double Agents using reinforcement learning, testing both fooling and ToM rewards. Notably, we find a bidirectionally emergent relationship between ToM and attacker-fooling: rewarding fooling success alone improves ToM, and rewarding ToM alone improves fooling. Across four attackers with different strengths, six defender methods, and both in-distribution and out-of-distribution (OOD) evaluation, we find that gains in ToM and attacker-fooling are well-correlated, highlighting belief modeling as a key driver of success on ToM-SB. AI Double Agents that combine both ToM and fooling rewards yield the strongest fooling and ToM performance, outperforming Gemini3-Pro and GPT-5.4 with ToM prompting on hard scenarios. We also show that ToM-SB and AI Double Agents can be extended to stronger attackers, demonstrating generalization to OOD settings and the upgradability of our task.
- hf_ai_summary: Large language models face challenges in theory-of-mind reasoning for adversarial interactions, but reinforcement learning-trained AI double agents demonstrate improved belief manipulation and theory-of-mind capabilities through bidirectional reward optimization.

## Source Excerpt

As large language models (LLMs) become the engine behind conversational systems, their ability to reason about the intentions and states of their dialogue partners (i.e., form and use a theory-of-mind, or ToM) becomes increasingly critical for safe interaction with potentially adversarial partners. We propose a novel privacy-themed ToM challenge, ToM for Steering Beliefs (ToM-SB), in which a defender must act as a Double Agent to steer the beliefs of an attacker with partial prior knowledge within a shared universe. To succeed on ToM-SB, the defender must engage with and form a ToM of the attacker, with a goal of fooling the attacker into believing they have succeeded in extracting sensitive information. We find that strong frontier models like Gemini3-Pro and GPT-5.4 struggle on ToM-SB, often failing to fool attackers in hard scenarios with partial attacker prior knowledge, even when prompted to reason about the attacker's beliefs (ToM prompting). To close this gap, we train models on ToM-SB to act as AI Double Agents using reinforcement learning, testing both fooling and ToM rewards. Notably, we find a bidirectionally emergent relationship between ToM and attacker-fooling: rewarding fooling success alone improves ToM, and rewarding ToM alone improves fooling. Across four attackers with different strengths, six defender methods, and both in-distribution and out-of-distribution (OOD) evaluation, we find that gains in ToM and attacker-fooling are well-correlated, highlighting belief modeling as a key driver of success on ToM-SB. AI Double Agents that combine both ToM and fooling rewards yield the strongest fooling and ToM performance, outperforming Gemini3-Pro and GPT-5.4 with ToM prompting on hard scenarios. We also show that ToM-SB and AI Double Agents can be extended to stronger attackers, demonstrating generalization to OOD settings and the upgradability of our task.

## Open Questions

- What exact reward formulations were used for the fooling and ToM objectives?
- How was theory-of-mind measured quantitatively on ToM-SB?
- What were the six defender methods compared in the experiments?
- How much stronger were the out-of-distribution attackers, and what did upgradability require in practice?
