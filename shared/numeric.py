from math import sqrt


def calculate_pentagonal(n: int) -> int:
    return (3*n*n - n) // 2


def is_pentagonal(number: int) -> bool:
    if number <= 0:
        return False

    n = (1 + sqrt(24*number + 1)) / 6

    return n.is_integer()


def is_permutation(number1: int, number2: int) -> bool:
    return sorted(str(number1)) == sorted(str(number2))


def is_pandigital(number: int) -> bool:
    return ''.join(sorted(str(number))) == '123456789'


def largest_permutation(number: int) -> int:
    digits = [0] * 10

    while number > 0:
        digits[number % 10] += 1
        number //= 10

    permutation = 0

    for i in range(9, -1, -1):
        for j in range(digits[i]):
            permutation = permutation * 10 + i

    return permutation


def smallest_permutation(number: int) -> int:
    digits = [0] * 10

    while number > 0:
        digits[number % 10] += 1
        number //= 10

    permutation = 0

    for i in range(9):
        for j in range(digits[i]):
            permutation = permutation * 10 + i

    return permutation
