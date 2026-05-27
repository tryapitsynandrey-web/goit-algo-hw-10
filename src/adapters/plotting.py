import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Callable


def save_integral_plot(
    func: Callable[[float], float], a: float, b: float, output_path: Path
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = np.array([func(val) for val in x])

    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2, label="f(x) = x^2")

    ix = np.linspace(a, b, 100)
    iy = np.array([func(val) for val in ix])
    ax.fill_between(ix, iy, color="gray", alpha=0.3, label=f"Integral [{a}, {b}]")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Monte Carlo Integration Area")
    ax.legend()

    plt.savefig(output_path)
    plt.close(fig)
