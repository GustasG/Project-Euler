# From: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes(number: int) -> list:
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


# Returns true if item exists in collection.
# False otherwise.
def binary_search(collection: list, item) -> bool:
    n = len(collection)
    L = 0
    R = n - 1

    while L <= R:
        mid = (L + R)//2

        if collection[mid] < item:
            L = mid + 1
        elif collection[mid] > item:
            R = mid - 1
        else:
            return True

    return False


def prime_sum(limit: int) -> int:
    primes_bellow_limit = primes(limit)

    biggest_number = 0
    biggest_length = 0

    for i in range(len(primes_bellow_limit)):
        for j in range(i + biggest_length, len(primes_bellow_limit)):
            total = sum(primes_bellow_limit[i:j])

            if total >= limit:
                break

            if binary_search(primes_bellow_limit, total):
                biggest_length = j - i
                biggest_number = total


    return biggest_number



def main():
    print(prime_sum(10**6))



if __name__ == "__main__":
    main()