from typing import List

from shared.paths import RESOURCE_DIR


def read_names(path) -> List[str]:
    with open(path, "r") as f:
        raw_names = f.read().replace('"', '')

        return sorted(raw_names.split(','))


def letter_position(letter: str) -> int:
    return ord(letter) - 64


if __name__ == '__main__':
    names = read_names(RESOURCE_DIR / 'problem_22_names.txt')
    s = sum((i + 1) * sum(map(letter_position, name)) for i, name in enumerate(names))

    print(s)
