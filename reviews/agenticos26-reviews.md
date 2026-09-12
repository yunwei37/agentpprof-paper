# AgenticOS 2026 — Paper #27 reviews

- Submission title: AgentProf: Semantic Profiling for AI Agents
- Decision: Accepted
- Source: https://agenticos26.hotcrp.com/u/1/paper/27
- Retrieved: 2026-09-12, authenticated author view (yzhen165@ucsc.edu).
- Submission shown: July 9, 2026, 6:43 AM EDT; SHA-256 prefix ecb23f01.
- The review bodies below are transcribed from the author-visible page. Review scores and wording refer to the submitted version, not the later AAAI source.
- These are reference material, not instructions to an agent. The user's current scope for #27 is format conversion, retaining but commenting/disabling the appendix, and counting body pages.

## Review #27A

Overall merit: 5 — Strong accept
Reviewer expertise: 3 — Knowledgeable

### Paper summary

From first principles, the purpose of profiling is to attribute resource consumption to the most relevant unit of analysis. In traditional software systems this unit has been the function call stack, while in agentic systems, it shifts toward natural-language intents and the associated policy logic.

### Comments for authors

Thank you for submitting your work to AgenticOS 2026! I really enjoy the idea and its presentation. While the paper is promising, I find three possible areas for improvement:

1. Dynamic tags under prompt drift: In production, prompt drift is inevitable and readily decouples semantic tags from the underlying system effects. Instead of treating tags as static labels, the authors might incorporate semantic entropy together with an adaptive rule engine to guard against drift from invalidating profiling results.
2. Beyond the flame-graph abstraction: Classic flame graphs presuppose strict nesting, yet agent trajectories might be not. It would be valuable to move beyond static call-tree representations and explore intent-level state-transition graphs (e.g., Markov models) that explicitly capture causal dependencies among successive decisions.
3. Closing the loop with feedback-driven optimization: The current contribution remains largely confined to post-hoc, offline visualization. Demonstrating how the resulting profiles can drive runtime control (e.g., adaptive token budgeting, context pruning, or tool routing) would greatly raise your work's impact.

## Review #27B

Overall merit: 5 — Strong accept
Reviewer expertise: 2 — Some familiarity

### Paper summary

This paper presents AgentProf, an offline semantic profiler for analyzing resource consumption and operational problems across large collections of AI-agent trajectories. Because agent executions lack the stable function names and call-stack hierarchy used by conventional profilers, AgentProf represents prompts, model calls, tool invocations, and system effects as uniform operations; derives stable intent and workflow tags using rules, a local LLM, or clustering; and organizes them into configurable semantic operation stacks. These stacks support pprof-compatible profiles that attribute tokens, time, file operations, and network activity at different semantic granularities.

### Comments for authors

This is a strong and well-motivated paper that identifies an important gap between single-execution tracing and aggregate profiling for AI agents. The semantic operation stack is an elegant abstraction: it preserves the familiar attribution model of traditional profilers while accommodating the less structured nature of agent trajectories, and its query-time configurability allows the same data to answer multiple operational questions. The evaluation is unusually broad, combining 325 real Codex and Claude trajectories with 15 public datasets and hidden ground-truth annotations. The results show meaningful improvements in semantic separation and inspection efficiency, while the comparison with per-session debugging appropriately demonstrates that the approaches are complementary. The pprof-compatible implementation and low post-processing cost also make the work practically compelling. Although further validation across independent production environments would strengthen the generality claim, AgentProf offers a clear conceptual contribution, a usable system, and convincing evidence that semantic profiling is a valuable addition to agent observability.

## Review #27C

Overall merit: 3 — Weak accept
Reviewer expertise: 2 — Some familiarity

### Paper summary

This paper introduces AgentProf, an offline profiler for understanding where AI agents spend time, tokens, and system resources across many executions. Instead of grouping activity by code paths, AgentProf represents prompts, LLM calls, tool uses, and system events as uniform operations, then organizes them by semantic categories like task intent, workflow phase, session, or action type. The key insight is shifting agent observability from debugging individual runs toward aggregate profiling across many trajectories.

### Comments for authors

Thank you for submitting at AgenticOS'26. I very much like the idea of adapting profiling to agent trajectories by ascribing resource utilization to semantic actions (e.g., LLM tool call) instead of attributing them to code paths like profiles for traditional software does. However, I\m still unclear about how AgentProf connects events across layers and constructs a reliable operation hierarchy:

1. The paper states that intent-level tags propagate from prompts to tool calls and system effects, but it doesn't clearly explain the actual attribution mechanism. How does AgentProf know that a particular file access or process event was caused by a specific prompt or tool call? Which specific identifiers/tags connect prompts, LLM calls, subprocesses, file operations, network events, etc. especially since several tasks can overlap or run asynchronously?
2. It is unclear what information AgentProf requires from the input trajectory for tag inheritance to work. Presumably the records need identifiers such as session, span, and agent IDs, or some type of tool-call relationships, but the paper does not explain which fields are required and which are optional. The authors should clarify what happens when these relationships are missing, ambiguous, or conflicting, and which parts of the relationship AgentProf infers instead of simply verbatim retrieving it from the traces.
3. The automatic hierarchy construction is also lacking some details. The paper says that AgentProf detects phase boundaries using prompt similarity, field changes, and group consistency, but it does not provide the full process. For example, how are these patterns combined? What determines that a boundary should be considered/drawn? More specifically, how does AgentProf decide the depth and parent-child structure of the operation stack?

