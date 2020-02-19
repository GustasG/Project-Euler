import math


def primes(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def is_permutation(number1: int, number2: int) -> bool:
    return sorted(str(number1)) == sorted(str(number2))


def min_phi_permutation(limit: int) -> int:
    min_phi = 0
    max_ratio = math.inf
    primes_bellow = primes(2 * int(limit ** 0.5))

    for x in primes_bellow:
        for y in primes_bellow:
            n = x * y

            if n > limit:
                break

            phi = (x - 1)*(y - 1)
            ratio = n/phi

            if is_permutation(n, phi) and ratio < max_ratio:
                min_phi = n
                max_ratio = ratio

    return min_phi


def main():
    print(min_phi_permutation(10**7))



if __name__ == "__main__":
    main()