from math import ceil
from fractions import Fraction

from shared.generators import number_digits


def second_part(current: int, depth: int) -> Fraction:
    n = (1 if current % 3 != 2 else 2 * ceil(current / 3))

    if current == depth:
        return Fraction(1, n)
    return Fraction(1, n + second_part(current + 1, depth))


def n_th_e_convergence(n: int) -> Fraction:
    if n == 1:
        return Fraction(2)
    return 2 + second_part(1, n - 1)


def main() -> None:
    value = n_th_e_convergence(100)

    print(sum(number_digits(value.numerator)))


if __name__ == '__main__':
    main()
