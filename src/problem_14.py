def chain(number):
    if number == 1:
        return 1

    if number % 2 == 0:
        return 1 + chain(number // 2)
    else:
        return 1 + chain(3 * number + 1)


def collatz_sequence(upper_bound):
    longest = -1

    for i in range(upper_bound // 2, upper_bound):
        current_long = chain(i)

        if current_long > longest:
            number = i
            longest = current_long

    return number


print(collatz_sequence(10**6))