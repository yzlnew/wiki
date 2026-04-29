---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, agent-evals, environment-interaction, reasoning-behavior-shaping, llm-systems, llm-agents, long-horizon, skill-bank, skill-retrieval, interactive-environments, game-playing]
source_count: 1
updated: 2026-04-25
source_url: https://arxiv.org/abs/2604.20987
paper_id: 2604.20987
published: 2026-04-22T04:00:00+08:00
submitted_on_daily: 2026-04-24T10:38:50+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks

## Summary

- one_sentence_summary: COSPLAY is a co-evolution framework for long-horizon LLM agents that pairs a decision agent with a learnable skill bank to improve skill retrieval, action generation, and reusable skill discovery across episodes.
- why_relevant: It is directly about agent architectures for long-horizon decision making and tool-like skill reuse, with an evaluation focused on interactive environments and reward-based performance.
- filter_reason: Directly targets agent architectures for long-horizon interaction with skill retrieval, skill discovery, and delayed-reward decision making.
- hugging_face_paper: https://huggingface.co/papers/2604.20987
- original_paper: https://arxiv.org/abs/2604.20987
- source_basis: `original abstract page`

## Key Points

- The paper frames long-horizon interactive environments as a testbed for multi-step reasoning, skill chaining, delayed rewards, and partial observability.
- COSPLAY couples an LLM decision agent with a managed skill pipeline that discovers reusable skills from unlabeled rollouts and stores them in a learnable skill bank.
- The decision agent retrieves skills from the bank to guide action taking, while the skill pipeline continually extracts, refines, and updates skills and their contracts.
- The authors report experiments across six game environments, with an 8B base model achieving over 25.1 percent average reward improvement versus four frontier LLM baselines on single-player benchmarks.
- The system is reported to remain competitive on multi-player social reasoning games, suggesting the approach generalizes beyond isolated task settings.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.20987
- Hugging Face API entry: https://huggingface.co/api/papers/2604.20987
- arXiv abstract: https://arxiv.org/abs/2604.20987
- GitHub: https://github.com/wuxiyang1996/cos-play
- Project page: https://wuxiyang1996.github.io/COSPLAY_page/

## Paper Metadata

- authors: `Xiyang Wu`, `Zongxia Li`, `Guangyao Shi`, `Alexander Duffy`, `Tyler Marques`, `Matthew Lyle Olson`, `Tianyi Zhou`, `Dinesh Manocha`
- organization: `Good Start Labs`
- ai_keywords: `large language models`, `skill bank`, `co-evolution framework`, `skill retrieval`, `action generation`, `skill discovery`, `skill refinement`, `delayed rewards`, `partial observability`, `multi-step reasoning`, `skill chaining`
- upvotes: `14`
- num_comments: `2`
- abstract: Long horizon interactive environments are a testbed for evaluating agents skill usage abilities. These environments demand multi step reasoning, the chaining of multiple skills over many timesteps, and robust decision making under delayed rewards and partial observability. Games are a good testbed for evaluating agent skill usage in environments. Large Language Models (LLMs) offer a promising alternative as game playing agents, but they often struggle with consistent long horizon decision making because they lack a mechanism to discover, retain, and reuse structured skills across episodes. We present COSPLAY, a co evolution framework in which an LLM decision agent retrieves skills from a learnable skill bank to guide action taking, while an agent managed skill pipeline discovers reusable skills from the agents unlabeled rollouts to form a skill bank. Our framework improves both the decision agent to learn better skill retrieval and action generation, while the skill bank agent continually extracts, refines, and updates skills together with their contracts. Experiments across six game environments show that COSPLAY with an 8B base model achieves over 25.1 percent average reward improvement against four frontier LLM baselines on single player game benchmarks while remaining competitive on multi player social reasoning games.
- hf_ai_summary: A co-evolution framework enables large language models to discover, retain, and reuse structured skills across episodes in long-horizon interactive environments through a learnable skill bank and skill pipeline.

## Source Excerpt

Long horizon interactive environments are a testbed for evaluating agents skill usage abilities. These environments demand multi step reasoning, the chaining of multiple skills over many timesteps, and robust decision making under delayed rewards and partial observability. Games are a good testbed for evaluating agent skill usage in environments. Large Language Models (LLMs) offer a promising alternative as game playing agents, but they often struggle with consistent long horizon decision making because they lack a mechanism to discover, retain, and reuse structured skills across episodes. We present COSPLAY, a co evolution framework in which an LLM decision agent retrieves skills from a learnable skill bank to guide action taking, while an agent managed skill pipeline discovers reusable skills from the agents unlabeled rollouts to form a skill bank. Our framework improves both the decision agent to learn better skill retrieval and action generation, while the skill bank agent continually extracts, refines, and updates skills together with their contracts. Experiments across six game environments show that COSPLAY with an 8B base model achieves over 25.1 percent average reward improvement against four frontier LLM baselines on single player game benchmarks while remaining competitive on multi player social reasoning games.

## Open Questions

- How are skills represented in the bank, and what does a skill contract contain?
- What is the training or update loop that co-evolves the decision agent and skill pipeline?
- Which six game environments were used, and how does performance vary by environment?
- How much of the gain comes from skill retrieval versus skill discovery and refinement?
- Does the method transfer to non-game tool-using tasks or general agent benchmarks?
