def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))


def main():
    values = []

    for base in range(2, 100):
        for exponent in range(2, 100):
            number = base ** exponent
            
            if sum_digits(number) == base:
                values.append(number)


    values.sort()

    for i in range(len(values)):
        print(f'a[{i + 1}] = {values[i]}')


if __name__ == "__main__":
    main()