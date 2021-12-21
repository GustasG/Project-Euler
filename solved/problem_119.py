from typing import Any, Generator

from shared.generators import number_digits


def generate_digit_powers() -> Generator[int, Any, None]:
    for base in range(2, 100):
        number = base

        for exponent in range(100):
            number *= base

            if sum(number_digits(number)) == base:
                yield number


def main() -> None:
    values = sorted(generate_digit_powers())

    for i, value in enumerate(values, start=1):
        print(f'a[{i}] = {value}')


if __name__ == "__main__":
    main()
