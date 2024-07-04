#!/usr/bin/python3
"""
Prime Game
"""


def find_multiples(num, targets):
    """
    Find multiples of a given number within a list and remove them.

    Parameters:
    num (int): The number to find multiples of.
    targets (list of int): The list of numbers to search within.

    Returns:
    list of int: The list with multiples of num removed.
    """
    targets = [i for i in targets if i % num != 0]
    return targets


def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(n):
    """
    Count prime numbers and remove them along with their
    multiples from a set.

    Parameters:
    n (set of int): The set of numbers to process.

    Returns:
    int: The count of prime numbers found.
    """
    counter = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if is_prime(i):
            counter += 1
            target.remove(i)
            target = find_multiples(i, target)
    return counter


def is_winner(x, nums):
    """
    Determine the winner after x rounds of the prime game.

    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number
    and its multiples from the set. The player that cannot make a
    move loses the game.

    They play x rounds of the game, where n may be different for
    each round. Assuming Maria always goes first and both players
    play optimally, determine who the winner of each game is.

    Parameters:
    x (int): The number of rounds to play.
    nums (list of int): The list of n values for each round.

    Returns:
    str or None: The winner ("Maria" or "Ben") or None if it's a draw.
    """
    players = {'Maria': 0, 'Ben': 0}

    for num in nums[:x]:
        cluster = set(range(1, num + 1))
        prime_count = find_primes(cluster)

        if prime_count % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
