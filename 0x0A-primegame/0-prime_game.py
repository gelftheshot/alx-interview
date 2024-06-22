#!/usr/bin/python3

"""
This module simulates a game between Maria and Ben involving prime numbers.
Players take turns choosing a prime number from a set of consecutive integers
starting from 1 up to n, removing that number and its multiples. The player
who cannot make a move loses.

The game is played over x rounds, each with a different n. Assuming Maria
always goes first and both players play optimally, this module determines
the winner of each game and the overall round winner.

Functions:
    isWinner(x, nums): Determines the game winner over x rounds.

Constraints:
    - No external packages can be imported.
    - The values of n and x will not exceed 10000.
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def simulate_round(n):
    """
    Determine the winner of one round by counting
    the number of prime numbers
    up to n and checking if this count is odd.
    """
    primes = [i for i in range(2, n+1) if is_prime(i)]
    return len(primes) % 2 != 0


def isWinner(x, nums):
    """
    Determines the winner of the game played over x rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): An array where each element
    represents the set of consecutive integers from 1 to n for each round.

    Returns:
    str: The name of the player who won the most rounds.
    Returns None if the winner cannot be determined or if input is invalid.
    """
    if x <= 0 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n <= 0:
            continue
        if simulate_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
