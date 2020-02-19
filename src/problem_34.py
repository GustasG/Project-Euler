from math import factorial

def getDigits(number: int) -> list:
    return map(int, str(number))


def calculateDigitFactorials():
    total = 0

    for i in range(3, sum(factorial(i) for i in range(10))):
        digits = getDigits(i)

        if sum(factorial(x) for x in digits) == i:
            total += i

    return total


print('Total sum: {0}'.format(calculateDigitFactorials()))