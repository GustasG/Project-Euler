#!/usr/bin/python3

def main():
    champernownes_constant = ''.join(str(x) for x in range(1, 1000000 + 1))

    ans = int(champernownes_constant[1 - 1])
    ans *= int(champernownes_constant[10 - 1])
    ans *= int(champernownes_constant[100 - 1])
    ans *= int(champernownes_constant[1000 - 1])
    ans *= int(champernownes_constant[10000 - 1])
    ans *= int(champernownes_constant[100000 - 1])
    ans *= int(champernownes_constant[1000000 - 1])

    print(ans)


if __name__ == "__main__":
    main()