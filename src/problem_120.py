#!/usr/bin/python3


def main():
    r_max = lambda a: 2*a*((a-1)//2)

    print(sum(r_max(a) for a in range(3, 1000 + 1)))


if __name__ == "__main__":
    main()