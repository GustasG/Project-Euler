from math import factorial

def calculatePaths(n: int) -> int:
    return factorial(2 * n) // (factorial(n) ** 2)


print(calculatePaths(20))