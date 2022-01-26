from math import factorial

from shared.generators import number_digits


def chain_length(number: int) -> int:
    numbers = set()

    while number not in numbers:
        numbers.add(number)
        number = sum(map(factorial, number_digits(number)))

    return len(numbers)


def main() -> None:
    s = sum(chain_length(i) == 60 for i in range(1, 1_000_000))

    print(s)


if __name__ == '__main__':
    main()
