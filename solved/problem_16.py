from shared.generators import number_digits


def main() -> None:
    s = sum(number_digits(2 ** 1000))

    print(s)


if __name__ == '__main__':
    main()
