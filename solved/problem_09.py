from typing import Optional


def calculate_multiple(s: int) -> Optional[int]:
    for a in range(1, s):
        for b in range(a, s):
            if 2 * a * b + s**2 == 2 * s * (a + b):
                return a * b * (s - a - b)


def main() -> None:
    m = calculate_multiple(1000)

    print(m)


if __name__ == "__main__":
    main()
