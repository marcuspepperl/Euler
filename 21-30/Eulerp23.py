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


def is_abundant(num):

    prime_dict = prime_factorization(num)

    sum_of_divisors = 1

    for power in prime_dict.keys():
        sum_of_powers = 0
        max_exponent = prime_dict[power]
        for exponent in range(max_exponent + 1):
            sum_of_powers += power ** exponent

        sum_of_divisors *= sum_of_powers

    sum_of_divisors -= num

    return sum_of_divisors > num


def not_sum_abundant(num, abundant_below_num):

    half_num = num // 2
    sum_abundant_flag = False
    for lower_abundant in range(1, half_num + 1):
        if lower_abundant in abundant_below_num and num - lower_abundant in abundant_below_num:
            sum_abundant_flag = True
            break

    return not sum_abundant_flag

def problem_solver():

    MAX_POS_NUM = 28123

    abundant_below_max = set()
    for num in range(1, MAX_POS_NUM):
        if is_abundant(num):
            abundant_below_max.add(num)

    sum_not_sum_abundant = 0
    for num in range(1, MAX_POS_NUM):
        if not_sum_abundant(num, abundant_below_max):
            sum_not_sum_abundant += num

    print('The answer is: ', sum_not_sum_abundant)


    return

problem_solver()
# print(not_sum_abundant(1))
