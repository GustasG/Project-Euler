import pyprimes


def findPanaitopolPrimesSum(upper_bound):
    total = 0

    for n in range(1, upper_bound):
        p = n ** 2 + (n + 1) ** 2

        if p >= upper_bound:
            break

        if pyprimes.isprime(p):
            total += 1

    return total


print("total sum:", findPanaitopolPrimesSum(5 * (10 ** 15)))