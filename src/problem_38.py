#!/usr/bin/python3

def is_pandigital(number: int) -> bool:
    return ''.join(sorted(number)) == '123456789'


def find_biggest_pandigital(number: int) -> bool:
    for i in range(1, 1000):
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


def main():
    for i in range(10000, 9000, -1):
        if find_biggest_pandigital(i):
            break


if __name__ == "__main__":
    main()