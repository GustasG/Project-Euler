import math

class Number:
    def __init__(self, line: int, base: int, exponent: int):
        self.line = line
        self.base = base
        self.exponent = exponent

    def __eq__(self, other):
        return self.base == other.base and self.exponent == other.exponent

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        return self.exponent * math.log(self.base) < other.exponent * math.log(other.base)

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)


def parse_file(file_name: str) -> list:
    file_data = open(file_name, 'r').read().split('\n')

    numbers = []

    for i in range(len(file_data)):
        line = file_data[i]
        values = line.split(',')

        numbers.append(Number(i + 1, int(values[0]), int(values[1])))

    return numbers


def find_biggest(file_name: str) -> int:
    numbers = parse_file(file_name)
    biggest = max(numbers)
    
    return biggest.line



def main():
    file_name = 'problem_99_numbers.txt'

    print(find_biggest(file_name))
    


if __name__ == "__main__":
    main()