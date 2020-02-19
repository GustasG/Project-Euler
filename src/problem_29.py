def generate_terms(a_upper, b_upper):
    values = [a ** b for a in range(2, a_upper + 1) for b in range(2, b_upper + 1)]
    return set(values)

def main():
    terms = generate_terms(100, 100)

    print('Total number: {0}'.format(len(terms)))

if __name__ == "__main__":
    main()