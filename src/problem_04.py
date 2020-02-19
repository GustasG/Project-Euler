def is_polindrome(number):
    temp = number
    new_number = 0

    while temp > 0:
        last_digit = temp % 10
        new_number = new_number * 10 + last_digit
        temp = temp // 10

    return new_number == number

def number_iteration(digit_count):
    biggest_number = -1

    for i in range(10 ** (digit_count - 1), 10 ** digit_count):
        for j in range(10 ** (digit_count - 1), 10 ** digit_count):
            current_number = i * j
            if is_polindrome(current_number) and (current_number) > biggest_number:
                biggest_number = current_number

    return biggest_number

print(number_iteration(3))