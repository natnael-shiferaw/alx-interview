#!/usr/bin/python3
"""
Prime Game
"""

def find_multiples(num, targets):
    """
    Finds and removes multiples of a given number within a list
    """
    return [i for i in targets if i % num != 0]

def is_prime(i):
    """
    Check if a number is prime.
    """
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def find_primes(n):
    """
    Dispatch a given set into prime numbers and non-prime numbers.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def is_winner(x, nums):
    """
    Determine the winner of the prime game after x rounds.

    Args:
        x (int): number of rounds
        nums (list): list of n values for each round

    Returns:
        str: name of the player that won the most rounds or None if it's a tie
    """
    if x <= 0 or not nums:
        return None

    players = {'Maria': 0, 'Ben': 0}

    for num in nums:
        primes = find_primes(num)
        turn = 0  # Maria starts first

        while primes:
            prime = primes.pop(0)
            primes = find_multiples(prime, primes)
            turn = 1 - turn  # Switch turns

        if turn == 0:  # If turn is 0, Ben made the last move and won
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
