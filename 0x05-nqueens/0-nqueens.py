#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
This program solves the N queens problem for a given N value.
Usage: nqueens N
where N is an integer greater or equal to 4
"""

import sys

def is_safe(board, row, col, N):
    """
    A helper function to check if the current placement of queen at (row, col) is safe or not
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def n_queens(board, col, N, solutions):
    """
    Main function that solves the N queens problem using backtracking
    """
    if col == N:
        # All queens have been placed, add the solution to the list of solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            # Place the queen at the current position
            board[row][col] = 1

            # Recur to place rest of the queens
            n_queens(board, col+1, N, solutions)

            # Backtrack and remove the queen from the current position
            board[row][col] = 0


if __name__ == '__main__':
    # Check if the user has entered a valid value for N
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with all zeros
    board = [[0 for x in range(N)] for y in range(N)]

    # Solve the N queens problem
    solutions = []
    n_queens(board, 0, N, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)
