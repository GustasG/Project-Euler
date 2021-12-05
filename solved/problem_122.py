from numba import njit, prange


@njit
def search(chain: list[int], exponent: int, max_depth: int) -> bool:
    if len(chain) > max_depth:
        return False

    last = chain[-1]

    for i, element in enumerate(chain):
        s = chain[len(chain) - 1 - i] + last

        if s == exponent:
            return True

        chain.append(s)

        if search(chain, exponent, max_depth):
            return True

        chain.pop()

    return False


@njit
def find_chain(exponent: int) -> list[int]:
    depth = 1

    while True:
        chain = [1]

        if search(chain, exponent, depth):
            return chain

        depth += 1


def main() -> None:
    s = sum(len(find_chain(i))
            for i in prange(2, 200 + 1))

    print(s)


if __name__ == '__main__':
    main()
