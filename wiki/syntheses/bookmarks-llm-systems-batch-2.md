---
type: source-summary
status: active
tags: [bookmarks, llm, training, systems, math, experiments]
source_count: 5
updated: 2026-04-07
source_path: ../../sources/library/bookmarks/bookmarks.md
---

# Bookmarks LLM Systems Batch 2

## Source

- 原始文件：`sources/library/bookmarks/bookmarks.md`
- 批次范围：LLM systems residuals / math / architecture experiments
- 处理日期：2026-04-07

## Summary

这一批链接更像第一轮 `LLM Systems and Training` 的补丁包，而不是新的独立分支。它们把前一批已经建立的主线继续往下补：一头是训练规模和系统余量，一头是数学与结构实验，另一头是小规模训练实验如何验证配方和架构选择。

`How To Scale Your Model` 继续补足扩展训练规模的系统视角，`An Illustrated Guide to Automatic Sparse Differentiation` 和 `Einsum` 相关脉络则补足张量与稀疏计算的数学底座。`Beating GPT-2 for <<$100`、`Manifold Dial - mHC Visualizer` 和 `GDN vs Mamba2` 这类链接更偏实验性：它们不是纯概念介绍，而是在用具体实验、可视化或低成本训练案例回答“某个架构或方法到底值不值得继续走下去”。

## Key Claims

- 这批资料的价值在于补齐系统余量，而不是另起炉灶
- 训练规模问题和数学底座问题仍然是同一类判断的一部分
- 小规模、低成本实验可以作为架构和训练配方的早期筛选器
- 可视化和 benchmark 风格的链接更适合作为“实验记录”来读，而不只是参考文章

## Evidence Notes

- `How To Scale Your Model`：继续提供训练规模、TPU / system scaling 的方法论
- `An Illustrated Guide to Automatic Sparse Differentiation`：补充稀疏自动微分、Jacobian / Hessian 的计算视角
- `Beating GPT-2 for <<$100: the nanochat journey`：说明可以用较低成本复现实验性训练路径
- `Manifold Dial - mHC Visualizer`：以可视化方式呈现稳定性或结构行为，属于架构实验工具
- `Zeyuan Allen-Zhu ... GDN vs Mamba2`：把模型架构比较、规模和训练条件放在同一实验语境里

## Related

- [[llm-systems-and-training|LLM Systems and Training]]
- [[ai-and-llms|AI and LLMs]]
- [[learning-and-research|Learning and Research]]

## Follow-ups

- `GDN`、`Mamba2`、`nanochat`、`mHC Visualizer` 是否值得拆成实体页
- 是否要单独整理一页“efficient training experiments”
- 这批 residuals 之后还会不会继续出现更明确的 post-training 或 model architecture 簇

## Links

- [Zeyuan Allen-Zhu, Sc.D. on X](https://x.com/ZeyuanAllenZhu/status/2027248721478758902)
- [Beating GPT-2 for <<$100: the nanochat journey](https://github.com/karpathy/nanochat/discussions/481)
- [Manifold Dial - mHC Visualizer](https://subhadipmitra.com/mhc-visualizer/)
- [An Illustrated Guide to Automatic Sparse Differentiation](https://iclr-blogposts.github.io/2025/blog/sparse-autodiff/)
- [How To Scale Your Model](https://jax-ml.github.io/scaling-book/)
