#!/usr/bin/python3

import time

def get_number_divisors(number):
    return [x for x in range(1, (number//2) + 1) if number%x == 0]


def divisors_sum(number):
    return sum(get_number_divisors(number))


def get_abundant_numbers(upper_limit):
    return [x for x in range(1, upper_limit) if divisors_sum(x) > x]


def binary_search(collection, item):
    first = 0
    last = len(collection) - 1
    found = False

    while first <= last and not found:
        mid = (first + last)//2

        if collection[mid] == item:
    	    found = True
        else:
    	    if item < collection[mid]:
    	        last = mid - 1
    	    else:
                first = mid + 1

    return found

# abundant numbers has to be sorted
def can_express_in_abundant_sum(abundant_numbers, number):
    for num1 in abundant_numbers:
        num2 = number - num1

        if binary_search(abundant_numbers, num2):
            return True

        if num1 > number:
            return False
        
    return False


def main():
    upper_limit = 28123

    abundant_numbers = get_abundant_numbers(upper_limit)
    
    sum = 0
    for i in range(1, upper_limit):
        if can_express_in_abundant_sum(abundant_numbers, i) is False:
            sum += i
    
    print(sum)


if __name__ == "__main__":
    start = time.time()

    main()

    end = time.time()

    print('Elapsed time: {0}sec'.format(end - start))