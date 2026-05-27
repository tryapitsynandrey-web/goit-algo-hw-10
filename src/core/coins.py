def find_coins_greedy(amount: int) -> dict[int, int]:
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer.")
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if amount == 0:
        return {}

    from config.settings import DEFAULT_COINS

    coins = sorted(DEFAULT_COINS, reverse=True)
    result: dict[int, int] = {}

    for coin in coins:
        if amount == 0:
            break
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin

    return result


def find_min_coins(
    amount: int, denominations: list[int] | None = None
) -> dict[int, int]:
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer.")
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if amount == 0:
        return {}

    if denominations is None:
        from config.settings import DEFAULT_COINS

        coins = sorted(DEFAULT_COINS, reverse=True)
    else:
        coins = sorted(denominations, reverse=True)

    # dp[i] will store the minimum number of coins for amount i
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    # coin_used[i] will store the first coin used to make amount i
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float("inf"):
        return {}

    result: dict[int, int] = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result
