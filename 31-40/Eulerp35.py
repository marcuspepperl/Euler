import math

def is_prime(n):

    is_prime = True
    if not n % 2:
        is_prime = False

    if is_prime:
        for div in range(3, math.ceil(math.sqrt(n)), 2):
            if not n % div:
                is_prime = False
                break
    return is_prime


def rotate(n, i):

    n_str = str(n)
    return int(n_str[i:] + n_str[:i])


def fully_primes(max_num):

    count = 1
    for num in range(3, max_num + 1):
        is_rotation_prime = True
        num_length = len(str(num))
        for i in range(num_length):
            if not is_prime(rotate(num, i)):
                is_rotation_prime = False
                break
        if is_rotation_prime:
            count += 1

    return count



print(fully_primes(10 ** 6))
