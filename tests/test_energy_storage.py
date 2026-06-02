"""Tests for the energy storage round-trip efficiency model."""

import pytest

from picoding.models.energy_storage import (
    calculate_round_trip_efficiency,
    validate_efficiency_range,
)


# --- calculate_round_trip_efficiency ---


def test_typical_efficiency() -> None:
    assert calculate_round_trip_efficiency(100.0, 85.0) == pytest.approx(0.85)


def test_partial_efficiency() -> None:
    assert calculate_round_trip_efficiency(200.0, 150.0) == pytest.approx(0.75)


def test_zero_output_is_zero_efficiency() -> None:
    # Boundary: all energy is lost during storage
    assert calculate_round_trip_efficiency(100.0, 0.0) == pytest.approx(0.0)


def test_output_equal_to_input_is_full_efficiency() -> None:
    # Boundary: lossless storage
    assert calculate_round_trip_efficiency(50.0, 50.0) == pytest.approx(1.0)


def test_raises_when_input_is_zero() -> None:
    with pytest.raises(ValueError, match="input_energy_kwh must be greater than zero"):
        calculate_round_trip_efficiency(0.0, 0.0)


def test_raises_when_input_is_negative() -> None:
    with pytest.raises(ValueError, match="input_energy_kwh must be greater than zero"):
        calculate_round_trip_efficiency(-10.0, 5.0)


def test_raises_when_output_is_negative() -> None:
    with pytest.raises(
        ValueError, match="output_energy_kwh must be greater than or equal to zero"
    ):
        calculate_round_trip_efficiency(100.0, -5.0)


def test_raises_when_output_exceeds_input() -> None:
    with pytest.raises(
        ValueError, match="output_energy_kwh.*cannot exceed input_energy_kwh"
    ):
        calculate_round_trip_efficiency(100.0, 110.0)


# --- validate_efficiency_range ---


def test_efficiency_within_range() -> None:
    assert validate_efficiency_range(0.85, 0.70, 0.95) is True


def test_efficiency_at_lower_bound() -> None:
    assert validate_efficiency_range(0.70, 0.70, 0.95) is True


def test_efficiency_at_upper_bound() -> None:
    assert validate_efficiency_range(0.95, 0.70, 0.95) is True


def test_efficiency_below_range() -> None:
    assert validate_efficiency_range(0.60, 0.70, 0.95) is False


def test_efficiency_above_range() -> None:
    assert validate_efficiency_range(0.99, 0.70, 0.95) is False


def test_raises_when_minimum_is_negative() -> None:
    with pytest.raises(
        ValueError, match="minimum_expected_efficiency must be between 0.0 and 1.0"
    ):
        validate_efficiency_range(0.85, -0.1, 0.95)


def test_raises_when_maximum_exceeds_one() -> None:
    with pytest.raises(
        ValueError, match="maximum_expected_efficiency must be between 0.0 and 1.0"
    ):
        validate_efficiency_range(0.85, 0.70, 1.1)


def test_raises_when_minimum_exceeds_maximum() -> None:
    with pytest.raises(
        ValueError,
        match="minimum_expected_efficiency.*cannot exceed maximum_expected_efficiency",
    ):
        validate_efficiency_range(0.85, 0.95, 0.70)
