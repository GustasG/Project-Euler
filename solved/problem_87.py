from math import isqrt
from typing import Any, Generator

from shared.accelerated import eratosthenes_sieve


def prime_power_triples(limit: int) -> Generator[int, Any, None]:
    primes = eratosthenes_sieve(isqrt(limit))

    for x in primes:
        for y in primes:
            for z in primes:
                number = x**2 + y**3 + z**4

                if number >= limit:
                    break

                yield number


def main() -> None:
    limit = 50 * 10**6
    size = len(set(prime_power_triples(limit)))

    print(size)


if __name__ == "__main__":
    main()
