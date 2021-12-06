from numba import njit

from math import sqrt


def bigger_side_perimeter(limit: int) -> int:
    total = 0

    for i in range(3, (limit - 1) // 3, 2):
        height = sqrt(i ** 2 - ((i + 1) / 2) ** 2)
        area = height * (i + 1) / 4

        if area >= limit:
            break

        if height.is_integer():
            print(i, i, i + 1)
            total += 3*i + 1

    return total


def smaller_side_perimeter(limit: int) -> int:
    total = 0

    for i in range(3, (limit + 1) // 3, 2):
        height = sqrt(i ** 2 - ((i - 1) / 2) ** 2)
        area = height * (i - 1) / 4

        if area >= limit:
            break

        if height.is_integer():
            print(i, i, i - 1)
            total += 3*i - 1

    return total


def main() -> None:
    limit = 10 ** 9

    print(bigger_side_perimeter(limit))


if __name__ == '__main__':
    main()
