---
type: source-summary
status: active
tags: [hf-daily-papers, papers, generated]
source_count: 25
updated: 2026-04-29
generator: scripts/update_hf_daily_papers.py
---

# Hugging Face Daily Papers Latest

## Summary

- generated_at: 2026-04-29T16:10:01+08:00
- window_days: 3
- total_items: 25
- accepted: 10
- maybe: 6
- rejected: 9
- staged_for_ingest: 10
- reused_from_state: 25
- filter_mode: cheap Codex subagent over title + abstract + HF AI summary
- extraction_mode: cheap Codex subagent grounded in original paper pages or arXiv abstract pages when available

## Notes

- This file is generated from Hugging Face Daily Papers and should be updated by script, not edited by hand.
- Accepted papers are written to `sources/inbox/hf-daily-papers/` for later ingest.
- Model credentials are handled by local Codex CLI auth and local ignored env config.
- Knowledge extraction prefers original paper pages or arXiv abstract pages before falling back to Hugging Face metadata.

## Accept

- [Step-Audio-R1.5 Technical Report](https://huggingface.co/papers/2604.25719)
  - paper_id: `2604.25719`; decision: `accept`; score: `84`; upvotes: `8`
  - reason: Directly relevant post-training work on RLVR versus RLHF, with a concrete argument about reward design and reasoning behavior shaping.
  - matched: `reinforcement-learning`, `post-training`, `reward-modeling`, `rlhf`, `reasoning-behavior-shaping`, `llm-systems`
  - weak_signals: `audio-language-models`, `long-turn-dialogues`, `verifiable-rewards`
  - downrank: `domain-specific-audio-focus`, `technical-report-not-core-agent-work`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-25719-step-audio-r1-5-technical-report.md`
- [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://huggingface.co/papers/2604.25256)
  - paper_id: `2604.25256`; decision: `accept`; score: `92`; upvotes: `21`
  - reason: A strong agent-evaluation benchmark for autonomous scientific literature discovery, directly relevant to agent architectures and evaluation.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `scientific-literature-discovery`, `autonomous-research`, `web-browsing-benchmark`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-25256-autoresearchbench-benchmarking-ai-agents-on-complex-scientific-literature-discov.md`
- [TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://huggingface.co/papers/2604.24005)
  - paper_id: `2604.24005`; decision: `accept`; score: `92`; upvotes: `5`
  - reason: Strong match on agent training and post-training: it studies on-policy distillation stability for multi-turn autonomous agents with benchmark gains.
  - matched: `agents`, `post-training`, `reinforcement-learning`, `agent-evals`, `llm-systems`
  - weak_signals: `temporal-curriculum`, `trajectory-level-kl`, `student-teacher-distillation`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-24005-tcod-exploring-temporal-curriculum-in-on-policy-distillation-for-multi-turn-auto.md`
- [GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction](https://huggingface.co/papers/2604.23941)
  - paper_id: `2604.23941`; decision: `accept`; score: `88`; upvotes: `0`
  - reason: A technically detailed GUI grounding model for autonomous agents and environment interaction, with clear deployment and architecture insights.
  - matched: `agents`, `tool-use`, `llm-systems`, `environment-interaction`, `agent-architectures`
  - weak_signals: `mobile-device-deployment`, `encoder-decoder-architecture`, `data-refinement-pipeline`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-23941-goclick-lightweight-element-grounding-model-for-autonomous-gui-interaction.md`
- [AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark](https://huggingface.co/papers/2604.24441)
  - paper_id: `2604.24441`; decision: `accept`; score: `85`; upvotes: `1`
  - reason: A technically useful benchmark for GUI agents that measures functionality understanding, grounding, and interaction outcome prediction.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `gui-navigation`, `digital-autonomy`, `benchmark`, `semantic-grounding`, `dynamic-state-prediction`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-24441-autogui-v2-a-comprehensive-multi-modal-gui-functionality-understanding-benchmark.md`
- [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://huggingface.co/papers/2604.25727)
  - paper_id: `2604.25727`; decision: `accept`; score: `88`; upvotes: `5`
  - reason: Directly targets terminal agents, trajectory synthesis, and benchmark-driven training for agentic system improvement.
  - matched: `agents`, `agent-evals`, `llm-systems`, `environment-interaction`, `post-training`
  - weak_signals: `multi-agent-harness`, `workflow-path-sampling`, `terminal-bench`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-25727-toward-scalable-terminal-task-synthesis-via-skill-graphs.md`
- [DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios](https://huggingface.co/papers/2604.25914)
  - paper_id: `2604.25914`; decision: `accept`; score: `82`; upvotes: `32`
  - reason: A strong agent-evaluation benchmark for real-world environment interaction and task alignment in a practical workflow domain.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `benchmark`, `workflow`, `environment-interaction`
  - downrank: `domain-specific-dv`, `not-rlhf`, `not-mechanistic-interpretability`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-25914-dv-world-benchmarking-data-visualization-agents-in-real-world-scenarios.md`
- [Recursive Multi-Agent Systems](https://huggingface.co/papers/2604.25917)
  - paper_id: `2604.25917`; decision: `accept`; score: `92`; upvotes: `53`
  - reason: A technically grounded multi-agent architecture paper with recursive reasoning, credit assignment, and evaluation across code and reasoning benchmarks.
  - matched: `agents`, `agent-architectures`, `reasoning`, `llm-systems`, `agent-evals`
  - weak_signals: `code-generation`, `tool-use-adjacent`, `efficiency/latency trade-offs`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-25917-recursive-multi-agent-systems.md`
- [Towards Understanding the Robustness of Sparse Autoencoders](https://huggingface.co/papers/2604.18756)
  - paper_id: `2604.18756`; decision: `accept`; score: `82`; upvotes: `1`
  - reason: Sparse autoencoders for jailbreak robustness directly ties mechanistic interpretability to alignment/security behavior shaping.
  - matched: `mechanistic-interpretability`, `representation-analysis`, `alignment`, `post-training`
  - weak_signals: `llm-systems`, `reasoning-behavior-shaping`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-18756-towards-understanding-the-robustness-of-sparse-autoencoders.md`
- [Why Fine-Tuning Encourages Hallucinations and How to Fix It](https://huggingface.co/papers/2604.15574)
  - paper_id: `2604.15574`; decision: `accept`; score: `88`; upvotes: `13`
  - reason: Directly addresses post-training hallucination mitigation with continual-learning methods and a mechanism analysis of interference.
  - matched: `post-training`, `reinforcement-learning`, `mechanistic-interpretability`, `llm-systems`
  - weak_signals: `self-distillation`, `continual-learning`, `representation-interference`, `hallucination-mitigation`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-29-2604-15574-why-fine-tuning-encourages-hallucinations-and-how-to-fix-it.md`

## Maybe

- [Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models](https://huggingface.co/papers/2604.21523)
  - paper_id: `2604.21523`; decision: `maybe`; score: `58`; upvotes: `1`
  - reason: Useful evaluation work on VLM judges and benchmarking reliability, but it is adjacent to rather than centered on the main RL/agent/interpretability priorities.
  - matched: `llm-systems`, `agent-evals`
  - weak_signals: `benchmarking`, `evaluation reliability`, `pairwise comparison`, `factual grounding`
  - downrank: `vision-language models`, `image-to-text`, `text-to-image`, `consumer-eval-focus`
- [BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate](https://huggingface.co/papers/2604.25203)
  - paper_id: `2604.25203`; decision: `maybe`; score: `68`; upvotes: `5`
  - reason: Relevant to alignment and post-training via synthetic data, debate-based verification, and custom guardrail training, but it is not primarily an RL or agent-methods paper.
  - matched: `post-training`, `alignment`, `agent-evals`, `llm-systems`
  - weak_signals: `multi-agent debate`, `synthetic training data`, `fine-tuning`, `custom guardrails`
  - downrank: `not core reinforcement learning`, `not mechanistic-interpretability`, `guardrail/classifier focus rather than agent architecture`
- [Co-Director: Agentic Generative Video Storytelling](https://huggingface.co/papers/2604.24842)
  - paper_id: `2604.24842`; decision: `maybe`; score: `54`; upvotes: `6`
  - reason: Agentic multi-agent orchestration and bandit-based optimization are methodologically relevant, but the application is video storytelling rather than core agent/RL work.
  - matched: `agents`, `llm-systems`
  - weak_signals: `hierarchical-multi-agent-framework`, `agentic-pipelines`, `multi-armed-bandit`, `self-refinement`
  - downrank: `application-domain-video-storytelling`, `no-rllhfrlpost-training`, `not-mechanistic-interpretability`, `limited-direct-agent-eval-focus`
- [A Systematic Post-Train Framework for Video Generation](https://huggingface.co/papers/2604.25427)
  - paper_id: `2604.25427`; decision: `maybe`; score: `62`; upvotes: `1`
  - reason: Applies RLHF and GRPO in a concrete post-training pipeline, but the target domain is video generation rather than LLM agents or RL research.
  - matched: `post-training`, `reinforcement-learning`, `rlhf`, `grpo`, `llm-systems`
  - weak_signals: `systematic pipeline`, `implementation-details`, `evaluation-oriented`, `inference-optimization`
  - downrank: `video-generation-domain`, `not-agents`, `not-mechanistic-interpretability`, `adjacent-rather-than-core`
- [Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora](https://huggingface.co/papers/2604.24819)
  - paper_id: `2604.24819`; decision: `maybe`; score: `72`; upvotes: `30`
  - reason: Strong LLM systems and post-training/data-debugging angle, but it is more about domain corpus engineering than core RL or agent methods.
  - matched: `llm-systems`, `post-training`, `reasoning-behavior-shaping`, `agent-evals`
  - weak_signals: `structured-evaluation`, `data-repair`, `benchmarking`, `unit-testing`, `debugging`
  - downrank: `not-rl`, `not-agent-architecture`, `not-mechanistic-interpretability`
- [IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance](https://huggingface.co/papers/2604.23446)
  - paper_id: `2604.23446`; decision: `maybe`; score: `68`; upvotes: `1`
  - reason: Technically useful neurosymbolic EQA and counterfactual reasoning system for safety-critical operations, but it is only indirectly related to the top-priority RL/agents/interpreting topics.
  - matched: `llm-systems`, `reasoning`, `alignment`
  - weak_signals: `neurosymbolic`, `counterfactual-reasoning`, `explainability`, `knowledge-graph`
  - downrank: `industrial-maintenance`, `embodied-question-answering`, `domain-specific-application`

## Reject

- [MAIC-UI: Making Interactive Courseware with Generative UI](https://huggingface.co/papers/2604.25806)
  - paper_id: `2604.25806`; decision: `reject`; score: `12`; upvotes: `3`
  - reason: This is an educational generative-UI authoring system, not work on RL, agents, or mechanistic interpretability.
  - weak_signals: `llm-systems`
  - downrank: `education`, `generative-ui`, `zero-code-authoring`, `no-agent-loop`, `no-training-or-eval-focus`
- [Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](https://huggingface.co/papers/2604.21481)
  - paper_id: `2604.21481`; decision: `reject`; score: `24`; upvotes: `1`
  - reason: Useful evaluation methodology, but the paper is about multilingual TTS preference analysis rather than RL, agents, or interpretability.
  - matched: `llm-systems`
  - weak_signals: `pairwise-evaluation`, `benchmarking`, `leaderboard-analysis`
  - downrank: `tts`, `speech-perception`, `linguistic-diversity`, `outside-core-topics`
- [Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://huggingface.co/papers/2604.25819)
  - paper_id: `2604.25819`; decision: `reject`; score: `12`; upvotes: `12`
  - reason: Focused on efficient audio-video generation, not RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `multimodal-generation`, `audio-video-synthesis`, `architecture-only`, `no-agent-or-reasoning-focus`
- [Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models](https://huggingface.co/papers/2604.25636)
  - paper_id: `2604.25636`; decision: `reject`; score: `18`; upvotes: `20`
  - reason: Focuses on multimodal image refinement rather than RL, agents, or mechanistic interpretability.
  - weak_signals: `llm-systems`
  - downrank: `vision-generation`, `multimodal-models`, `text-to-image`, `image-editing`
- [IAM: Identity-Aware Human Motion and Shape Joint Generation](https://huggingface.co/papers/2604.25164)
  - paper_id: `2604.25164`; decision: `reject`; score: `4`; upvotes: `1`
  - reason: This is about identity-aware human motion generation, not RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `computer-vision`, `motion-generation`, `human-shape-modeling`
- [Meta-CoT: Enhancing Granularity and Generalization in Image Editing](https://huggingface.co/papers/2604.24625)
  - paper_id: `2604.24625`; decision: `reject`; score: `22`; upvotes: `22`
  - reason: Primarily an image-editing method; only a light reward-shaping hook and no clear RL, agents, or interpretability focus.
  - matched: `reasoning-behavior-shaping`
  - weak_signals: `CoT-Editing Consistency Reward`, `training strategy for generalization`, `behavior alignment via reward`
  - downrank: `image-editing`, `multimodal-understanding`, `limited relevance to RLHF or agents`
- [Improving Robustness of Tabular Retrieval via Representational Stability](https://huggingface.co/papers/2604.24040)
  - paper_id: `2604.24040`; decision: `reject`; score: `22`; upvotes: `1`
  - reason: Focuses on table retrieval robustness and embedding geometry, which is useful systems work but not aligned with the core RL, agents, or interpretability priorities.
  - matched: `llm-systems`
  - weak_signals: `retrieval-benchmarks`, `representation-stability`, `encoder-geometry`
  - downrank: `outside-core-priorities`, `no-rl-or-agents`, `no-mechanistic-interpretability`, `applied-retrieval-only`
- [Sapiens2](https://huggingface.co/papers/2604.21681)
  - paper_id: `2604.21681`; decision: `reject`; score: `12`; upvotes: `11`
  - reason: A human-centric vision model family with no substantive RL, agents, or interpretability content.
  - weak_signals: `llm-systems`
  - downrank: `computer-vision`, `dense-prediction`, `human-centric-vision`, `benchmark-improvement`
- [Personality Shapes Gender Bias in Persona-Conditioned LLM Narratives Across English and Hindi: An Empirical Investigation](https://huggingface.co/papers/2604.23600)
  - paper_id: `2604.23600`; decision: `reject`; score: `18`; upvotes: `0`
  - reason: This is a bias study of persona-conditioned narrative generation, not a strong fit for RL, agents, or mechanistic interpretability.
  - weak_signals: `llm-systems`, `alignment`
  - downrank: `persona-conditioning`, `gender-bias`, `story-generation`, `representational-harms`
