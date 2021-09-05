from math import factorial

from shared.generators import number_digits


def calculate_digit_factorials() -> int:
    limit = sum(factorial(i) for i in range(10))

    return sum(i for i in range(3, limit)
               if sum(factorial(x) for x in number_digits(i)) == i)


if __name__ == '__main__':
    s = calculate_digit_factorials()

    print(s)
