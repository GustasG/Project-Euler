from math import factorial


def lattice_paths(n: int) -> int:
    return factorial(2 * n) // (factorial(n) ** 2)


if __name__ == '__main__':
    p = lattice_paths(20)

    print(p)
