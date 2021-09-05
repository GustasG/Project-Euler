def count_fractions(d_end: int) -> int:
    phi = [i for i in range(d_end + 1)]

    result = 0

    for i in range(2, d_end + 1):
        if phi[i] == i:
            for j in range(i, d_end + 1, i):
                phi[j] = (i - 1) * phi[j] // i

        result += phi[i]

    return result


if __name__ == "__main__":
    c = count_fractions(10**6)

    print(c)
