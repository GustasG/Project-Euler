from typing import Tuple

from shared.primes import is_prime
from shared.generators import prime_generator


def find_quadratic_primes() -> Tuple[int, int]:
    max = 0
    max_a = 0
    max_b = 0

    for a in range(-999, 1_000):
        for b in prime_generator(1_000):
            n = 0

            while is_prime(n*n + a*n + b):
                n += 1
            
            if n > max:
                max = n
                max_a = a
                max_b = b

    return max_a, max_b


def main() -> None:
    a, b = find_quadratic_primes()

    print(a * b)


if __name__ == "__main__":
    main()
