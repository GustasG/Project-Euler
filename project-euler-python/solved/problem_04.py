from typing import Iterator


def is_polindrome(number: int) -> bool:
    temp = number
    new_number = 0

    while temp > 0:
        last_digit = temp % 10
        new_number = new_number * 10 + last_digit
        temp //= 10

    return new_number == number


def number_iteration(digit_count: int) -> Iterator[int]:
    for i in range(10 ** (digit_count - 1), 10 ** digit_count):
        for j in range(10 ** (digit_count - 1), 10 ** digit_count):
            current = i * j

            if is_polindrome(current):
                yield current


if __name__ == "__main__":
    number = max(number_iteration(3))
    print(number)
