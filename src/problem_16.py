from typing import Iterator

def digits(number: int) -> Iterator[int]:
    while number > 0:
        yield number % 10
        number //= 10

def digits_sum(number: int, exp: int) -> int:
    return sum(digits(number ** exp))


print(digits_sum(2, 1000))