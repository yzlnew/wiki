---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, agents, agent-evals, reward-modeling, credit-assignment, shapley-values, social-dialogue, sotopia]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.18982
paper_id: 2604.18982
published: 2026-04-21T04:00:00+08:00
submitted_on_daily: 2026-04-23T13:53:25+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution

## Summary

- one_sentence_summary: SAVOIR proposes a cooperative-game-theory-based reinforcement learning framework for social dialogue agents that assigns credit to utterances with expected utility shifts and Shapley values, and reports state-of-the-art results on SOTOPIA.
- why_relevant: This is directly relevant to reinforcement learning post-training for agents, especially reward attribution and training language agents for interactive, tool-less but socially complex environments.
- filter_reason: Directly relevant to RL credit assignment for language agents, with principled reward attribution and benchmarked post-training results.
- hugging_face_paper: https://huggingface.co/papers/2604.18982
- original_paper: https://arxiv.org/abs/2604.18982
- source_basis: `original abstract page`

## Key Points

- The paper targets the credit assignment problem in multi-turn social dialogue RL: how individual utterances contribute to final conversation outcomes.
- Instead of retrospective reward attribution, SAVOIR uses expected utility shifts to estimate an utterance's prospective strategic value for future trajectories.
- Shapley values are used to distribute credit with axiomatic guarantees of efficiency, symmetry, and marginality.
- On the SOTOPIA benchmark, the method reportedly reaches new state-of-the-art results across evaluation settings.
- The authors claim a 7B model with SAVOIR matches or exceeds proprietary systems including GPT-4o and Claude-3.5-Sonnet, while larger reasoning models still underperform.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.18982
- Hugging Face API entry: https://huggingface.co/api/papers/2604.18982
- arXiv abstract: https://arxiv.org/abs/2604.18982
- GitHub: https://github.com/jyyyyy0/SAVOIR

## Paper Metadata

- authors: `Xiachong Feng`, `Yi Jiang`, `Xiaocheng Feng`, `Deyi Yin`, `Libo Qin`, `Yangfan Ye`, `Lei Huang`, `Weitao Ma`, `Yuxuan Gu`, `Chonghan Qin`, `Bing Qin`, `Lingpeng Kong`
- organization: `The University of Hong Kong`
- ai_keywords: `reinforcement learning`, `credit assignment problem`, `language models`, `dialogue outcomes`, `cooperative game theory`, `expected utility shifts`, `Shapley values`, `social intelligence`, `language agents`, `SOTOPIA benchmark`, `episode-level rewards`
- upvotes: `3`
- num_comments: `2`
- abstract: Social intelligence, the ability to navigate complex interpersonal interactions, presents a fundamental challenge for language agents. Training such agents via reinforcement learning requires solving the credit assignment problem: determining how individual utterances contribute to multi-turn dialogue outcomes. Existing approaches directly employ language models to distribute episode-level rewards, yielding attributions that are retrospective and lack theoretical grounding. We propose SAVOIR (ShApley Value fOr SocIal RL), a novel principled framework grounded in cooperative game theory. Our approach combines two complementary principles: expected utility shifts evaluation from retrospective attribution to prospective valuation, capturing an utterance's strategic potential for enabling favorable future trajectories; Shapley values ensure fair credit distribution with axiomatic guarantees of efficiency, symmetry, and marginality. Experiments on the SOTOPIA benchmark demonstrate that SAVOIR achieves new state-of-the-art performance across all evaluation settings, with our 7B model matching or exceeding proprietary models including GPT-4o and Claude-3.5-Sonnet. Notably, even large reasoning models consistently underperform, suggesting social intelligence requires qualitatively different capabilities than analytical reasoning.
- hf_ai_summary: SAVOIR framework uses cooperative game theory to improve social intelligence in language agents by combining expected utility shifts and Shapley values for better credit assignment in dialogue systems.

## Source Excerpt

Social intelligence, the ability to navigate complex interpersonal interactions, presents a fundamental challenge for language agents. Training such agents via reinforcement learning requires solving the credit assignment problem: determining how individual utterances contribute to multi-turn dialogue outcomes. Existing approaches directly employ language models to distribute episode-level rewards, yielding attributions that are retrospective and lack theoretical grounding. We propose SAVOIR (ShApley Value fOr SocIal RL), a novel principled framework grounded in cooperative game theory. Our approach combines two complementary principles: expected utility shifts evaluation from retrospective attribution to prospective valuation, capturing an utterance's strategic potential for enabling favorable future trajectories; Shapley values ensure fair credit distribution with axiomatic guarantees of efficiency, symmetry, and marginality. Experiments on the SOTOPIA benchmark demonstrate that SAVOIR achieves new state-of-the-art performance across all evaluation settings, with our 7B model matching or exceeding proprietary models including GPT-4o and Claude-3.5-Sonnet. Notably, even large reasoning models consistently underperform, suggesting social intelligence requires qualitatively different capabilities than analytical reasoning.

## Open Questions

- How exactly is expected utility shift computed from dialogue context in the training pipeline?
- What reward model or evaluator is used to estimate dialogue outcomes for the Shapley attribution?
- Does the method generalize beyond SOTOPIA-style social dialogue tasks to other agent settings?
- What are the compute and sample-efficiency costs of Shapley-based credit assignment compared with simpler baselines?
