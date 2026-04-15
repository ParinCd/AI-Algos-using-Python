def print_board_fancy(board):
    # ANSI color codes
    DARK  = "\033[48;5;94m"     # brownish dark square
    LIGHT = "\033[48;5;228m"    # light beige/cream
    QUEEN = "\033[1;38;5;196m♛ "  # bright red queen
    RESET = "\033[0m"

    n = len(board)

    for r in range(n):
        row_str = ""

        for c in range(n):
            is_dark = (r + c) % 2 == 1
            color = DARK if is_dark else LIGHT

            if board[r][c] == 1:
                square = QUEEN
            else:
                square = "  "  # two spaces to match queen width

            row_str += color + square + RESET

        print(row_str)

    print()  # empty line after board


def is_safe(board, row, col):
    n = len(board)

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0  # backtrack

    return False


def four_queens():
    n = 4
    board = [[0] * n for _ in range(n)]

    print("Solving 4-Queens...\n")

    if solve_n_queens(board, 0):
        print("One solution:\n")
        print_board_fancy(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    four_queens()