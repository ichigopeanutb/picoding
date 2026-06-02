# Maintainer Workflows

PiCoding is designed for careful collaboration between human maintainers and AI coding agents. Agents can reduce maintenance burden, but maintainers should keep review authority over assumptions, implementation quality, security, and releases.

## Issue Triage

AI coding agents can help:

- Summarize long issues into problem statement, expected behavior, assumptions, and open questions.
- Identify whether an issue is a bug report, feature request, model example request, documentation request, or security concern.
- Ask for missing units, constraints, validation criteria, or reproduction steps.
- Suggest labels and priority based on project scope.
- Identify duplicate or related issues.

Maintainers should verify that summaries preserve the technical meaning of the original report.

## Pull Request Review

AI coding agents can help:

- Summarize what changed and why.
- Check whether assumptions, variables, equations, units, and limitations are documented.
- Look for missing validation logic or weak boundary tests.
- Identify changes that mix unrelated refactors with feature work.
- Draft review comments that are specific and respectful.

Maintainers should independently review any physical model, safety-sensitive claim, or generated implementation.

## Test Generation

AI coding agents can help propose tests for:

- Normal operating ranges.
- Invalid inputs.
- Boundary conditions.
- Unit consistency.
- Conservation, balance, or monotonicity checks.
- Regression cases from issues.

Generated tests should be reviewed for correctness. A passing test suite does not prove physical validity outside the documented model scope.

## Documentation Updates

AI coding agents can help:

- Update README sections after roadmap or API changes.
- Draft model documentation from code and tests.
- Convert review discussions into maintainable docs.
- Identify examples that are missing assumptions, equations, or limitations.
- Keep issue and pull request templates aligned with project goals.

Maintainers should check that documentation does not overclaim accuracy, adoption, production readiness, or validation status.

## Release Notes

AI coding agents can help:

- Summarize merged pull requests.
- Group changes into features, fixes, documentation, examples, tests, and maintenance.
- Identify breaking changes or migration notes.
- Draft concise release notes for maintainer review.

Release notes should clearly distinguish experimental examples from stable interfaces.

## Security Review

AI coding agents can help:

- Scan changes for unsafe file handling, command execution, secret exposure, or untrusted input paths.
- Review agent workflows for risky automation behavior.
- Identify whether a report belongs in public issues or private security handling.
- Draft mitigation checklists for maintainers.

Security-sensitive findings should be handled privately until maintainers decide disclosure is appropriate.

## Example Validation

AI coding agents can help:

- Compare examples against their stated assumptions, variables, equations, and validation rules.
- Identify missing boundary cases or invalid input cases.
- Check that examples do not imply production readiness without evidence.
- Suggest clearer limitations and out-of-scope notes.
- Draft review checklists for domain experts.

Maintainers should verify example behavior with domain knowledge before treating an example as authoritative.

## Dependency Review

AI coding agents can help:

- Summarize dependency changes.
- Identify new transitive dependencies and licenses.
- Flag known vulnerabilities from available tooling.
- Check whether a dependency is necessary for the project stage.
- Draft upgrade notes and compatibility checks.

Maintainers should avoid adding dependencies before the project has a clear need, especially in core model logic.
