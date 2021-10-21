from shared.algebra import square_sum, arithmetic_progression_sum


def square_difference(number: int) -> int:
    return arithmetic_progression_sum(1, number, number) ** 2 - square_sum(number)


if __name__ == "__main__":
    diff = square_difference(100)

    print(diff)
