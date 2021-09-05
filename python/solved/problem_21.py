def sum_divisors(number: int) -> int:
    return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)


def sum_amicable_numbers(upper_bound: int) -> int:
    s = 0

    for i in range(1, upper_bound):
        number1 = sum_divisors(i)
        number2 = sum_divisors(number1)

        if number2 == i and number1 != i:
            s += number1

    return s


if __name__ == '__main__':
    n = sum_amicable_numbers(10000)

    print(n)
