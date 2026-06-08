# AutoImprove Loop

PiCoding adapts the AutoResearch concept into a practical AutoImprove system.

The goal is not to create an unsupervised infinite loop. The goal is to make small, measurable experiments easier to run, record, review, keep, or discard.

## Loop

1. Check git status.

```bash
git status
```

2. Create or continue branch.

```bash
git checkout -b autoresearch/autoimprove
```

If the branch already exists, continue on it.

3. Read recent experiment results.

```bash
tail -20 experiments/results.tsv
```

4. Choose exactly one small hypothesis.

Good hypotheses are narrow, measurable, and reversible. Example:

```text
If eval/run_eval.py checks required keyword uniqueness, schema quality scoring will become more meaningful without requiring external APIs.
```

5. Modify the minimum necessary files.

Respect `AGENTS.md`. Do not modify protected files unless explicitly asked.

6. Commit the experiment.

```bash
git add .
git commit -m "experiment: <short description>"
```

7. Run evaluation.

```bash
bash scripts/eval.sh > run.log 2>&1
```

8. Parse the result.

Look for:

```text
EVAL_STATUS=pass
EVAL_SCORE=<number>
EVAL_RUNTIME_SECONDS=<number>
```

9. Add one row to `experiments/results.tsv`.

The TSV columns are:

```text
timestamp
commit
status
score
tests_passed
tests_failed
runtime_seconds
category
description
```

10. Keep or discard.

If improved, keep.

If worse, unclear, or crashed, run:

```bash
git reset --hard HEAD~1
```

11. Continue only when instructed by the human.

## First Implementation Boundary

This repository starts with human-gated AutoImprove, not infinite autonomous execution.

Agents should run one experiment at a time, record the result, and stop for maintainer review.
