#!/usr/bin/python3


# From: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def sieve(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def main():
    prime_count = 10**6
    remainder = 10**10

    primes = sieve(prime_count)

    for n in range(0, len(primes), 2):
        deg = n + 1

        if 2*deg*primes[n] > remainder:
            print(deg)
            break




if __name__ == "__main__":
    main()