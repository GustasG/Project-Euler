import math

def combinations(n: int, r: int) -> int:
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def max_combinations(upper: int) -> int:
    total = 0

    for n in range(1, upper + 1):
        for r in range(1, n + 1):
            if combinations(n, r) > 1000000:
                total += 1

    return total



def main():
    print(max_combinations(100))


if __name__ == "__main__":
    main()