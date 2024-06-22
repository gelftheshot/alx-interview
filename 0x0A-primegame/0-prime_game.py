#!/usr/bin/python3

def isWinner(x, nums):
    """

    """#!/usr/bin/python3
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

def isWinner(x, nums):
    """
    Determines the winner of the game played over x rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): An array where each element represents the set of consecutive integers from 1 to n for each round.

    Returns:
    str: The name of the player who won the most rounds. Returns None if the winner cannot be determined.
    """