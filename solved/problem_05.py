from math import lcm


def main() -> None:
    m = lcm(*range(1, 20))

    print(m)


if __name__ == "__main__":
    main()
