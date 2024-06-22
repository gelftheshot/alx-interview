#!/usr/bin/python3



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
    primes = [i for i in range(2, n+1) if is_prime(i)]
    return len(primes) % 2 != 0

def isWinner(x, nums):
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
