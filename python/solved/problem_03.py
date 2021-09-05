from shared.generators import factorization


if __name__ == "__main__":
    number = 600851475143
    prime = max(factorization(number))

    print(prime)
