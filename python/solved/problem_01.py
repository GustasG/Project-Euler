def summation(k: int, n: int) -> int:
    p = (n - 1) // k
    return k * p * (p + 1) // 2


def multiples(number: int) -> int:
    return summation(3, number) + summation(5, number) - summation(3 * 5, number)


if __name__ == "__main__":
    m = multiples(1000)
    print(m)
