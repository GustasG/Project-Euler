from shared.combinatorics import combinations


def max_combinations(limit: int) -> int:
    return sum(combinations(n, r) > 1_000_000
               for n in range(1, limit + 1)
               for r in range(1, n + 1))


if __name__ == "__main__":
    c = max_combinations(100)

    print(c)
