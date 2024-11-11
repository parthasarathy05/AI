def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    # Base case: all queens are placed
    if row == n:
        # Copy the board to save the current solution
        solution = ["".join("Q" if cell else "." for cell in line) for line in board]
        solutions.append(solution)
        return True

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            # Recursively place queens in the next row
            solve_n_queens(board, row + 1, n, solutions)
            # Backtrack: remove the queen
            board[row][col] = 0

    return False

def solve_8_queen_problem():
    n = 8  # 8x8 board
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    
    print("Total solutions found:", len(solutions))
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for line in solution:
            print(line)
        print()

# Call the function
solve_8_queen_problem()
