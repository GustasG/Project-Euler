def get_multip(sum: int) -> int:
    for a in range(1, sum):
        for b in range(a, sum):
            if 2*a*b + sum**2 == 2*sum*(a + b):
                return a * b * (sum - a - b)


def main():
    print(get_multip(1000))

if __name__ == "__main__":
    main()