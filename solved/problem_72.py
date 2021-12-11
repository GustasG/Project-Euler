from shared.accelerated import phi_fractions


def main() -> None:
    c = sum(phi_fractions(10 ** 6))

    print(c)


if __name__ == "__main__":
    main()
