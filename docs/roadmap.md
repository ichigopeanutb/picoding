# PiCoding Roadmap

PiCoding is early-stage. This roadmap describes the intended direction, not a guarantee of timeline or scope.

## Phase 0: Repository Initialization

Goals:

- Establish core repository structure.
- Add README, license, contribution guide, code of conduct, and security policy.
- Create initial documentation and example directories.
- Define GitHub issue and pull request templates.
- Clarify early-stage positioning and contribution expectations.

## Phase 1: Physics-Aware Prompt Templates

Goals:

- Create prompt templates for translating physical systems into structured software artifacts.
- Capture assumptions, variables, units, equations, constraints, validation logic, and tests.
- Provide templates for AI coding agents, human reviewers, and model authors.
- Add examples that show how prompts evolve into implementation tasks.

Potential outputs:

- `docs/templates/` for prompt and review templates.
- Examples for heat transfer, power draw, motion, load balancing, and resource constraints.
- Guidance for identifying missing assumptions before code generation.

## Phase 2: Prototype Model Examples

Goals:

- Build a library of small, inspectable prototype-model examples.
- Show how to structure models as assumptions, equations, implementation, tests, and limitations.
- Cover domains such as energy infrastructure, AI data centers, robotics, chips, and hardware systems.

Potential outputs:

- Markdown-first examples.
- Minimal executable examples.
- Model validation checklists.
- Example review notes for AI-generated implementations.

## Phase 3: Test Generation and Validation Workflows

Goals:

- Define repeatable patterns for generating tests from physical assumptions.
- Add validation workflows for domains, units, invariants, tolerances, and boundary conditions.
- Explore how AI agents can propose tests while maintainers retain review control.

Potential outputs:

- Test-generation templates.
- Example test suites for prototype models.
- Documentation for validation boundaries and known limitations.
- CI checks as the implementation matures.

## Phase 4: AI-Agent-Assisted Maintainer Workflows

Goals:

- Document workflows where AI coding agents support sustainable maintenance.
- Add guidance for issue triage, PR review, release notes, documentation updates, and dependency review.
- Develop checklists that make agent output easier to audit.

Potential outputs:

- Maintainer playbooks.
- Review prompts for physical reasoning and model validation.
- Release-note and changelog templates.
- Security and dependency review workflows.

## Phase 5: Broader Ecosystem Integrations

Goals:

- Explore integrations with simulation libraries, notebooks, CI systems, documentation tools, and AI-agent environments.
- Support reusable components that can fit into existing engineering and research workflows.
- Build community conventions around physics-aware AI coding.

Potential outputs:

- Package integrations.
- Example notebooks.
- Agent workflow adapters.
- Documentation publishing workflows.
- Community-maintained model example catalog.
