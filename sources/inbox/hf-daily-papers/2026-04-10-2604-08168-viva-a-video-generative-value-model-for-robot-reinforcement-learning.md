---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, value-modeling, agent-environment-interaction, robotics, video-generation, long-horizon]
source_count: 1
updated: 2026-04-10
source_url: https://arxiv.org/abs/2604.08168
paper_id: 2604.08168
published: 2026-04-09T04:00:00+08:00
submitted_on_daily: 2026-04-10T12:29:52+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# ViVa: A Video-Generative Value Model for Robot Reinforcement Learning

## Summary

- one_sentence_summary: ViVa repurposes a pretrained video generator as a robot value model that predicts future proprioception and a scalar state value, improving reinforcement-learning guidance for long-horizon manipulation.
- why_relevant: It is directly relevant to reinforcement learning and post-training because it studies value modeling for agent-environment interaction, with a mechanistic twist on using generative video priors for better credit assignment in robotics.
- filter_reason: A value-model method for robot RL that uses generative temporal prediction is directly relevant to reinforcement learning and environment-interaction methods.
- hugging_face_paper: https://huggingface.co/papers/2604.08168
- original_paper: https://arxiv.org/abs/2604.08168
- source_basis: `original abstract page`

## Key Points

- The paper targets robot reinforcement learning under partial observability and delayed feedback, where value functions are needed to estimate task progress and support policy improvement.
- ViVa is a video-generative value model: it takes the current observation plus robot proprioception and jointly predicts future proprioception and a scalar value for the current state.
- The core idea is to use spatiotemporal priors from a pretrained video generator so value estimation is grounded in anticipated embodiment dynamics rather than static snapshots.
- Integrated into RECAP, ViVa reportedly gives substantial gains on real-world box assembly tasks.
- Qualitative analysis suggests the model produces more reliable value signals and can generalize to novel objects.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.08168
- Hugging Face API entry: https://huggingface.co/api/papers/2604.08168
- arXiv abstract: https://arxiv.org/abs/2604.08168
- GitHub: https://github.com/GigaAI-research/ViVa
- Project page: https://viva-value-model.github.io/

## Paper Metadata

- authors: `Jindi Lv`, `Hao Li`, `Jie Li`, `Yifei Nie`, `Fankun Kong`, `Yang Wang`, `Xiaofeng Wang`, `Zheng Zhu`, `Chaojun Ni`, `Qiuping Deng`, `Hengtao Li`, `Jiancheng Lv`, `Guan Huang`
- organization: `GigaAI-Research`
- ai_keywords: `Vision-language-action models`, `reinforcement learning`, `value functions`, `vision-language models`, `video-generative models`, `proprioception`, `spatiotemporal priors`, `RECAP`, `embodiment dynamics`
- upvotes: `7`
- num_comments: `1`
- abstract: Vision-language-action (VLA) models have advanced robot manipulation through large-scale pretraining, but real-world deployment remains challenging due to partial observability and delayed feedback. Reinforcement learning addresses this via value functions, which assess task progress and guide policy improvement. However, existing value models built on vision-language models (VLMs) struggle to capture temporal dynamics, undermining reliable value estimation in long-horizon tasks. In this paper, we propose ViVa, a video-generative value model that repurposes a pretrained video generator for value estimation. Taking the current observation and robot proprioception as input, ViVa jointly predicts future proprioception and a scalar value for the current state. By leveraging the spatiotemporal priors of a pretrained video generator, our approach grounds value estimation in anticipated embodiment dynamics, moving beyond static snapshots to intrinsically couple value with foresight. Integrated into RECAP, ViVa delivers substantial improvements on real-world box assembly. Qualitative analysis across all three tasks confirms that ViVa produces more reliable value signals, accurately reflecting task progress. By leveraging spatiotemporal priors from video corpora, ViVa also generalizes to novel objects, highlighting the promise of video-generative models for value estimation.
- hf_ai_summary: ViVa, a video-generative value model, improves robot manipulation by leveraging pretrained video generators to estimate values based on anticipated embodiment dynamics rather than static observations.

## Source Excerpt

Vision-language-action (VLA) models have advanced robot manipulation through large-scale pretraining, but real-world deployment remains challenging due to partial observability and delayed feedback. Reinforcement learning addresses this via value functions, which assess task progress and guide policy improvement. However, existing value models built on vision-language models (VLMs) struggle to capture temporal dynamics, undermining reliable value estimation in long-horizon tasks. In this paper, we propose ViVa, a video-generative value model that repurposes a pretrained video generator for value estimation. Taking the current observation and robot proprioception as input, ViVa jointly predicts future proprioception and a scalar value for the current state. By leveraging the spatiotemporal priors of a pretrained video generator, our approach grounds value estimation in anticipated embodiment dynamics, moving beyond static snapshots to intrinsically couple value with foresight. Integrated into RECAP, ViVa delivers substantial improvements on real-world box assembly. Qualitative analysis across all three tasks confirms that ViVa produces more reliable value signals, accurately reflecting task progress. By leveraging spatiotemporal priors from video corpora, ViVa also generalizes to novel objects, highlighting the promise of video-generative models for value estimation.

## Open Questions

- What exact pretrained video generator architecture is reused, and which components are fine-tuned versus frozen?
- How is the scalar value supervised or trained, and what reward or return target is used?
- What are the three tasks mentioned in the qualitative analysis, and how much of the improvement is due to better value estimation versus the surrounding RECAP setup?
- How well does ViVa compare with non-generative value baselines on held-out or harder long-horizon tasks?
