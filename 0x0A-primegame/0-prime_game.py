#!/usr/bin/python3

"""
This module contains a game simulation between two players, Maria and Ben, who play a game involving prime numbers.
Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from
the set and removing that number and its multiples from the set. The player who cannot make a move loses the game.

The game is played over x rounds, with the possibility of a different n for each round. Assuming Maria always goes first
and both players play optimally, this module determines the winner of each game and who won the most rounds overall.

Functions:
    isWinner(x, nums): Determines the winner of the game played over x rounds.

Constraints:
    - No external packages can be imported.
    - The values of n and x will not exceed 10000.
"""

def is_prime(n):
    """
    Determines if a given number n is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    This function implements a fast algorithm for checking primality, based on the observation that a prime
    number n cannot have a divisor greater than sqrt(n). Therefore, it only checks divisibility up to sqrt(n).

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
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
        the fuction to determine the winner of
        one round
    """
    primes = [i for i in range(2, n+1) if is_prime(i)]
    return len(primes) % 2 != 0

def isWinner(x, nums):
    """
    Determines the winner of the game played over x rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): An array where each element represents the set of consecutive integers from 1 to n for each round.

    Returns:
    str: The name of the player who won the most rounds. Returns None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
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



