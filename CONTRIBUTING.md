# Contributing to PiCoding

Thank you for your interest in contributing to PiCoding. This project is early-stage, and thoughtful contributions can shape both the technical direction and the maintainer workflow.

## How to Contribute

Useful contributions include:

- Model examples that connect assumptions, variables, equations, validation logic, code structure, and tests.
- Prompt templates for physics-aware AI coding workflows.
- Documentation improvements.
- Test patterns for simulation and validation logic.
- Small implementation utilities in `src/picoding/`.
- Issue triage, review comments, and roadmap feedback.

Before starting a large change, please open an issue or discussion-style proposal so maintainers and contributors can align on scope.

## Opening Issues

When opening an issue, include:

- A clear summary of the problem or proposal.
- The affected area, such as docs, examples, tests, templates, or source code.
- Relevant physical assumptions, constraints, units, or validation requirements.
- Any examples, references, expected behavior, or failure cases.
- Whether you are willing to work on the change.

For model-example requests, please describe the physical system, intended audience, level of complexity, and any known limitations.

## Pull Requests

Pull requests should be focused and reviewable. A good pull request:

- Explains what changed and why it matters.
- States the assumptions involved.
- Adds or updates tests where behavior changes.
- Updates documentation when examples, APIs, or workflows change.
- Keeps unrelated refactors out of the same change.
- Uses clear commit messages when possible.

Maintainers may ask for changes that make assumptions more explicit, improve validation, or narrow the scope of a contribution.

## Code Style

PiCoding is still defining its implementation style. Until more tooling is added:

- Prefer simple, readable code over clever abstractions.
- Use clear names for variables, units, equations, and validation rules.
- Keep model logic separated from presentation, I/O, or agent orchestration.
- Make invalid states visible with explicit errors or validation results.
- Avoid hidden unit conversions unless they are documented and tested.

Future phases may add formatting, linting, typing, and package-specific style checks.

## Documentation Expectations

Documentation should be clear enough for both domain experts and software contributors. When adding a model, prompt, or workflow, include:

- The purpose of the model or workflow.
- Assumptions and exclusions.
- Variables and units.
- Equations or rules used.
- Validation criteria.
- Known limitations.
- Suggested tests.

Avoid presenting examples as production-ready engineering tools unless they have been independently validated.

## Testing Expectations

Tests should reflect both software behavior and physical reasoning. Where relevant, include tests for:

- Normal operating ranges.
- Boundary conditions.
- Invalid inputs.
- Units and dimensional consistency.
- Conservation or balance checks.
- Regression cases from reported issues.

If a contribution cannot reasonably include automated tests, explain why and describe the manual or conceptual validation performed.

## AI-Assisted Contributions

AI coding agents can help draft code, tests, documentation, and review notes. Contributors remain responsible for verifying generated content, especially physical assumptions, equations, units, and safety-sensitive claims.
