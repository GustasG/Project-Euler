import math

def sum_divisors(number):
    sum = 0

    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            sum += i
    return sum


def sum_amicable_numbers(upper_bound):
    sum = 0

    for i in range(1, upper_bound):
        number1 = sum_divisors(i)
        number2 = sum_divisors(number1)

        if number2 == i and number1 != i:
            sum += number1

    return sum

print(sum_amicable_numbers(10000))