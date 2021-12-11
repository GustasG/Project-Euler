from math import gcd

from numba import njit, prange

from shared.accelerated import produce_radicals


@njit(boundscheck=False, parallel=True)
def find_abc_hits(limit: int) -> list[tuple[int, int, int]]:
    radicals = produce_radicals(limit)
    hits = []

    for a in prange(1, limit):
        for b in range(a + 1, limit - a):
            c = a + b

            if radicals[a] * radicals[b] * radicals[c] < c and gcd(a, b) == 1:
                hits.append((a, b, c))

    return hits


def main() -> None:
    limit = 120_000

    s = sum(hit[2]
            for hit in find_abc_hits(limit))

    print(s)


if __name__ == '__main__':
    main()
