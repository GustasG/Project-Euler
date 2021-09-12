def is_polyndromic(number: int) -> bool:
    new_number = str(number)

    for i in range(len(new_number) // 2):
        if new_number[i] != new_number[len(new_number) - i - 1]:
            return False

    return True


def calculate_polyndromic(n: int) -> int:
    return sum(i for i in range(1, n)
               if is_polyndromic(i) and is_polyndromic(int(bin(i)[2:])))


if __name__ == '__main__':
    n = 10 ** 6
    p = calculate_polyndromic(n)

    print(p)
