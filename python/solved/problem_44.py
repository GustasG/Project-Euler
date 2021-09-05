from typing import List

from shared.numeric import calculate_pentagonal, is_pentagonal


def find_pentagonal() -> int:
    pentagonals: List[int] = []
    i = 0

    while True:
        i += 1
        s = calculate_pentagonal(i)

        for pj in pentagonals:
            pk = s - pj
            diff = pj - pk

            if is_pentagonal(pk) and is_pentagonal(diff):
                return abs(pk - pj)

        pentagonals.append(s)


def main() -> None:
    p = find_pentagonal()

    print(p)


if __name__ == "__main__":
    main()
