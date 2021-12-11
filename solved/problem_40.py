def main() -> None:
    if __name__ == "__main__":
        champernownes_constant = ''.join(str(x) for x in range(1, 1_000_000 + 1))

        ans = int(champernownes_constant[1 - 1])
        ans *= int(champernownes_constant[10 - 1])
        ans *= int(champernownes_constant[100 - 1])
        ans *= int(champernownes_constant[1_000 - 1])
        ans *= int(champernownes_constant[10_000 - 1])
        ans *= int(champernownes_constant[100_000 - 1])
        ans *= int(champernownes_constant[1_000_000 - 1])

        print(ans)


if __name__ == '__main__':
    main()
