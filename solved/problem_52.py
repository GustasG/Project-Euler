from shared.numeric import is_permutation


def is_max_permutation(number: int, multiple: int) -> bool:
    for i in range(2, multiple + 1):
        if not is_permutation(number, number * i):
            return False
    return True


def permutation_multiples(multiple: int) -> int:
    i = 0

    while True:
        i += 1

        if is_max_permutation(i, multiple):
            return i


if __name__ == "__main__":
    m = permutation_multiples(6)

    print(m)
