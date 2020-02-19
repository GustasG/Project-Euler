def parse_file(file_name:str) -> list:
    file_data = open(file_name, 'r').read().splitlines()

    matrix = []

    for line in file_data:
        matrix.append([int(number) for number in line.split(',')])

    return matrix


def find_minimal_path(matrix: list) -> int:
    solution = [matrix[i][-1] for i in range(len(matrix))]

    for i in range(len(matrix) - 2, -1, -1):
        solution[0] += matrix[0][i]

        for j in range(1, len(matrix)):
            solution[j] = min(solution[j], solution[j - 1]) + matrix[j][i]

        for j in range(len(matrix) - 2, -1, -1):
            solution[j] = min(solution[j], solution[j + 1] + matrix[j][i])

    return min(solution)


def main():
    file_name = 'problem_82_matrix.txt'

    matrix = parse_file(file_name)
    print(find_minimal_path(matrix))


if __name__ == "__main__":
    main()