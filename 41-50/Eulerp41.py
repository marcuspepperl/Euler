import math

def is_pandigital(num):
    num_str = str(num)
    return {int(ch) for ch in num_str} == {n for n in range(1, len(num_str) + 1)}


def is_prime(num):

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

def pandigital_primes(n):

    count = 0
    max_pan_prime = -1
    for num in range(3, n, 2):
        if is_pandigital(num) and is_prime(num):
            count += 1
            max_pan_prime = num
            if not count % 50 or count > 500:
                print(num, count)
        if not (num - 1) % (10 ** 6):
            print('Number:', num)

    return max_pan_prime

print('The maximum found pandigital prime is ', pandigital_primes(10 ** 8))
