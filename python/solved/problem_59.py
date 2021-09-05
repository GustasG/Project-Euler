from typing import List, Iterator
from itertools import permutations

from shared.paths import RESOURCE_DIR
from shared.collections import CircularBuffer


def read_file(path) -> List[int]:
    with open(path, 'r') as f:
        numbers = f.read().split(',')
        return list(map(int, numbers))


def decrypt(text: List[int], password: str) -> str:
    numeric_password = CircularBuffer[int](list(map(ord, password)))

    return ''.join(chr(text[i] ^ numeric_password[i]) for i in range(len(text)))


def bruteforce(values: List[int]) -> Iterator[str]:
    for password in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        yield decrypt(values, ''.join(str(l) for l in password))


if __name__ == "__main__":
    values = read_file(RESOURCE_DIR / 'problem_59_cipher.txt')

    # for test in bruteforce(values):
    #     if test.find('the') >= 0 and all(c in string.printable for c in test):
    #         print(test)

    text = decrypt(values, 'exp')

    print(f'Text: {text}')
    print(f'Sum: {sum(ord(num) for num in text)}')