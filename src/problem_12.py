import math

def divisor_counter(number: int) -> int:
    sum = 0

    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            if number // i == i:
                sum += 1
            else:
                sum += 2

    return sum

def triangular_number(divisor_number):
    triangle_number = 0
    sum = 0

    while True:
        sum += triangle_number

        if divisor_counter(sum) >= divisor_number:
            return sum
        else:
            triangle_number += 1


print(triangular_number(500))