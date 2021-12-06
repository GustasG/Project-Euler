from shared.generators import factorization, infinite_range


def is_consecutive_factors(numbers: list[int], length: int) -> bool:
    for number in numbers:
        if len(set(factorization(number))) != length:
            return False
    return True


def find_first_prime_factors(length: int) -> list[int]:
    for i in infinite_range(1):
        numbers = [(i + x) for x in range(length)]

        if is_consecutive_factors(numbers, length):
            return numbers


def main() -> None:
    f = min(find_first_prime_factors(4))

    print(f)


if __name__ == "__main__":
    main()
