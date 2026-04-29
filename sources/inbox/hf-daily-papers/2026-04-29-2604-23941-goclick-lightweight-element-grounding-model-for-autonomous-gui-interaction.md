---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, tool-use, llm-systems, environment-interaction, agent-architectures, gui, grounding, vision-language, on-device, data-curation]
source_count: 1
updated: 2026-04-29
source_url: https://arxiv.org/abs/2604.23941
paper_id: 2604.23941
published: 2026-04-27T04:00:00+08:00
submitted_on_daily: 2026-04-29T09:30:45+08:00
decision: accept
score: 88
generator: scripts/update_hf_daily_papers.py
---

# GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction

## Summary

- one_sentence_summary: GoClick is a 230M-parameter vision-language model for GUI element grounding that uses an encoder-decoder architecture and progressive data refinement to achieve strong accuracy and fast inference for on-device and device-cloud GUI agents.
- why_relevant: The paper is directly relevant to agent/tool-use systems because it focuses on a compact perception module for GUI interaction, with an explicit emphasis on deployment constraints, execution speed, and agent performance in a collaborative workflow.
- filter_reason: A technically detailed GUI grounding model for autonomous agents and environment interaction, with clear deployment and architecture insights.
- hugging_face_paper: https://huggingface.co/papers/2604.23941
- original_paper: https://arxiv.org/abs/2604.23941
- source_basis: `original abstract page`

## Key Points

- Targets GUI element grounding: locating the referenced interface element on a screenshot from a natural-language instruction, which is a core capability for GUI agents.
- Claims that simply shrinking decoder-only VLMs is suboptimal at small scale; the paper instead uses an encoder-decoder architecture and reports better performance for GUI grounding.
- Introduces a Progressive Data Refinement pipeline that applies task-type filtering and data-ratio adjustment to reduce a 10.8M raw dataset to a 3.8M-sample high-quality core set.
- Reports that training on the refined core set improves grounding accuracy, and that GoClick performs well on multiple benchmarks while remaining small and fast.
- Shows usefulness in a device-cloud collaboration setup, where GoClick helps cloud task planners localize elements more precisely and improves task success rates.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.23941
- Hugging Face API entry: https://huggingface.co/api/papers/2604.23941
- arXiv abstract: https://arxiv.org/abs/2604.23941
- GitHub: https://github.com/ZJULiHongxin/GoClick

## Paper Metadata

- authors: `Hongxin Li`, `Yuntao Chen`, `Zhaoxiang Zhang`
- ai_keywords: `vision-language model`, `GUI element grounding`, `encoder-decoder architecture`, `progressive data refinement`, `parameter-efficient fine-tuning`, `mobile device deployment`, `visual grounding accuracy`, `task type filtering`, `data ratio adjustment`, `device-cloud collaboration framework`
- upvotes: `0`
- num_comments: `1`
- abstract: Graphical User Interface (GUI) element grounding (precisely locating elements on screenshots based on natural language instructions) is fundamental for agents interacting with GUIs. Deploying this capability directly on resource-constrained devices like mobile phones is increasingly critical for GUI agents requiring low latency. However, this goal faces a significant challenge, as current visual grounding methods typically employ large vision-language model (VLM) (more than 2.5B parameters), making them impractical for on-device execution due to memory and computational constraints. To address this, this paper introduces GoClick, a lightweight GUI element grounding VLM with only 230M parameters that achieves excellent visual grounding accuracy, even on par with significantly larger models. Simply downsizing existing decoder-only VLMs is a straightforward way to design a lightweight model, but our experiments reveal that this approach yields suboptimal results. Instead, we select an encoder-decoder architecture, which outperforms decoder-only alternatives at small parameter scales for GUI grounding tasks. Additionally, the limited capacity of small VLMs encourages us to develop a Progressive Data Refinement pipeline that utilizes task type filtering and data ratio adjustment to extract a high-quality 3.8M-sample core set from a 10.8M raw dataset. Training GoClick using this core set brings notable grounding accuracy gains. Our experiments show that GoClick excels on multiple GUI element grounding benchmarks while maintaining a small size and high inference speed. GoClick also enhances GUI agent performance when integrated into a device-cloud collaboration framework, where GoClick helps cloud-based task planners perform precise element localization and achieve higher success rates. We hope our method serves as a meaningful exploration within the GUI agent community.
- hf_ai_summary: A lightweight vision-language model called GoClick is introduced for GUI element grounding on mobile devices, achieving high accuracy with only 230M parameters through encoder-decoder architecture and progressive data refinement techniques.

## Source Excerpt

Graphical User Interface (GUI) element grounding (precisely locating elements on screenshots based on natural language instructions) is fundamental for agents interacting with GUIs. Deploying this capability directly on resource-constrained devices like mobile phones is increasingly critical for GUI agents requiring low latency. However, this goal faces a significant challenge, as current visual grounding methods typically employ large vision-language model (VLM) (more than 2.5B parameters), making them impractical for on-device execution due to memory and computational constraints. To address this, this paper introduces GoClick, a lightweight GUI element grounding VLM with only 230M parameters that achieves excellent visual grounding accuracy, even on par with significantly larger models. Simply downsizing existing decoder-only VLMs is a straightforward way to design a lightweight model, but our experiments reveal that this approach yields suboptimal results. Instead, we select an encoder-decoder architecture, which outperforms decoder-only alternatives at small parameter scales for GUI grounding tasks. Additionally, the limited capacity of small VLMs encourages us to develop a Progressive Data Refinement pipeline that utilizes task type filtering and data ratio adjustment to extract a high-quality 3.8M-sample core set from a 10.8M raw dataset. Training GoClick using this core set brings notable grounding accuracy gains. Our experiments show that GoClick excels on multiple GUI element grounding benchmarks while maintaining a small size and high inference speed. GoClick also enhances GUI agent performance when integrated into a device-cloud collaboration framework, where GoClick helps cloud-based task planners perform precise element localization and achieve higher success rates. We hope our method serves as a meaningful exploration within the GUI agent community.

## Open Questions

- Which specific GUI grounding benchmarks were used, and how did GoClick compare numerically to larger baselines?
- How was the 10.8M raw dataset constructed, and what criteria defined the 3.8M core set?
- What exact device-cloud collaboration architecture was used, and which agent planner was paired with GoClick?
- What is the latency or memory footprint on actual mobile devices?
