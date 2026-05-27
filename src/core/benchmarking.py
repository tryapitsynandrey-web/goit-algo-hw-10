import timeit


def benchmark_coin_algorithms(amounts: list[int]) -> dict[str, dict[int, float]]:
    from src.core.coins import find_coins_greedy, find_min_coins

    results: dict[str, dict[int, float]] = {"greedy": {}, "dp": {}}

    for amount in amounts:
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
        results["greedy"][amount] = greedy_time

        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=100)
        results["dp"][amount] = dp_time

    return results
