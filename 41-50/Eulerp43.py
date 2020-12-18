import math
from itertools import permutations


def digits_strip(n, length):
    return (length - len(str(n))) * [0] + [int(digit) for digit in str(n)]


def rule_sort(divisibility_rules):
    sorted_rules = []

    rule_digits = {}
    for digits in divisibility_rules.keys():
        rule_digits[digits] = len(digits)

    for digit_count in sorted(list(set(rule_digits.values()))):
        digit_count_lst = []
        for digits, digit_num in rule_digits.items():
            if digit_num == digit_count:
                digit_count_lst.append(digits)
        sorted_rules.extend(sorted(digit_count_lst, key = divisibility_rules.get, reverse = True))

    return sorted_rules


def pandigital_divisibility(divisibility_rules):

    digits_set = {digit for digit in range(10)}

    free_set = digits_set.copy()
    for rule in divisibility_rules.keys():
        for digit in rule:
            if digit in free_set:
                free_set.remove(digit)
    free_set = list(free_set)

    satisfied_numbers = []

    sorted_rules = rule_sort(divisibility_rules)
    first_digits = sorted_rules[0]
    num_digits = len(first_digits)
    first_divisor = divisibility_rules[first_digits]

    for mul in range(math.floor(10 ** num_digits / first_divisor) + 1):
        multiple = digits_strip(first_divisor * mul, num_digits)
        if len(set(multiple)) == num_digits:
            number = [-1] * 10
            for ind in range(num_digits):
                number[first_digits[ind]] = multiple[ind]
            satisfied_numbers.append(number)

    rule_num = 1

    digits = tuple()
    divisor = 0
    num_digits = 0

    while satisfied_numbers != [] and rule_num < len(sorted_rules):

        new_satisfied_numbers = []
        digits = sorted_rules[rule_num]
        divisor = divisibility_rules[digits]
        num_digits = len(digits)
        new_digits = []

        for digit in digits:
            if satisfied_numbers[0][digit] == -1:
                new_digits.append(digit)

        for number in satisfied_numbers:

            remaining_digits = list(digits_set - set(number))

            for permutation in list(permutations(remaining_digits, len(new_digits))):

                pos_number = number.copy()
                for ind in range(len(new_digits)):
                    pos_number[new_digits[ind]] = permutation[ind]

                if sum([10 ** (len(digits) - 1 - digit[0]) * pos_number[digit[1]] for digit in enumerate(digits)]) % divisor == 0:
                    new_satisfied_numbers.append(pos_number)

        satisfied_numbers = new_satisfied_numbers
        rule_num += 1


    final_satisfied_numbers = []
    final_digits = []

    if free_set != set():
        for number in satisfied_numbers:

            remaining_digits = list(digits_set - set(number))
            free_permutations = permutations(remaining_digits)

            for permutation in free_permutations:
                new_number = number.copy()
                for ind in range(len(free_set)):
                    new_number[free_set[ind]] = permutation[ind]
                final_satisfied_numbers.append(new_number)

    special_numbers = []

    for num_lst in final_satisfied_numbers:
        num_str = ''
        for digit in num_lst:
            num_str += str(digit)
        special_numbers.append(int(num_str))

    return special_numbers

def writeup(rules, result):
    print('\nThe numbers must be pandigital containing exactly one digit from 0 - 9')
    print('in the form')
    print('d0 d1 d2 d3 d4 d5 d6 d7 d8 d9')
    print('\nThe rules are:')

    for digits in rule_sort(rules):
        for digit in digits:
            digit_str = 'd' + str(digit)
            print(digit_str, end = ' ')
        print('is divisible by', str(rules[digits]))

    print('\nThe numbers that satisfy these properties are')

    for num in result:
        print(num)

    print('\nThe sum of these numbers is')
    print(sum(result))
    return


def run():

    rules1 = {(2, 3, 4) : 10, (3, 4, 5) : 10, (4, 5, 6) : 7, (5, 6, 7) : 11, (6, 7, 8) : 13, (7, 8, 9) : 17}

    result1 = pandigital_divisibility(rules1)

    writeup(rules1, result1)


run()
