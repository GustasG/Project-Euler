def main() -> None:
    k = sum([[i * (3 * i - 1) // 2, i * (3 * i - 1) // 2 + i]
             for i in range(1, 250)], [])

    p = [1]
    sign = [1, 1, -1, -1]
    n = 0

    while p[n] > 0:
        n += 1
        px, i = 0, 0

        while k[i] <= n:
            px += sign[i % 4] * p[n - k[i]]
            i += 1

        p.append(px % 1_000_000)

    print(n)


if __name__ == '__main__':
    main()
