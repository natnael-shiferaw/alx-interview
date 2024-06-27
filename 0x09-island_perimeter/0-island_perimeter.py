#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A list of lists where 1 represents
                                    land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for cell1, cell2 in zip([0] + row, row + [0]):
            # Increase perimeter count if there is a boundary
            # between land and water
            perimeter += int(cell1 != cell2)
    return perimeter
