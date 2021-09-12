def spiral_diagonal_sum(size: int) -> int:
    return sum(4 * (2*n + 1)**2 - 12*n
               for n in range(1, size//2 + 1)) + 1


if __name__ == "__main__":
    print(spiral_diagonal_sum(1001))
