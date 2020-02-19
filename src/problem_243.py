def phi(number: int) -> int:
    result = number

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            while number % i == 0:
                number //= i

            result -= result//i

    if number > 1:
        result -= result//number

    return result


def number_resilience(number: int) -> float:
    return phi(number) / (number - 1)


def resilience_finder(resilience: float) -> int:
    d = 2

    while number_resilience(d) >= resilience:
        d += 1

    return d


def main():
    print(number_resilience(12))
    #print(resilience_finder(15499/94744))


if __name__ == "__main__":
    main()