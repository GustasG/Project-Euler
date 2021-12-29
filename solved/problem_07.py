from numba import njit

from shared.primes import is_prime


@njit
def find_primary(limit: int) -> int:
    count = 1
    candidate = 1

    while count < limit:
        candidate += 2

        if is_prime(candidate):
            count += 1

    return candidate


def main() -> None:
    prime = find_primary(10_001)
    print(prime)


if __name__ == "__main__":
    main()
