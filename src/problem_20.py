import math

def factorial_digit_sum(n):
    factorial = math.factorial(n)
    sum = 0
    
    while factorial > 0:
        sum += factorial % 10
        factorial = factorial // 10

    return sum


print(factorial_digit_sum(100))