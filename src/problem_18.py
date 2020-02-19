#!/usr/bin/python3

def read_file(file_name: str):
    numbers = []

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip() # Remove newline

            # Remove all empty str values
            line_values = line.split(' ')
            while '' in line_values:
                line_values.remove('')

            # Convert str to int and add to list
            line_numbers = [int(x) for x in line_values]
            numbers.append(line_numbers)

    return numbers


def max_path(numbers: list):
    # Begin at the end of pyramid and go up
    for index in range(len(numbers) - 2, -1, -1):
        for lenght in range(len(numbers[index])):
            numbers[index][lenght] = numbers[index][lenght] + max(numbers[index + 1][lenght], numbers[index + 1][lenght + 1])

    return numbers[0][0]


def main():
    numbers = read_file('problem_18_numbers.txt')
    print(max_path(numbers))



if __name__ == "__main__":
    main()