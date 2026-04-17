---
type: source-summary
status: active
tags: [hf-daily-papers, papers, generated]
source_count: 25
updated: 2026-04-16
generator: scripts/update_hf_daily_papers.py
---

# Hugging Face Daily Papers Latest

## Summary

- generated_at: 2026-04-16T09:43:52+08:00
- window_days: 3
- total_items: 25
- accepted: 6
- maybe: 12
- rejected: 7
- staged_for_ingest: 6
- reused_from_state: 0
- filter_mode: cheap Codex subagent over title + abstract + HF AI summary
- extraction_mode: cheap Codex subagent grounded in original paper pages or arXiv abstract pages when available

## Notes

- This file is generated from Hugging Face Daily Papers and should be updated by script, not edited by hand.
- Accepted papers are written to `sources/inbox/hf-daily-papers/` for later ingest.
- Model credentials are handled by local Codex CLI auth and local ignored env config.
- Knowledge extraction prefers original paper pages or arXiv abstract pages before falling back to Hugging Face metadata.

## Accept

- [Spec Kit Agents: Context-Grounded Agentic Workflows](https://huggingface.co/papers/2604.05278)
  - paper_id: `2604.05278`; decision: `accept`; score: `84`; upvotes: `1`
  - reason: Directly about coding-agent workflows and evaluation, with concrete multi-agent architecture and benchmark results.
  - matched: `agents`, `agent-architectures`, `agent-evals`, `llm-systems`, `tool-use`, `coding-agents`
  - weak_signals: `spec-driven-development`, `llm-as-judge`, `swe-bench-lite`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-16-2604-05278-spec-kit-agents-context-grounded-agentic-workflows.md`
- [The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents](https://huggingface.co/papers/2604.10577)
  - paper_id: `2604.10577`; decision: `accept`; score: `92`; upvotes: `13`
  - reason: A strong agent-safety evaluation paper on computer-use agents, multi-agent failure modes, and safety alignment dynamics.
  - matched: `agents`, `agent-evals`, `llm-systems`, `alignment`
  - weak_signals: `computer-use agents`, `multi-agent systems`, `safety defenses`, `environment interaction`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-16-2604-10577-the-blind-spot-of-agent-safety-how-benign-user-instructions-expose-critical-vuln.md`
- [ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)
  - paper_id: `2604.11784`; decision: `accept`; score: `94`; upvotes: `121`
  - reason: Directly targets GUI agents with RL training, standardized evaluation, and deployment infrastructure.
  - matched: `agents`, `reinforcement-learning`, `post-training`, `agent-evals`, `llm-systems`
  - weak_signals: `GUI agents`, `dense step-level supervision`, `cross-platform deployment`, `benchmark standardization`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-15-2604-11784-clawgui-a-unified-framework-for-training-evaluating-and-deploying-gui-agents.md`
- [Turing Test on Screen: A Benchmark for Mobile GUI Agent Humanization](https://huggingface.co/papers/2604.09574)
  - paper_id: `2604.09574`; decision: `accept`; score: `82`; upvotes: `27`
  - reason: A concrete benchmark and evaluation framework for mobile GUI agents, with technical details on behavior matching and performance trade-offs.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `adversarial-detection`, `behavioral-divergence`, `mobile-gui-agents`
  - downrank: `not-rlhf`, `not-mechanistic-interpretability`, `narrow-domain-humanization`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-15-2604-09574-turing-test-on-screen-a-benchmark-for-mobile-gui-agent-humanization.md`
- [CONSCIENTIA: Can LLM Agents Learn to Strategize? Emergent Deception and Trust in a Multi-Agent NYC Simulation](https://huggingface.co/papers/2604.09746)
  - paper_id: `2604.09746`; decision: `accept`; score: `92`; upvotes: `0`
  - reason: Strong match on LLM agents, strategic behavior in multi-agent interaction, and post-training via KTO for behavior shaping.
  - matched: `agents`, `agent-evals`, `post-training`, `reinforcement-learning`, `llm-systems`
  - weak_signals: `multi-agent simulation`, `adversarial persuasion`, `selective trust`, `selective cooperation`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-15-2604-09746-conscientia-can-llm-agents-learn-to-strategize-emergent-deception-and-trust-in-a.md`
- [Many-Tier Instruction Hierarchy in LLM Agents](https://huggingface.co/papers/2604.09443)
  - paper_id: `2604.09443`; decision: `accept`; score: `78`; upvotes: `13`
  - reason: Strongly relevant agent-evaluation work on scalable instruction conflict resolution in LLM agents.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `instruction-following`, `coding-tasks`, `architecture-tradeoffs`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-04-15-2604-09443-many-tier-instruction-hierarchy-in-llm-agents.md`

## Maybe

- [Parcae: Scaling Laws For Stable Looped Language Models](https://huggingface.co/papers/2604.12946)
  - paper_id: `2604.12946`; decision: `maybe`; score: `54`; upvotes: `2`
  - reason: Useful LLM systems/architecture work on stable looped models and scaling laws, but it is not directly about RL, agents, or interpretability.
  - matched: `llm-systems`
  - weak_signals: `scaling-laws`, `architecture-trade-offs`, `test-time-compute`
  - downrank: `not-rl`, `not-agents`, `not-mechanistic-interpretability`
- [Do Thought Streams Matter? Evaluating Reasoning in Gemini Vision-Language Models for Video Scene Understanding](https://huggingface.co/papers/2604.11177)
  - paper_id: `2604.11177`; decision: `maybe`; score: `63`; upvotes: `4`
  - reason: It studies internal reasoning traces and hallucination behavior, but the main setting is VLM video understanding rather than core RL/agents/interpretability.
  - matched: `reasoning-behavior`, `llm-systems`
  - weak_signals: `internal reasoning traces`, `evaluation metrics for thought-final coverage`, `compression-step hallucination`
  - downrank: `vision-language models`, `video scene understanding`, `not about RLHF or agents`, `limited direct interpretability depth`
- [Learning Versatile Humanoid Manipulation with Touch Dreaming](https://huggingface.co/papers/2604.13015)
  - paper_id: `2604.13015`; decision: `maybe`; score: `68`; upvotes: `2`
  - reason: Technically strong humanoid manipulation paper with an RL-based controller and contact-aware policy learning, but it is more robotics than core RL/post-training or agents.
  - matched: `reinforcement-learning`, `post-training`, `llm-systems`
  - weak_signals: `behavioral-cloning`, `contact-aware-representations`, `architecture-tradeoffs`, `benchmark`
  - downrank: `robotics`, `humanoid-manipulation`, `not-llm-centric`
- [LASA: Language-Agnostic Semantic Alignment at the Semantic Bottleneck for LLM Safety](https://huggingface.co/papers/2604.12710)
  - paper_id: `2604.12710`; decision: `maybe`; score: `66`; upvotes: `2`
  - reason: Representation-level safety alignment via semantic bottlenecks is adjacent to mechanistic/representation analysis, but the paper is primarily an LLM safety method rather than core RL or agents work.
  - matched: `mechanistic-interpretability`, `representation-analysis`, `post-training`
  - weak_signals: `alignment-method`, `language-agnostic representations`, `semantic bottleneck`
  - downrank: `llm-safety`, `cross-lingual focus`, `not agents or rl`
- [PokeRL: Reinforcement Learning for Pokemon Red](https://huggingface.co/papers/2604.10812)
  - paper_id: `2604.10812`; decision: `maybe`; score: `72`; upvotes: `1`
  - reason: A practical RL system paper with environment wrappers, anti-loop handling, and hierarchical reward design, but centered on a game benchmark rather than LLM post-training or agents.
  - matched: `reinforcement-learning`, `environment-interaction`, `reward-modeling`
  - weak_signals: `systems-playbook`, `benchmark-design`, `implementation-details`
  - downrank: `game-specific`, `not-llm`, `narrow-task-scope`
- [Spatial Competence Benchmark](https://huggingface.co/papers/2604.09594)
  - paper_id: `2604.09594`; decision: `maybe`; score: `48`; upvotes: `1`
  - reason: A benchmark paper on spatial reasoning and internal representations with deterministic evaluators is adjacent to evaluation and representation analysis, but not a core target area.
  - matched: `representation-analysis`, `llm-systems`, `agent-evals`
  - weak_signals: `deterministic-checkers`, `simulator-based-evaluators`, `internal-representation`, `action-planning`
  - downrank: `spatial-reasoning-benchmark`, `limited-direct-rl-or-agents-content`, `single-benchmark-focus`
- [BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation](https://huggingface.co/papers/2604.09497)
  - paper_id: `2604.09497`; decision: `maybe`; score: `68`; upvotes: `21`
  - reason: A practical LLM evaluation method with implementation and tradeoff details, but it is not directly about RL, agents, or mechanistic interpretability.
  - matched: `llm-systems`, `agent-evals`
  - weak_signals: `reference-based-evaluation`, `llm-as-a-judge`, `practical-benchmarking`
  - downrank: `not-rl`, `not-agents`, `not-mechanistic-interpretability`
- [Accelerating Speculative Decoding with Block Diffusion Draft Trees](https://huggingface.co/papers/2604.12989)
  - paper_id: `2604.12989`; decision: `maybe`; score: `68`; upvotes: `4`
  - reason: A speculative decoding systems paper with concrete drafter/tree verification mechanics, relevant to LLM efficiency but not a direct hit on agents, RL, or interpretability.
  - matched: `llm-systems`
  - weak_signals: `speculative-decoding`, `draft-models`, `architecture-trade-offs`, `benchmark-performance`
  - downrank: `not-reinforcement-learning`, `not-agents`, `not-mechanistic-interpretability`
- [When Reasoning Models Hurt Behavioral Simulation: A Solver-Sampler Mismatch in Multi-Agent LLM Negotiation](https://huggingface.co/papers/2604.11840)
  - paper_id: `2604.11840`; decision: `maybe`; score: `71`; upvotes: `1`
  - reason: Relevant to agent behavior and reasoning evaluation, but it is more about behavioral simulation than building or training agents.
  - matched: `agents`, `agent-evals`, `reasoning-behavior-shaping`
  - weak_signals: `multi-agent negotiation`, `bounded rationality`, `simulation fidelity`, `reflection conditions`
  - downrank: `not RLHF/reward-modeling`, `not mechanistic-interpretability`, `limited systems/implementation depth`
- [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](https://huggingface.co/papers/2604.12373)
  - paper_id: `2604.12373`; decision: `maybe`; score: `72`; upvotes: `4`
  - reason: Uses hidden-state and layer-level analysis to study privileged internal knowledge in LLM correctness, which fits representation analysis and mechanistic interpretability.
  - matched: `mechanistic-interpretability`, `representation-analysis`, `internal-dynamics`
  - weak_signals: `correctness-classifiers`, `hidden-states`, `layerwise-analysis`, `self-vs-peer-probes`
  - downrank: `not-about-reinforcement-learning`, `not-about-agents-or-tool-use`, `narrow-to-correctness-prediction`
- [Beyond Perception Errors: Semantic Fixation in Large Vision-Language Models](https://huggingface.co/papers/2604.12119)
  - paper_id: `2604.12119`; decision: `maybe`; score: `68`; upvotes: `1`
  - reason: Relevant for post-training, prompt interventions, and late-layer representation steering in VLMs, but not core RL or agents work.
  - matched: `post-training`, `mechanistic-interpretability`, `representation-analysis`, `llm-systems`
  - weak_signals: `controlled benchmark`, `prompt interventions`, `late-layer activation steering`, `training transfer effects`
  - downrank: `vision-language focus`, `no reinforcement-learning`, `not agentic`, `limited alignment framing`
- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://huggingface.co/papers/2604.11689)
  - paper_id: `2604.11689`; decision: `maybe`; score: `73`; upvotes: `8`
  - reason: Strongly relevant to vision-to-action alignment and embodied agent control, with useful benchmark and representation analysis, but not directly about RLHF or mechanistic interpretability.
  - matched: `agents`, `agent-evals`, `llm-systems`
  - weak_signals: `embodied-control`, `vision-to-action-alignment`, `benchmark`, `representation-analysis`
  - downrank: `not-llm-post-training`, `not-mechanistic-interpretability`, `vision-centric-rather-than-core-rl`

## Reject

- [Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models](https://huggingface.co/papers/2604.09687)
  - paper_id: `2604.09687`; decision: `reject`; score: `28`; upvotes: `1`
  - reason: Useful VLM evaluation work, but it is mostly about visual-detail failures rather than RL, agents, or mechanistic interpretability.
  - matched: `llm-systems`
  - weak_signals: `end-to-end evaluation`, `structured failure analysis`, `multimodal alignment`
  - downrank: `not-rllm`, `not-agents`, `not-mechanistic-interpretability`, `vision-language-models`
- [Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective](https://huggingface.co/papers/2604.14025)
  - paper_id: `2604.14025`; decision: `reject`; score: `9`; upvotes: `2`
  - reason: A 3D reconstruction survey with evaluation/dataset discussion, but it is mostly vision/graphics rather than the user’s core RL, agents, or interpretability interests.
  - weak_signals: `llm-systems`
  - downrank: `computer-vision`, `3d-reconstruction`, `survey`, `world-modeling`
- [GlotOCR Bench: OCR Models Still Struggle Beyond a Handful of Unicode Scripts](https://huggingface.co/papers/2604.12978)
  - paper_id: `2604.12978`; decision: `reject`; score: `18`; upvotes: `4`
  - reason: A multilingual OCR benchmark is useful, but it is not closely tied to RL, agents, or mechanistic interpretability.
  - weak_signals: `llm-systems`, `benchmarking`
  - downrank: `ocr`, `vision-language-models`, `multilingual-text`, `unicode-scripts`
- [Domain-Specific Latent Representations Improve the Fidelity of Diffusion-Based Medical Image Super-Resolution](https://huggingface.co/papers/2604.12152)
  - paper_id: `2604.12152`; decision: `reject`; score: `6`; upvotes: `1`
  - reason: Medical image super-resolution with diffusion is technically solid but outside the user's core interests in RL, agents, and interpretability.
  - weak_signals: `llm-systems`
  - downrank: `medical-imaging`, `diffusion`, `super-resolution`, `not-about-reinforcement-learning`, `not-about-agents`, `not-about-interpretability`
- [3DTV: A Feedforward Interpolation Network for Real-Time View Synthesis](https://huggingface.co/papers/2604.11211)
  - paper_id: `2604.11211`; decision: `reject`; score: `12`; upvotes: `1`
  - reason: This is a real-time view synthesis and rendering paper, not focused on RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `computer-vision`, `real-time-rendering`, `multi-view-video`, `AR/VR`
- [SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding](https://huggingface.co/papers/2604.13023)
  - paper_id: `2604.13023`; decision: `reject`; score: `18`; upvotes: `0`
  - reason: It is an audio-language grounding paper, not a strong match for RL, agents, or mechanistic interpretability.
  - matched: `llm-systems`
  - weak_signals: `temporal grounding`, `benchmarking`, `hallucination suppression`
  - downrank: `audio-language-domain`, `outside-core-priorities`, `no-agent-or-rl-methodology`
- [Hierarchical SVG Tokenization: Learning Compact Visual Programs for Scalable Vector Graphics Modeling](https://huggingface.co/papers/2604.05072)
  - paper_id: `2604.05072`; decision: `reject`; score: `18`; upvotes: `3`
  - reason: This is a vector graphics tokenization paper with little direct relevance to RL, agents, or interpretability.
  - weak_signals: `llm-systems`, `sequence-efficiency`, `tokenization`
  - downrank: `svg-generation`, `image-to-svg`, `text-to-svg`, `generic-generation`
