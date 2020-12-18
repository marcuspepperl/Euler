import math


def is_pandigital(multiplier1, multiplier2, product, digit_set):

    return len(str(multiplier1)) + len(str(multiplier2)) + len(str(product)) == 9 and set(list(str(multiplier1))).union(set(list(str(multiplier2))), set(list(str(product)))) == digit_set




def pandigital_products():

    pandigital_products = set()
    digits_set = {str(digit) for digit in range(1, 10)}
    multiplier1_range = {num for num in range(10, 100) if num % 10}
    for num1 in multiplier1_range:
        multiplier2_range = [val for val in range(max(num1 + 1, math.ceil(1000 / num1)), math.floor(10000 / num1) + 1) if len(str(val)) == 3 and val % 10]
        for num2 in multiplier2_range:
            if is_pandigital(num1, num2, num1 * num2, digits_set):
                pandigital_products.add(tuple([num1, num2, num1 * num2]))



    return pandigital_products



def run():
    solution_set = pandigital_products()
    print(solution_set)

    return


run()
