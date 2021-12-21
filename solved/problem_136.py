from shared.accelerated import eratosthenes_sieve


def main() -> None:
    limit = 50_000_000
    result = sum(prime < limit // 4 or prime < limit // 16 or (prime - 3) % 4 == 0
                 for prime in eratosthenes_sieve(limit))

    print(result)


if __name__ == '__main__':
    main()
