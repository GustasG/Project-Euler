from shared.primes import is_prime


def find_panaitopol_prime_sum(upper_bound: int) -> int:
    total = 0

    for n in range(1, upper_bound):
        p = n ** 2 + (n + 1) ** 2

        if p >= upper_bound:
            break

        if is_prime(p):
            total += 1

    return total


def main() -> None:
    s = find_panaitopol_prime_sum(5 * (10 ** 15))

    print(s)


if __name__ == '__main__':
    main()
