#!/usr/bin/python3

from math import sqrt

def is_pentagonal(x: int) -> bool:
    n = (1 + sqrt(1 + 24*x)) / 6

    return n.is_integer()


def main():
    i = 144
    
    while True:
        i += 1
        current_hexagonal = 2*i*i - i

        if is_pentagonal(current_hexagonal):
            print(current_hexagonal)
            break
            
        

if __name__ == "__main__":
    main()