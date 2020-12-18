def is_pandigital(str_1):
    return len(str_1) == 9 and set(str_1) == {str(digit) for digit in range(1, 10)}

def test_pandigital_products(num):
    digits = len(str(num))
    if not 1 < digits <= 4:
        return 0
    if digits == 4:
        multiply_num = 2
    elif digits == 3:
        multiply_num = 3
    else:
        multiply_num = 4

    product_str = ''
    for multiplier in range(1, multiply_num + 1):
        product_str += str(num * multiplier)

    if is_pandigital(product_str):
        return int(product_str)

    return 0


def largest_pandigital_products(max_num):
    greatest_pandigital_product = 0
    count = 1
    num = 1
    while num < max_num:
        pandigital_product = test_pandigital_products(num)
        if pandigital_product > greatest_pandigital_product:
            print('Product:', pandigital_product, 'Count:', count)
            greatest_pandigital_product = pandigital_product
        count += 1
        num += 1
    print('The largest pandigital product is', greatest_pandigital_product)

    return

largest_pandigital_products(100000)
# print(is_pandigital('983721456'))
# print(test_pandigital_products(192))
