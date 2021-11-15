def calculate_residues(m: int, n: int) -> list[int]:
    residues = [0] * n

    for i in range(1, m + 1):
        residues[pow(i, i, n)] += 1

    return residues


def main() -> None:
    m = 250_250
    n = 250

    residues = calculate_residues(m, n)

    print(residues)


if __name__ == '__main__':
    main()
