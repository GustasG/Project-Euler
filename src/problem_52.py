def is_permutation_equal(num1: int, num2: int) -> bool:
    return sorted(str(num1)) == sorted(str(num2))


def permutation_multiples(max_multip: int) -> int:
    i = 0

    while True:
        i += 1

        found = True

        for number in range(2, max_multip + 1):
            if not is_permutation_equal(i, i * number):
                found = False
                break

        if found:
            return i


def main():
    print(permutation_multiples(6))


if __name__ == "__main__":
    main()