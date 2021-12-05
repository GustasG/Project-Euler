from functools import cache

from numba import njit


@cache
@njit
def prime_factors(number: int) -> list[int]:
    factors = []
    prime = 2

    while number > 1:
        if number % prime == 0:
            factors.append(prime)
            number /= prime
            prime -= 1
        prime += 1

    return factors

