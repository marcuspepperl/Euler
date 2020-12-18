import itertools
import math

def is_prime(n):
    if n == 2:
        return True
    elif not n % 2:
        return False
    for factor in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if not n % factor:
            return False
    return True



def set_all_primes_below(n):
    if n < 2:
        return set()
    prime_set = {2}
    for pos_prime in range(3, n + 1, 2):
        if is_prime(pos_prime):
            prime_set.add(pos_prime)
    return prime_set

def construct_num(fixed_digits, digit_values, other_digits, final_digit, num_digits):
    digit_lst = [other_digits] * num_digits
    for digit_pos, digit_val in zip(fixed_digits, digit_values):
        digit_lst[digit_pos] = digit_val
    digit_lst[-1] = final_digit
    return int(''.join(map(str, digit_lst)))


def eight_prime_family_search(num_digits):
    prime_set = set_all_primes_below(10 ** num_digits)
    final_digit_set = {1, 3, 7, 9}
    for fixed_digits in itertools.combinations(range(num_digits - 1), num_digits - 4):
        if not sum(fixed_digits) % 3:
            continue
        for digit_values in itertools.permutations(range(10), num_digits - 4):
            if 0 in fixed_digits and digit_values[0] == 0:
                continue
            for final_digit in final_digit_set:
                if 0 not in fixed_digits:
                    other_digits = 1
                else:
                    other_digits = 0
                prime_count = 0
                prime_lst = []
                while prime_count + 10 - other_digits >= 8:
                    num = construct_num(fixed_digits, digit_values, other_digits, final_digit, num_digits)
                    if is_prime(num):
                        if prime_count == 0:
                            lowest_prime = num
                        prime_count += 1
                        prime_lst.append(num)
                    other_digits += 1
                if prime_count == 8:

                    print('Success:', lowest_prime)
                    print(prime_lst)
                    return
    return


def run():
    eight_prime_family_search(6)

run()
