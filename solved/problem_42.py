from shared.paths import RESOURCE_DIR


def read_words(path) -> list[str]:
    with open(path, 'r') as f:
        return f.read().replace('"', '').split(',')


def letter_position(letter: str) -> int:
    return ord(letter) - 64


def word_letter_position_sum(word: str) -> int:
    return sum(map(letter_position, word))


def main() -> None:
    words = read_words(RESOURCE_DIR / 'problem_42_words.txt')
    triangle_numbers = set([i * (i + 1) // 2 for i in range(100 * 100)])

    count = sum(value in triangle_numbers
                for value in map(word_letter_position_sum, words))

    print(count)


if __name__ == "__main__":
    main()
