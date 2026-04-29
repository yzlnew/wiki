---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, agents, agent-architectures, agent-evals, llm-systems, reasoning, visual-rag, lvlm, hierarchical-actions, grpo]
source_count: 1
updated: 2026-04-19
source_url: https://arxiv.org/abs/2604.14967
paper_id: 2604.14967
published: 2026-04-16T04:00:00+08:00
submitted_on_daily: 2026-04-17T08:58:28+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards

## Summary

- one_sentence_summary: UniDoc-RL is a reinforcement-learning framework for visual RAG that trains an LVLM agent to jointly retrieve, rerank, crop, and reason over visual evidence using hierarchical actions and dense multi-reward supervision.
- why_relevant: It is directly relevant to reinforcement learning for post-training, agentic tool use, and hierarchical action design in LVLM-based retrieval and reasoning systems.
- filter_reason: Directly relevant RL/GRPO work on hierarchical agent behavior, dense rewards, and sequential decision-making for visual RAG.
- hugging_face_paper: https://huggingface.co/papers/2604.14967
- original_paper: https://arxiv.org/abs/2604.14967
- source_basis: `original abstract page`

## Key Points

- Frames visual information acquisition as a sequential decision problem with a hierarchical action space, moving from coarse document retrieval to image selection and active region cropping.
- The agent jointly handles retrieval, reranking, active visual perception, and reasoning, rather than treating retrieval as a separate front-end step.
- Introduces a dense multi-reward scheme that gives task-aware supervision for each action in the trajectory.
- Uses Group Relative Policy Optimization (GRPO) to align behavior with multiple objectives without a separate value network.
- Curates a dataset of high-quality reasoning trajectories with fine-grained action annotations to support training.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.14967
- Hugging Face API entry: https://huggingface.co/api/papers/2604.14967
- arXiv abstract: https://arxiv.org/abs/2604.14967
- GitHub: https://github.com/deepglint/UniDoc-RL

## Paper Metadata

- authors: `Jun Wang`, `Shuo Tan`, `Zelong Sun`, `Tiancheng Gu`, `Yongle Zhao`, `Ziyong Feng`, `Kaicheng Yang`, `Cewu Lu`
- organization: `DeepGlint`
- ai_keywords: `Retrieval-Augmented Generation`, `Large Vision-Language Models`, `reinforcement learning`, `hierarchical action space`, `visual information acquisition`, `active visual perception`, `Group Relative Policy Optimization`, `dense multi-reward scheme`, `fine-grained visual semantics`, `sequential decision-making`
- upvotes: `9`
- num_comments: `2`
- abstract: Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.
- hf_ai_summary: UniDoc-RL introduces a reinforcement learning framework for LVLMs that jointly optimizes retrieval, reranking, visual perception, and reasoning through hierarchical decision-making and dense multi-reward supervision.

## Source Excerpt

Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.

## Open Questions

- What are the three benchmarks used for evaluation?
- What exact action hierarchy and reward components are used in the dense multi-reward scheme?
- How large is the curated trajectory dataset, and what domains or document types does it cover?
- Which prior RL-based methods does it outperform, and under what settings does the reported 17.7% gain appear?
