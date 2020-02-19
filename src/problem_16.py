def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))


def digits_sum(number: int, exponent: int) -> int:
    return sum_digits(number ** exponent)


print(digits_sum(2, 1000))