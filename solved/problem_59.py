from typing import Iterator
from itertools import permutations

from shared.paths import RESOURCE_DIR
from shared.collections import CircularBuffer


def read_file(path) -> list[int]:
    with open(path, 'r') as f:
        return list(map(int, f.read().split(',')))


def decrypt(text: list[int], password: str) -> str:
    numeric_password = CircularBuffer(map(ord, password))

    return ''.join(chr(text[i] ^ numeric_password[i]) for i in range(len(text)))


def bruteforce(values: list[int]) -> Iterator[str]:
    for password in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        yield decrypt(values, ''.join(str(letter) for letter in password))


def main() -> None:
    values = read_file(RESOURCE_DIR / 'problem_59_cipher.txt')

    # for test in bruteforce(values):
    #     if test.find('the') >= 0 and all(c in string.printable for c in test):
    #         print(test)

    text = decrypt(values, 'exp')

    print(f'Text: {text}')
    print(f'Sum: {sum(ord(num) for num in text)}')


if __name__ == "__main__":
    main()
