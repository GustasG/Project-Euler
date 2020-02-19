#!/usr/bin/python3

def find_cycle_length(number):
    last_pos = [0 for i in range(number)]

    position = 1
    divident = 1

    while True:
        remainder = divident % number

        if remainder == 0:
            return 0

        if last_pos[remainder] != 0:
            return position - last_pos[remainder]

        last_pos[remainder] = position

        position += 1
        divident = remainder * 10

def main():
    number = 1
    longest = -1

    for i in range(1, 1000):
        current_number_length = find_cycle_length(i)

        if current_number_length > longest:
            number = i
            longest = current_number_length

    print(number)


if __name__ == "__main__":
    main()