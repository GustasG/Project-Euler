import numpy as np

from shared.paths import RESOURCE_DIR


def read_file(path) -> np.ndarray:
    with open(path, 'r') as f:
        file_data = f.read().splitlines()

        return np.array([[int(number) for number in line.split(',')] for line in file_data])


def find_minimal_path(matrix: np.ndarray) -> int:
    solution = [matrix[i][-1] for i in range(len(matrix))]

    for i in range(len(matrix) - 2, -1, -1):
        solution[0] += matrix[0][i]

        for j in range(1, len(matrix)):
            solution[j] = min(solution[j], solution[j - 1]) + matrix[j][i]

        for j in range(len(matrix) - 2, -1, -1):
            solution[j] = min(solution[j], solution[j + 1] + matrix[j][i])

    return min(solution)


if __name__ == "__main__":
    matrix = read_file(RESOURCE_DIR / 'problem_82_matrix.txt')
    print(find_minimal_path(matrix))
