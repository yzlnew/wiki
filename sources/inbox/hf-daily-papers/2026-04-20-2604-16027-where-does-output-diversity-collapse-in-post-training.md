---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, reinforcement-learning, reasoning-behavior-shaping, llm-systems, diversity, sft, dpo, rl, reasoning, llm]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.16027
paper_id: 2604.16027
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-20T19:23:06+08:00
decision: accept
score: 91
generator: scripts/update_hf_daily_papers.py
---

# Where does output diversity collapse in post-training?

## Summary

- one_sentence_summary: The paper shows that output diversity collapse in post-trained language models is shaped mainly by training data composition, not just the post-training method or inference-time generation format.
- why_relevant: This is directly relevant to post-training and RL-style shaping of language model behavior because it isolates how supervised fine-tuning and DPO, together with data composition, affect output diversity and inference-time scaling.
- filter_reason: Directly studies post-training effects on output diversity across SFT, DPO, and RL-Zero with training-data and reasoning-format analysis.
- hugging_face_paper: https://huggingface.co/papers/2604.16027
- original_paper: https://arxiv.org/abs/2604.16027
- source_basis: `original abstract page`

## Key Points

- The authors study three Olmo 3 post-training lineages: Think (chain-of-thought distillation), Instruct (broad multi-source data), and RL-Zero, using 15 tasks and four diversity metrics.
- They find that where diversity collapse happens depends on the lineage: Think loses most semantic diversity at supervised fine-tuning, and DPO reduces diversity more in Instruct than in Think.
- Suppressing chain-of-thought reasoning at inference lowers accuracy on hard tasks but does not restore answer-level diversity, implying the collapse is encoded in model weights rather than caused by the output format.
- On six verifiable tasks, diversity loss can be decomposed into a quality-control component and a residual narrowing component, and this split varies by task.
- Think retains more correct-answer diversity than Instruct even though it collapses more in aggregate, suggesting aggregate diversity alone can hide meaningful differences in correct-output diversity.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.16027
- Hugging Face API entry: https://huggingface.co/api/papers/2604.16027
- arXiv abstract: https://arxiv.org/abs/2604.16027
- GitHub: https://github.com/ckarouzos/where-diversity-collapses

## Paper Metadata

- authors: `Constantinos Karouzos`, `Xingwei Tan`, `Nikolaos Aletras`
- ai_keywords: `post-trained language models`, `output diversity collapse`, `inference-time scaling`, `chain-of-thought distillation`, `supervised fine-tuning`, `DPO`, `generation format`, `model weights`, `diversity loss`, `quality-control component`, `residual component`
- upvotes: `10`
- num_comments: `1`
- abstract: Post-trained language models produce less varied outputs than their base counterparts. This output diversity collapse undermines inference-time scaling methods that rely on varied samples, and risks homogenizing model outputs on creative and value-laden tasks. Prior work attributes collapse to specific post-training methods, without separating the role of training data composition from the method, or the generation format from the model weights. We trace output diversity through three parallel post-training lineages of Olmo 3, Think (chain-of-thought distillation), Instruct (broad multi-source data), and RL-Zero, across 15 tasks and four text diversity metrics. We find that the location of collapse co-varies with data composition: the Think lineage loses most semantic diversity at supervised fine-tuning, and the effect of DPO is larger in Instruct than in Think. Suppressing chain-of-thought reasoning at inference in Think models drops accuracy on hard tasks, yet leaves answer-level diversity unchanged, showing that the collapse is embedded in the model weights by training data, not imposed by the generation format. Decomposing diversity loss on six verifiable tasks into a quality-control component (removal of incorrect outputs) and a residual component (genuine narrowing among correct outputs) reveals that the split is task-dependent, and Think models retain more correct-answer diversity than Instruct despite collapsing more in aggregate. Our results indicate that diversity collapse is determined during training by data composition and cannot be addressed at inference time alone.
- hf_ai_summary: Output diversity collapse in post-trained language models is primarily driven by training data composition rather than generation format, with different post-training methods affecting diversity differently across tasks.

## Source Excerpt

Post-trained language models produce less varied outputs than their base counterparts. This output diversity collapse undermines inference-time scaling methods that rely on varied samples, and risks homogenizing model outputs on creative and value-laden tasks. Prior work attributes collapse to specific post-training methods, without separating the role of training data composition from the method, or the generation format from the model weights. We trace output diversity through three parallel post-training lineages of Olmo 3, Think (chain-of-thought distillation), Instruct (broad multi-source data), and RL-Zero, across 15 tasks and four text diversity metrics. We find that the location of collapse co-varies with data composition: the Think lineage loses most semantic diversity at supervised fine-tuning, and the effect of DPO is larger in Instruct than in Think. Suppressing chain-of-thought reasoning at inference in Think models drops accuracy on hard tasks, yet leaves answer-level diversity unchanged, showing that the collapse is embedded in the model weights by training data, not imposed by the generation format. Decomposing diversity loss on six verifiable tasks into a quality-control component (removal of incorrect outputs) and a residual component (genuine narrowing among correct outputs) reveals that the split is task-dependent, and Think models retain more correct-answer diversity than Instruct despite collapsing more in aggregate. Our results indicate that diversity collapse is determined during training by data composition and cannot be addressed at inference time alone.

## Open Questions

- Which specific data characteristics in Think versus Instruct are most responsible for the observed diversity collapse?
- How robust are the findings across other model families beyond Olmo 3?
- Do the four diversity metrics agree on the same collapse locations, or do they capture different failure modes?
- Can any training-time intervention preserve diversity without hurting accuracy on hard tasks?
