from typing import Set


def generate_terms(a_upper: int, b_upper: int) -> Set[int]:
    values = [a ** b for a in range(2, a_upper + 1) for b in range(2, b_upper + 1)]
    return set(values)


if __name__ == "__main__":
    total = len(generate_terms(100, 100))

    print(total)
