from numba import njit


@njit()
def find_divisible_subsets(residues: list[int], n: int) -> list[int]:
    subsets = [0] * n
    subsets[0] = 1

    for i in range(1, len(residues)):
        subsets = [(value + subsets[(j - residues[i]) % len(subsets)]) % 10**16
                   for (j, value) in enumerate(subsets)]

    subsets[0] -= 1

    return subsets


def main() -> None:
    m = 250_250
    n = 250

    residues = [pow(i, i, n) for i in range(0, m + 1)]
    subsets = find_divisible_subsets(residues, n)

    print(subsets[0])


if __name__ == '__main__':
    main()
