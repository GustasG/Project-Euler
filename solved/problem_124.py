from shared.accelerated import produce_radicals


def main() -> None:
    limit = 100000
    index = 10000

    radicals = [(i, int(value))
                for i, value in enumerate(produce_radicals(limit))][1:]

    sorted_radicals = sorted(radicals, key=lambda x: x[1])
    print(sorted_radicals[index - 1][0])


if __name__ == '__main__':
    main()
