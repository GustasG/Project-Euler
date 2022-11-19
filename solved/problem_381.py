from shared.accelerated import eratosthenes_sieve


def s(p: int) -> int:
    return -3 * pow(8, -1, p) % p


def main():
    primes = eratosthenes_sieve(10 ** 8)
    primes = primes[2:]  # skip 2 and 3

    print(sum(map(s, primes)))


if __name__ == '__main__':
    main()
