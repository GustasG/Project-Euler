from math import log
from typing import List
from dataclasses import dataclass

from shared.paths import RESOURCE_DIR


@dataclass
class Number:
    line: int
    base: int
    exponent: int

    def __eq__(self, other):
        return self.exponent * log(self.base) == other.exponent * log(other.base)

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        return self.exponent * log(self.base) < other.exponent * log(other.base)

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)


def read_file(path) -> List[Number]:
    with open(path, 'r') as f:
        return [Number(i + 1, *map(int, line.split(',')))
                for i, line in enumerate(f)]


def main():
    numbers = read_file(RESOURCE_DIR / 'problem_99_numbers.txt')
    biggest = max(numbers)

    print(biggest.line)


if __name__ == "__main__":
    main()
