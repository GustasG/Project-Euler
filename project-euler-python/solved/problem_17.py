def getNumericVal(number):
    if number == 1:
        return 3

    elif number == 2:
        return 3

    elif number == 3:
        return 5

    elif number == 4:
        return 4

    elif number == 5:
        return 4

    elif number == 6:
        return 3

    elif number == 7:
        return 5

    elif number == 8:
        return 5

    elif number == 9:
        return 4

def lessThan20(number):
    if number < 10:
        return getNumericVal(number)

    if number == 10:
        return 3

    elif number == 11:
        return 6

    elif number == 12:
        return 6

    elif number == 13:
        return 8

    elif number == 14:
        return 8

    elif number == 15:
        return 7

    elif number == 16:
        return 7

    elif number == 17:
        return 9

    elif number == 18:
        return 8

    elif number == 19:
        return 8

def lessThan100(number):
    if number < 20:
        return lessThan20(number)


    value1 = number % 10
    value2 = number // 10

    if value2 == 2:
        if value1 == 0:
            return 6
        else:
            return 6 + getNumericVal(value1)

    elif value2 == 3:
        if value1 == 0:
            return 6
        else:
            return 6 + getNumericVal(value1)

    elif value2 == 4:
        if value1 == 0:
            return 5
        else:
            return 5 + getNumericVal(value1)

    elif value2 == 5:
        if value1 == 0:
            return 5
        else:
            return 5 + getNumericVal(value1)

    elif value2 == 6:
        if value1 == 0:
            return 5
        else:
            return 5 + getNumericVal(value1)

    elif value2 == 7:
        if value1 == 0:
            return 7
        else:
            return 7 + getNumericVal(value1)

    elif value2 == 8:
        if value1 == 0:
            return 6
        else:
            return 6 + getNumericVal(value1)

    elif value2 == 9:
        if value1 == 0:
            return 6
        else:
            return 6 + getNumericVal(value1)

def lessThan1000(number):
    temp = number

    value1 = temp % 10
    temp = temp // 10

    value2 = temp % 10
    temp = temp // 10

    value3 = temp

    if value1 == 0 and value2 == 0:
        return getNumericVal(value3) + 7
    else:
        return getNumericVal(value3) + 7 + 3 + lessThan100(10 * value2 + value1)

def countLetters(max_val):
    count = 0

    for i in range(1, max_val + 1):
        if i <= 9:
            count += getNumericVal(i)
        elif i < 100:
            count += lessThan100(i)
        elif i < 1000:
            count += lessThan1000(i)
        elif i == 1000:
            count += 11

    return count


print(countLetters(1000))