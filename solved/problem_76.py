def summation_count(target: int) -> int:
    targets = [0] * (target + 1)
    targets[0] = 1

    for i in range(1, target):
        for j in range(i, target + 1):
            targets[j] += targets[j - i]

    return targets[-1]


def main() -> None:
    print(summation_count(100))


if __name__ == '__main__':
    main()
