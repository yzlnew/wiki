---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, agents, tool-use, llm-systems, post-training, multimodal, visual-reasoning]
source_count: 1
updated: 2026-04-24
source_url: https://arxiv.org/abs/2604.19945
paper_id: 2604.19945
published: 2026-04-21T04:00:00+08:00
submitted_on_daily: 2026-04-23T13:34:53+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Visual Reasoning through Tool-supervised Reinforcement Learning

## Summary

- one_sentence_summary: ToolsRL is a two-stage reinforcement learning framework for multimodal large language models that uses direct tool supervision to learn visual tool use before optimizing task accuracy on complex visual reasoning problems.
- why_relevant: The paper is directly relevant to reinforcement learning post-training for tool-using multimodal agents, and it also speaks to how curricula can structure agentic tool competence.
- filter_reason: Directly combines reinforcement learning with tool-use training for multimodal reasoning agents.
- hugging_face_paper: https://huggingface.co/papers/2604.19945
- original_paper: https://arxiv.org/abs/2604.19945
- source_basis: `original abstract page`

## Key Points

- Introduces Tool-supervised Reinforcement Learning (ToolsRL) for teaching MLLMs to use visual tools more effectively.
- Uses simple, interpretable tools such as zoom-in, rotate, flip, and draw point/line, chosen because their supervision is easy to collect.
- Training is staged: first optimize tool-specific rewards to learn tool calling, then train with accuracy-targeted rewards while tools remain available.
- The curriculum is designed to reduce optimization conflicts between learning to call tools and learning to solve the downstream reasoning task.
- The paper reports that the curriculum is efficient and yields strong tool-use capabilities on complex visual reasoning tasks.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.19945
- Hugging Face API entry: https://huggingface.co/api/papers/2604.19945
- arXiv abstract: https://arxiv.org/abs/2604.19945

## Paper Metadata

- authors: `Qihua Dong`, `Gozde Sahin`, `Pei Wang`, `Zhaowei Cai`, `Robik Shrestha`, `Hao Yang`, `Davide Modolo`
- organization: `Amazon AGI`
- ai_keywords: `Tool-supervised Reinforcement Learning`, `multimodal large language models`, `visual reasoning tasks`, `tool-use learning`, `reinforcement learning curriculum`, `tool-specific rewards`, `accuracy targeted rewards`, `tool calling capability`
- upvotes: `3`
- num_comments: `1`
- abstract: In this paper, we investigate the problem of how to effectively master tool-use to solve complex visual reasoning tasks for Multimodal Large Language Models. To achieve that, we propose a novel Tool-supervised Reinforcement Learning (ToolsRL) framework, with direct tool supervision for more effective tool-use learning. We focus on a series of simple, native, and interpretable visual tools, including zoom-in, rotate, flip, and draw point/line, whose tool supervision is easy to collect. A reinforcement learning curriculum is developed, where the first stage is solely optimized by a set of well motivated tool-specific rewards, and the second stage is trained with the accuracy targeted rewards while allowing calling tools. In this way, tool calling capability is mastered before using tools to complete visual reasoning tasks, avoiding the potential optimization conflict among those heterogeneous tasks. Our experiments have shown that the tool-supervised curriculum training is efficient and ToolsRL can achieve strong tool-use capabilities for complex visual reasoning tasks.
- hf_ai_summary: A novel Tool-supervised Reinforcement Learning framework is presented that enables multimodal large language models to effectively learn tool-use for complex visual reasoning through a two-stage curriculum approach.

## Source Excerpt

In this paper, we investigate the problem of how to effectively master tool-use to solve complex visual reasoning tasks for Multimodal Large Language Models. To achieve that, we propose a novel Tool-supervised Reinforcement Learning (ToolsRL) framework, with direct tool supervision for more effective tool-use learning. We focus on a series of simple, native, and interpretable visual tools, including zoom-in, rotate, flip, and draw point/line, whose tool supervision is easy to collect. A reinforcement learning curriculum is developed, where the first stage is solely optimized by a set of well motivated tool-specific rewards, and the second stage is trained with the accuracy targeted rewards while allowing calling tools. In this way, tool calling capability is mastered before using tools to complete visual reasoning tasks, avoiding the potential optimization conflict among those heterogeneous tasks. Our experiments have shown that the tool-supervised curriculum training is efficient and ToolsRL can achieve strong tool-use capabilities for complex visual reasoning tasks.

## Open Questions

- Which visual reasoning benchmarks were used to evaluate ToolsRL?
- How does ToolsRL compare against non-curriculum RL or supervised tool-use baselines?
- What exact reward functions were used in each curriculum stage?
- How much tool supervision data was needed for the visual tools?
- Does the approach generalize beyond the specific tools listed in the paper?
