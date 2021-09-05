import decimal


def sqrt_sum(number: int) -> int:
    num_sqrt = str(decimal.Decimal(number).sqrt()).split('.')

    if len(num_sqrt) == 1:
        return 0
    else:
        return sum(map(int, num_sqrt[1][0:99])) + int(num_sqrt[0])


if __name__ == "__main__":
    decimal.getcontext().prec = 105
    total = sum(sqrt_sum(i) for i in range(1, 100))

    print(total)
