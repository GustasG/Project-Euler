#!/usr/bin/python3

import pyprimes

def primes(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def find_quadratic_primes():
    max = 0
    max_a = 0
    max_b = 0

    first_primes = primes(1000)

    for a in range(-999, 1000):
        for b in first_primes:
            n = 0

            while pyprimes.isprime(n*n + a*n + b):
                n += 1
            
            if n > max:
                max = n
                max_a = a
                max_b = b

    return max_a, max_b

def main():
    max_a, max_b = find_quadratic_primes()

    print(max_a * max_b)




if __name__ == "__main__":
    main()