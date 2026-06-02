"""Energy storage round-trip efficiency model.

This module provides a simple model for calculating and validating the
round-trip efficiency of an energy storage system such as a battery or
pumped-hydro facility.

Assumptions:
- Energy values are in kilowatt-hours (kWh).
- Round-trip efficiency is defined as output energy divided by input energy.
- Output energy cannot exceed input energy; energy gain is not physically
  possible in this model.
- The model does not account for temperature, state of charge, degradation,
  cycle count, or self-discharge.
- This is a simplified educational model, not a production engineering tool.

Formula:
    round_trip_efficiency = output_energy_kwh / input_energy_kwh

Example usage:
    >>> from picoding.models.energy_storage import calculate_round_trip_efficiency
    >>> efficiency = calculate_round_trip_efficiency(
    ...     input_energy_kwh=100.0, output_energy_kwh=85.0
    ... )
    >>> print(f"Round-trip efficiency: {efficiency:.1%}")
    Round-trip efficiency: 85.0%
"""


def calculate_round_trip_efficiency(
    input_energy_kwh: float,
    output_energy_kwh: float,
) -> float:
    """Calculate the round-trip efficiency of an energy storage system.

    Round-trip efficiency is the ratio of energy recovered from storage to
    energy put into storage. Losses occur due to heat dissipation, internal
    resistance, and conversion inefficiencies during charge and discharge.

    Args:
        input_energy_kwh: Energy charged into the storage system, in kWh.
            Must be greater than zero.
        output_energy_kwh: Energy discharged from the storage system, in kWh.
            Must be greater than or equal to zero and must not exceed
            input_energy_kwh.

    Returns:
        Round-trip efficiency as a dimensionless ratio in [0.0, 1.0].
        A value of 1.0 represents lossless storage; 0.0 represents total loss.

    Raises:
        ValueError: If input_energy_kwh is not greater than zero.
        ValueError: If output_energy_kwh is negative.
        ValueError: If output_energy_kwh exceeds input_energy_kwh.

    Examples:
        >>> calculate_round_trip_efficiency(100.0, 85.0)
        0.85
        >>> calculate_round_trip_efficiency(50.0, 0.0)
        0.0
        >>> calculate_round_trip_efficiency(50.0, 50.0)
        1.0
    """
    if input_energy_kwh <= 0:
        raise ValueError(
            f"input_energy_kwh must be greater than zero, got {input_energy_kwh}"
        )
    if output_energy_kwh < 0:
        raise ValueError(
            f"output_energy_kwh must be greater than or equal to zero, got {output_energy_kwh}"
        )
    if output_energy_kwh > input_energy_kwh:
        raise ValueError(
            f"output_energy_kwh ({output_energy_kwh}) cannot exceed input_energy_kwh "
            f"({input_energy_kwh}): energy gain is not physically possible in this model"
        )
    return output_energy_kwh / input_energy_kwh


def validate_efficiency_range(
    efficiency: float,
    minimum_expected_efficiency: float,
    maximum_expected_efficiency: float,
) -> bool:
    """Check whether a round-trip efficiency falls within an expected range.

    This function is useful for comparing a measured or calculated efficiency
    against a configurable acceptance band, for example the manufacturer's
    specified operating range or a project-specific design target.

    Args:
        efficiency: The round-trip efficiency to check, as a dimensionless
            ratio. Typically in [0.0, 1.0].
        minimum_expected_efficiency: Lower bound of the acceptable range,
            inclusive. Must be in [0.0, 1.0].
        maximum_expected_efficiency: Upper bound of the acceptable range,
            inclusive. Must be in [0.0, 1.0] and >= minimum_expected_efficiency.

    Returns:
        True if efficiency falls within [minimum_expected_efficiency,
        maximum_expected_efficiency], False otherwise.

    Raises:
        ValueError: If minimum_expected_efficiency is outside [0.0, 1.0].
        ValueError: If maximum_expected_efficiency is outside [0.0, 1.0].
        ValueError: If minimum_expected_efficiency exceeds maximum_expected_efficiency.

    Examples:
        >>> validate_efficiency_range(0.85, 0.70, 0.95)
        True
        >>> validate_efficiency_range(0.60, 0.70, 0.95)
        False
        >>> validate_efficiency_range(0.70, 0.70, 0.95)
        True
    """
    if not (0.0 <= minimum_expected_efficiency <= 1.0):
        raise ValueError(
            f"minimum_expected_efficiency must be between 0.0 and 1.0, "
            f"got {minimum_expected_efficiency}"
        )
    if not (0.0 <= maximum_expected_efficiency <= 1.0):
        raise ValueError(
            f"maximum_expected_efficiency must be between 0.0 and 1.0, "
            f"got {maximum_expected_efficiency}"
        )
    if minimum_expected_efficiency > maximum_expected_efficiency:
        raise ValueError(
            f"minimum_expected_efficiency ({minimum_expected_efficiency}) cannot exceed "
            f"maximum_expected_efficiency ({maximum_expected_efficiency})"
        )
    return minimum_expected_efficiency <= efficiency <= maximum_expected_efficiency


if __name__ == "__main__":
    print("Energy Storage Round-Trip Efficiency Example")
    print("=" * 45)

    input_energy_kwh = 100.0
    output_energy_kwh = 85.0
    minimum_expected_efficiency = 0.70
    maximum_expected_efficiency = 0.95

    efficiency = calculate_round_trip_efficiency(input_energy_kwh, output_energy_kwh)
    in_range = validate_efficiency_range(
        efficiency, minimum_expected_efficiency, maximum_expected_efficiency
    )

    print(f"Input energy:          {input_energy_kwh} kWh")
    print(f"Output energy:         {output_energy_kwh} kWh")
    print(f"Round-trip efficiency: {efficiency:.1%}")
    print(f"Expected range:        {minimum_expected_efficiency:.0%} – {maximum_expected_efficiency:.0%}")
    print(f"Within expected range: {in_range}")
