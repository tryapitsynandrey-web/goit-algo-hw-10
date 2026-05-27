from src.core.benchmarking import benchmark_coin_algorithms


def test_benchmark_structure():
    amounts = [10, 50]
    results = benchmark_coin_algorithms(amounts)

    assert "greedy" in results
    assert "dp" in results

    assert 10 in results["greedy"]
    assert 50 in results["greedy"]

    assert isinstance(results["greedy"][10], float)
    assert isinstance(results["dp"][50], float)
