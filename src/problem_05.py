#!/usr/bin/python3

from math import gcd

def calculate_lcm(number1: int, number2: int) -> int:
    return (number1 * number2) // gcd(number1, number2)


def calculate_multiple(first_number: int, last_number: int) -> int:
    numbers = [i for i in range(first_number, last_number + 1)]

    multiple = calculate_lcm(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        multiple = calculate_lcm(multiple, numbers[i])

    return multiple


def main():
    print(calculate_multiple(1, 20))

if __name__ == "__main__":
    main()