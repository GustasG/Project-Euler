from pyprimes import isprime


def trunce_left(number: int) -> bool:
    number_to_rotate = str(number)

    while len(number_to_rotate) > 1:
        number_to_rotate = number_to_rotate[1:]

        if not(isprime(int(number_to_rotate))):
            return False

    return True


def trunce_right(number: int) -> bool:
    number_to_rotate = str(number)

    while len(number_to_rotate) > 1:
        number_to_rotate = number_to_rotate[:-1]

        if not(isprime(int(number_to_rotate))):
            return False

    return True


def trunce(number: int) -> bool:
    return isprime(number) and trunce_left(number) and trunce_right(number)


def main():
    total = 0
    total_numbers = 0
    i = 10

    while total_numbers < 11:
        i += 1
        
        if trunce(i):
            total += i
            total_numbers += 1



    print(f'Total: {total}')


if __name__ == "__main__":
    main()




