#!/usr/bin/python3
"""
    returns the perimeter of the island described in grid:
    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
"""


def island_perimeter(grid):
    """
        returns the perimeter of the island described in grid:
        grid is a list of list of integers:
            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically (not diagonally).
    """
    p = 0
    l_col = len(grid)
    l_row = len(grid[0])
    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            if ele == 1:
                p = p + 4
                if j < l_row - 1:
                    if grid[i][j+1] == 1:
                        p = p - 2
                if i < l_col - 1:
                    if grid[i+1][j] == 1:
                        p = p - 2
    return p
