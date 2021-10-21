def calculate_triangles(max_p: int) -> int:
    max_value = -1
    max_p_val = -1

    for p in range(12, max_p + 1, 2):
        current_value = sum((p*p - 2*a*p) % (2*p - 2*a) == 0
                            for a in range(2, p // 3))

        if current_value > max_value:
            max_value = current_value
            max_p_val = p

    return max_p_val


if __name__ == '__main__':
    m = calculate_triangles(1000)

    print(m)
