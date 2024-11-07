#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check for conflicts with other queens
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    if row == N:
        # All queens are placed, add solution
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens(N, row + 1, board, solutions)

def main():
    # Validate input
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

    # Solve the N Queens problem
    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
