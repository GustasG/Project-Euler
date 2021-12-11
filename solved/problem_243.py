from numba import njit

from shared.accelerated import phi_fractions


@njit()
def main() -> None:
    fractions = phi_fractions(1_000_000_000)
    limit = 15499 / 94744

    for i in range(2, len(fractions)):
        if fractions[i] / (i - 1) < limit:
            print(i)
            break


if __name__ == "__main__":
    main()
