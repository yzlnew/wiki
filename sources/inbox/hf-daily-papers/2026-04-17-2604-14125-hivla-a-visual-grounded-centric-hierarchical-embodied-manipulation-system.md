---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-architectures, environment-interaction, llm-systems, robotics, vla, hierarchical-architecture, visual-grounding, diffusion-transformer, manipulation]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14125
paper_id: 2604.14125
published: 2026-04-15T04:00:00+08:00
submitted_on_daily: 2026-04-17T09:51:03+08:00
decision: accept
score: 79
generator: scripts/update_hf_daily_papers.py
---

# HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System

## Summary

- one_sentence_summary: HiVLA is a hierarchical vision-language-action system that separates VLM-based semantic planning and visual grounding from a diffusion-transformer action executor to preserve reasoning while improving robotic manipulation.
- why_relevant: This is directly relevant to agents and tool-using systems because it proposes a modular planning-and-execution architecture that preserves higher-level reasoning while improving grounded action performance, which is closely aligned with post-training and embodied control design.
- filter_reason: Hierarchical VLA manipulation architecture with explicit planning/execution split is directly relevant to agent architectures and environment interaction.
- hugging_face_paper: https://huggingface.co/papers/2604.14125
- original_paper: https://arxiv.org/abs/2604.14125
- source_basis: `original abstract page`

## Key Points

- The paper argues that end-to-end VLA fine-tuning on control data can degrade the reasoning abilities inherited from the base VLM.
- HiVLA decouples high-level semantic planning from low-level motor control instead of training a single monolithic policy.
- At the high level, a VLM planner performs task decomposition and visual grounding, producing structured plans with a subtask instruction and a target bounding box.
- At the low level, a flow-matching Diffusion Transformer action expert uses a cascaded cross-attention mechanism to fuse global context, object-centric crops, and skill semantics for execution.
- The authors report gains in simulation and real-world experiments, with particular strength in long-horizon skill composition and fine-grained manipulation of small objects in cluttered scenes.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14125
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14125
- arXiv abstract: https://arxiv.org/abs/2604.14125
- Project page: https://tianshuoy.github.io/HiVLA-page/

## Paper Metadata

- authors: `Tianshuo Yang`, `Guanyu Chen`, `Yutian Chen`, `Zhixuan Liang`, `Yitian Liu`, `Zanxin Chen`, `Chunpu Xu`, `Haotian Liang`, `Jiangmiao Pang`, `Yao Mu`, `Ping Luo`
- ai_keywords: `Vision-Language-Action models`, `Vision-Language Models`, `diffusion models`, `Diffusion Transformer`, `cross-attention mechanism`, `cascaded cross-attention`, `task decomposition`, `visual grounding`, `structured plans`, `bounding box`, `motor control`, `semantic planning`, `zero-shot reasoning`, `skill composition`, `fine-grained manipulation`, `cluttered scenes`
- upvotes: `16`
- num_comments: `3`
- abstract: While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs task decomposition and visual grounding to generate structured plans, comprising a subtask instruction and a precise target bounding box. Then, to translate this plan into physical actions, we introduce a flow-matching Diffusion Transformer (DiT) action expert in low-level part equipped with a novel cascaded cross-attention mechanism. This design sequentially fuses global context, high-resolution object-centric crops and skill semantics, enabling the DiT to focus purely on robust execution. Our decoupled architecture preserves the VLM's zero-shot reasoning while allowing independent improvement of both components. Extensive experiments in simulation and the real world demonstrate that HiVLA significantly outperforms state-of-the-art end-to-end baselines, particularly excelling in long-horizon skill composition and the fine-grained manipulation of small objects in cluttered scenes.
- hf_ai_summary: HiVLA presents a hierarchical vision-language-action framework that decouples semantic planning from motor control using a diffusion transformer action expert with cascaded cross-attention for improved robotic manipulation.

## Source Excerpt

While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs task decomposition and visual grounding to generate structured plans, comprising a subtask instruction and a precise target bounding box. Then, to translate this plan into physical actions, we introduce a flow-matching Diffusion Transformer (DiT) action expert in low-level part equipped with a novel cascaded cross-attention mechanism. This design sequentially fuses global context, high-resolution object-centric crops and skill semantics, enabling the DiT to focus purely on robust execution. Our decoupled architecture preserves the VLM's zero-shot reasoning while allowing independent improvement of both components. Extensive experiments in simulation and the real world demonstrate that HiVLA significantly outperforms state-of-the-art end-to-end baselines, particularly excelling in long-horizon skill composition and the fine-grained manipulation of small objects in cluttered scenes.

## Open Questions

- How is the VLM planner trained, and does it require task-specific supervision for bounding boxes and subtask instructions?
- What datasets and benchmarks were used in simulation and real-world evaluation?
- How much of the performance gain comes from the hierarchical decomposition versus the cascaded cross-attention design?
- Does the system generalize to unseen objects, tasks, or environments beyond the reported cluttered-scene scenarios?
