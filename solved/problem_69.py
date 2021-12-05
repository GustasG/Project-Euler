from shared.primes import is_prime


def phi_max(n: int) -> int:
    answer, prime = 1, 1

    while answer < n:
        prime += 1
        if is_prime(prime):
            answer *= prime

    return answer // prime


def main() -> None:
    m = phi_max(1000000)

    print(m)


if __name__ == "__main__":
    main()
