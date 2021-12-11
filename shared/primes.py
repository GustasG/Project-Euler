from math import sqrt

from numba import njit


@njit(fastmath=True)
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
        for i in range(5, int(sqrt(number)) + 1, 6):
            if number % i == 0:
                return False
            elif number % (i + 2) == 0:
                return False
        return True
