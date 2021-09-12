import sys
from fractions import Fraction

from shared.generators import number_digits


def second_part(depth: int) -> Fraction:
    if depth == 0:
        return Fraction(1, 2)
    return Fraction(1, 2 + second_part(depth - 1))


def sqrt_2(depth: int) -> Fraction:
    return 1 + second_part(depth)


def main() -> None:
    sys.setrecursionlimit(2000)
    s = 0

    for i in range(1000):
        value = sqrt_2(i)

        if len(list(number_digits(value.numerator))) > len(list(number_digits(value.denominator))):
            s += 1

    print(s)


if __name__ == '__main__':
    main()
