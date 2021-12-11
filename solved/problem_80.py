import decimal


def sqrt_sum(number: int) -> int:
    num_sqrt = str(decimal.Decimal(number).sqrt()).split('.')

    if len(num_sqrt) == 1:
        return 0
    else:
        return sum(map(int, num_sqrt[1][0:99])) + int(num_sqrt[0])


def main() -> None:
    decimal.getcontext().prec = 105
    total = sum(map(sqrt_sum, range(1, 100)))

    print(total)


if __name__ == "__main__":
    main()
