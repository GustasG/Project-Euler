from bisect import bisect_left 

def generate_primes(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def is_permutation(number1: int, number2: int) -> bool:
    return sorted(str(number1)) == sorted(str(number2))


def binary_search(collection: list, x) -> bool: 
    i = bisect_left(collection, x)

    if i != len(collection) and collection[i] == x:
        return True
    else:
        return False


def main():
    primes = generate_primes(10**4)
    primes = primes[primes.index(1009):]


    for increment in range(1, 10**4):
        for first_number in primes:
            second_number = first_number + increment
            third_number = second_number + increment

            if first_number >= 10**4 or second_number >= 10**4 or third_number >= 10**4:
                break

            if is_permutation(first_number, second_number) and is_permutation(first_number, third_number) and binary_search(primes, first_number) and binary_search(primes, second_number) and binary_search(primes, third_number):
                print(f'first = {first_number}, second = {second_number}, third = {third_number}, increment = {increment}')


if __name__ == "__main__":
    main()