def main() -> None:
    s = sum(2*a*((a-1)//2)
            for a in range(3, 1000 + 1))

    print(s)


if __name__ == "__main__":
    main()
