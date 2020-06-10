import math

def digit_sum(number: int) -> int:
    return sum(map(int, str(number)))

def main():
    s = digit_sum(math.factorial(100))
    print(s)


if __name__ == "__main__":
    main()
