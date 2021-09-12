from typing import Any, Set, Generator


def divisor_sum(number: int) -> int:
    return sum(i for i in range(1, (number//2) + 1)
               if number % i == 0)


def calculate_abundant_numbers(limit: int) -> Generator[int, Any, None]:
    for x in range(1, limit):
        if divisor_sum(x) > x:
            yield x


def can_express_in_abundant_sum(numbers: Set[int], number: int) -> bool:
    for num1 in numbers:
        if number - num1 in numbers:
            return True

        if num1 > number:
            return False
    return False


def main() -> None:
    upper_limit = 28123

    abundant_numbers = set(calculate_abundant_numbers(upper_limit))
    s = sum(i for i in range(1, upper_limit)
            if not can_express_in_abundant_sum(abundant_numbers, i))

    print(s)


if __name__ == "__main__":
    main()
