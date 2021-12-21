from functools import cache

from shared.generators import number_digits


@cache
def chain_product(number: int) -> int:
    while number != 1 and number != 89:
        number = sum(digit * digit for digit in number_digits(number))
        number = chain_product(number)
    return number


def main() -> None:
    limit = 10_000_000
    result = sum(chain_product(i) == 89
                 for i in range(2, limit))

    print(result)


if __name__ == '__main__':
    main()
