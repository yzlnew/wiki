---
type: source-summary
status: active
tags: [hf-daily-papers, papers, generated]
source_count: 21
updated: 2026-05-05
generator: scripts/update_hf_daily_papers.py
---

# Hugging Face Daily Papers Latest

## Summary

- generated_at: 2026-05-05T09:42:59+08:00
- window_days: 3
- total_items: 21
- accepted: 6
- maybe: 4
- rejected: 11
- staged_for_ingest: 6
- reused_from_state: 2
- filter_mode: cheap Codex subagent over title + abstract + HF AI summary
- extraction_mode: cheap Codex subagent grounded in original paper pages or arXiv abstract pages when available

## Notes

- This file is generated from Hugging Face Daily Papers and should be updated by script, not edited by hand.
- Accepted papers are written to `sources/inbox/hf-daily-papers/` for later ingest.
- Model credentials are handled by local Codex CLI auth and local ignored env config.
- Knowledge extraction prefers original paper pages or arXiv abstract pages before falling back to Hugging Face metadata.

## Accept

- [Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning](https://huggingface.co/papers/2605.00347)
  - paper_id: `2605.00347`; decision: `accept`; score: `94`; upvotes: `7`
  - reason: Long-horizon RL training for VLM agents with PPO/GRPO comparisons and practical stability guidance is directly aligned with agents and post-training.
  - matched: `reinforcement-learning`, `agents`, `post-training`, `llm-systems`, `agent-evals`
  - weak_signals: `vision-language-models`, `long-horizon-decision-making`, `generalization`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-05-2605-00347-odysseus-scaling-vlms-to-100-turn-decision-making-in-games-via-reinforcement-lea.md`
- [MASCing: Configurable Mixture-of-Experts Behavior via Activation Steering Masks](https://huggingface.co/papers/2604.27818)
  - paper_id: `2604.27818`; decision: `accept`; score: `86`; upvotes: `2`
  - reason: Technically detailed MoE behavior steering for safety reconfiguration without retraining, which is useful for post-training and model control work.
  - matched: `post-training`, `llm-systems`, `mechanistic-interpretability`, `reasoning-behavior-shaping`
  - weak_signals: `routing-dependencies`, `expert-circuits`, `safety-reconfiguration`
  - downrank: `safety-focused rather than core RL/agent work`, `no direct RLHF or tool-use component`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-05-2604-27818-mascing-configurable-mixture-of-experts-behavior-via-activation-steering-masks.md`
- [Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction](https://huggingface.co/papers/2604.27221)
  - paper_id: `2604.27221`; decision: `accept`; score: `92`; upvotes: `27`
  - reason: A technically detailed multi-agent web-search/extraction system with coordinated agents, decomposition, and verification fits the agents and LLM-systems priorities.
  - matched: `agents`, `llm-systems`, `agent-evals`, `tool-use`
  - weak_signals: `parallel execution`, `shared workspace`, `run-verify-reflect`, `external memory`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-04-2604-27221-web2bigtable-a-bi-level-multi-agent-llm-system-for-internet-scale-information-se.md`
- [From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills](https://huggingface.co/papers/2604.24026)
  - paper_id: `2604.24026`; decision: `accept`; score: `88`; upvotes: `11`
  - reason: Proposes a structured skill representation for agent systems and shows gains on skill discovery and risk assessment.
  - matched: `agents`, `llm-systems`, `agent-architectures`, `agent-evals`
  - weak_signals: `skill-representation`, `risk-assessment`, `skill-discovery`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-04-2604-24026-from-skill-text-to-skill-structure-the-scheduling-structural-logical-representat.md`
- [Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://huggingface.co/papers/2605.00416)
  - paper_id: `2605.00416`; decision: `accept`; score: `88`; upvotes: `10`
  - reason: Strongly relevant fleet-scale reinforcement learning post-training for embodied policies with deployment-time learning and real-world evaluation.
  - matched: `reinforcement-learning`, `post-training`, `llm-systems`, `agent-environment-interaction`
  - weak_signals: `robotics rather than language-model agents`, `policy improvement and evaluation methodology`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-04-2605-00416-learning-while-deploying-fleet-scale-reinforcement-learning-for-generalist-robot.md`
- [Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring](https://huggingface.co/papers/2605.00754)
  - paper_id: `2605.00754`; decision: `accept`; score: `92`; upvotes: `2`
  - reason: Directly on reward models and post-training, with concrete code-oriented evaluation and multilingual preference training.
  - matched: `post-training`, `reinforcement-learning`, `reward-modeling`, `llm-systems`
  - weak_signals: `code-generation`, `benchmarking`, `cross-lingual-transfer`, `multi-criteria-scoring`
  - inbox_file: `sources/inbox/hf-daily-papers/2026-05-04-2605-00754-themis-training-robust-multilingual-code-reward-models-for-flexible-multi-criter.md`

## Maybe

- [Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance](https://huggingface.co/papers/2605.00553)
  - paper_id: `2605.00553`; decision: `maybe`; score: `68`; upvotes: `10`
  - reason: Technically useful for post-training and reward-driven optimization, but it is primarily about LLM red-teaming via GFlowNets rather than core RLHF or agent work.
  - matched: `post-training`, `reward-modeling`, `llm-systems`
  - weak_signals: `distribution-matching`, `training-stability`, `mode-collapse`, `robust-optimization`
  - downrank: `red-teaming-focus`, `not-agents`, `not-mechanistic-interpretability`, `adjacent-to-core-rlhf`
- [Online Self-Calibration Against Hallucination in Vision-Language Models](https://huggingface.co/papers/2605.00323)
  - paper_id: `2605.00323`; decision: `maybe`; score: `67`; upvotes: `2`
  - reason: Uses online preference alignment and DPO to reduce hallucination, which is adjacent to post-training and reward-based shaping but not core RL/agents work.
  - matched: `post-training`, `alignment`, `llm-systems`
  - weak_signals: `preference-data`, `online-learning`, `direct-preference-optimization`, `self-supervision`
  - downrank: `vision-language-models`, `hallucination-mitigation`, `multimodal-focus`
- [Learning to Act and Cooperate for Distributed Black-Box Consensus Optimization](https://huggingface.co/papers/2605.00691)
  - paper_id: `2605.00691`; decision: `maybe`; score: `58`; upvotes: `2`
  - reason: Relevant as an LLM-guided multi-agent coordination method, but it is optimization/control rather than core RL, RLHF, or agent tool-use work.
  - matched: `agents`, `llm-systems`, `agent-architectures`
  - weak_signals: `multiagent-systems`, `agent-cooperation`, `trajectory-driven guidance`, `distributed optimization`
  - downrank: `not-rlhf`, `not-mechanistic-interpretability`, `not-agent-tool-use`, `niche-optimization-benchmark`
- [Let ViT Speak: Generative Language-Image Pre-training](https://huggingface.co/papers/2605.00809)
  - paper_id: `2605.00809`; decision: `maybe`; score: `36`; upvotes: `10`
  - reason: Technical multimodal pretraining work for MLLMs, but it is not directly about RL, agents, or interpretability.
  - matched: `llm-systems`
  - weak_signals: `multimodal-pretraining`, `vision-language-models`, `architecture-tradeoffs`, `benchmark-results`
  - downrank: `outside-core-priorities`, `no-agent-or-rl-component`, `no-mechanistic-interpretability`

## Reject

- [Soft Anisotropic Diagrams for Differentiable Image Representation](https://huggingface.co/papers/2604.21984)
  - paper_id: `2604.21984`; decision: `reject`; score: `3`; upvotes: `0`
  - reason: This is a differentiable image representation/compression paper, not aligned with RL, agents, interpretability, or alignment work.
  - weak_signals: `differentiable-pipelines`, `gpu-systems`
  - downrank: `computer-vision`, `image-representation`, `compression`, `no-agent-or-reasoning-focus`
- [Better Models, Faster Training: Sigmoid Attention for single-cell Foundation Models](https://huggingface.co/papers/2604.27124)
  - paper_id: `2604.27124`; decision: `reject`; score: `18`; upvotes: `2`
  - reason: Strong technical work on attention for biological foundation models, but it is outside the user’s main RL, agent, and interpretability priorities.
  - weak_signals: `llm-systems`, `architecture-tradeoffs`, `training-stability`
  - downrank: `biology-domain`, `not-rlhf`, `not-agents`, `not-mechanistic-interpretability`
- [Prox-E: Fine-Grained 3D Shape Editing via Primitive-Based Abstractions](https://huggingface.co/papers/2604.23774)
  - paper_id: `2604.23774`; decision: `reject`; score: `8`; upvotes: `13`
  - reason: This is a 3D editing method with VLM guidance, not aligned with RL, agents, or interpretability priorities.
  - weak_signals: `llm-systems`
  - downrank: `3d-editing`, `vision-language-model`, `geometry`, `graphics`
- [When Do Diffusion Models learn to Generate Multiple Objects?](https://huggingface.co/papers/2605.00273)
  - paper_id: `2605.00273`; decision: `reject`; score: `18`; upvotes: `5`
  - reason: Focuses on diffusion image generation and compositional data effects, which is outside the core RL/agents/interpretability priorities.
  - weak_signals: `compositional-generalization`, `benchmarking`
  - downrank: `diffusion-models`, `text-to-image`, `no-agent-or-rl-angle`
- [Trees to Flows and Back: Unifying Decision Trees and Diffusion Models](https://huggingface.co/papers/2605.00414)
  - paper_id: `2605.00414`; decision: `reject`; score: `18`; upvotes: `5`
  - reason: Primarily about decision trees and diffusion-model theory, with no clear RL, agent, or interpretability focus.
  - weak_signals: `llm-systems`
  - downrank: `generative-models`, `decision-trees`, `diffusion-models`, `theoretical-unification`
- [Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://huggingface.co/papers/2604.23586)
  - paper_id: `2604.23586`; decision: `reject`; score: `4`; upvotes: `1`
  - reason: This is a talking-head generation paper, not aligned with RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `audio-video-generation`, `talking-head-synthesis`, `cross-modal-generation`
- [LASE: Language-Adversarial Speaker Encoding for Indic Cross-Script Identity Preservation](https://huggingface.co/papers/2605.00777)
  - paper_id: `2605.00777`; decision: `reject`; score: `11`; upvotes: `1`
  - reason: This is a speech representation paper about cross-script speaker encoding, not core RL, agents, or mechanistic interpretability.
  - weak_signals: `representation-analysis`
  - downrank: `speech`, `voice-cloning`, `multilingual-speech`, `identity-preservation`, `diarisation`
- [AnalogRetriever: Learning Cross-Modal Representations for Analog Circuit Retrieval](https://huggingface.co/papers/2604.23195)
  - paper_id: `2604.23195`; decision: `reject`; score: `18`; upvotes: `2`
  - reason: Focused on analog circuit retrieval, with only a minor agentic-RAG connection and little relevance to RL, agents, or interpretability.
  - matched: `llm-systems`
  - weak_signals: `agentic-framework`, `retrieval-augmented-generation`
  - downrank: `domain-specific-cad`, `analog-circuit-design`, `cross-modal-retrieval`
- [UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://huggingface.co/papers/2605.00658)
  - paper_id: `2605.00658`; decision: `reject`; score: `12`; upvotes: `69`
  - reason: This is a video generation framework, not directly about RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `video-generation`, `multimodal-graphics`, `conditional-generation`
- [Map2World: Segment Map Conditioned Text to 3D World Generation](https://huggingface.co/papers/2605.00781)
  - paper_id: `2605.00781`; decision: `reject`; score: `8`; upvotes: `13`
  - reason: A 3D world generation method is not meaningfully aligned with RL, agents, or interpretability.
  - weak_signals: `llm-systems`
  - downrank: `3d-generation`, `scene-generation`, `content-creation`
- [End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](https://huggingface.co/papers/2605.00503)
  - paper_id: `2605.00503`; decision: `reject`; score: `8`; upvotes: `4`
  - reason: Mostly a vision generative modeling paper with no clear connection to RL, agents, or mechanistic interpretability.
  - weak_signals: `llm-systems`
  - downrank: `computer-vision`, `image-generation`, `benchmark-only`
