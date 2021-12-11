from shared.accelerated import eratosthenes_sieve


def main() -> None:
    prime_count = 10**6
    remainder = 10**10

    primes = eratosthenes_sieve(prime_count)

    for n in range(0, len(primes), 2):
        deg = n + 1

        if 2 * deg * primes[n] > remainder:
            print(deg)
            break


if __name__ == "__main__":
    main()
