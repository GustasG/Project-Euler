#!/usr/bin/python3

MAX_ITERATIONS = 25

def reverse(number: int) -> int:
    reversed = 0

    while number > 0:
        remainder = number % 10
        reversed = (reversed * 10) + remainder
        number //= 10

    return reversed


def is_palindrome(number: int) -> bool:
    return number == reverse(number)


def is_lychrel(number: int) -> int:
    for i in range(MAX_ITERATIONS):
        number += reverse(number)

        if is_palindrome(number):
            return False

    return True


def main():
    upper = 10**4

    count = sum(is_lychrel(i) for i in range(1, upper))
    print(count)


if __name__ == "__main__":
    main()