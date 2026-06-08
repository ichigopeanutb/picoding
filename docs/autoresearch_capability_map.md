# AutoResearch Capability Map

This document classifies the capabilities described by the AutoResearch concept and maps them into a practical AutoImprove system for PiCoding.

PiCoding is an early-stage framework for physics-aware AI coding and prototype-model development. The AutoImprove system should support fixed evaluations, experiment logging, business research cases, and human review without overbuilding.

## 1. Agent Loop Capability

### What This Capability Means

An agent repeatedly forms a hypothesis, modifies allowed files, runs an evaluation, compares results, and decides whether to keep or discard the change.

Sub-capabilities:

- hypothesis generation
- code modification
- experiment execution
- result evaluation
- keep / discard decision
- repeated iteration

### Why It Matters

The loop turns vague improvement work into measurable experiments. It also limits risk because each change is small, reversible, and tied to a result.

### How It Maps To This Repo

PiCoding uses the loop to improve documentation, examples, evaluation cases, prompt patterns, and simple model tooling. The first implementation is human-gated rather than fully autonomous.

### Files That Should Implement It

- `AGENTS.md`
- `AUTORESEARCH.md`
- `experiments/results.tsv`
- `scripts/eval.sh`

### Evaluation Or Review

Partly automatic. Test and schema results can be evaluated automatically. Hypothesis quality and strategic relevance require human review.

## 2. Evaluation Harness Capability

### What This Capability Means

The repository has a fixed command that runs tests and evaluation cases in a reproducible way. Evaluation files are protected so agents cannot change the benchmark while trying to improve the score.

Sub-capabilities:

- fixed evaluation command
- protected evaluation files
- measurable score
- reproducible run
- anti-cheating mechanism

### Why It Matters

Without a fixed harness, agents can accidentally or intentionally make success easier by changing the standard.

### How It Maps To This Repo

PiCoding starts with a schema-completeness evaluation for case definitions. Later versions can add output-quality rubrics, golden output comparison, and domain-specific validation checks.

### Files That Should Implement It

- `scripts/eval.sh`
- `eval/run_eval.py`
- `eval/cases.json`
- `tests/`
- `golden_outputs/`

### Evaluation Or Review

Automatically evaluated for schema completeness and test execution. Human review remains necessary for business strategy quality and model realism.

## 3. Experiment Management Capability

### What This Capability Means

Experiments are isolated, committed before evaluation, logged after evaluation, and reverted if they fail or produce unclear improvements.

Sub-capabilities:

- git branch isolation
- commit-before-run
- result logging
- crash handling
- rollback mechanism

### Why It Matters

Experiment management prevents untracked changes, ambiguous results, and accumulated low-quality modifications.

### How It Maps To This Repo

PiCoding records baseline and future experiment results in `experiments/results.tsv`. Agents should work on an AutoImprove branch and keep experiments small.

### Files That Should Implement It

- `AUTORESEARCH.md`
- `AGENTS.md`
- `experiments/results.tsv`

### Evaluation Or Review

Mostly procedural. Git status, commit hashes, evaluation status, and TSV rows are inspectable automatically. Deciding whether an experiment is meaningful still needs human judgment.

## 4. Simplicity and Engineering Discipline

### What This Capability Means

Agents should prefer small, readable, reversible improvements. They should avoid dependencies, large rewrites, weakened tests, and unnecessary complexity.

Sub-capabilities:

- prefer simple changes
- prefer deletion over addition
- small reversible experiments
- no unnecessary dependencies
- no weakening tests

### Why It Matters

Autonomous or semi-autonomous coding can drift into complexity quickly. Simplicity keeps the project maintainable and reviewable.

### How It Maps To This Repo

PiCoding is early-stage. The first AutoImprove implementation should be plain Markdown, JSON, Bash, and Python standard library code.

### Files That Should Implement It

- `AGENTS.md`
- `AUTORESEARCH.md`
- `CONTRIBUTING.md`

### Evaluation Or Review

Mostly human-reviewed. Some signals, such as dependency count and test results, can be automated later.

## 5. Case Library Capability

### What This Capability Means

The repo stores evaluation cases, richer research cases, golden outputs, scoring rubrics, and required output formats.

Sub-capabilities:

- eval cases
- research cases
- golden outputs
- scoring rubric
- required output format

### Why It Matters

Cases define what the project is trying to improve. They also keep agent behavior anchored to realistic domains instead of generic output.

### How It Maps To This Repo

PiCoding starts with five business and infrastructure-oriented cases related to AI servers, financing risk, cultural IP, optical communication, and AI data center energy strategy.

### Files That Should Implement It

- `eval/cases.json`
- `research_cases/`
- `golden_outputs/`

### Evaluation Or Review

Case schema is automatic. Strategic quality, realism, and final answers require human review.

## 6. Human Steering Capability

### What This Capability Means

Humans define the goals, write markdown instructions, review successful traces, and decide which domains matter.

Sub-capabilities:

- human defines goals
- human writes markdown instructions
- human reviews successful traces
- human decides which domains matter

### Why It Matters

The human controls the direction and evaluation values. Agents help execute bounded experiments; they do not replace domain ownership.

### How It Maps To This Repo

PiCoding uses Markdown files as steering artifacts. Maintainers can update `AGENTS.md`, `AUTORESEARCH.md`, `research_cases/`, and docs to guide future experiments.

### Files That Should Implement It

- `AGENTS.md`
- `AUTORESEARCH.md`
- `docs/`
- `research_cases/`
- `golden_outputs/`

### Evaluation Or Review

Human review required. Automation can confirm structure, not strategic judgment.

## 7. Business Research Extension

### What This Capability Means

The AutoImprove system can support structured business and infrastructure research cases, not only code benchmarks.

Sub-capabilities:

- AI infrastructure case analysis
- financing structure analysis
- energy storage strategy
- optical communication investment research
- VC fund / government bid strategy
- 2Y2C-style strategic consulting outputs

### Why It Matters

PiCoding is positioned around real-world systems. Business cases help test whether agents can reason across engineering constraints, capital structure, infrastructure deployment, and validation logic.

### How It Maps To This Repo

The first case library focuses on AI infrastructure, financing risk, energy strategy, and optical communication. These are stored as human-review cases and lightly checkable eval cases.

### Files That Should Implement It

- `eval/cases.json`
- `research_cases/`
- `golden_outputs/`
- `docs/maintainer-workflows.md`

### Evaluation Or Review

Mostly human-reviewed. Automatic evaluation can check required sections, keywords, schema completeness, and output format. Human experts should review strategic correctness.
