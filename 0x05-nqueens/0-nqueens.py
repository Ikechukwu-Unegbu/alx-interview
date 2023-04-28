#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse N from command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is valid
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chess board
    board = [[0 for j in range(n)] for i in range(n)]

    # Initialize solution list
    solutions = []

    # Iterate over rows
    for i in range(n):
        # Iterate over columns
        for j in range(n):
            # Place queen if it's safe
            if all(board[k][j] == 0 for k in range(i)) \
               and all(board[i][k] == 0 for k in range(j)) \
               and all(board[i-k][j-k] == 0 for k in range(min(i,j)+1)) \
               and all(board[i-k][j+k] == 0 for k in range(min(i,n-j))):
                board[i][j] = 1

                # Check if it's a solution
                if i == n-1:
                    solutions.append([[i,j] for i,j in enumerate(board[-1]) if j == 1])
                else:
                    break
            else:
                # Remove previous queens and backtrack
                for k in range(i+1):
                    board[k][j-1] = 0
                if j == 0:
                    print(solutions)
                    sys.exit(0)
                j -= 2
                break
