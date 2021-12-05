from shared.generators import prime_generator


def main() -> None:
    s = sum(prime_generator(2 * 10**6))

    print(s)


if __name__ == "__main__":
    main()
