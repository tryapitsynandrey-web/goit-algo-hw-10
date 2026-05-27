from typing import Callable
import numpy as np


def monte_carlo_integral(
    func: Callable[[float], float],
    a: float,
    b: float,
    samples: int,
    seed: int | None = None,
) -> float:
    if not isinstance(samples, int) or samples <= 0:
        raise ValueError("Samples must be a positive integer.")
    if b <= a:
        raise ValueError("Interval endpoint 'b' must be greater than 'a'.")

    rng = np.random.default_rng(seed)
    x_random = rng.uniform(a, b, samples)
    y_values = np.array([func(x) for x in x_random])

    integral = (b - a) * np.mean(y_values)
    return float(integral)
