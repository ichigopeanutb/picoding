# Agent Operating Rules

## Core Objective

Agents should improve this repository through small, measurable, reversible experiments.

PiCoding uses an AutoImprove workflow inspired by autonomous research loops, but this repository starts with human-gated iteration. Agents propose and run bounded experiments; humans decide which domains, examples, and strategic outputs matter.

## Protected Files

Do not modify these unless explicitly asked:

- `tests/`
- `eval/`
- `scripts/eval.sh`
- `experiments/results.tsv`
- `golden_outputs/`

Protected files define the evaluation harness and historical record. Changing them without instruction can hide regressions or weaken review quality.

## Allowed Modification Areas

Agents may modify:

- `src/`
- `prompts/`
- `docs/`
- `examples/`
- `README.md`
- `research_cases/`

## Hard Rules

- Do not fake evaluation results.
- Do not delete tests to make results pass.
- Do not weaken evaluation criteria.
- Do not introduce large dependencies without need.
- Prefer simple changes.
- Prefer deletion over addition.
- Use small reversible experiments.
- Every experiment must be committed before evaluation.
- Bad experiments must be reverted.
- Results must be logged.

## Evaluation Command

The single evaluation command is:

```bash
bash scripts/eval.sh
```

## Keep / Discard Rule

Keep a change if:

- more tests pass,
- benchmark score improves,
- required case coverage improves,
- runtime improves without hurting quality,
- code becomes simpler while behavior remains correct.

Discard a change if:

- tests fail,
- score worsens,
- output quality becomes generic,
- evaluation crashes,
- the improvement is unclear.

## Human-Gated Operation

Do not run forever. Continue only when instructed by the human maintainer.

Human review is required for business strategy quality, case realism, golden outputs, and any change that affects the evaluation standard.
