from dataclasses import dataclass
import math
from typing import Iterator

import numpy as np

from shared.paths import RESOURCE_DIR


@dataclass(frozen=True)
class Number:
    base: int
    exponent: int

    def __eq__(self, other):
        return self.exponent * math.log(self.base) == other.exponent * math.log(other.base)

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        return self.exponent * math.log(self.base) < other.exponent * math.log(other.base)

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)


def read_file(path) -> Iterator[Number]:
    with open(path, 'r') as f:
        for line in f:
            yield Number(*map(int, line.split(',')))


def main():
    numbers = list(read_file(RESOURCE_DIR / 'problem_99_numbers.txt'))
    print(np.argmax(numbers) + 1)


if __name__ == "__main__":
    main()
