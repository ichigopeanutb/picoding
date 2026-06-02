# Simple Physics Model Example

This example shows how PiCoding can translate a simple physical model into assumptions, variables, equations, validation logic, code structure, and tests.

The model estimates the final temperature of a well-mixed object after constant heating for a short period, ignoring heat loss.

## Problem Statement

Given an object with known mass and specific heat capacity, estimate how much its temperature increases when constant heating power is applied for a fixed time.

## Assumptions

- The object is well mixed and has a single uniform temperature.
- Heating power is constant over the interval.
- Heat loss to the environment is ignored.
- Mass and specific heat capacity are constant.
- No phase change occurs.
- Inputs use SI units.
- The model is appropriate only for short intervals or insulated systems where heat loss is negligible.

## Variables

| Symbol | Name | Unit | Notes |
| --- | --- | --- | --- |
| `m` | Mass | kg | Must be greater than 0 |
| `c` | Specific heat capacity | J/(kg K) | Must be greater than 0 |
| `P` | Heating power | W | Must be greater than or equal to 0 |
| `t` | Heating duration | s | Must be greater than or equal to 0 |
| `T0` | Initial temperature | K or C | Temperature differences are equivalent in K and C |
| `dT` | Temperature increase | K | Computed |
| `T1` | Final temperature | Same as `T0` | Computed |

## Equations

Energy added:

```text
Q = P * t
```

Temperature change:

```text
dT = Q / (m * c)
```

Final temperature:

```text
T1 = T0 + dT
```

## Validation Logic

The implementation should reject invalid physical states:

- `mass_kg > 0`
- `specific_heat_j_per_kg_k > 0`
- `power_w >= 0`
- `duration_s >= 0`
- All numeric inputs are finite.

The implementation should also document model limitations:

- It does not model heat loss.
- It does not model phase changes.
- It does not estimate uncertainty.
- It does not check material-specific safe temperature limits.

## Suggested Code Structure

```text
src/picoding/
  __init__.py
  models/
    heating.py
tests/
  test_heating.py
```

Example function shape:

```python
def final_temperature_no_loss(
    initial_temperature: float,
    mass_kg: float,
    specific_heat_j_per_kg_k: float,
    power_w: float,
    duration_s: float,
) -> float:
    """Estimate final temperature after constant heating without heat loss."""
```

## Suggested Tests

Normal case:

```text
Given:
  T0 = 20 C
  m = 2 kg
  c = 1000 J/(kg K)
  P = 100 W
  t = 10 s

Expected:
  Q = 1000 J
  dT = 1000 / (2 * 1000) = 0.5 K
  T1 = 20.5 C
```

Boundary cases:

- Zero power returns the initial temperature.
- Zero duration returns the initial temperature.
- Larger mass produces a smaller temperature increase for the same energy input.
- Larger specific heat capacity produces a smaller temperature increase for the same energy input.

Invalid input tests:

- Negative mass raises an error.
- Zero mass raises an error.
- Negative specific heat capacity raises an error.
- Negative power raises an error.
- Negative duration raises an error.
- Non-finite values such as `NaN` or infinity raise an error.
