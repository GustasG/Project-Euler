#!/usr/bin/python3

import math

def calculate_lcm(number1: int, number2: int) -> int:
    return (number1 * number2) // math.gcd(number1, number2)


def calculate_multiple(first_number: int, last_number: int) -> int:
    multiple = calculate_lcm(first_number, first_number + 1)

    for i in range(first_number + 1, last_number + 1):
        multiple = calculate_lcm(multiple, i)

    return multiple


def main():
    print(calculate_multiple(1, 20))

if __name__ == "__main__":
    main()