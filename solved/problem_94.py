def calculate_perimeter(limit: int) -> int:
    x, y = 2, 1
    perimeter = 0

    while True:
        a3 = 2 * x - 1
        area3 = y * (x - 2)

        if a3 > limit:
            break

        if area3 > 0 and a3 % 3 == 0 and area3 % 3 == 0:
            perimeter += a3 + 1

        a3 = 2 * x + 1

        if a3 % 3 == 0 and (y * (x + 2)) % 3 == 0:
            perimeter += a3 - 1

        x, y = 2*x + 3*y, x + 2*y

    return perimeter


def main() -> None:
    limit = 10 ** 9

    print(calculate_perimeter(limit))


if __name__ == '__main__':
    main()
