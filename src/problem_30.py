#!/usr/bin/python3

def getDigits(number: int) -> list:
    return map(int, str(number))


def calculateDigitPowers(power: int) -> int:
    total = 0
    
    bound = (power + 1) * 9 ** power
    for i in range(2, bound):
        if sum(digit ** power for digit in getDigits(i)) == i:
            total += i

    return total


print('Total sum: {0}'.format(calculateDigitPowers(5)))