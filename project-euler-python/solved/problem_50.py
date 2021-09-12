from shared.generators import prime_generator


def prime_sum(limit: int) -> int:
    primes_bellow_limit = list(prime_generator(limit))

    biggest_number = 0
    biggest_length = 0

    for i in range(len(primes_bellow_limit)):
        for j in range(i + biggest_length, len(primes_bellow_limit)):
            total = sum(primes_bellow_limit[i:j])

            if total >= limit:
                break

            if total in primes_bellow_limit:
                biggest_length = j - i
                biggest_number = total

    return biggest_number


if __name__ == "__main__":
    s = prime_sum(10**6)

    print(s)
