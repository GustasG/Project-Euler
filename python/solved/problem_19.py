from datetime import date


def sunday_count(year_begin: int, year_end: int) -> int:
    return sum(date(year, month, 1).weekday() == 6
               for year in range(year_begin, year_end + 1)
               for month in range(1, 13))


if __name__ == '__main__':
    c = sunday_count(1901, 2000)

    print(c)
