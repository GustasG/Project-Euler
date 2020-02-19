#!/usr/bin/python3

def is_pandigital(first_number: int, second_number: int, third_number: int) -> bool:
    final_val = str(first_number) + str(second_number) + str(third_number)

    return ''.join(sorted(final_val)) == '123456789'


def find_pandigital_numbers() -> int:
    products = set()

    for i in range(2, 100):
        j_begin = 123
        if i <= 9:
            j_begin = 1234

        for j in range(j_begin, 10000//i + 1):
            product = i * j

            if is_pandigital(i, j, product):
                print(f'{i} * {j} = {product}')
                products.add(product)

    return sum(products)




if __name__ == "__main__":
    print('Result sum: {0}'.format(find_pandigital_numbers()))