from numba import njit


@njit
def chain(number: int) -> int:
    if number == 1:
        return 1

    if number % 2 == 0:
        return 1 + chain(number // 2)
    else:
        return 1 + chain(3 * number + 1)


@njit
def collatz_sequence(limit: int) -> int:
    longest = -1
    idx = -1

    for i in range(limit // 2, limit):
        current_length = chain(i)

        if current_length > longest:
            idx = i
            longest = current_length

    return idx


def main() -> None:
    s = collatz_sequence(10**6)

    print(s)


if __name__ == '__main__':
    main()
