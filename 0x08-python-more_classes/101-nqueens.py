#!/usr/bin/python3
"""program that solve"""


import sys


def is_safe(board, row, col):
    # Check if the current position is attacked by any previously placed queens

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the diagonal
    for i in range(row):
        if abs(row - i) == abs(col - board[i]):
            return False

    return True


def solve_nqueens(n):
    def backtrack(board, row):
        if row == n:
            # All queens have been placed, print the solution
            print(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    # Initialize the board with -1 values
    board = [-1] * n
    backtrack(board, 0)


# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        raise ValueError
except ValueError:
    print("N must be a number and at least 4")
    sys.exit(1)

solve_nqueens(n)
