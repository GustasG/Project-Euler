from math import isqrt


def main() -> None:
    idx, biggest = 0, 0

    for D in range(2, 1_000 + 1):
        limit = isqrt(D)

        if limit ** 2 == D:
            continue

        m, d = 0, 1
        a = limit

        numm1, denm1 = 1, 0
        current, den = a, 1

        while current ** 2 - D * den ** 2 != 1:
            m = d * a - m
            d = (D - m ** 2) // d
            a = (limit + m) // d

            numm2, numm1 = numm1, current
            denm2, denm1 = denm1, den

            current = a * numm1 + numm2
            den = a * denm1 + denm2

        if current > biggest:
            biggest = current
            idx = D

    print(idx)


if __name__ == '__main__':
    main()
