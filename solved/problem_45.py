from shared.numeric import is_pentagonal


if __name__ == "__main__":
    i = 144

    while True:
        i += 1
        current_hexagonal = 2*i*i - i

        if is_pentagonal(current_hexagonal):
            print(current_hexagonal)
            break
