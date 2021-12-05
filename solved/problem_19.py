from datetime import date


def is_saturday(year: int, month: int, day: int) -> bool:
    return date(year, month, day).weekday() == 6


def sunday_count(year_begin: int, year_end: int) -> int:
    return sum(is_saturday(year, month, 1)
               for month in range(1, 13)
               for year in range(year_begin, year_end + 1))


def main() -> None:
    c = sunday_count(1901, 2000)

    print(c)


if __name__ == '__main__':
    main()
