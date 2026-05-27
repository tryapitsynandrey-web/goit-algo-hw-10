import pytest
from src.core.coins import find_coins_greedy, find_min_coins


def test_find_coins_greedy_zero():
    assert find_coins_greedy(0) == {}


def test_find_min_coins_zero():
    assert find_min_coins(0) == {}


def test_find_coins_greedy_113():
    assert find_coins_greedy(113) == {50: 2, 10: 1, 2: 1, 1: 1}


def test_find_min_coins_113():
    assert find_min_coins(113) == {50: 2, 10: 1, 2: 1, 1: 1}


def test_greedy_and_dp_equivalence():
    amount = 47
    assert find_coins_greedy(amount) == find_min_coins(amount)


def test_negative_amount_raises_value_error():
    with pytest.raises(ValueError):
        find_coins_greedy(-5)
    with pytest.raises(ValueError):
        find_min_coins(-5)


def test_non_integer_amount_raises_type_error():
    with pytest.raises(TypeError):
        find_coins_greedy(10.5)  # type: ignore
    with pytest.raises(TypeError):
        find_min_coins(10.5)  # type: ignore


def test_non_canonical_coins():
    denominations = [4, 3, 1]
    amount = 6

    # DP should find the optimal solution
    dp_res = find_min_coins(amount, denominations=denominations)
    assert dp_res == {3: 2}  # 3 + 3 = 6 (2 coins)
