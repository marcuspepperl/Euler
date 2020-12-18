import math

def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False

    is_prime = True
    for factor in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if not num % factor:
            is_prime = False
            break

    return is_prime


def is_truncatable_prime(num):
    num_str = str(num)
    is_truncatable_prime = True
    for digit in range(0, len(num_str)):
        if not is_prime(int(num_str[len(num_str) - 1 - digit :])) or not is_prime(int(num_str[: digit + 1])):
            is_truncatable_prime = False
            break
    return is_truncatable_prime


def all_truncatable_primes():
    count = 0
    num = 11
    sum = 0
    while count < 11:
        if is_truncatable_prime(num):
            count += 1
            sum += num
            print('Number:', num, 'Count:', count, 'Sum:', sum)
        num += 2
    print('\nFinal Sum:', sum)
    return


# print(is_prime(132))
# print(is_truncatable_prime(132))
# print(is_truncatable_prime(3797))
all_truncatable_primes()
