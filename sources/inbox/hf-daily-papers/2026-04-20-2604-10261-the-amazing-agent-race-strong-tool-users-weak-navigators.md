---
type: source-summary
status: active
tags: [hf-daily-papers, papers, inbox, agents, agent-evals, tool-use, llm-systems, reasoning-behavior-shaping, benchmark, navigation, evaluation, wikipedia, dag]
source_count: 1
updated: 2026-04-21
source_url: https://arxiv.org/abs/2604.10261
paper_id: 2604.10261
published: 2026-04-17T04:00:00+08:00
submitted_on_daily: 2026-04-20T23:32:39+08:00
decision: accept
score: 94
generator: scripts/update_hf_daily_papers.py
---

# The Amazing Agent Race: Strong Tool Users, Weak Navigators

## Summary

- one_sentence_summary: The Amazing Agent Race (AAR) is a Wikipedia-based tool-use benchmark with DAG-shaped multi-step tasks that shows LLM agents fail more on navigation than on tool calling.
- why_relevant: It is directly relevant to agent evaluation and tool-using systems because it isolates navigation failures from tool invocation failures, and it also suggests architecture can matter as much as model scale.
- filter_reason: A strong agent/tool-use benchmark with DAG navigation, multi-step tool chains, and diagnostic evaluation metrics directly matches the user’s agent and systems interests.
- hugging_face_paper: https://huggingface.co/papers/2604.10261
- original_paper: https://arxiv.org/abs/2604.10261
- source_basis: `original abstract page`

## Key Points

- The paper argues that common tool-use benchmarks are too linear: across six benchmarks, 55% to 100% of instances are simple 2- to 5-step chains.
- AAR introduces directed acyclic graph puzzles with fork-merge tool chains, covering 1,400 procedurally generated instances split into 800 sequential legs and 600 compositional DAG legs.
- Tasks require agents to navigate Wikipedia, execute multi-step tool chains, and combine results into a verifiable answer, with live-API validation and four difficulty levels.
- Three metrics separate failure modes: finish-line accuracy, pit-stop visit rate, and roadblock completion rate.
- In evaluation across three agent frameworks, the best result is 37.2% accuracy; navigation errors dominate at 27% to 52% of trials, while tool-use errors stay below 17%.

## Related

- [Agent Workflows](../../../wiki/topics/agent-workflows.md)
- [Llm Systems And Training](../../../wiki/topics/llm-systems-and-training.md)
- [Ai And Llms](../../../wiki/topics/ai-and-llms.md)

## Sources

- Hugging Face paper page: https://huggingface.co/papers/2604.10261
- Hugging Face API entry: https://huggingface.co/api/papers/2604.10261
- arXiv abstract: https://arxiv.org/abs/2604.10261
- GitHub: https://github.com/minnesotanlp/the-amazing-agent-race
- Project page: https://minnesotanlp.github.io/the-amazing-agent-race/

## Paper Metadata

- authors: `Zae Myung Kim`, `Dongseok Lee`, `Jaehyung Kim`, `Vipul Raheja`, `Dongyeop Kang`
- organization: `Minnesota NLP`
- ai_keywords: `tool-use benchmarks`, `directed acyclic graph`, `DAG puzzles`, `agent frameworks`, `Wikipedia`, `multi-step tool chains`, `verifiable answer`, `procedural generation`, `live-API validation`, `finish-line accuracy`, `pit-stop visit rate`, `roadblock completion rate`, `navigation errors`, `tool-use errors`, `agent architecture`, `model scale`
- upvotes: `2`
- num_comments: `1`
- abstract: Existing tool-use benchmarks for LLM agents are overwhelmingly linear: our analysis of six benchmarks shows 55 to 100% of instances are simple chains of 2 to 5 steps. We introduce The Amazing Agent Race (AAR), a benchmark featuring directed acyclic graph (DAG) puzzles (or "legs") with fork-merge tool chains. We release 1,400 instances across two variants: sequential (800 legs) and compositional (600 DAG legs). Agents must navigate Wikipedia, execute multi-step tool chains, and aggregate results into a verifiable answer. Legs are procedurally generated from Wikipedia seeds across four difficulty levels with live-API validation. Three complementary metrics (finish-line accuracy, pit-stop visit rate, and roadblock completion rate) separately diagnose navigation, tool-use, and arithmetic failures. Evaluating three agent frameworks on 1,400 legs, the best achieves only 37.2% accuracy. Navigation errors dominate (27 to 52% of trials) while tool-use errors remain below 17%, and agent architecture matters as much as model scale (Claude Code matches Codex CLI at 37% with 6x fewer tokens). The compositional structure of AAR reveals that agents fail not at calling tools but at navigating to the right pages, a blind spot invisible to linear benchmarks. The project page can be accessed at: https://minnesotanlp.github.io/the-amazing-agent-race
- hf_ai_summary: The Amazing Agent Race benchmark introduces DAG-based puzzles to evaluate LLM agents' navigation and tool-use capabilities beyond traditional linear benchmarks, revealing that navigation errors dominate performance issues.

## Source Excerpt

Existing tool-use benchmarks for LLM agents are overwhelmingly linear: our analysis of six benchmarks shows 55 to 100% of instances are simple chains of 2 to 5 steps. We introduce The Amazing Agent Race (AAR), a benchmark featuring directed acyclic graph (DAG) puzzles (or "legs") with fork-merge tool chains. We release 1,400 instances across two variants: sequential (800 legs) and compositional (600 DAG legs). Agents must navigate Wikipedia, execute multi-step tool chains, and aggregate results into a verifiable answer. Legs are procedurally generated from Wikipedia seeds across four difficulty levels with live-API validation. Three complementary metrics (finish-line accuracy, pit-stop visit rate, and roadblock completion rate) separately diagnose navigation, tool-use, and arithmetic failures. Evaluating three agent frameworks on 1,400 legs, the best achieves only 37.2% accuracy. Navigation errors dominate (27 to 52% of trials) while tool-use errors remain below 17%, and agent architecture matters as much as model scale (Claude Code matches Codex CLI at 37% with 6x fewer tokens). The compositional structure of AAR reveals that agents fail not at calling tools but at navigating to the right pages, a blind spot invisible to linear benchmarks. The project page can be accessed at: this https URL

## Open Questions

- Which three agent frameworks were evaluated, and how were they configured?
- How does performance vary across the four difficulty levels and between sequential versus compositional legs?
- What kinds of navigation mistakes account for most failures on AAR?
- How exactly are the live-API validation and verifiable answers implemented?
