from shared.generators import fibonacci, even


def main() -> None:
    limit = 4_000_000
    s = sum(map(even, fibonacci(limit)))

    print(s)


if __name__ == "__main__":
    main()
