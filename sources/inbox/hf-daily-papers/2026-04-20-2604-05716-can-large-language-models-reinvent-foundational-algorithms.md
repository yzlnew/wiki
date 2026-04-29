---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, reinforcement-learning, post-training, reasoning-behavior, llm-systems, unlearning, reasoning, llm-algorithms]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.05716
paper_id: 2604.05716
published: 2026-04-07T04:00:00+08:00
submitted_on_daily: 2026-04-20T15:44:39+08:00
decision: accept
score: 84
generator: scripts/update_hf_daily_papers.py
---

# Can Large Language Models Reinvent Foundational Algorithms?

## Summary

- one_sentence_summary: The paper studies whether LLMs can reinvent foundational computer science algorithms after unlearning them, using a GRPO-based unlearning pipeline and controlled hint-based reinvention tests.
- why_relevant: It is directly relevant to reinforcement learning and post-training because it combines GRPO-style unlearning, test-time RL, and analysis of reasoning stability during algorithm reinvention.
- filter_reason: Uses GRPO-based unlearning and test-time RL to study reasoning reinforcement and failure modes like thought collapse.
- hugging_face_paper: https://huggingface.co/papers/2604.05716
- original_paper: https://arxiv.org/abs/2604.05716
- source_basis: `original abstract page`

## Key Points

- Introduces an "Unlearn-and-Reinvent" pipeline that first removes a target algorithm from an LLM's pretrained knowledge and then tests whether the model can reconstruct it.
- Uses a GRPO-based, on-policy unlearning method to make the removal step effective.
- Evaluates 3 open-weight models on 10 target algorithms under 3 hint levels, with Qwen3-4B-Thinking-2507 reinveting 50% of algorithms with no hint, 70% with hint level 1, and 90% with hint level 2.
- Finds that a few high-level hints can improve success, but step-by-step hints still fail on some harder algorithms.
- Reports that test-time reinforcement learning helps the model reinvent the Strassen algorithm at hint level 2, and that a generative verifier helps preserve reasoning strength and avoid "thought collapse".

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.05716
- Hugging Face API entry: https://huggingface.co/api/papers/2604.05716
- arXiv abstract: https://arxiv.org/abs/2604.05716
- GitHub: https://github.com/Algo-Reinvention/algo-reinvention
- Project page: https://huggingface.co/spaces/jzhao1122/qwen3-thinking-dijkstra

## Paper Metadata

- authors: `Jian Zhao`, `Haoren Luo`, `Yu Wang`, `Yuhan Cao`, `Pingyue Sheng`, `Tianxing He`
- ai_keywords: `LLMs`, `foundational innovation`, `LLM unlearning`, `GRPO-based unlearning`, `reinforcement learning`, `generative verifier`, `thought collapse`
- upvotes: `5`
- num_comments: `2`
- abstract: LLMs have shown strong potential to advance scientific discovery. Whether they possess the capacity for foundational innovation, however, remains an open question. In this work, we focus on a prerequisite for foundational innovation: can LLMs reinvent foundational algorithms in computer science? Our Unlearn-and-Reinvent pipeline applies LLM unlearning to remove a specific foundational algorithm, such as Dijkstra's or Euclid's algorithm, from an LLM's pretrained knowledge, and then tests whether the model can reinvent it in a controlled environment. To enable effective unlearning, we adopt a GRPO-based, on-policy unlearning method. Across 10 target algorithms, 3 strong open-weight models, and 3 hint levels, our experiments demonstrate that (1) the strongest model Qwen3-4B-Thinking-2507 successfully reinvents 50% of the algorithms with no hint, 70% at hint level 1, and 90% at hint level 2; (2) a few high-level hints can enhance the reinvention success rate, but even step-by-step hints fail for those complicated algorithms; and (3) test-time reinforcement learning enables successful reinvention for the Strassen algorithm at hint level 2. Through analyses of output trajectories and ablation studies, we find that generative verifier in the reinvention phase plays a critical role in sustaining models' reasoning strength, helping to avoid the ``thought collapse'' phenomenon. These findings offer insights into both the potential and current limits of LLMs' innovative thinking.
- hf_ai_summary: Large language models can reinvent foundational computer science algorithms through an unlearning and reinvention process, with performance varying based on hint levels and reinforced learning techniques.

## Source Excerpt

LLMs have shown strong potential to advance scientific discovery. Whether they possess the capacity for foundational innovation, however, remains an open question. In this work, we focus on a prerequisite for foundational innovation: can LLMs reinvent foundational algorithms in computer science? Our \textit{Unlearn-and-Reinvent} pipeline applies LLM unlearning to remove a specific foundational algorithm, such as Dijkstra's or Euclid's algorithm, from an LLM's pretrained knowledge, and then tests whether the model can reinvent it in a controlled environment. To enable effective unlearning, we adopt a GRPO-based, on-policy unlearning method. Across 10 target algorithms, 3 strong open-weight models, and 3 hint levels, our experiments demonstrate that (1) the strongest model Qwen3-4B-Thinking-2507 successfully reinvents 50% of the algorithms with no hint, 70% at hint level 1, and 90% at hint level 2; (2) a few high-level hints can enhance the reinvention success rate, but even step-by-step hints fail for those complicated algorithms; and (3) test-time reinforcement learning enables successful reinvention for the Strassen algorithm at hint level 2. Through analyses of output trajectories and ablation studies, we find that generative verifier in the reinvention phase plays a critical role in sustaining models' reasoning strength, helping to avoid the ``thought collapse'' phenomenon. These findings offer insights into both the potential and current limits of LLMs' innovative thinking.

## Open Questions

- How well does the unlearning method actually remove algorithmic knowledge versus merely suppressing surface-form recall?
- What exact scoring or verification procedure is used in the generative verifier during reinvention?
- Which 10 algorithms were tested, and what properties made the harder ones resistant even to step-by-step hints?
