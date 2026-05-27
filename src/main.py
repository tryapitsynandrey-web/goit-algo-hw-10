import logging
from config.settings import (
    DEFAULT_MC_SAMPLES,
    DEFAULT_SEED,
    DEFAULT_MC_INTERVAL,
    DEFAULT_PLOT_PATH,
    BENCHMARK_AMOUNTS,
)
from src.core.coins import find_coins_greedy, find_min_coins
from src.core.integration import monte_carlo_integral
from src.core.benchmarking import benchmark_coin_algorithms
from src.adapters.plotting import save_integral_plot
from src.utils.logging_config import setup_logging


def f(x: float) -> float:
    return x**2


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("--- Task 1: Coin Change ---")
    amount = 113
    greedy_res = find_coins_greedy(amount)
    dp_res = find_min_coins(amount)

    print(f"Amount: {amount}")
    print(f"Greedy result: {greedy_res}")
    print(f"Dynamic programming result: {dp_res}")

    logger.info("--- Benchmarking Coin Algorithms ---")
    bench_results = benchmark_coin_algorithms(BENCHMARK_AMOUNTS)
    for amt in BENCHMARK_AMOUNTS:
        g_time = bench_results["greedy"][amt]
        dp_time = bench_results["dp"][amt]
        print(f"Amount {amt:5d} -> Greedy: {g_time:.5f}s, DP: {dp_time:.5f}s")

    logger.info("--- Task 2: Monte Carlo Integration ---")
    a, b = DEFAULT_MC_INTERVAL
    analytical_result = 8 / 3

    convergence_sizes = [1_000, 10_000, 100_000]
    print("Convergence demonstration:")
    for n in convergence_sizes:
        est = monte_carlo_integral(func=f, a=a, b=b, samples=n, seed=DEFAULT_SEED)
        err = abs(est - analytical_result)
        print(f"  samples={n:>7d}  estimate={est:.10f}  abs_error={err:.10f}")

    mc_result = monte_carlo_integral(
        func=f, a=a, b=b, samples=DEFAULT_MC_SAMPLES, seed=DEFAULT_SEED
    )

    abs_error = abs(mc_result - analytical_result)
    rel_error = abs_error / analytical_result if analytical_result != 0 else 0

    print(f"Monte Carlo estimate ({DEFAULT_MC_SAMPLES} samples): {mc_result}")
    print(f"Analytical result: {analytical_result}")

    scipy_value = None
    try:
        from scipy.integrate import quad  # type: ignore[import-untyped]

        scipy_value, _ = quad(f, a, b)
        print(f"SciPy result: {scipy_value}")
    except ImportError:
        logger.warning("SciPy is not installed. Skipping SciPy verification.")

    print(f"Absolute Error: {abs_error}")
    print(f"Relative Error: {rel_error:.5%}")

    logger.info("--- Generating Plot ---")
    save_integral_plot(f, a, b, DEFAULT_PLOT_PATH)
    print(f"Plot saved to: {DEFAULT_PLOT_PATH}")


if __name__ == "__main__":
    main()
