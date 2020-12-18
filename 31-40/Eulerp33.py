import math


def prime_factorization(num):

    least_possible_divisor = 2
    prime_dict = {}
    while num != 1:
        while num % least_possible_divisor == 0:
            prime_dict[least_possible_divisor] = prime_dict.get(least_possible_divisor, 0) + 1
            num = num / least_possible_divisor

        if least_possible_divisor % 2 == 1:
            least_possible_divisor += 2
        else:
            least_possible_divisor += 1

    return prime_dict


def common_factors(num1, num2):

    prime_dict_1 = prime_factorization(num1)
    prime_dict_2 = prime_factorization(num2)
    common_factors = {}
    for key in set(prime_dict_1.keys()).intersection(set(prime_dict_2.keys())):
        min_power = min(prime_dict_1.get(key, 0), prime_dict_2.get(key, 0))
        common_factors[key] = min_power

    return common_factors

def least_common_terms(fraction_num, fraction_denom):

    greatest_factor = max(generate_all_multiples(common_factors(fraction_num, fraction_denom)))

    result_num = fraction_num // greatest_factor
    result_denom = fraction_denom // greatest_factor


    return result_num, result_denom


def generate_all_multiples(factor_dict):

    full_powers_lst = []
    length_lst = []

    for power in sorted(factor_dict.keys()):

        exponents = factor_dict[power]
        powers_lst = []

        for exponent in range(exponents + 1):
            powers_lst.append(power ** exponent)

        full_powers_lst.append(tuple(powers_lst))

        length_lst.append(exponents + 1)

    permutations = 1
    for length in length_lst:
        permutations *= length

    all_multiples = []

    for n in range(1, permutations + 1):
        multiple = 1
        num = n
        remaining_permutations = permutations
        for index in range(len(full_powers_lst)):

            num_powers = len(full_powers_lst[index])
            selected_power_order = math.ceil(num / remaining_permutations * num_powers)

            multiple *= full_powers_lst[index][selected_power_order - 1]
            remaining_permutations = remaining_permutations / num_powers
            num -= remaining_permutations * selected_power_order

        all_multiples.append(multiple)

    return all_multiples


def multiply_fractions(fraction_lst):

    product_numerator = 1
    product_denominator = 1
    print(product_denominator)

    for fraction in fraction_lst:
        product_numerator *= fraction[0]
        product_denominator *= fraction[1]

    return product_numerator, product_denominator


def create_one_shared_digit(digit1, digit2):

    numb = 10 * digit1 + digit2
    set1 = {digit1 * 10 + i for i in range(1, 10) if digit1 * 10 + i > numb}
    set2 = {digit2 * 10 + i for i in range(1, 10) if digit2 * 10 + i > numb}
    set3 = {j * 10 + digit1 for j in range(1, 10) if j * 10 + digit1 > numb}
    set4 = {j * 10 + digit2 for j in range(1, 10) if j * 10 + digit2 > numb}
    numb_set = set1.union(set2, set3, set4)
    if 10 * digit1 + digit2 in numb_set:
        numb_set.remove(10 * digit1 + digit2)
    if 10 * digit2 + digit1 in numb_set:
        numb_set.remove(10 * digit2 + digit1)

    return numb_set

def remove_common_digit(num1, num2):

    if len(str(num1)) != 2 or len(str(num2)) != 2:
        return 0
    digits_lst_1 = list(str(num1))
    digits_lst_2 = list(str(num2))
    digits_set_1 = set(str(num1))
    digits_set_2 = set(str(num2))


    same_digit = list(digits_set_1.intersection(digits_set_2))

    digits_lst_1.remove(same_digit[0])
    digits_lst_2.remove(same_digit[0])
    return int(digits_lst_1[0]), int(digits_lst_2[0])





def curious_fractions():

    curious_fractions_lst = []
    pos_numerator = [num1 for num1 in range(10, 100) if num1 % 10]

    for numerator in pos_numerator:

        digits_lst = list(str(numerator))
        tens_digit = int(digits_lst[0])
        ones_digit = int(digits_lst[1])

        pos_denominator = create_one_shared_digit(tens_digit, ones_digit)


        for denominator in pos_denominator:
            common_factors_dict = common_factors(numerator, denominator)
            if common_factors_dict == dict():
                continue
            common_multiples_lst = generate_all_multiples(common_factors_dict)
            removed_digit_tuple = remove_common_digit(numerator, denominator)


            for multiple in common_multiples_lst:

                numerator_divided = numerator // multiple
                denominator_divided = denominator // multiple

                if tuple([numerator_divided, denominator_divided]) == removed_digit_tuple:
                    curious_fractions_lst.append(tuple([numerator, denominator]) + removed_digit_tuple)


                alternative_range = list(range(2, math.floor(10 / denominator_divided) + 1))

                for additional_multiple in alternative_range:

                    alternative_numerator = numerator_divided * additional_multiple
                    alternative_denominator = denominator_divided * additional_multiple

                    if tuple([alternative_numerator, alternative_denominator]) == removed_digit_tuple:
                        curious_fractions_lst.append(tuple([numerator, denominator]) + removed_digit_tuple)





    return curious_fractions_lst


def curious_fractions_check(curious_fractions_lst):
    print('\nCheck:')
    for fraction in curious_fractions_lst:
        print(fraction[0], '/', fraction[1], '=', fraction[2], '/', fraction[3], fraction[0] / fraction[1] == fraction[2] / fraction[3])

    return

def run():


    curious_fractions_lst = curious_fractions()
    print('\nThe list of curious fractions:')
    print(curious_fractions_lst)

    curious_fractions_check(curious_fractions_lst)
    stripped_curious_fractions = []

    for elem in curious_fractions_lst:
        stripped_curious_fractions.append(elem[:2])


    product = multiply_fractions(stripped_curious_fractions)

    answer = least_common_terms(int(product[0]), int(product[1]))

    print('\nThe answer is:', answer[1])


    return


run()
