#!/usr/bin/python3

def prime_sieve(number: int) -> list:        
    sieve = [True] * number

    for i in range(3, int(number**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, number, 2) if sieve[i]]


def prime_power_triples(limit: int) -> int:
    numbers = []

    for x in prime_sieve(int(limit**0.5) + 1):
        remainder_yz = limit - x**2

        if remainder_yz <= 1:
            break

        for y in prime_sieve(int(remainder_yz**(1/3)) + 1):
            remainder_z = remainder_yz - y**3

            if remainder_z <= 1:
                break

            for z in prime_sieve(int(remainder_z**0.25) + 1):
                number = x**2 + y**3 + z**4

                if number < limit:
                    numbers.append(number)


    return len(set(numbers))


def main():
    limit = 50*10**6
    print(prime_power_triples(limit))


if __name__ == "__main__":
    main()