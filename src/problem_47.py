import math

def factorize(number: int) -> list:
    factors = []

    for d in range(2, int(math.sqrt(number) + 1)):
        while number % d == 0:
            factors.append(d)
            number //= d

    if number > 1:
       factors.append(number)

    return factors


def find_first_prime_factors(length: int) -> list:
    i = 0

    while True:
        i += 1
        numbers = [(i + x) for x in range(length)]

        found = True
        for number in numbers:
            if len(set(factorize(number))) != length:
                found = False
                break

        if found:
            return numbers




def main():
    print(min(find_first_prime_factors(4)))


if __name__ == "__main__":
    main()