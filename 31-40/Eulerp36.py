import math

def generate_two_palindromes(num):

    num_str_1 = str(num)
    num_str_2 = num_str_1[::-1]

    return int(num_str_2[:-1] + num_str_1), int(num_str_2 + num_str_1)


def convert_to_binary(num):

    rev_binary_str = ''
    while num != 0:
        remainder = num % 2
        rev_binary_str += str(remainder)
        num = (num - remainder) // 2

    return rev_binary_str

def is_palindrome(num_str):

    return num_str == num_str[::-1]


# print(generate_two_palindromes(12))
# print(convert_to_binary(10))
# print(is_palindrome('10'))


def sum_double_palindromes(n):

    n -= 1
    total = 0
    max_power = math.floor(math.log10(n))
    if max_power % 2 == 0:
        max_iter_power = (max_power + 2)// 2
    else:
        max_iter_power = (max_power + 1) // 2

    print('Max Iteration Number:', 10 ** max_iter_power - 1)
    for val in range(1, 10 ** max_iter_power, 2):

        num1, num2 = generate_two_palindromes(val)
        if is_palindrome(convert_to_binary(num1)) and num1 <= n:
            print(num1, convert_to_binary(num1), math.floor(math.log10(num1)))
            total += num1

        if is_palindrome(convert_to_binary(num2)) and num2 <= n and num2 != num1:
            print(num2, convert_to_binary(num2), math.floor(math.log10(num2)))
            total += num2

    return total




print('Total:', sum_double_palindromes(10000000000000))
