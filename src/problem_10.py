def sieve(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def prime_sum(upper_limit: int) -> int:
    primes = sieve(upper_limit)

    return sum(primes)


def main():
    print(prime_sum(2 * 10**6))

if __name__ == "__main__":
    main()