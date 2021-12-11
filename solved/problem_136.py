from shared.accelerated import eratosthenes_sieve


def main() -> None:
    limit = 50_000_000
    primes = eratosthenes_sieve(limit)
    result = 0

    for prime in primes:
        if prime < limit // 4 or prime < limit // 16 or (prime - 3) % 4 == 0:
            result += 1

    print(result)


if __name__ == '__main__':
    main()
