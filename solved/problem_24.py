import itertools


DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main() -> None:
    p = list(itertools.permutations(DIGITS))
    index = 1_000_000

    print(''.join(map(str, p[index - 1])))


if __name__ == '__main__':
    main()
