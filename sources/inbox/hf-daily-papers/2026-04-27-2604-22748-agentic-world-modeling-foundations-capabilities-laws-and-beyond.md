---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, reinforcement-learning, world-models, survey, taxonomy, evaluation]
source_count: 1
updated: 2026-04-27
source_url: https://arxiv.org/abs/2604.22748
paper_id: 2604.22748
published: 2026-04-24T04:00:00+08:00
submitted_on_daily: 2026-04-27T08:04:03+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

## Summary

- one_sentence_summary: This survey proposes a two-axis taxonomy for world models, separating capability into predictor, simulator, and evolver levels and organizing environments by physical, digital, social, and scientific law regimes.
- why_relevant: It directly connects reinforcement learning, agentic systems, and environment modeling by organizing how predictive world models support action-taking agents across physical, digital, social, and scientific settings.
- filter_reason: A technically grounded world-model roadmap with strong overlap in agents, environment interaction, and evaluation methodology.
- hugging_face_paper: https://huggingface.co/papers/2604.22748
- original_paper: https://arxiv.org/abs/2604.22748
- source_basis: `original abstract page`

## Key Points

- Introduces a "levels x laws" framework: L1 Predictor learns one-step transitions, L2 Simulator composes action-conditioned multi-step rollouts, and L3 Evolver updates its own model when predictions fail.
- Defines four governing-law regimes for world models: physical, digital, social, and scientific, emphasizing that each regime imposes different constraints and failure modes.
- Synthesizes over 400 papers and summarizes more than 100 representative systems across model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery.
- Analyzes methods, failure modes, and evaluation practices across level-regime pairs, and proposes decision-centric evaluation principles plus a minimal reproducible evaluation package.
- Frames world modeling as a bottleneck for sustained interaction agents that manipulate objects, navigate software, coordinate with others, or design experiments.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.22748
- Hugging Face API entry: https://huggingface.co/api/papers/2604.22748
- arXiv abstract: https://arxiv.org/abs/2604.22748
- GitHub: https://github.com/matrix-agent/awesome-agentic-world-modeling
- Project page: https://agentic-world-modeling.xyz/

## Paper Metadata

- authors: `Meng Chu`, `Xuan Billy Zhang`, `Kevin Qinghong Lin`, `Lingdong Kong`, `Jize Zhang`, `Teng Tu`, `Weijian Ma`, `Ziqi Huang`, `Senqiao Yang`, `Wei Huang`, `Yeying Jin`, `Zhefan Rao`, `Jinhui Ye`, `Xinyu Lin`, `Xichen Zhang`, `Qisheng Hu`, `Shuai Yang`, `Leyang Shen`, `Wei Chow`, `Yifei Dong`, `Fengyi Wu`, `Quanyu Long`, `Bin Xia`, `Shaozuo Yu`, `Mingkang Zhu`, `Wenhu Zhang`, `Jiehui Huang`, `Haokun Gui`, `Haoxuan Che`, `Long Chen`, `Qifeng Chen`, `Wenxuan Zhang`, `Wenya Wang`, `Xiaojuan Qi`, `Yang Deng`, `Yanwei Li`, `Mike Zheng Shou`, `Zhi-Qi Cheng`, `See-Kiong Ng`, `Ziwei Liu`, `Philip Torr`, `Jiaya Jia`
- ai_keywords: `world model`, `levels x laws taxonomy`, `L1 Predictor`, `L2 Simulator`, `L3 Evolver`, `predictive environment models`, `model-based reinforcement learning`, `video generation`, `web agents`, `GUI agents`, `multi-agent social simulation`, `AI-driven scientific discovery`, `action-conditioned rollouts`, `domain laws`, `failure modes`, `evaluation practices`, `architectural guidance`, `open problems`, `governance challenges`
- upvotes: `0`
- num_comments: `0`
- abstract: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
- hf_ai_summary: World models are categorized into three capability levels and four law regimes to better understand and develop predictive environment models for AI agents across diverse domains.

## Source Excerpt

As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.

## Open Questions

- What are the concrete criteria used to distinguish L1, L2, and L3 systems in borderline cases?
- What does the proposed minimal reproducible evaluation package include?
- Which failure modes are most common for each law regime?
- How do the recommended evaluation principles differ for web and GUI agents versus scientific discovery systems?
