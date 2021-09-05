from shared.generators import number_digits


def max_digit_sum(limit: int) -> int:
    return max(sum(number_digits(a ** b))
               for a in range(2, limit)
               for b in range(limit))


if __name__ == "__main__":
    s = max_digit_sum(100)

    print(s)
