import math

def sieveOfSundaram(n):
    values = []

    nNew = (n - 2) // 2
  
    marked = [0] * (nNew + 1)
    for i in range(1, nNew + 1): 
        j = i; 
        while i + j + 2 * i * j <= nNew: 
            marked[i + j + 2 * i * j] = 1
            j += 1
  
    if (n > 2):
        values.append(2)
  
    for i in range(1, nNew + 1): 
        if (marked[i] == 0):
            values.append(2 * i + 1)


    return values


def isPrime(number_to_check):
    if number_to_check == 1:
        return False
    elif number_to_check < 4:
        return True
    elif number_to_check % 2 == 0:
        return False
    elif number_to_check < 9:
        return True
    elif number_to_check % 3 == 0:
        return False
    else:
        bound = round(math.sqrt(number_to_check))
        f = 5
        while f <= bound:
            if number_to_check % f == 0:
                return False
            elif number_to_check % (f + 2)  == 0:
                return False
            f += 6
        return True


def rotate(value):
    temp_val = str(value)

    if ("0" or "2" or "4" or "5" or "6" or "8") in temp_val:
        return False

    test_val = temp_val
    for i in range(0, len(temp_val) - 1):
        test_val = test_val[1:] + test_val[0]

        if isPrime(int(test_val)) == False:
            return False

    return True


def calculateCircularPrimes(N):
    all_primes = sieveOfSundaram(N)

    circular_primes = []

    for prime in all_primes:
        if rotate(prime):
            circular_primes.append(prime)


    return len(circular_primes)


print(calculateCircularPrimes(10 ** 6))