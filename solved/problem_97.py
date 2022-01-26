def main() -> None:
    last_digits = 10**10

    num_mod = 28433 % last_digits
    two_mod = pow(2, 7830457, last_digits)
    one_mod = 1 % last_digits

    ans = (num_mod * two_mod) % last_digits + one_mod
    ans %= last_digits

    print(ans)


if __name__ == "__main__":
    main()
