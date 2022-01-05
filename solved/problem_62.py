from dataclasses import dataclass

from shared.generators import infinite_range
from shared.numeric import largest_permutation


@dataclass
class Permutation:
    number: int
    permutations: int = 1


def cubic_permutations(target: int) -> int:
    cubes = dict()

    for i in infinite_range(1):
        permutation = largest_permutation(i ** 3)

        if permutation not in cubes:
            cubes[permutation] = Permutation(i)
        else:
            cubes[permutation].permutations += 1

        if cubes[permutation].permutations == target:
            return cubes[permutation].number


def main() -> None:
    number = cubic_permutations(5)

    print(number ** 3)


if __name__ == '__main__':
    main()
