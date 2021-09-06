from typing import Any, Generator

from shared.generators import prime_generator


def prime_power_triples(limit: int) -> Generator[int, Any, None]:
    for x in prime_generator(int(limit**0.5) + 1):
        remainder_yz = limit - x**2

        if remainder_yz <= 1:
            break

        for y in prime_generator(int(remainder_yz**(1/3)) + 1):
            remainder_z = remainder_yz - y**3

            if remainder_z <= 1:
                break

            for z in prime_generator(int(remainder_z**0.25) + 1):
                number = x**2 + y**3 + z**4

                if number < limit:
                    yield number


def main() -> None:
    limit = 50*10**6
    size = len(set(prime_power_triples(limit)))

    print(size)


if __name__ == "__main__":
    main()
