import itertools


DIVISORS = [2, 3, 5, 7, 11, 13, 17]


def calculate_divisibility(number: str) -> bool:
	for i, divisor in enumerate(DIVISORS):
		if int(number[i + 1:i + 4]) % divisor != 0:
			return False
	return True


def main() -> None:
	s = 0

	for value in itertools.permutations('0123456789'):
		current_number = ''.join(str(i) for i in value)

		if not current_number.startswith('0') and calculate_divisibility(current_number):
			s += int(current_number)

	print(s)


if __name__ == "__main__":
	main()
