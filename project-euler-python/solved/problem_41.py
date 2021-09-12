from shared.generators import prime_generator


def is_pandigital(number: int) -> bool:
    temp_number = str(number)

    for i in range(1, len(temp_number) + 1):
        if str(i) not in temp_number:
            return False
    return True


if __name__ == '__main__':
    primes = set(prime_generator(10 ** 7))
    biggest = max(i for i in range(10 ** 6, 10 ** 7)
                  if i in primes and is_pandigital(i))

    print(biggest)
