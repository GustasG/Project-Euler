from shared.generators import number_digits


def main() -> None:
    values = []

    for base in range(2, 100):
        number = base
        
        for exponent in range(100):
            number *= base
            
            if sum(number_digits(number)) == base:
                values.append(number)

    values.sort()

    for i in range(len(values)):
        print(f'a[{i + 1}] = {values[i]}')


if __name__ == "__main__":
    main()
