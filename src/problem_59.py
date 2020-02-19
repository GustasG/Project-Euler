#!/usr/bin/python3

from itertools import permutations
import string


def get_values(file_name: str) -> list:
    with open(file_name, 'r') as f:
        file_data = f.read()
        numbers = file_data.split(',')

        return list(map(int, numbers))


def decrypt(enc_values: list, password: tuple) -> str:
    pass_len = len(password)
    encv_len = len(enc_values)

    return ''.join(chr(enc_values[i] ^ ord(password[i % pass_len])) for i in range(encv_len))


def bruteforce(values: list):
    for password in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        decoded = decrypt(values, password)

        if decoded.find('the') >= 0 and all(c in string.printable for c in decoded):
            print('Password: {0}'.format(''.join(password)))
            print(decoded)
            print('')

def main():
    values = get_values('problem_59_cipher.txt')

    bruteforce(values)
    text = decrypt(values, 'exp')

    print(f'Text: {text}')
    print(f'Sum: {sum(ord(num) for num in text)}')

if __name__ == "__main__":
    main()