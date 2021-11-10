from numba import njit


@njit()
def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        f = 5
        while f <= round(number ** 0.5):
            if number % f == 0:
                return False
            elif number % (f + 2) == 0:
                return False
            f += 6
        return True
