from itertools import accumulate

def parse_file(file_name:str) -> list:
    file_data = open(file_name, 'r').read().splitlines()

    matrix = []

    for line in file_data:
        matrix.append([int(number) for number in line.split(',')])

    return matrix


def find_minimal_path(matrix: list) -> int:
    matrix[0] = list(accumulate(element for element in matrix[0]))

    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[0][i - 1]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


def main():
    file_name = 'problem_81_matrix.txt'

    matrix = parse_file(file_name)
    print(find_minimal_path(matrix))


if __name__ == "__main__":
    main()