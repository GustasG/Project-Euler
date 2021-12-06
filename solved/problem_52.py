from shared.numeric import is_permutation
from shared.generators import infinite_range


def is_max_permutation(number: int, multiple: int) -> bool:
    for i in range(2, multiple + 1):
        if not is_permutation(number, number * i):
            return False
    return True


def permutation_multiples(multiple: int) -> int:
    for i in infinite_range(1):
        if is_max_permutation(i, multiple):
            return i


def main() -> None:
    m = permutation_multiples(6)

    print(m)


if __name__ == "__main__":
    main()