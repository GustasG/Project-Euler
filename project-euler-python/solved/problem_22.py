from typing import List

from shared.paths import RESOURCE_DIR


def read_names(path) -> List[str]:
    with open(path, "r") as f:
        return f.read().replace('"', '').split(',')


def letter_position(letter: str) -> int:
    return ord(letter) - 64


def word_letter_sum(word: str) -> int:
    return sum(map(letter_position, word))


def main() -> None:
    names = sorted(read_names(RESOURCE_DIR / 'problem_22_names.txt'))
    s = sum((i + 1) * word_letter_sum(name)
            for i, name in enumerate(names))

    print(s)


if __name__ == '__main__':
    main()
