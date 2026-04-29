---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reward-modeling, rlhf, llm-systems, video-language-models, human-ai-oversight, captioning, dpo, sft, inference-time-scaling]
source_count: 1
updated: 2026-04-28
source_url: https://arxiv.org/abs/2604.21718
paper_id: 2604.21718
published: 2026-04-22T04:00:00+08:00
submitted_on_daily: 2026-04-27T15:45:46+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# Building a Precise Video Language with Human-AI Oversight

## Summary

- one_sentence_summary: This paper introduces a structured video-specification scheme and the CHAI human-AI oversight workflow to improve precise video captioning, reward modeling, and downstream video generation control.
- why_relevant: It is relevant to post-training and reward-modeling because it turns human critique and preference data into supervision for improving video-language models, and it has a clear model-oversight angle rather than just dataset building.
- filter_reason: Directly studies scalable human-AI oversight, reward modeling, SFT, and DPO for model improvement.
- hugging_face_paper: https://huggingface.co/papers/2604.21718
- original_paper: https://arxiv.org/abs/2604.21718
- source_basis: `original abstract page`

## Key Points

- Defines a structured caption specification covering subjects, scenes, motion, spatial relations, and camera dynamics, grounded in hundreds of visual primitives created with professional video creators.
- Introduces CHAI, where trained experts critique and revise model-generated pre-captions into improved post-captions, separating text generation from human verification.
- Uses critiques and pre/post-caption preferences as supervision for open-source VLMs, improving caption generation, reward modeling, critique generation, and inference-time scaling via SFT and DPO.
- Ablations indicate that critique quality, especially precision, recall, and constructiveness, directly affects downstream performance.
- With modest expert supervision, the resulting model reportedly outperforms closed-source systems such as Gemini-3.1-Pro, and the method also improves prompt-following for video generation models on detailed cinematography control.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.21718
- Hugging Face API entry: https://huggingface.co/api/papers/2604.21718
- arXiv abstract: https://arxiv.org/abs/2604.21718
- GitHub: https://github.com/chancharikmitra/CHAI
- Project page: https://linzhiqiu.github.io/papers/chai/

## Paper Metadata

- authors: `Zhiqiu Lin`, `Chancharik Mitra`, `Siyuan Cen`, `Isaac Li`, `Yuhan Huang`, `Yu Tong Tiffany Ling`, `Hewei Wang`, `Irene Pi`, `Shihang Zhu`, `Ryan Rao`, `George Liu`, `Jiaxi Li`, `Ruojin Li`, `Yili Han`, `Yilun Du`, `Deva Ramanan`
- organization: `Carnegie Mellon University`
- ai_keywords: `video-language models`, `video captioning`, `CHAI`, `Critique-based Human-AI Oversight`, `visual primitives`, `SFT`, `DPO`, `inference-time scaling`, `reward modeling`, `video generation models`, `cinematography`
- upvotes: `9`
- num_comments: `1`
- abstract: Video-language models (VLMs) learn to reason about the dynamic visual world through natural language. We introduce a suite of open datasets, benchmarks, and recipes for scalable oversight that enable precise video captioning. First, we define a structured specification for describing subjects, scenes, motion, spatial, and camera dynamics, grounded by hundreds of carefully defined visual primitives developed with professional video creators such as filmmakers. Next, to curate high-quality captions, we introduce CHAI (Critique-based Human-AI Oversight), a framework where trained experts critique and revise model-generated pre-captions into improved post-captions. This division of labor improves annotation accuracy and efficiency by offloading text generation to models, allowing humans to better focus on verification. Additionally, these critiques and preferences between pre- and post-captions provide rich supervision for improving open-source models (Qwen3-VL) on caption generation, reward modeling, and critique generation through SFT, DPO, and inference-time scaling. Our ablations show that critique quality in precision, recall, and constructiveness, ensured by our oversight framework, directly governs downstream performance. With modest expert supervision, the resulting model outperforms closed-source models such as Gemini-3.1-Pro. Finally, we apply our approach to re-caption large-scale professional videos (e.g., films, commercials, games) and fine-tune video generation models such as Wan to better follow detailed prompts of up to 400 words, achieving finer control over cinematography including camera motion, angle, lens, focus, point of view, and framing. Our results show that precise specification and human-AI oversight are key to professional-level video understanding and generation. Data and code are available on our project page: https://linzhiqiu.github.io/papers/chai/
- hf_ai_summary: Video-language models are enhanced through structured visual specifications and human-AI oversight frameworks that improve captioning accuracy and enable detailed video generation control.

## Source Excerpt

Video-language models (VLMs) learn to reason about the dynamic visual world through natural language. We introduce a suite of open datasets, benchmarks, and recipes for scalable oversight that enable precise video captioning. First, we define a structured specification for describing subjects, scenes, motion, spatial, and camera dynamics, grounded by hundreds of carefully defined visual primitives developed with professional video creators such as filmmakers. Next, to curate high-quality captions, we introduce CHAI (Critique-based Human-AI Oversight), a framework where trained experts critique and revise model-generated pre-captions into improved post-captions. This division of labor improves annotation accuracy and efficiency by offloading text generation to models, allowing humans to better focus on verification. Additionally, these critiques and preferences between pre- and post-captions provide rich supervision for improving open-source models (Qwen3-VL) on caption generation, reward modeling, and critique generation through SFT, DPO, and inference-time scaling. Our ablations show that critique quality in precision, recall, and constructiveness, ensured by our oversight framework, directly governs downstream performance. With modest expert supervision, the resulting model outperforms closed-source models such as Gemini-3.1-Pro. Finally, we apply our approach to re-caption large-scale professional videos (e.g., films, commercials, games) and fine-tune video generation models such as Wan to better follow detailed prompts of up to 400 words, achieving finer control over cinematography including camera motion, angle, lens, focus, point of view, and framing. Our results show that precise specification and human-AI oversight are key to professional-level video understanding and generation. Data and code are available on our project page: this https URL

## Open Questions

- What benchmark tasks and metrics were used to compare against Gemini-3.1-Pro?
- How much expert supervision was required to reach the reported gains?
- What is the exact training recipe for using critique data in SFT, DPO, and inference-time scaling?
- How large are the released datasets and how are the visual primitives operationalized in annotation guidelines?
- How much of the improvement comes from the structured specification versus the CHAI oversight process?
