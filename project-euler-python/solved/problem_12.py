import math


def divisor_counter(number: int) -> int:
    s = 0

    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            if number // i == i:
                s += 1
            else:
                s += 2

    return s


def triangular_number(divisor_number: int) -> int:
    triangle_number = 0
    s = 0

    while True:
        s += triangle_number

        if divisor_counter(s) >= divisor_number:
            return s
        else:
            triangle_number += 1


if __name__ == '__main__':
    n = triangular_number(500)

    print(n)
