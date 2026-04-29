---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reward-modeling, rlhf, reasoning-behavior-shaping, llm-systems, rlvr, audio-lm, reasoning, dialogue]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.25719
paper_id: 2604.25719
published: 2026-04-28T04:00:00+08:00
submitted_on_daily: 2026-04-29T13:52:58+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# Step-Audio-R1.5 Technical Report

## Summary

- one_sentence_summary: Step-Audio-R1.5 argues that RLVR for audio reasoning can improve benchmark accuracy while harming conversational quality, and proposes RLHF as a better post-training direction for immersive long-turn spoken dialogue.
- why_relevant: It is directly relevant to reinforcement learning post-training because it contrasts RLVR and RLHF in a multimodal language model setting and highlights how reward design shapes behavior beyond benchmark scores.
- filter_reason: Directly relevant post-training work on RLVR versus RLHF, with a concrete argument about reward design and reasoning behavior shaping.
- hugging_face_paper: https://huggingface.co/papers/2604.25719
- original_paper: https://arxiv.org/abs/2604.25719
- source_basis: `original abstract page`

## Key Points

- The paper frames a "verifiable reward trap": optimizing audio language models for isolated, verifiable text labels can neglect continuous acoustic context.
- It claims RLVR produces strong results on standardized objective benchmarks but degrades real-world conversational feel.
- The reported failure modes are reduced prosodic naturalness, weakened emotional continuity, and lower user immersion, especially in long-turn dialogues.
- Step-Audio-R1.5 is presented as a shift from RLVR to RLHF for audio reasoning and dialogue post-training.
- The abstract claims the new approach preserves analytical reasoning while improving the interactive experience of spoken dialogue.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.25719
- Hugging Face API entry: https://huggingface.co/api/papers/2604.25719
- arXiv abstract: https://arxiv.org/abs/2604.25719

## Paper Metadata

- authors: `Yuxin Zhang`, `Xiangyu Tony Zhang`, `Daijiao Liu`, `Fei Tian`, `Yayue Deng`, `Jun Chen`, `Qingjian Lin`, `Haoyang Zhang`, `Yuxin Li`, `Jinglan Gong`, `Yechang Huang`, `Liang Zhao`, `Chengyuan Yao`, `Hexin Liu`, `Eng Siong Chng`, `Xuerui Yang`, `Gang Yu`, `Xiangyu Zhang`, `Daxin Jiang`
- organization: `StepFun`
- ai_keywords: `Chain-of-Thought`, `Reinforcement Learning with Verified Rewards`, `RLVR`, `Reinforcement Learning from Human Feedback`, `RLHF`, `audio language models`, `auditory domain`, `acoustic contexts`, `verifiable reward trap`, `long-turn dialogues`, `prosodic naturalness`, `emotional continuity`, `user immersion`
- upvotes: `7`
- num_comments: `1`
- abstract: Recent advancements in large audio language models have extended Chain-of-Thought (CoT) reasoning into the auditory domain, enabling models to tackle increasingly complex acoustic and spoken tasks. To elicit and sustain these extended reasoning chains, the prevailing paradigm -- driven by the success of text-based reasoning models -- overwhelmingly relies on Reinforcement Learning with Verified Rewards (RLVR). However, as models are strictly optimized to distill rich, continuous auditory contexts into isolated, verifiable text labels, a fundamental question arises: are we fostering true audio intelligence, or merely reducing a continuous sensory medium into a discrete puzzle? We identify this as the "verifiable reward trap." While RLVR yields remarkable scores on standardized objective benchmarks, it systematically degrades the real-world conversational feel of audio models. By prioritizing isolated correctness over acoustic nuance, RLVR reduces dynamic interactions to mechanical "answering machines," severely compromising prosodic naturalness, emotional continuity, and user immersion, particularly in long-turn dialogues. To bridge the gap between mechanical objective verification and genuine sensory empathy, we introduce Step-Audio-R1.5, marking a paradigm shift toward Reinforcement Learning from Human Feedback (RLHF) in audio reasoning. Comprehensive evaluations demonstrate that Step-Audio-R1.5 not only maintains robust analytical reasoning but profoundly transforms the interactive experience, redefining the boundaries of deeply immersive long-turn spoken dialogue.
- hf_ai_summary: Audio language models trained with reinforcement learning from verified rewards suffer from reduced conversational quality, prompting a shift toward reinforcement learning from human feedback for improved immersive dialogue experiences.

## Source Excerpt

Recent advancements in large audio language models have extended Chain-of-Thought (CoT) reasoning into the auditory domain, enabling models to tackle increasingly complex acoustic and spoken tasks. To elicit and sustain these extended reasoning chains, the prevailing paradigm -- driven by the success of text-based reasoning models -- overwhelmingly relies on Reinforcement Learning with Verified Rewards (RLVR). However, as models are strictly optimized to distill rich, continuous auditory contexts into isolated, verifiable text labels, a fundamental question arises: are we fostering true audio intelligence, or merely reducing a continuous sensory medium into a discrete puzzle? We identify this as the "verifiable reward trap." While RLVR yields remarkable scores on standardized objective benchmarks, it systematically degrades the real-world conversational feel of audio models. By prioritizing isolated correctness over acoustic nuance, RLVR reduces dynamic interactions to mechanical "answering machines," severely compromising prosodic naturalness, emotional continuity, and user immersion, particularly in long-turn dialogues. To bridge the gap between mechanical objective verification and genuine sensory empathy, we introduce Step-Audio-R1.5, marking a paradigm shift toward Reinforcement Learning from Human Feedback (RLHF) in audio reasoning. Comprehensive evaluations demonstrate that Step-Audio-R1.5 not only maintains robust analytical reasoning but profoundly transforms the interactive experience, redefining the boundaries of deeply immersive long-turn spoken dialogue.

## Open Questions

- What specific RLHF data collection or preference setup was used for Step-Audio-R1.5?
- What benchmarks and human evaluation protocols were used to support the claims about conversational quality?
- How large is the gap in analytical reasoning versus conversational immersion compared with RLVR baselines?
- Does the method generalize beyond long-turn spoken dialogue to other audio tasks?
