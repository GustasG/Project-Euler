from shared.generators import factorization


def main():
    number = 600851475143
    prime = max(factorization(number))

    print(prime)


if __name__ == "__main__":
    main()
