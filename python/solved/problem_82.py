import numpy as np

from shared.paths import RESOURCE_DIR


def read_file(path) -> np.ndarray:
    with open(path, 'r') as f:
        return np.array([[int(number) for number in line.split(',')]
                         for line in f])


def find_minimal_path(matrix: np.ndarray) -> int:
    solution = [matrix[i][-1] for i in range(len(matrix))]

    for i in range(len(matrix) - 2, -1, -1):
        solution[0] += matrix[0][i]

        for j in range(1, len(matrix)):
            solution[j] = min(solution[j], solution[j - 1]) + matrix[j][i]

        for j in range(len(matrix) - 2, -1, -1):
            solution[j] = min(solution[j], solution[j + 1] + matrix[j][i])

    return min(solution)


def main() -> None:
    matrix = read_file(RESOURCE_DIR / 'problem_82_matrix.txt')
    print(find_minimal_path(matrix))


if __name__ == "__main__":
    main()
