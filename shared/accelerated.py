from math import sqrt

import numpy as np
from numba import njit


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


@njit(boundscheck=False)
def eratosthenes_sieve(n: int) -> list[int]:
    is_prime = np.full(n, True)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            is_prime[i**2::i] = False

    return [i
            for i, flag in enumerate(is_prime)
            if flag]


@njit(boundscheck=False)
def phi_fractions(limit: int) -> np.ndarray:
    fractions = np.arange(limit + 1)
    fractions[1] = 0

    for i in range(2, limit + 1):
        if fractions[i] == i:
            fractions[i::i] = (i - 1) * fractions[i::i] // i

    return fractions


@njit(boundscheck=False)
def produce_radicals(limit: int) -> np.ndarray:
    radicals = np.ones(limit + 1)

    for i in range(2, limit):
        if radicals[i] == 1:
            radicals[i] = i
            radicals[2 * i::i] *= i

    return radicals


@njit
def number_digits(number: int) -> list[int]:
    digits = []

    while number > 0:
        digits.append(number % 10)
        number //= 10

    return digits
