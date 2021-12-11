from functools import cache
import sys


@cache
def ack(m: int, n: int) -> int:
    if m == 0:
        return (n + 1) % 14**8
    if m > 0 and n == 0:
        return (ack(m - 1, 1)) % 14**8
    return ack(m - 1, ack(m, n - 1)) % 14**8


def main() -> None:
    mod = 14 ** 8

    ack4 = (pow(2, 65536, mod) - pow(3, mod)) % mod
    print(ack4)

    # sys.setrecursionlimit(5000)
    # print(ack(4, 4))
    # pass


if __name__ == '__main__':
    main()
