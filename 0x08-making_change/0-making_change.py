#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if total >= coin:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin

    return count if total == 0 else -1
