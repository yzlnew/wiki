---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, mechanistic-interpretability, representation-analysis, internal-dynamics, vision-language, graph-probing, causal-intervention]
source_count: 1
updated: 2026-04-11
source_url: https://arxiv.org/abs/2603.27070
paper_id: 2603.27070
published: 2026-03-28T04:00:00+08:00
submitted_on_daily: 2026-04-10T10:06:30+08:00
decision: accept
score: 82
generator: scripts/update_hf_daily_papers.py
---

# Structural Graph Probing of Vision-Language Models

## Summary

- one_sentence_summary: The paper probes vision-language models by turning each layer into a neuron co-activation correlation graph and finds that this topology predicts behavior and exposes recurrent hub neurons whose perturbation changes outputs.
- why_relevant: It is a mechanistic interpretability paper that analyzes internal model structure and causal intervention in multimodal models, which aligns closely with internal dynamics and representation analysis.
- filter_reason: A mechanistic interpretability paper that probes internal topology, identifies hub neurons, and tests causal interventions.
- hugging_face_paper: https://huggingface.co/papers/2603.27070
- original_paper: https://arxiv.org/abs/2603.27070
- source_basis: `original abstract page`

## Key Points

- Each layer is represented as a within-layer correlation graph built from neuron-neuron co-activations, framing internal computation as neural topology.
- The resulting correlation topology contains recoverable behavioral signal, so population-level structure is not just descriptive but predictive.
- Cross-modal structure becomes more consolidated with depth around a compact set of recurrent hub neurons.
- Targeted perturbation of those hub neurons substantially alters model output, suggesting they are causally influential internal components.
- The authors position neural topology as an intermediate interpretability scale between local attribution and full circuit recovery.

## Related

- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2603.27070
- Hugging Face API entry: https://huggingface.co/api/papers/2603.27070
- arXiv abstract: https://arxiv.org/abs/2603.27070
- GitHub: https://github.com/he-h/vlm-graph-probing

## Paper Metadata

- authors: `Haoyu He`, `Yue Zhuo`, `Yu Zheng`, `Qi R. Wang`
- organization: `Northeastern University`
- ai_keywords: `vision-language models`, `neural topology`, `correlation graph`, `neuron-neuron co-activations`, `multimodal performance`, `recurrent hub neurons`, `intervention`, `behavioral signal`
- upvotes: `1`
- num_comments: `1`
- abstract: Vision-language models (VLMs) achieve strong multimodal performance, yet how computation is organized across populations of neurons remains poorly understood. In this work, we study VLMs through the lens of neural topology, representing each layer as a within-layer correlation graph derived from neuron-neuron co-activations. This view allows us to ask whether population-level structure is behaviorally meaningful, how it changes across modalities and depth, and whether it identifies causally influential internal components under intervention. We show that correlation topology carries recoverable behavioral signal; moreover, cross-modal structure progressively consolidates with depth around a compact set of recurrent hub neurons, whose targeted perturbation substantially alters model output. Neural topology thus emerges as a meaningful intermediate scale for VLM interpretability: richer than local attribution, more tractable than full circuit recovery, and empirically tied to multimodal behavior. Code is publicly available at https://github.com/he-h/vlm-graph-probing.
- hf_ai_summary: Vision-language models exhibit structured neural topology where correlation graphs reveal behaviorally significant patterns and influential recurrent hub neurons that drive multimodal performance.

## Source Excerpt

Vision-language models (VLMs) achieve strong multimodal performance, yet how computation is organized across populations of neurons remains poorly understood. In this work, we study VLMs through the lens of neural topology, representing each layer as a within-layer correlation graph derived from neuron-neuron co-activations. This view allows us to ask whether population-level structure is behaviorally meaningful, how it changes across modalities and depth, and whether it identifies causally influential internal components under intervention. We show that correlation topology carries recoverable behavioral signal; moreover, cross-modal structure progressively consolidates with depth around a compact set of recurrent hub neurons, whose targeted perturbation substantially alters model output. Neural topology thus emerges as a meaningful intermediate scale for VLM interpretability: richer than local attribution, more tractable than full circuit recovery, and empirically tied to multimodal behavior. Code is publicly available at this https URL .

## Open Questions

- Which specific behavioral signals were recovered from the correlation graphs?
- What VLM architectures and datasets were used to build and evaluate the topology?
- How were hub neurons identified and how robust are they across models or prompts?
- What intervention method was used for perturbation, and how large were the output changes quantitatively?
