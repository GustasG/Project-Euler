from shared.primes import is_prime
from shared.generators import infinite_range


def sum_partition(numbers: list[int], size: int, target: int) -> int:
    if target == 0:
        return 1

    if target < 0:
        return 0

    if size <= 0 and target >= 1:
        return 0

    return sum_partition(numbers, size - 1, target) + sum_partition(numbers, size, target - numbers[size - 1])


def find_first_prime_summation(quantity: int) -> int:
    primes = []

    for i in infinite_range(1):
        if is_prime(i):
            primes.append(i)

        if sum_partition(primes, len(primes), i) > quantity:
            return i


def main() -> None:
    print(find_first_prime_summation(5_000))


if __name__ == '__main__':
    main()
