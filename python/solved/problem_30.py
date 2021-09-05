from shared.generators import number_digits


def calculate_digit_powers(power: int) -> int:
    return sum(i for i in range(2, (power + 1) * 9 ** power)
               if sum(digit ** power for digit in number_digits(i)) == i)


if __name__ == '__main__':
    s = calculate_digit_powers(5)

    print(s)
