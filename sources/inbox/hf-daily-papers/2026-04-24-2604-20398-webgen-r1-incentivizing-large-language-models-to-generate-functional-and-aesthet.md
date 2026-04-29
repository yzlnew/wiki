---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, llm-systems, llm, website-generation, agentic-systems, multimodal-reward]
source_count: 1
updated: 2026-04-25
source_url: https://arxiv.org/abs/2604.20398
paper_id: 2604.20398
published: 2026-04-22T04:00:00+08:00
submitted_on_daily: 2026-04-24T11:42:24+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning

## Summary

- one_sentence_summary: WebGen-R1 is an end-to-end RL framework that teaches a 7B LLM to generate functional, visually coherent multi-page websites by combining scaffolded structured generation with cascaded multimodal rewards.
- why_relevant: This is directly relevant to reinforcement learning and post-training for agentic, tool-like code generation systems, especially where the training signal must cover functional behavior and visual quality rather than only text or unit-test-style correctness.
- filter_reason: Directly applies reinforcement learning to post-training a small LLM for project-level code generation with structured rewards.
- hugging_face_paper: https://huggingface.co/papers/2604.20398
- original_paper: https://arxiv.org/abs/2604.20398
- source_basis: `original abstract page`

## Key Points

- The paper targets project-level website generation, which is harder than single-file code generation because it must handle cross-page interactions, functional correctness, and subjective aesthetics.
- WebGen-R1 uses a scaffold-driven structured generation paradigm to constrain the action space and preserve architectural integrity during generation.
- Its reward design is cascaded and multimodal, combining structural guarantees, execution-grounded functional feedback, and vision-based aesthetic supervision.
- In experiments, the method reportedly turns a 7B base model from producing nearly nonfunctional websites into generating deployable multi-page websites.
- The paper claims the approach outperforms much larger open-source models and matches DeepSeek-R1 on functional success while doing better on rendering validity and aesthetic alignment.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.20398
- Hugging Face API entry: https://huggingface.co/api/papers/2604.20398
- arXiv abstract: https://arxiv.org/abs/2604.20398

## Paper Metadata

- authors: `Juyong Jiang`, `Chenglin Cai`, `Chansung Park`, `Jiasi Shen`, `Sunghun Kim`, `Jianguo Li`, `Yue Wang`
- ai_keywords: `Large Language Models`, `reinforcement learning`, `website generation`, `structured generation paradigm`, `cascaded multimodal reward`, `functional correctness`, `aesthetic supervision`, `end-to-end RL framework`, `multi-page websites`, `agent-based frameworks`
- upvotes: `3`
- num_comments: `2`
- abstract: While Large Language Models (LLMs) excel at function-level code generation, project-level tasks such as generating functional and visually aesthetic multi-page websites remain highly challenging. Existing works are often limited to single-page static websites, while agentic frameworks typically rely on multi-turn execution with proprietary models, leading to substantial token costs, high latency, and brittle integration. Training a small LLM end-to-end with reinforcement learning (RL) is a promising alternative, yet it faces a critical bottleneck in designing reliable and computationally feasible rewards for website generation. Unlike single-file coding tasks that can be verified by unit tests, website generation requires evaluating inherently subjective aesthetics, cross-page interactions, and functional correctness. To this end, we propose WebGen-R1, an end-to-end RL framework tailored for project-level website generation. We first introduce a scaffold-driven structured generation paradigm that constrains the large open-ended action space and preserves architectural integrity. We then design a novel cascaded multimodal reward that seamlessly couples structural guarantees with execution-grounded functional feedback and vision-based aesthetic supervision. Extensive experiments demonstrate that our WebGen-R1 substantially transforms a 7B base model from generating nearly nonfunctional websites into producing deployable, aesthetically aligned multi-page websites. Remarkably, our WebGen-R1 not only consistently outperforms heavily scaled open-source models (up to 72B), but also rivals the state-of-the-art DeepSeek-R1 (671B) in functional success, while substantially exceeding it in valid rendering and aesthetic alignment. These results position WebGen-R1 as a viable path for scaling small open models from function-level code generation to project-level web application generation.
- hf_ai_summary: A reinforcement learning framework for project-level website generation that combines structured scaffolding with multimodal rewards to produce functional and aesthetically pleasing multi-page sites from small language models.

## Source Excerpt

While Large Language Models (LLMs) excel at function-level code generation, project-level tasks such as generating functional and visually aesthetic multi-page websites remain highly challenging. Existing works are often limited to single-page static websites, while agentic frameworks typically rely on multi-turn execution with proprietary models, leading to substantial token costs, high latency, and brittle integration. Training a small LLM end-to-end with reinforcement learning (RL) is a promising alternative, yet it faces a critical bottleneck in designing reliable and computationally feasible rewards for website generation. Unlike single-file coding tasks that can be verified by unit tests, website generation requires evaluating inherently subjective aesthetics, cross-page interactions, and functional correctness. To this end, we propose WebGen-R1, an end-to-end RL framework tailored for project-level website generation. We first introduce a scaffold-driven structured generation paradigm that constrains the large open-ended action space and preserves architectural integrity. We then design a novel cascaded multimodal reward that seamlessly couples structural guarantees with execution-grounded functional feedback and vision-based aesthetic supervision. Extensive experiments demonstrate that our WebGen-R1 substantially transforms a 7B base model from generating nearly nonfunctional websites into producing deployable, aesthetically aligned multi-page websites. Remarkably, our WebGen-R1 not only consistently outperforms heavily scaled open-source models (up to 72B), but also rivals the state-of-the-art DeepSeek-R1 (671B) in functional success, while substantially exceeding it in valid rendering and aesthetic alignment. These results position WebGen-R1 as a viable path for scaling small open models from function-level code generation to project-level web application generation.

## Open Questions

- What exact benchmarks, tasks, and evaluation metrics were used for functional success, valid rendering, and aesthetic alignment?
- How is the cascaded multimodal reward computed in practice, and what are the relative contributions of each reward component?
- What scaffold constraints are enforced during generation, and how much do they matter compared with the reward design?
- How stable is end-to-end RL training for this setting across different base models or website complexity levels?
