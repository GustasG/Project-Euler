#!/usr/bin/python3

import itertools

divisors = [2, 3, 5, 7, 11, 13, 17]

def calculateDivisibility(number):
	for i in range(len(divisors)):
		if int(number[1 + i: 4 + i]) % divisors[i] != 0:
			return False

	return True

def main():
	sum = 0

	for value in itertools.permutations('0123456789'):
		if value[0] == '0':
			continue

		current_number = ''.join(str(i) for i in value)

		if calculateDivisibility(current_number):
			sum += int(current_number)

	print('Total sum: {0}'.format(sum))



if __name__ == "__main__":
	main()
