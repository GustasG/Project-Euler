from math import isqrt

from shared.primes import is_prime
from shared.generators import infinite_range


def diagonally_bellow(ratio: float) -> int:
    length = 0
    total, primes = 1, 0

    for n in infinite_range(1):
        for _ in range(4):
            length += n
            total += 1

            if is_prime(2 * length + 1):
                primes += 1

        if primes / total <= ratio:
            break

    return isqrt(2 * length + 1)


def main() -> None:
    print(diagonally_bellow(0.1))


if __name__ == '__main__':
    main()
