#!/usr/bin/python3
"""
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
"""
from collections import deque


def makeChange(coins, total):
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_total, coin_count = queue.popleft()

        for coin in coins:
            next_total = current_total + coin
            if next_total == total:
                return coin_count + 1
            if next_total < total and next_total not in visited:
                visited.add(next_total)
                queue.append((next_total, coin_count + 1))

    return -1
