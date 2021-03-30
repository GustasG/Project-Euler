#!/usr/bin/python3

from typing import Any, List, Iterator
from itertools import permutations
import string
import os

class CircularBuffer:
    def __init__(self, values: List[Any]) -> None:
        self.values = values

    def __getitem__(self, key: int) -> Any:
        return self.values[key % len(self.values)]


def read_file(file_name: str) -> List[int]:
    with open(file_name, 'r') as f:
        numbers = f.read().split(',')
        return list(map(int, numbers))

def decrypt(text: List[int], password: str) -> str:
    numeric_password = CircularBuffer(list(map(ord, password)))

    return ''.join(chr(text[i] ^ numeric_password[i]) for i in range(len(text)))


def bruteforce(values: List[int]) -> Iterator[str]:
    for password in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        yield decrypt(values, password)


def main():
    values = read_file(os.path.join('res', 'problem_59_cipher.txt'))

    # for test in bruteforce(values):
    #     if test.find('the') >= 0 and all(c in string.printable for c in test):
    #         print(test)

    text = decrypt(values, 'exp')

    print(f'Text: {text}')
    print(f'Sum: {sum(ord(num) for num in text)}')

if __name__ == "__main__":
    main()