def chain(number: int) -> int:
    if number == 1:
        return 1

    if number % 2 == 0:
        return 1 + chain(number // 2)
    else:
        return 1 + chain(3 * number + 1)


def collatz_sequence(limit: int) -> int:
    longest = -1
    idx = -1

    for i in range(limit // 2, limit):
        current_long = chain(i)

        if current_long > longest:
            idx = i
            longest = current_long

    return idx


if __name__ == '__main__':
    s = collatz_sequence(10**6)

    print(s)
