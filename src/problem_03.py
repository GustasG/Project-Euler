from typing import Iterator

def factorize(number: int) -> Iterator[int]:
    for d in range(2, int(number**0.5) + 1):
        while number % d == 0:
            number //= d
            yield d

    if number > 1:
        yield number

def primary_factor_analyse(number: int) -> int:
    return(max(factorize(number)))


def main():
    prime = primary_factor_analyse(600851475143)
    print(f'Biggest prime: {prime}')


if __name__ == "__main__":
    main()