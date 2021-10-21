from math import factorial


def combinations(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))
