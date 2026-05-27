import pytest
from src.core.integration import monte_carlo_integral


def test_invalid_samples():
    with pytest.raises(ValueError):
        monte_carlo_integral(lambda x: x**2, 0, 2, samples=0)


def test_invalid_interval():
    with pytest.raises(ValueError):
        monte_carlo_integral(lambda x: x**2, 2, 0, samples=100)


def test_reproducible_seed():
    res1 = monte_carlo_integral(lambda x: x**2, 0, 2, 1000, seed=42)
    res2 = monte_carlo_integral(lambda x: x**2, 0, 2, 1000, seed=42)
    assert res1 == res2


def test_monte_carlo_estimate_accuracy():
    analytical = 8 / 3
    estimate = monte_carlo_integral(lambda x: x**2, 0, 2, samples=100_000, seed=42)

    abs_error = abs(estimate - analytical)
    rel_error = abs_error / analytical

    assert abs_error < 0.05
    assert rel_error < 0.05
