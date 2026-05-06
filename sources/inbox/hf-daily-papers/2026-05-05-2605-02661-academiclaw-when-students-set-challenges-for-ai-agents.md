---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, llm-systems, tool-use, benchmark, academic-tasks, evaluation, safety, rl]
source_count: 1
updated: 2026-05-06
source_url: https://arxiv.org/abs/2605.02661
paper_id: 2605.02661
published: 2026-05-04T04:00:00+08:00
submitted_on_daily: 2026-05-05T09:37:59+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# AcademiClaw: When Students Set Challenges for AI Agents

## Summary

- one_sentence_summary: AcademiClaw is a bilingual benchmark of 80 long-horizon academic tasks from real student workflows, designed to test whether current AI agents can handle complex assistant-level work beyond standard benchmarks.
- why_relevant: This is relevant to agent and tool-use research because it benchmarks long-horizon, real-world academic agent tasks and includes diagnostic analysis of model behavior, failure modes, and efficiency signals.
- filter_reason: A strong agent-evaluation benchmark with long-horizon, real-world tasks and detailed diagnostic methodology.
- hugging_face_paper: https://huggingface.co/papers/2605.02661
- original_paper: https://arxiv.org/abs/2605.02661
- source_basis: `original abstract page`

## Key Points

- The benchmark is built from 230 student-submitted candidates and reduced through expert review to 80 tasks spanning 25+ domains.
- Tasks cover real academic workflows such as homework, research projects, competitions, personal projects, plus difficult areas like olympiad mathematics, linguistics, GPU-intensive reinforcement learning, and full-stack system debugging.
- 16 tasks require CUDA GPU execution, and each task runs in an isolated Docker sandbox.
- Scoring uses task-completion rubrics with six complementary techniques, plus a separate five-category safety audit for behavioral analysis.
- Experiments on six frontier models found the best model reached only a 55% pass rate, with analyses showing domain-specific capability gaps, different model behaviors, and weak correlation between token use and output quality.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2605.02661
- Hugging Face API entry: https://huggingface.co/api/papers/2605.02661
- arXiv abstract: https://arxiv.org/abs/2605.02661
- GitHub: https://github.com/GAIR-NLP/AcademiClaw

## Paper Metadata

- authors: `Junjie Yu`, `Pengrui Lu`, `Weiye Si`, `Hongliang Lu`, `Jiabao Wu`, `Kaiwen Tao`, `Kun Wang`, `Lingyu Yang`, `Qiran Zhang`, `Xiuting Guo`, `Xuanyu Wang`, `Yang Wang`, `Yanjie Wang`, `Yi Yang`, `Zijian Hu`, `Ziyi Yang`, `Zonghan Zhou`, `Binghao Qiang`, `Borui Zhang`, `Chenning Li`, `Enchang Zhang`, `Feifan Chen`, `Feng Jian`, `Fengyin Sun`, `Hao Qiu`, `Hao Zheng`, `Haoran Zhu`, `Hongyu Liu`, `Jianbin Deng`, `Jiaxin Song`, `Jiaying Chi`, `Jiayou Shi`, `Jie Fang`, `Jinghui Zhong`, `Jingyu Zhou`, `Jinze Li`, `Junfeng Yi`, `Junyan Yu`, `Junzhi Xue`, `Ni Song`, `Pengyi Chen`, `Qi Chen`, `Quansheng Li`, `Rui Tao`, `Shenghai Gong`, `Shenhang Lu`, `Tianqi Shen`, `Tianxiang Zhu`, `Tiehan Kang`, `Tingyu Li`, `Wendi Wu`, `Xiao Shen`, `Xiao Zhou`, `Xiaotao Zhang`, `Xinrong Li`, `Xuankun Yang`, `Xun Zhang`, `Yan Li`, `Ye Lu`, `Yi Wang`, `Yibo Zhou`, `Yichi Zhang`, `Yihao Sun`, `Yijun Huang`, `Yixin Zhu`, `Yixuan Wu`, `Yuchen Sun`, `Yue Wu`, `Yuheng Sun`, `Yukun Li`, `Yutian Tu`, `Yuxuan Qin`, `Yuzhuo Wu`, `Zeyu Li`, `Zhengyu Lou`, `Zhenning Ran`, `Zizhu He`, `Pengfei Liu`
- ai_keywords: `OpenClaw`, `academic workflows`, `task completion`, `multi-dimensional rubrics`, `safety audit`, `frontier models`, `token consumption`, `output quality`
- upvotes: `8`
- num_comments: `2`
- abstract: Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined. We introduce AcademiClaw, a bilingual benchmark of 80 complex, long-horizon tasks sourced directly from university students' real academic workflows -- homework, research projects, competitions, and personal projects -- that they found current AI agents unable to solve effectively. Curated from 230 student-submitted candidates through rigorous expert review, the final task set spans 25+ professional domains, ranging from olympiad-level mathematics and linguistics problems to GPU-intensive reinforcement learning and full-stack system debugging, with 16 tasks requiring CUDA GPU execution. Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis. Experiments on six frontier models show that even the best achieves only a 55\% pass rate. Further analysis uncovers sharp capability boundaries across task domains, divergent behavioral strategies among models, and a disconnect between token consumption and output quality, providing fine-grained diagnostic signals beyond what aggregate metrics reveal. We hope that AcademiClaw and its open-sourced data and code can serve as a useful resource for the OpenClaw community, driving progress toward agents that are more capable and versatile across the full breadth of real-world academic demands. All data and code are available at https://github.com/GAIR-NLP/AcademiClaw.
- hf_ai_summary: AcademiClaw presents a comprehensive benchmark for evaluating AI agents on complex academic tasks spanning multiple domains, revealing significant capability gaps in current models.

## Source Excerpt

Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined. We introduce AcademiClaw, a bilingual benchmark of 80 complex, long-horizon tasks sourced directly from university students' real academic workflows -- homework, research projects, competitions, and personal projects -- that they found current AI agents unable to solve effectively. Curated from 230 student-submitted candidates through rigorous expert review, the final task set spans 25+ professional domains, ranging from olympiad-level mathematics and linguistics problems to GPU-intensive reinforcement learning and full-stack system debugging, with 16 tasks requiring CUDA GPU execution. Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis. Experiments on six frontier models show that even the best achieves only a 55\% pass rate. Further analysis uncovers sharp capability boundaries across task domains, divergent behavioral strategies among models, and a disconnect between token consumption and output quality, providing fine-grained diagnostic signals beyond what aggregate metrics reveal. We hope that AcademiClaw and its open-sourced data and code can serve as a useful resource for the OpenClaw community, driving progress toward agents that are more capable and versatile across the full breadth of real-world academic demands. All data and code are available at this https URL .

## Open Questions

- What are the six complementary scoring techniques used in the task-completion rubric?
- What are the five safety-audit categories, and how are they measured?
- Which six frontier models were evaluated, and how did their results differ by task domain?
- What specific behavioral strategies distinguished the models in the analysis?
- Is the dataset and evaluation code publicly usable for reproducing the benchmark results?
