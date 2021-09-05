from shared.generators import fibonacci


if __name__ == "__main__":
    limit = 4_000_000
    s = sum(x for x in fibonacci(limit) if x % 2 == 0)

    print(s)
