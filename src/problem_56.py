#!/usr/bin/python3

def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))


def max_digit_sum(limit: int) -> int:
    return max(sum_digits(a**b) for a in range(2, limit) for b in range(limit))


def main():
    print(max_digit_sum(100))


if __name__ == "__main__":
    main()