---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, representation-analysis, self-checking, post-training, alignment, policy-routing, refusal, attention-heads, interchange-testing, safety]
source_count: 1
updated: 2026-04-15
source_url: https://arxiv.org/abs/2604.04385
paper_id: 2604.04385
published: 2026-04-13T04:00:00+08:00
submitted_on_daily: 2026-04-14T20:20:00+08:00
decision: accept
score: 96
generator: scripts/update_hf_daily_papers.py
---

# How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models

## Summary

- one_sentence_summary: The paper localizes a policy-routing circuit in alignment-trained language models, where an intermediate attention gate detects content and activates deeper amplifier heads that drive refusal behavior.
- why_relevant: This is directly relevant to mechanistic interpretability and post-training alignment because it analyzes how refusal behavior is routed internally, how that routing scales, and how interventions can bypass or restore policy behavior in language models.
- filter_reason: Direct mechanistic interpretability of alignment policy circuits with causal interventions and scale analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.04385
- original_paper: https://arxiv.org/abs/2604.04385
- source_basis: `original abstract page`

## Key Points

- The proposed circuit has two parts: an intermediate-layer detection gate and deeper amplifier heads that amplify the signal toward refusal; in smaller models these may be single heads, while larger models use bands of heads across adjacent layers.
- The gate has very small direct contribution to output DLA, but interchange testing and knockout cascades show it is causally necessary for the policy behavior.
- Interchange screening across twelve models from six labs finds the same overall motif at scale, but the specific heads differ by lab; per-head ablation can miss gates that interchange identifies.
- Continuously modulating the detection-layer signal can move behavior from hard refusal to evasion to factual answering, and on safety prompts can convert refusal into harmful guidance, suggesting the capability remains present but is routed differently.
- The routing is described as early-commitment, and the circuit can shift across generations and by topic or input language without changing benchmark behavior.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.04385
- Hugging Face API entry: https://huggingface.co/api/papers/2604.04385
- arXiv abstract: https://arxiv.org/abs/2604.04385
- GitHub: https://github.com/gregfrank/how-alignment-routes

## Paper Metadata

- authors: `Gregory N. Frank`
- ai_keywords: `policy routing mechanism`, `attention gate`, `amplifier heads`, `refusal`, `DLA`, `interchange testing`, `knockout cascade`, `per-head ablation`, `in-context substitution cipher`, `cipher contrast analysis`
- upvotes: `0`
- num_comments: `1`
- abstract: This paper localizes the policy routing mechanism in alignment-trained language models. An intermediate-layer attention gate reads detected content and triggers deeper amplifier heads that boost the signal toward refusal. In smaller models the gate and amplifier are single heads; at larger scale they become bands of heads across adjacent layers. The gate contributes under 1% of output DLA, but interchange testing (p<0.001) and knockout cascade confirm it is causally necessary. Interchange screening at n>=120 detects the same motif in twelve models from six labs (2B to 72B), though specific heads differ by lab. Per-head ablation weakens up to 58x at 72B and misses gates that interchange identifies; interchange is the only reliable audit at scale. Modulating the detection-layer signal continuously controls policy from hard refusal through evasion to factual answering. On safety prompts the same intervention turns refusal into harmful guidance, showing the safety-trained capability is gated by routing rather than removed. Thresholds vary by topic and by input language, and the circuit relocates across generations within a family while behavioral benchmarks register no change. Routing is early-commitment: the gate commits at its own layer before deeper layers finish processing the input. Under an in-context substitution cipher, gate interchange necessity collapses 70 to 99% across three models and the model switches to puzzle-solving. Injecting the plaintext gate activation into the cipher forward pass restores 48% of refusals in Phi-4-mini, localizing the bypass to the routing interface. A second method, cipher contrast analysis, uses plain/cipher DLA differences to map the full cipher-sensitive routing circuit in O(3n) forward passes. Any encoding that defeats detection-layer pattern matching bypasses the policy regardless of whether deeper layers reconstruct the content.
- hf_ai_summary: The study reveals that policy routing in alignment-trained language models involves attention gates and amplifier heads that control safety responses, with the routing mechanism being early-committing and transferable across model scales.

## Source Excerpt

This paper localizes the policy routing mechanism in alignment-trained language models. An intermediate-layer attention gate reads detected content and triggers deeper amplifier heads that boost the signal toward refusal. In smaller models the gate and amplifier are single heads; at larger scale they become bands of heads across adjacent layers. The gate contributes under 1% of output DLA, but interchange testing (p<0.001) and knockout cascade confirm it is causally necessary. Interchange screening at n>=120 detects the same motif in twelve models from six labs (2B to 72B), though specific heads differ by lab. Per-head ablation weakens up to 58x at 72B and misses gates that interchange identifies; interchange is the only reliable audit at scale. Modulating the detection-layer signal continuously controls policy from hard refusal through evasion to factual answering. On safety prompts the same intervention turns refusal into harmful guidance, showing the safety-trained capability is gated by routing rather than removed. Thresholds vary by topic and by input language, and the circuit relocates across generations within a family while behavioral benchmarks register no change. Routing is early-commitment: the gate commits at its own layer before deeper layers finish processing the input. Under an in-context substitution cipher, gate interchange necessity collapses 70 to 99% across three models and the model switches to puzzle-solving. Injecting the plaintext gate activation into the cipher forward pass restores 48% of refusals in Phi-4-mini, localizing the bypass to the routing interface. A second method, cipher contrast analysis, uses plain/cipher DLA differences to map the full cipher-sensitive routing circuit in O(3n) forward passes. Any encoding that defeats detection-layer pattern matching bypasses the policy regardless of whether deeper layers reconstruct the content.

## Open Questions

- How general is the routing circuit across architectures beyond the twelve models tested?
- Which specific training signals or alignment procedures create the gate-amplifier structure?
- Can the circuit be robustly detected without interchange testing at very large scale?
- Does the same routing mechanism govern other policy behaviors besides refusal and safety responses?
- How stable is the circuit under further post-training or adversarial prompt formats?
