def factorize(number: int) -> list:
    factors = []

    for d in range(2, int(number**0.5 + 1)):
        while number % d == 0:
            factors.append(d)
            number //= d

    if number > 1:
       factors.append(number)

    return factors


def primary_factor_analyse(number: int) -> int:
    return(max(factorize(number)))


print("Biggest prime:", primary_factor_analyse(600851475143))