def difference(limit: int, distinct: int) -> int:
    solutions = [0] * (limit + 1)

    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            if i * j > limit:
                break
            elif (i + j) % 4 == 0 and 3 * j > i and (3 * j - i) % 4 == 0:
                solutions[i * j] += 1

    return sum(value == distinct
               for value in solutions)


def main() -> None:
    print(difference(10 ** 6, 10))


if __name__ == '__main__':
    main()
