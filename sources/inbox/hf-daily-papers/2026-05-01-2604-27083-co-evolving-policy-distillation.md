---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reward-modeling, reasoning-behavior-shaping, llm-systems, rlvr, policy-distillation, multimodal-reasoning, agents]
source_count: 1
updated: 2026-05-02
source_url: https://arxiv.org/abs/2604.27083
paper_id: 2604.27083
published: 2026-04-29T04:00:00+08:00
submitted_on_daily: 2026-05-01T09:44:09+08:00
decision: accept
score: 92
generator: scripts/update_hf_daily_papers.py
---

# Co-Evolving Policy Distillation

## Summary

- one_sentence_summary: Co-Evolving Policy Distillation (CoPD) is a post-training method that jointly trains multiple experts with bidirectional policy distillation during RLVR to reduce capability loss and unify text, image, and video reasoning into one model.
- why_relevant: This is directly relevant to post-training and RL-based reasoning systems because it proposes a training-time alternative to standard distillation for combining specialist agents or modalities into one stronger model.
- filter_reason: Directly advances post-training and reinforcement-learning-based capability consolidation with a concrete distillation/training method.
- hugging_face_paper: https://huggingface.co/papers/2604.27083
- original_paper: https://arxiv.org/abs/2604.27083
- source_basis: `original abstract page`

## Key Points

- The paper analyzes two standard post-training paradigms for merging expert capabilities: mixed RLVR and sequential expert training followed by OPD.
- It argues that mixed RLVR loses performance through inter-capability divergence, while post-hoc OPD misses teacher knowledge because teacher-student behavior gaps are too large.
- CoPD interleaves OPD with ongoing RLVR training and lets experts serve as mutual teachers, making distillation bidirectional.
- The goal is to keep experts behaviorally aligned while preserving complementary knowledge during training rather than after separate specialization.
- Experiments reportedly show strong gains on integrated text, image, and video reasoning, beating mixed RLVR and MOPD and even some domain-specific experts.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.27083
- Hugging Face API entry: https://huggingface.co/api/papers/2604.27083
- arXiv abstract: https://arxiv.org/abs/2604.27083

## Paper Metadata

- authors: `Naibin Gu`, `Chenxu Yang`, `Qingyi Si`, `Chuanyu Qin`, `Dingyu Yao`, `Peng Fu`, `Zheng Lin`, `Weiping Wang`, `Nan Duan`, `Jiaqi Wang`
- ai_keywords: `post-training`, `RLVR`, `OPD`, `policy distillation`, `Co-Evolving Policy Distillation`, `expert capabilities`, `behavioral pattern gaps`, `mutual teachers`, `bidirectional policy distillation`, `multi-modal reasoning`
- upvotes: `34`
- num_comments: `1`
- abstract: RLVR and OPD have become standard paradigms for post-training. We provide a unified analysis of these two paradigms in consolidating multiple expert capabilities into a single model, identifying capability loss in different ways: mixed RLVR suffers from inter-capability divergence cost, while the pipeline of first training experts and then performing OPD, though avoiding divergence, fails to fully absorb teacher capabilities due to large behavioral pattern gaps between teacher and student. We propose Co-Evolving Policy Distillation (CoPD), which encourages parallel training of experts and introduces OPD during each expert's ongoing RLVR training rather than after complete expert training, with experts serving as mutual teachers (making OPD bidirectional) to co-evolve. This enables more consistent behavioral patterns among experts while maintaining sufficient complementary knowledge throughout. Experiments validate that CoPD achieves all-in-one integration of text, image, and video reasoning capabilities, significantly outperforming strong baselines such as mixed RLVR and MOPD, and even surpassing domain-specific experts. The model parallel training pattern offered by CoPD may inspire a novel training scaling paradigm.
- hf_ai_summary: Co-Evolving Policy Distillation enables unified integration of multiple expert capabilities through parallel training and bidirectional policy distillation, outperforming existing methods in multi-modal reasoning tasks.

## Source Excerpt

RLVR and OPD have become standard paradigms for post-training. We provide a unified analysis of these two paradigms in consolidating multiple expert capabilities into a single model, identifying capability loss in different ways: mixed RLVR suffers from inter-capability divergence cost, while the pipeline of first training experts and then performing OPD, though avoiding divergence, fails to fully absorb teacher capabilities due to large behavioral pattern gaps between teacher and student. We propose Co-Evolving Policy Distillation (CoPD), which encourages parallel training of experts and introduces OPD during each expert's ongoing RLVR training rather than after complete expert training, with experts serving as mutual teachers (making OPD bidirectional) to co-evolve. This enables more consistent behavioral patterns among experts while maintaining sufficient complementary knowledge throughout. Experiments validate that CoPD achieves all-in-one integration of text, image, and video reasoning capabilities, significantly outperforming strong baselines such as mixed RLVR and MOPD, and even surpassing domain-specific experts. The model parallel training pattern offered by CoPD may inspire a novel training scaling paradigm.

## Open Questions

- What exact tasks and benchmarks were used to evaluate the text, image, and video reasoning claims?
- How is bidirectional OPD implemented in practice, and what optimization objective is used?
- Does CoPD require matched expert architectures or can it work across heterogeneous models?
- What is the compute cost of parallel expert training compared with mixed RLVR or sequential OPD?
- How much of the reported gain comes from the co-evolution schedule versus the bidirectional teacher setup?
