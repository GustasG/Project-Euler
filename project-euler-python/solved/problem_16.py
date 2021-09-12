from shared.generators import number_digits


def digits_sum(number: int, exp: int) -> int:
    return sum(number_digits(number ** exp))


if __name__ == '__main__':
    s = digits_sum(2, 1000)

    print(s)
