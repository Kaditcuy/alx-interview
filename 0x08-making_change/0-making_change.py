#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    coin_list = sorted(coins, reverse=True)
    coin_qty = 0

    for coin in coin_list:
        if coin <= total:
            coin_qty += total // coin;

            total %= coin
            if total == 0:
                return coin_qty

    return-1
