def n_th_digit_fib_number(digit_number: int) -> int:
    previous_number = 1
    current_number = 1
    current_term = 2

    while len(str(current_number)) < digit_number:
        previous_number, current_number = current_number, current_number + previous_number
        current_term += 1

    return current_term

print(n_th_digit_fib_number(1000))