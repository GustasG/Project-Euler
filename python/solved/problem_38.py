def is_pandigital(number: str) -> bool:
    return ''.join(sorted(number)) == '123456789'


def find_biggest_pandigital(number: int) -> bool:
    for _ in range(1, 1_000):
        test_value = ''.join([str(number * x) for x in range(1, i)])

        if len(test_value) > 9:
            return False
        elif len(test_value) < 9:
            continue
        else:
            if is_pandigital(test_value):
                print(test_value)
                return True
    return False


if __name__ == "__main__":
    for i in range(10_000, 9_000, -1):
        if find_biggest_pandigital(i):
            break
