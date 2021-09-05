import math

from shared.generators import number_digits


if __name__ == "__main__":
    s = sum(number_digits(math.factorial(100)))
    print(s)

