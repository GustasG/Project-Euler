from shared.paths import RESOURCE_DIR


def read_file(path) -> list[list[int]]:
    numbers = []

    with open(path, 'r') as f:
        for line in f:
            line = line.strip() # Remove newline

            # Remove all empty str values
            line_values = line.split(' ')
            while '' in line_values:
                line_values.remove('')

            # Convert str to int and add to list
            line_numbers = [int(x) for x in line_values]
            numbers.append(line_numbers)

    return numbers


def max_path(numbers: list[list[int]]) -> int:
    numbers = numbers.copy()

    for index in range(len(numbers) - 2, -1, -1):
        for length in range(len(numbers[index])):
            numbers[index][length] = numbers[index][length] + max(numbers[index + 1][length], numbers[index + 1][length + 1])

    return numbers[0][0]


if __name__ == "__main__":
    numbers = read_file(RESOURCE_DIR / 'problem_18_numbers.txt')
    p = max_path(numbers)

    print(p)
