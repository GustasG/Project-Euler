def squares_sum(number: int) -> int:
    return number * (number+1) * (2*number + 1) // 6

def sum_sqared(number: int) -> int:
    return ((1 + number) * number // 2) ** 2

def sqare_difference(number: int) -> int:
    return sum_sqared(number) - squares_sum(number)

def main():
    print(sqare_difference(100))

if __name__ == "__main__":
    main()
