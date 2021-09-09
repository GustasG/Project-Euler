from math import factorial

from shared.generators import number_digits


def main() -> None:
    s = sum(number_digits(factorial(100)))
    print(s)


if __name__ == "__main__":
    main()
