#!/usr/bin/python3

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
    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            if ele == 1:
                p = p + 4
                if grid[i][j+1] == 1:
                    p = p - 2
                if grid[i+1][j] == 1:
                    p = p - 2
    return p 

