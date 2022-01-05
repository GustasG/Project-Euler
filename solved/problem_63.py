from shared.generators import number_digits, iterator_length


def main() -> None:
    count = 0

    for base in range(1, 10):
        for exp in range(1, 100):
            number_length = iterator_length(number_digits(base ** exp))

            if number_length == exp:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
