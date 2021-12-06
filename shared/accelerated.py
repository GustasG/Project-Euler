from math import sqrt
from functools import cache

from numba import njit, prange


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


@njit
def eratosthenes_sieve(n: int) -> list[int]:
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in prange(i ** 2, n, i):
                is_prime[j] = False

    return [i
            for i, flag in enumerate(is_prime)
            if flag]
