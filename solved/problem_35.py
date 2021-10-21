from shared.primes import is_prime
from shared.generators import prime_generator


def rotate(value: int) -> bool:
    temp_val = str(value)

    if ("0" or "2" or "4" or "5" or "6" or "8") in temp_val:
        return False

    test_val = temp_val
    for i in range(0, len(temp_val) - 1):
        test_val = test_val[1:] + test_val[0]

        if not is_prime(int(test_val)):
            return False

    return True


if __name__ == '__main__':
    n = 10 ** 6
    p = sum(rotate(prime) for prime in prime_generator(n))

    print(p)
