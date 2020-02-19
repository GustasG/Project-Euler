#!/usr/bin/python3


def count_fractions(d_end):
    phi = [i for i in range(d_end + 1)]

    result = 0

    for i in range(2, d_end + 1):
        if phi[i] == i:
            for j in range(i, d_end + 1, i):
                phi[j] = (i - 1) * phi[j] // i

        result += phi[i]

    return result


def main():
    print(count_fractions(10**6))


if __name__ == "__main__":
    main()