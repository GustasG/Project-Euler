def main() -> None:
    limit = 1_000_000
    n, d = 2, 5

    while d <= limit:
        n += 3
        d += 7

    print(n - 3)


if __name__ == '__main__':
    main()
