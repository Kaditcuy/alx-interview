#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
    """
    returns least quantity of coins to make change
    out of total
    """

    if total <= 0:
        return 0

    coin_list = sorted(coins, reverse=True)
    coin_qty = 0

    for coin in coin_list:
        if coin <= total:
            coin_qty += total // coin

            total %= coin
            if total == 0:
                return coin_qty

    return -1
