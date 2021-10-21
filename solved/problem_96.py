import numpy as np
from typing import List, Tuple
from dataclasses import dataclass

from shared.paths import RESOURCE_DIR


@dataclass
class Board:
    grid: np.ndarray

    def __post_init__(self):
        assert self.grid.shape == (9, 9)


def find_next_cell_to_fill(grid: np.ndarray, i: int, j: int) -> Tuple[int, int]:
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y

    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return x, y

    return -1, -1


def is_valid(grid: np.ndarray, i: int, j: int, e: int) -> bool:
    rowOk = all([e != grid[i][x] for x in range(9)])

    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])

        if columnOk:
            secTopX, secTopY = 3 * (i//3), 3 * (j//3)

            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solve_sudoku(grid: np.ndarray, i: int = 0, j: int = 0) -> bool:
    i, j = find_next_cell_to_fill(grid, i, j)

    if i == -1:
        return True

    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e

            if solve_sudoku(grid, i, j):
                return True
            grid[i][j] = 0
    return False


def read_file(path) -> List[Board]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

        return [Board(np.array([list(map(int, lines[i + j])) for j in range(9)]))
                for i in range(1, len(lines), 10)]


def main() -> None:
    boards = read_file(RESOURCE_DIR / 'problem_96_sudoku.txt')

    total = 0
    for i, board in enumerate(boards):
        print(f'Solving: Grid {i + 1}...')

        solve_sudoku(board.grid)
        total += 100*board.grid[0][0] + 10*board.grid[0][1] + board.grid[0][2]

    print(total)


if __name__ == "__main__":
    main()
