#!/usr/bin/python3

from typing import List, Iterator
from itertools import permutations
import string
import os


def get_values(file_name: str) -> List[int]:
    with open(file_name, 'r') as f:
        numbers = f.read().split(',')
        return list(map(int, numbers))


def decrypt(text: List[int], password: str) -> str:
    numeric_password = list(map(ord, password))

    return ''.join(chr(text[i] ^ numeric_password[i % len(numeric_password)]) for i in range(len(text)))


def bruteforce(values: List[int]) -> Iterator[str]:
    for password in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        decrypted = decrypt(values, password)

        if decrypted.find('the') >= 0 and all(c in string.printable for c in decrypted):
            yield decrypted

def main():
    values = get_values(os.path.join('res', 'problem_59_cipher.txt'))

#    for test in bruteforce(values):
#        print(test)

    text = decrypt(values, 'exp')

    print(f'Text: {text}')
    print(f'Sum: {sum(ord(num) for num in text)}')

if __name__ == "__main__":
    main()