from math import isqrt
from typing import Any, Iterable, Iterator

from shared.primes import is_prime


def even(iterable: Iterable[int]) -> Iterator[int]:
    for value in iterable:
        if value % 2 == 0:
            yield value


def odd(iterable: Iterable[int]) -> Iterator[int]:
    for value in iterable:
        if value % 2 != 0:
            yield value


def fibonacci(limit: int) -> Iterator[int]:
    prev, curr = 1, 1

    while curr < limit:
        yield curr
        prev, curr = curr, curr + prev


def prime_generator(limit: int) -> Iterator[int]:
    for i in range(2, limit):
        if is_prime(i):
            yield i


def number_digits(number: int) -> Iterator[int]:
    while number > 0:
        yield number % 10
        number //= 10


def factorization(number: int) -> Iterator[int]:
    for d in range(2, isqrt(number) + 1):
        while number % d == 0:
            number //= d
            yield d

    if number > 1:
        yield number


def infinite_range(start: int = 0, step: int = 1) -> Iterator[int]:
    current = start

    while True:
        yield current
        current += step


def iterator_length(iterator: Iterable[Any]) -> int:
    length = 0

    for _ in iterator:
        length += 1

    return length
