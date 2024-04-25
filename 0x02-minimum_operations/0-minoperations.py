#!/usr/bin/python3
"""
minimum operations of copy and past
"""


from sys import argv


def minOperations(n):
    """
    Calculates the minimum number of operations
    to go from one 'H' to n 'H's
    """

    if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n
