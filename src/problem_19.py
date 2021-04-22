#!/usr/bin/env python3

'''
Zeller's Rule:
0- Sunday
1- Monday
2- Tuesday
3- Wednesday
4- Thursday
5- Friday
6- Saturday 
'''
def dayOfWeek(year: int, month: int, day: int) -> int:
    if month == 1 or month == 2:
        return dayOfWeek(year - 1, month + 12, day)

    M = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    D = year % 100
    C = year // 100
    
    if month > 12:
        month_correction = M[month - 12]
    else:
        month_correction = M[month - 1]

    return (day + (13 * month_correction - 1)//5 + D +  D//4 + C//4 - 2*C) % 7



def findMondays(year_begin: int, year_end: int) -> int:
    sum = 0

    for year in range(year_begin, year_end + 1):
        for month in range(1, 13):
            if dayOfWeek(year, month, 1) == 0:
                sum += 1

    return sum


print(findMondays(1901, 2000))