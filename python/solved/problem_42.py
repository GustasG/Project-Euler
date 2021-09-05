from typing import List

from shared.paths import RESOURCE_DIR


def read_words(path) -> List[str]:
    with open(path, 'r') as f:
        return f.read().replace('"', '').split(',')


def letter_position(letter: str) -> int:
    return ord(letter) - 64


if __name__ == "__main__":
    triangle_numbers = set([i * (i + 1) // 2 for i in range(100 * 100)])
    words = read_words(RESOURCE_DIR / 'problem_42_words.txt')

    count = sum(sum(map(letter_position, word)) in triangle_numbers
                for word in words)

    print(count)
