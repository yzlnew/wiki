---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, gui-agents, benchmark, vision-language-models, grounding, state-prediction]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.24441
paper_id: 2604.24441
published: 2026-04-27T04:00:00+08:00
submitted_on_daily: 2026-04-29T09:27:50+08:00
decision: accept
score: 85
generator: scripts/update_hf_daily_papers.py
---

# AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark

## Summary

- one_sentence_summary: AutoGUI-v2 is a multi-platform benchmark for measuring whether GUI agents understand interface functionality, grounding, and interaction outcomes rather than just completing tasks or matching elements.
- why_relevant: This is directly relevant to agents and tool-using systems because it evaluates the internal functional understanding and state prediction that GUI agents need for reliable post-training and deployment.
- filter_reason: A technically useful benchmark for GUI agents that measures functionality understanding, grounding, and interaction outcome prediction.
- hugging_face_paper: https://huggingface.co/papers/2604.24441
- original_paper: https://arxiv.org/abs/2604.24441
- source_basis: `original abstract page`

## Key Points

- Introduces a benchmark for deep GUI functionality understanding and interaction outcome prediction, not just black-box task completion.
- Uses a VLM-human collaborative pipeline that recursively parses screenshots into hierarchical functional regions to generate evaluation tasks.
- Contains 2,753 tasks across six operating systems and tests region-level semantics, element-level grounding, and dynamic state prediction.
- Evaluation shows a split between model strengths: some open-source agent-tuned VLMs perform better at functional grounding, while commercial models perform better at functionality captioning.
- All evaluated models struggle with complex interaction logic for uncommon actions, indicating that predictive understanding of GUI behavior remains limited.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.24441
- Hugging Face API entry: https://huggingface.co/api/papers/2604.24441
- arXiv abstract: https://arxiv.org/abs/2604.24441
- GitHub: https://github.com/ZJULiHongxin/AutoGUI-v2

## Paper Metadata

- authors: `Hongxin Li`, `Xiping Wang`, `Jingran Su`, `Zheng Ju`, `Yuntao Chen`, `Qing Li`, `Zhaoxiang Zhang`
- ai_keywords: `Vision-Language Models`, `GUI navigation`, `digital autonomy`, `mental model`, `interface dynamics`, `digital world state`, `benchmark`, `VLM-human collaborative pipeline`, `multi-platform screenshots`, `functional regions`, `semantic grounding`, `dynamic state prediction`, `agent data`, `functionality captioning`, `interaction logic`
- upvotes: `0`
- num_comments: `1`
- abstract: Autonomous agents capable of navigating Graphical User Interfaces (GUIs) hold the potential to revolutionize digital productivity. However, achieving true digital autonomy extends beyond reactive element matching; it necessitates a predictive mental model of interface dynamics and the ability to foresee the "digital world state" resulting from interactions. Despite the perceptual capabilities of modern Vision-Language Models (VLMs), existing benchmarks remain bifurcated (focusing either on black-box task completion or static, shallow grounding), thereby failing to assess whether agents truly comprehend the implicit functionality and transition logic of GUIs. To bridge this gap, we introduce AutoGUI-v2, a comprehensive benchmark designed to evaluate deep GUI functionality understanding and interaction outcome prediction. We construct the benchmark using a novel VLM-human collaborative pipeline that recursively parses multi-platform screenshots into hierarchical functional regions to generate diverse evaluation tasks. Providing 2,753 tasks across six operating systems, AutoGUI-v2 rigorously tests agents on region and element-level semantics, grounding, and dynamic state prediction. Our evaluation reveals a striking dichotomy in VLMs: while open-source models fine-tuned on agent data (e.g., Qwen3-VL) excel at functional grounding, commercial models (e.g., Gemini-2.5-Pro-Thinking) dominate in functionality captioning. Crucially, all models struggle with complex interaction logic of uncommon actions, highlighting that deep functional understanding remains a significant hurdle. By systematically measuring these foundational capabilities, AutoGUI-v2 offers a new lens for advancing the next generation of GUI agents.
- hf_ai_summary: AutoGUI-v2 is a comprehensive benchmark for evaluating GUI functionality understanding and interaction prediction capabilities of autonomous agents across multiple platforms.

## Source Excerpt

Autonomous agents capable of navigating Graphical User Interfaces (GUIs) hold the potential to revolutionize digital productivity. However, achieving true digital autonomy extends beyond reactive element matching; it necessitates a predictive mental model of interface dynamics and the ability to foresee the "digital world state" resulting from interactions. Despite the perceptual capabilities of modern Vision-Language Models (VLMs), existing benchmarks remain bifurcated (focusing either on black-box task completion or static, shallow grounding), thereby failing to assess whether agents truly comprehend the implicit functionality and transition logic of GUIs. To bridge this gap, we introduce AutoGUI-v2, a comprehensive benchmark designed to evaluate deep GUI functionality understanding and interaction outcome prediction. We construct the benchmark using a novel VLM-human collaborative pipeline that recursively parses multi-platform screenshots into hierarchical functional regions to generate diverse evaluation tasks. Providing 2,753 tasks across six operating systems, AutoGUI-v2 rigorously tests agents on region and element-level semantics, grounding, and dynamic state prediction. Our evaluation reveals a striking dichotomy in VLMs: while open-source models fine-tuned on agent data (e.g., Qwen3-VL) excel at functional grounding, commercial models (e.g., Gemini-2.5-Pro-Thinking) dominate in functionality captioning. Crucially, all models struggle with complex interaction logic of uncommon actions, highlighting that deep functional understanding remains a significant hurdle. By systematically measuring these foundational capabilities, AutoGUI-v2 offers a new lens for advancing the next generation of GUI agents.

## Open Questions

- What six operating systems are covered, and how are tasks distributed across them?
- How is 'functional grounding' scored relative to 'functionality captioning' and dynamic state prediction?
- What uncommon actions and interaction-logics were most failure-prone?
- How much of the benchmark relies on human annotation versus model-assisted parsing in the pipeline?
