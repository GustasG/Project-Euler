from shared.numeric import is_permutation
from shared.accelerated import eratosthenes_sieve


def main() -> None:
    primes = eratosthenes_sieve(10**4)

    for increment in range(1, 10**4):
        for first_number in primes:
            second_number = first_number + increment
            third_number = second_number + increment

            if first_number >= 10**4 or second_number >= 10**4 or third_number >= 10**4:
                break

            if is_permutation(first_number, second_number) and is_permutation(first_number, third_number)\
                    and first_number in primes and second_number in primes and third_number in primes:
                print(f'{first_number=}, {second_number=}, {third_number=}, {increment=}')


if __name__ == "__main__":
    main()
