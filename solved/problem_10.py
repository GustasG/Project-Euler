from shared.generators import prime_generator


if __name__ == "__main__":
    s = sum(prime_generator(2 * 10**6))

    print(s)
