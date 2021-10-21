def is_pandigital(first: int, second: int, third: int) -> bool:
    final_val = str(first) + str(second) + str(third)

    return ''.join(sorted(final_val)) == '123456789'


def find_pandigital_numbers() -> int:
    products = []

    for i in range(2, 100):
        for j in range(1234 if i <= 9 else 123, 10000//i + 1):
            product = i * j

            if is_pandigital(i, j, product):
                print(f'{i} * {j} = {product}')
                products.append(product)

    return sum(set(products))


if __name__ == "__main__":
    print(find_pandigital_numbers())
