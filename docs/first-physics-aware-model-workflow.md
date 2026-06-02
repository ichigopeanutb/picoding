# First Physics-Aware Model Workflow

This workflow shows how PiCoding can turn a real-world physical problem into a reviewable coding task with explicit assumptions, validation rules, tests, and limitations.

It is intentionally general enough to fit early work in energy systems, robotics, chips, hardware, and scientific computing while still giving contributors a concrete structure to follow.

## Workflow Goals

Use this workflow when you need to move from a physical idea to:

- a clear problem statement
- explicit assumptions and boundary conditions
- named variables and units
- equations or model logic
- validation criteria
- an implementation outline
- tests that cover normal, boundary, and invalid cases
- documentation of limitations and next steps

## Step 1: Define the Physical Problem

Start with the smallest problem that is still useful.

Questions to answer:

- What physical behavior are you trying to represent?
- Who is the intended audience for the result?
- Is the goal estimation, simulation, validation, comparison, or control logic?
- What does the model intentionally leave out?

Example:

> Estimate round-trip efficiency for a simple energy storage system using input and output energy measurements.

## Step 2: List Assumptions and Boundary Conditions

Assumptions should be explicit before code is written. They determine whether a model is educational, approximate, or ready for deeper validation.

Common categories:

- operating range
- constant versus changing inputs
- ignored losses or side effects
- measurement quality
- environmental conditions
- time scale
- whether units are fixed

Example assumptions for an energy storage workflow:

- Input and output energy are measured over the same charge-discharge cycle.
- Energy values are provided in kilowatt-hours.
- The example ignores time-varying efficiency and thermal effects.
- The model is intended for educational validation, not production dispatch decisions.
- Input energy must be greater than zero.

## Step 3: Identify Variables and Units

Document every variable with a name, unit, and any domain constraints.

| Variable | Meaning | Unit | Constraint |
| --- | --- | --- | --- |
| `input_energy_kwh` | Energy stored during charging | kWh | `> 0` |
| `output_energy_kwh` | Energy recovered during discharge | kWh | `>= 0` |
| `round_trip_efficiency` | Recovered energy divided by input energy | ratio | `0 <= value <= 1` in the base example |
| `minimum_expected_efficiency` | Lower validation threshold | ratio | `0 <= value <= 1` |
| `maximum_expected_efficiency` | Upper validation threshold | ratio | `0 <= value <= 1` and `>= minimum` |

If a future workflow mixes units, document conversions directly and test them. Do not hide conversions inside convenience helpers without explaining them.

## Step 4: Write the Governing Equations or Model Logic

Keep the first version small enough to inspect by hand.

Example equation:

```text
round_trip_efficiency = output_energy_kwh / input_energy_kwh
```

Related validation rule:

```text
minimum_expected_efficiency <= round_trip_efficiency <= maximum_expected_efficiency
```

If the workflow is based on rules instead of equations, write those rules in plain language before implementing them.

## Step 5: Define Validation Criteria

Validation should cover both software correctness and physical plausibility.

Recommended checks:

- reject non-finite numeric inputs
- reject impossible domains such as zero or negative input energy
- verify expected ranges for derived values
- describe what a failing validation means
- separate hard input errors from softer expectation checks when useful

Example validation outcomes:

- Raise an error if `input_energy_kwh <= 0`.
- Raise an error if `output_energy_kwh < 0`.
- Report a failed expectation if the computed efficiency falls outside the configured range.
- Document that efficiency above `1.0` indicates invalid data or a broken assumption in this simplified model.

## Step 6: Generate an Initial Code Structure

Choose a structure that keeps model logic easy to review.

Suggested layout:

```text
examples/
  energy_storage_efficiency.py
tests/
  test_energy_storage_efficiency.py
```

For larger contributions, move reusable logic into `src/picoding/` and leave examples focused on runnable demonstrations.

## Step 7: Generate Tests

Tests should reflect the model's assumptions and limits, not only line coverage.

Minimum test categories:

- normal operating case
- boundary case
- invalid input case
- expectation or regression case

Example test ideas for the energy storage model:

- `100 kWh` in and `90 kWh` out returns `0.9`.
- `0 kWh` input raises an error.
- negative output energy raises an error.
- an efficiency below the configured minimum is flagged as out of range.

## Step 8: Document Limitations and Next Steps

Every workflow should say what it does not model.

Example limitations:

- no thermal losses
- no degradation over repeated cycles
- no power-rate constraints
- no uncertainty model
- no measurement noise treatment

Possible next steps:

- add time-series inputs
- add separate charge and discharge efficiency terms
- track temperature as an additional state
- compare measured data to expected bounds across many cycles

## Worked Example: Energy Storage Efficiency

This example shows the full workflow in a compact form.

### Problem

Estimate whether a storage system's round-trip efficiency falls within an expected operating range.

### Assumptions

- The measurement covers one complete charge-discharge cycle.
- All energy values use kilowatt-hours.
- Auxiliary loads and thermal effects are excluded.
- The result is illustrative and should not be treated as production-validated engineering analysis.

### Variables

- `input_energy_kwh`
- `output_energy_kwh`
- `minimum_expected_efficiency`
- `maximum_expected_efficiency`

### Equation

```text
round_trip_efficiency = output_energy_kwh / input_energy_kwh
```

### Validation Logic

- Require finite numeric inputs.
- Require `input_energy_kwh > 0`.
- Require `output_energy_kwh >= 0`.
- Require `0 <= minimum_expected_efficiency <= maximum_expected_efficiency <= 1`.

### Testing Expectations

- A nominal case such as `120 kWh` in and `108 kWh` out should compute `0.9`.
- A zero-input case should fail immediately.
- A negative-output case should fail immediately.
- A case below the minimum expected efficiency should remain computable but be reported as outside the expected range.

## Review Checklist

Before opening a pull request for a new model workflow or example, verify that the change:

- states the model purpose clearly
- names assumptions and exclusions explicitly
- documents variables and units
- shows the governing equation or rule set
- defines validation behavior
- includes tests or explains why they are not applicable
- avoids overstating physical validity or production readiness
