def print_board(board):
    """Print an 8×8 chessboard with queens using ANSI colors"""
    DARK  = "\033[48;5;94m"         # brown/dark square
    LIGHT = "\033[48;5;228m"        # cream/light square
    QUEEN = "\033[1;38;5;196m♛ "   # bright red queen
    RESET = "\033[0m"

    print("  " + " ".join(str(i) for i in range(8)))  # column numbers

    for r in range(8):
        row = f"{r} "  # row number
        for c in range(8):
            color = DARK if (r + c) % 2 == 1 else LIGHT
            cell = QUEEN if board[r][c] == 1 else "  "
            row += color + cell + RESET
        print(row)
    print()


def is_safe(board, row, col):
    """Check if queen can be placed at board[row][col]"""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, solutions):
    """
    Backtracking solver - collects ALL solutions
    """
    if row == 8:
        # Found a solution → make a copy and store it
        solutions.append([row[:] for row in board])
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1, solutions)
            board[row][col] = 0  # backtrack


def show_all_solutions():
    board = [[0] * 8 for _ in range(8)]
    solutions = []

    print("Solving 8-Queens... (92 solutions total)\n")
    solve_n_queens(board, 0, solutions)

    print(f"Found {len(solutions)} solutions.\n")

    for idx, sol in enumerate(solutions, 1):
        print(f"\nSolution #{idx:2d}  (queen columns: { [c for r in sol for c,v in enumerate(r) if v==1] })")
        print_board(sol)


if __name__ == "__main__":
    show_all_solutions()