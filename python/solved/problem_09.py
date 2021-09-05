def get_multip(s: int) -> int:
    for a in range(1, s):
        for b in range(a, s):
            if 2*a*b + s**2 == 2*s*(a + b):
                return a * b * (s - a - b)


if __name__ == "__main__":
    m = get_multip(1000)

    print(m)
