from typing import List
from itertools import accumulate

from shared.paths import RESOURCE_DIR


def read_file(path) -> List[List[int]]:
    with open(path, 'r') as f:

        return [list(map(int, line.split(',')))
                for line in f]


def find_minimal_path(matrix: List[List[int]]) -> int:
    matrix[0] = list(accumulate(element for element in matrix[0]))

    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[0][i - 1]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


def main() -> None:
    matrix = read_file(RESOURCE_DIR / 'problem_81_matrix.txt')
    print(find_minimal_path(matrix))


if __name__ == "__main__":
    main()
