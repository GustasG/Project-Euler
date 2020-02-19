def isPolindromic(number):
    new_number = str(number)

    for i in range(0, len(new_number) // 2):
        if new_number[i] != new_number[len(new_number) - i - 1]:
            return False

    return True


def findPolyndromic(N):
    sum = 0

    for i in range(1, N):
        if isPolindromic(i) and isPolindromic(bin(i)[2:]):
            sum += i

    return sum



print(findPolyndromic(10 ** 6))


