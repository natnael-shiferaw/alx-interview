#!/usr/bin/python3
"""
N-Queens Problem Solver
"""

import sys


def print_usage_and_exit():
    """Prints usage information and exits with status 1."""
    print('Usage: nqueens N')
    exit(1)


def validate_and_get_n():
    """
    Validates the input and returns the integer N.

    Returns:
        int: The number of queens and the size of the board (n x n).
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    return n


def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n (int): The number of queens and the size of the board (n x n).

    Returns:
        list: A list of solutions, where each solution is a list of tuples
              representing the positions of queens on the board.
    """
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    """
    Determine if two queens attack each other.

    Args:
        square (tuple): The position of the first queen (row, column).
        queen (tuple): The position of the second queen (row, column).

    Returns:
        bool: True if the queens attack each other, False otherwise.
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or
            abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """
    Check if a queen can be safely placed at a given position.

    Args:
        sqr (tuple): The position to check (row, column).
        queens (list): A list of positions of queens already
                       placed on the board.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


def format_solution(solution):
    """
    Format the solution by converting 1-based positions to 0-based.

    Args:
        solution (list): A list of tuples representing the
                         positions of queens.

    Returns:
        list: A formatted list with 0-based positions.
    """
    return [[i - 1 for i in p] for p in solution]

if __name__ == '__main__':
    n_q = validate_and_get_n()
    for answer in reversed(solve_nqueens(n_q)):
        print(format_solution(answer))

