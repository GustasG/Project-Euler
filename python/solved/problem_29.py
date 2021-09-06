from typing import Any, Generator


def generate_terms(a_upper: int, b_upper: int) -> Generator[int, Any, None]:
    for a in range(2, a_upper + 1):
        for b in range(2, b_upper + 1):
            yield a ** b


def main() -> None:
    total = len(set(generate_terms(100, 100)))

    print(total)


if __name__ == "__main__":
    main()
