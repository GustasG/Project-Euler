#!/usr/bin/python3

def main():
	exponent = 10**10
	total = sum(pow(i, i, exponent) for i in range(1, 1000 + 1)) % exponent

	print(f'Last 10 digits: {total}')


if __name__ == "__main__":
	main()