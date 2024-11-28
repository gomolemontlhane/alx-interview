#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins, or -1 if not possible.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
