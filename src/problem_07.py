import math

def isPrime(number_to_check: int) -> bool:
    if number_to_check == 1:
        return False
    elif number_to_check < 4:
        return True
    elif number_to_check % 2 == 0:
        return False
    elif number_to_check < 9:
        return True
    elif number_to_check % 3 == 0:
        return False
    else:
        bound = round(math.sqrt(number_to_check))
        f = 5
        while f <= bound:
            if number_to_check % f == 0:
                return False
            elif number_to_check % (f + 2)  == 0:
                return False
            f += 6
        return True


def find_primary(limit: int) -> int:
    count = 1
    candidate = 1

    while count < limit:
        candidate += 2

        if isPrime(candidate):
            count += 1

    return candidate


def main():
    prime = find_primary(10001)
    print(prime)

if __name__ == "__main__":
    main()

