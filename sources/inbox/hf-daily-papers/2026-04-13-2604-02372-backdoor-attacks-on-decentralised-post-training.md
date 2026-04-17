---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, post-training, llm-systems, alignment, agent-evals, llm-security, pipeline-parallelism, backdoor-attacks, poisoning]
source_count: 1
updated: 2026-04-14
source_url: https://arxiv.org/abs/2604.02372
paper_id: 2604.02372
published: 2026-03-31T04:00:00+08:00
submitted_on_daily: 2026-04-13T18:37:15+08:00
decision: accept
score: 89
generator: scripts/update_hf_daily_papers.py
---

# Backdoor Attacks on Decentralised Post-Training

## Summary

- one_sentence_summary: This paper introduces what it describes as the first backdoor attack on decentralized post-training with pipeline parallelism, showing that an attacker controlling only an intermediate pipeline stage can substantially misalign an LLM during post-training.
- why_relevant: It is directly relevant to post-training robustness and LLM systems security, especially the risk of malicious behavior emerging from decentralized and pipeline-parallel training setups used in alignment workflows.
- filter_reason: Directly relevant post-training security work on decentralized LLM alignment with a concrete backdoor attack and robustness evaluation.
- hugging_face_paper: https://huggingface.co/papers/2604.02372
- original_paper: https://arxiv.org/abs/2604.02372
- source_basis: `original abstract page`

## Key Points

- Targets decentralized post-training in which data and model are split across data parallelism or pipeline parallelism, with a focus on the pipeline-parallel setting.
- The adversary model is limited: the attacker controls an intermediate stage of the pipeline, not the full model or the dataset, so standard data-poisoning attacks do not apply.
- The attack injects a backdoor that causes model misalignment, and the paper reports that inserting the trigger word drops alignment from 80% to 6%.
- The authors evaluate robustness against safety alignment training on the final model and report that the backdoor still succeeds in 60% of cases.
- The reported effect is described as independent of the learned domain or dataset, suggesting the vulnerability is structural to the decentralized post-training setup.

## Related

- [Reinforcement Learning And Post Training](../../../wiki/topics/reinforcement-learning-and-post-training.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.02372
- Hugging Face API entry: https://huggingface.co/api/papers/2604.02372
- arXiv abstract: https://arxiv.org/abs/2604.02372

## Paper Metadata

- authors: `Oğuzhan Ersoy`, `Nikolay Blagoev`, `Jona te Lintelo`, `Stefanos Koffas`, `Marina Krček`, `Stjepan Picek`
- organization: `Gensyn`
- ai_keywords: `decentralized post-training`, `pipeline parallelism`, `poisoning attacks`, `backdoor attacks`, `model misalignment`, `safety alignment training`
- upvotes: `10`
- num_comments: `2`
- abstract: Decentralised post-training of large language models utilises data and pipeline parallelism techniques to split the data and the model. Unfortunately, decentralised post-training can be vulnerable to poisoning and backdoor attacks by one or more malicious participants. There have been several works on attacks and defenses against decentralised data parallelism or federated learning. However, existing works on the robustness of pipeline parallelism are limited to poisoning attacks. To the best of our knowledge, this paper presents the first backdoor attack on pipeline parallelism, designed to misalign the trained model. In our setup, the adversary controls an intermediate stage of the pipeline rather than the whole model or the dataset, making existing attacks, such as data poisoning, inapplicable. Our experimental results show that even such a limited adversary can inject the backdoor and cause misalignment of the model during post-training, independent of the learned domain or dataset. With our attack, the inclusion of the trigger word reduces the alignment percentage from 80% to 6%. We further test the robustness of our attack by applying safety alignment training on the final model, and demonstrate that our backdoor attack still succeeds in 60% of cases.
- hf_ai_summary: A backdoor attack targeting pipeline parallelism in decentralized post-training of large language models achieves significant misalignment even when controlling only an intermediate stage of the pipeline.

## Source Excerpt

Decentralised post-training of large language models utilises data and pipeline parallelism techniques to split the data and the model. Unfortunately, decentralised post-training can be vulnerable to poisoning and backdoor attacks by one or more malicious participants. There have been several works on attacks and defenses against decentralised data parallelism or federated learning. However, existing works on the robustness of pipeline parallelism are limited to poisoning attacks. To the best of our knowledge, this paper presents the first backdoor attack on pipeline parallelism, designed to misalign the trained model. In our setup, the adversary controls an intermediate stage of the pipeline rather than the whole model or the dataset, making existing attacks, such as data poisoning, inapplicable. Our experimental results show that even such a limited adversary can inject the backdoor and cause misalignment of the model during post-training, independent of the learned domain or dataset. With our attack, the inclusion of the trigger word reduces the alignment percentage from $80\%$ to $6\%$. We further test the robustness of our attack by applying safety alignment training on the final model, and demonstrate that our backdoor attack still succeeds in $60\%$ of cases.

## Open Questions

- What specific model architecture, pipeline configuration, and datasets were used in the experiments?
- How was alignment percentage measured, and what evaluation protocol defined success for the backdoor?
- What trigger design and attack insertion mechanism were used at the intermediate pipeline stage?
- How effective are the proposed or implicit defenses beyond safety alignment training, if any were tested?
