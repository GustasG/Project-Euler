from shared.paths import RESOURCE_DIR


def read_file(path) -> list[list[int]]:
    with open(path, 'r') as f:
        return [list(map(int, line.split(' ')))
                for line in f]


def max_path(numbers: list[list[int]]) -> int:
    for index in range(len(numbers) - 2, -1, -1):
        for length in range(len(numbers[index])):
            numbers[index][length] = numbers[index][length] + max(numbers[index + 1][length], numbers[index + 1][length + 1])

    return numbers[0][0]


def main() -> None:
    numbers = read_file(RESOURCE_DIR / 'problem_18_numbers.txt')
    p = max_path(numbers)

    print(p)


if __name__ == "__main__":
    main()
