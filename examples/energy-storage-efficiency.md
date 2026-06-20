# Energy Storage Efficiency Example

This example shows how PiCoding can translate a simple energy storage model into assumptions, variables, equations, validation logic, code structure, and tests.

The model calculates round-trip efficiency: the ratio of energy recovered from an energy storage system to the energy put in.

## Problem Statement

Given a known amount of energy charged into a storage system and a known amount recovered on discharge, calculate the round-trip efficiency and determine whether it falls within an expected operating range.

## Assumptions

- Energy is measured in kilowatt-hours (kWh).
- Round-trip efficiency is defined as output energy divided by input energy.
- Output energy cannot exceed input energy. Energy gain is not physically possible in this model.
- Losses during charging and discharging are combined into a single efficiency ratio. They are not modelled separately.
- The model does not account for temperature, state of charge, degradation over cycles, self-discharge, or auxiliary power consumption.
- Efficiency bounds for range validation are supplied by the caller and represent a configurable acceptance band, not a universal physical constraint.
- This is a simplified educational model, not a production engineering tool.

## Variables

| Symbol | Name | Unit | Notes |
| --- | --- | --- | --- |
| `E_in` | Input energy | kWh | Energy charged into storage. Must be greater than 0. |
| `E_out` | Output energy | kWh | Energy recovered on discharge. Must be ≥ 0 and ≤ `E_in`. |
| `η` | Round-trip efficiency | dimensionless | Computed. In [0.0, 1.0]. |
| `η_min` | Minimum expected efficiency | dimensionless | Configurable lower bound. Must be in [0.0, 1.0]. |
| `η_max` | Maximum expected efficiency | dimensionless | Configurable upper bound. Must be ≥ `η_min`. |

## Equations

Round-trip efficiency:

```text
η = E_out / E_in
```

Range check:

```text
η_min ≤ η ≤ η_max
```

## Validation Logic

The implementation rejects physically invalid inputs:

- `input_energy_kwh > 0`
- `output_energy_kwh >= 0`
- `output_energy_kwh <= input_energy_kwh`
- `0.0 <= minimum_expected_efficiency <= 1.0`
- `0.0 <= maximum_expected_efficiency <= 1.0`
- `minimum_expected_efficiency <= maximum_expected_efficiency`

Known limitations:

- Does not model charge and discharge losses separately.
- Does not account for self-discharge over time.
- Does not model temperature or cycle-count effects on efficiency.
- Does not validate whether the efficiency bounds are physically reasonable for a given storage technology.

## Code Structure

```text
src/picoding/
  __init__.py
  models/
    __init__.py
    energy_storage.py
tests/
  test_energy_storage.py
```

Function shapes:

```python
def calculate_round_trip_efficiency(
    input_energy_kwh: float,
    output_energy_kwh: float,
) -> float:
    """Calculate round-trip efficiency as output / input energy."""


def validate_efficiency_range(
    efficiency: float,
    minimum_expected_efficiency: float,
    maximum_expected_efficiency: float,
) -> bool:
    """Return True if efficiency falls within the expected range."""
```

## Example Usage

```python
from picoding.models.energy_storage import (
    calculate_round_trip_efficiency,
    validate_efficiency_range,
)

efficiency = calculate_round_trip_efficiency(
    input_energy_kwh=100.0,
    output_energy_kwh=85.0,
)
print(f"Round-trip efficiency: {efficiency:.1%}")  # 85.0%

in_range = validate_efficiency_range(
    efficiency,
    minimum_expected_efficiency=0.70,
    maximum_expected_efficiency=0.95,
)
print(f"Within expected range: {in_range}")  # True
```

The module is also directly runnable:

```text
python -m picoding.models.energy_storage
```

## Suggested Tests

Normal case:

```text
Given:
  input_energy_kwh  = 100.0 kWh
  output_energy_kwh = 85.0 kWh

Expected:
  η = 85.0 / 100.0 = 0.85
```

Boundary cases:

- Zero output energy returns an efficiency of 0.0 (total loss).
- Output equal to input returns an efficiency of 1.0 (lossless storage).
- Efficiency exactly at `η_min` or `η_max` is considered within range.

Invalid input tests:

- `input_energy_kwh = 0` raises `ValueError`.
- `input_energy_kwh < 0` raises `ValueError`.
- `output_energy_kwh < 0` raises `ValueError`.
- `output_energy_kwh > input_energy_kwh` raises `ValueError`.
- `minimum_expected_efficiency < 0` raises `ValueError`.
- `maximum_expected_efficiency > 1` raises `ValueError`.
- `minimum_expected_efficiency > maximum_expected_efficiency` raises `ValueError`.
