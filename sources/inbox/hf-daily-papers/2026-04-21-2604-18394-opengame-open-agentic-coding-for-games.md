---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, reinforcement-learning, post-training, llm-systems, code-agents, evaluation, web-games]
source_count: 1
updated: 2026-04-22
source_url: https://arxiv.org/abs/2604.18394
paper_id: 2604.18394
published: 2026-04-20T04:00:00+08:00
submitted_on_daily: 2026-04-21T11:26:21+08:00
decision: accept
score: 93
generator: scripts/update_hf_daily_papers.py
---

# OpenGame: Open Agentic Coding for Games

## Summary

- one_sentence_summary: OpenGame is an open-source agentic framework for end-to-end web game creation that combines reusable game-building skills, a specialized code model, and a benchmark for evaluating playable games.
- why_relevant: It is directly relevant to reinforcement learning, post-training, and agentic tool-using systems because it applies execution-grounded RL to a code agent and evaluates end-to-end behavior in an interactive environment.
- filter_reason: Strongly aligned with agentic coding, execution-grounded RL, and agent evaluation for interactive environments.
- hugging_face_paper: https://huggingface.co/papers/2604.18394
- original_paper: https://arxiv.org/abs/2604.18394
- source_basis: `original abstract page`

## Key Points

- Introduces `Game Skill`, which combines a `Template Skill` for accumulating reusable project skeletons and a `Debug Skill` for maintaining verified fixes across game projects.
- Uses `GameCoder-27B`, a code LLM trained with continual pre-training, supervised fine-tuning, and execution-grounded reinforcement learning.
- Argues that static code checks are insufficient for interactive games, so evaluation must account for playability and integration across many files and engine state.
- Proposes `OpenGame-Bench`, which measures `Build Health`, `Visual Usability`, and `Intent Alignment` using headless browser execution and VLM judging.
- Reports state-of-the-art results across 150 diverse game prompts, suggesting agentic code systems can move beyond isolated programming tasks into complex interactive applications.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.18394
- Hugging Face API entry: https://huggingface.co/api/papers/2604.18394
- arXiv abstract: https://arxiv.org/abs/2604.18394
- GitHub: https://github.com/leigest519/OpenGame
- Project page: https://www.opengame-project-page.com/

## Paper Metadata

- authors: `Yilei Jiang`, `Jinyuan Hu`, `Qianyin Xiao`, `Yaozhi Zheng`, `Ruize Ma`, `Kaituo Feng`, `Jiaming Han`, `Tianshuo Peng`, `Kaixuan Fan`, `Manyuan Zhang`, `Xiangyu Yue`
- ai_keywords: `Large Language Models`, `code agents`, `game engines`, `real-time loops`, `cross-file inconsistencies`, `scene wiring`, `logical incoherence`, `Game Skill`, `Template Skill`, `Debug Skill`, `GameCoder-27B`, `continual pre-training`, `supervised fine-tuning`, `execution-grounded reinforcement learning`, `OpenGame-Bench`, `Build Health`, `Visual Usability`, `Intent Alignment`, `headless browser execution`, `VLM judging`
- upvotes: `49`
- num_comments: `1`
- abstract: Game development sits at the intersection of creative design and intricate software engineering, demanding the joint orchestration of game engines, real-time loops, and tightly coupled state across many files. While Large Language Models (LLMs) and code agents now solve isolated programming tasks with ease, they consistently stumble when asked to produce a fully playable game from a high-level design, collapsing under cross-file inconsistencies, broken scene wiring, and logical incoherence. We bridge this gap with OpenGame, the first open-source agentic framework explicitly designed for end-to-end web game creation. At its core lies Game Skill, a reusable, evolving capability composed of a Template Skill that grows a library of project skeletons from experience and a Debug Skill that maintains a living protocol of verified fixes - together enabling the agent to scaffold stable architectures and systematically repair integration errors rather than patch isolated syntax bugs. Powering this framework is GameCoder-27B, a code LLM specialized for game engine mastery through a three-stage pipeline of continual pre-training, supervised fine-tuning, and execution-grounded reinforcement learning. Since verifying interactive playability is fundamentally harder than checking static code, we further introduce OpenGame-Bench, an evaluation pipeline that scores agentic game generation along Build Health, Visual Usability, and Intent Alignment via headless browser execution and VLM judging. Across 150 diverse game prompts, OpenGame establishes a new state-of-the-art. We hope OpenGame pushes code agents beyond discrete software engineering problems and toward building complex, interactive real-world applications. Our framework will be fully open-sourced.
- hf_ai_summary: OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

## Source Excerpt

Game development sits at the intersection of creative design and intricate software engineering, demanding the joint orchestration of game engines, real-time loops, and tightly coupled state across many files. While Large Language Models (LLMs) and code agents now solve isolated programming tasks with ease, they consistently stumble when asked to produce a fully playable game from a high-level design, collapsing under cross-file inconsistencies, broken scene wiring, and logical incoherence. We bridge this gap with OpenGame, the first open-source agentic framework explicitly designed for end-to-end web game creation. At its core lies Game Skill, a reusable, evolving capability composed of a Template Skill that grows a library of project skeletons from experience and a Debug Skill that maintains a living protocol of verified fixes - together enabling the agent to scaffold stable architectures and systematically repair integration errors rather than patch isolated syntax bugs. Powering this framework is GameCoder-27B, a code LLM specialized for game engine mastery through a three-stage pipeline of continual pre-training, supervised fine-tuning, and execution-grounded reinforcement learning. Since verifying interactive playability is fundamentally harder than checking static code, we further introduce OpenGame-Bench, an evaluation pipeline that scores agentic game generation along Build Health, Visual Usability, and Intent Alignment via headless browser execution and VLM judging. Across 150 diverse game prompts, OpenGame establishes a new state-of-the-art. We hope OpenGame pushes code agents beyond discrete software engineering problems and toward building complex, interactive real-world applications. Our framework will be fully open-sourced.

## Open Questions

- How much of the gain comes from execution-grounded reinforcement learning versus continual pre-training or supervised fine-tuning?
- What specific game engines or web game stacks does OpenGame support in practice?
- How is `Intent Alignment` operationalized in the VLM judging pipeline?
- Does the benchmark generalize to non-game interactive applications, or is it game-specific?
