from math import inf, isqrt

from shared.generators import prime_generator
from shared.numeric import is_permutation


def min_phi_permutation(limit: int) -> int:
    min_phi = 0
    max_ratio = inf
    primes_bellow = list(prime_generator(2 * isqrt(limit)))

    for x in primes_bellow:
        for y in primes_bellow:
            n = x * y

            if n > limit:
                break

            phi = (x - 1)*(y - 1)
            ratio = n/phi

            if ratio < max_ratio and is_permutation(n, phi):
                min_phi = n
                max_ratio = ratio

    return min_phi


def main() -> None:
    p = min_phi_permutation(10**7)

    print(p)


if __name__ == "__main__":
    main()
