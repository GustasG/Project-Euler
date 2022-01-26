from shared.primes import is_prime


def trunce_left(number: int) -> bool:
    number_to_rotate = str(number)

    while len(number_to_rotate) > 1:
        number_to_rotate = number_to_rotate[1:]

        if not is_prime(int(number_to_rotate)):
            return False
    return True


def trunce_right(number: int) -> bool:
    number_to_rotate = str(number)

    while len(number_to_rotate) > 1:
        number_to_rotate = number_to_rotate[:-1]

        if not is_prime(int(number_to_rotate)):
            return False
    return True


def trunce(number: int) -> bool:
    return is_prime(number) and trunce_left(number) and trunce_right(number)


if __name__ == "__main__":
    total = 0
    total_numbers = 0
    i = 10

    while total_numbers < 11:
        i += 1

        if trunce(i):
            total += i
            total_numbers += 1

    print(total)
