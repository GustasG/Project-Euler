from math import factorial

from shared.generators import number_digits


def is_digit_factorial_sum_equal_to_number(number: int) -> bool:
    return sum(map(factorial, number_digits(number))) == number


def calculate_digit_factorials() -> int:
    limit = sum(map(factorial, range(10)))

    return sum(filter(is_digit_factorial_sum_equal_to_number, range(3, limit)))


def main() -> None:
    s = calculate_digit_factorials()

    print(s)


if __name__ == '__main__':
    main()
