def isPandigital(number):
    temp_number = str(number)

    for i in range(1, len(temp_number) + 1):
        if str(i) not in temp_number:
            return False

    return True


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



primes = set(sieveOfSundaram(10 ** 7))

for i in range(10 ** 6, 10 ** 7):
    if i in primes and isPandigital(i):
        biggest = i



print("Biggest:", biggest)



