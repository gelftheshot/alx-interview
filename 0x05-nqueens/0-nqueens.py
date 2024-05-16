#!/usr/bin/python3
import sys


def solve_n_queen(n):
    """the main method that solves the problem
    Args:
        n (int) is the number of rows and clo
    """

    colomon = set()
    diagonal1 = set()
    diagonal2 = set()
    global result
    result = []

    board = [["."] * n for i in range(n)]

    def backtracker(row):
        """this is the function that back track our possible resulets"""
        if (row == n):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q":
                        result.append([i, j])
            print(result)
            for i in range(n):
                result.pop()
            return
        for col in range(n):
            if (col in colomon or (row + col) in diagonal1 or
                    (row - col) in diagonal2):
                continue
            colomon.add(col)
            diagonal1.add(col + row)
            diagonal2.add(row - col)
            board[row][col] = "Q"

            backtracker(row + 1)
            colomon.remove(col)
            diagonal1.remove(col + row)
            diagonal2.remove(row - col)
            board[row][col] = "."
    backtracker(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queen(int(sys.argv[1]))
