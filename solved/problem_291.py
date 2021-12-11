from math import sqrt

import gmpy2


def count_panaitopol_primes(limit: int) -> int:
    return sum(gmpy2.is_prime(i**2 + (i + 1)**2, 5)
               for i in range(1, int(sqrt(limit / 2))))


def main() -> None:
    limit = 5 * 10**15
    s = count_panaitopol_primes(limit)

    print(s)


if __name__ == '__main__':
    main()
