import numpy as np
from numba import njit

from shared.paths import RESOURCE_DIR


@njit
def find_next_cell_to_fill(board: np.ndarray, i: int, j: int) -> tuple[int, int]:
    for x in range(i, 9):
        for y in range(j, 9):
            if board[x][y] == 0:
                return x, y

    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x, y

    return -1, -1


@njit
def is_valid(board: np.ndarray, i: int, j: int, value: int) -> bool:
    valid_horizontally = value not in board[i]
    valid_vertically = value not in board[:, j]
    valid_subgrid = value not in board[3 * (i // 3):3 * (i // 3) + 3, 3 * (j // 3):3 * (j // 3) + 3]

    return valid_horizontally and valid_vertically and valid_subgrid


@njit
def solve_sudoku(board: np.ndarray, i: int = 0, j: int = 0) -> bool:
    i, j = find_next_cell_to_fill(board, i, j)

    if i == -1:
        return True

    for e in range(1, 10):
        if is_valid(board, i, j, e):
            board[i][j] = e

            if solve_sudoku(board, i, j):
                return True
            board[i][j] = 0
    return False


def read_file(path) -> list[np.ndarray]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

        return [np.array([list(map(int, lines[i + j])) for j in range(9)])
                for i in range(1, len(lines), 10)]


def main() -> None:
    boards = read_file(RESOURCE_DIR / 'problem_96_sudoku.txt')

    total = 0
    for i, board in enumerate(boards, start=1):
        print(f'Solving: board {i}...')

        solve_sudoku(board)
        total += 100*board[0][0] + 10*board[0][1] + board[0][2]

    print(total)


if __name__ == "__main__":
    main()
