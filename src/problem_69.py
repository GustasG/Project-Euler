#!/usr/bin/python3

import pyprimes

def phiMax(n: int) -> int:
    answer = 1
    prime = 1

    while answer < n:
        prime += 1
        if pyprimes.isprime(prime):
            print(prime)
            answer *= prime

    return answer // prime


def main():
    print(f'Max phi: {phiMax(1000000)}')

if __name__ == "__main__":
    main()