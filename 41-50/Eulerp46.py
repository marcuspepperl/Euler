import math

def is_prime(n):
    if n == 2:
        return True
    elif not n % 2:
        return False
    for div in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True


def goldbach_check(n):
    for num in range(9, n + 1, 2):
        if not is_prime(num):
            max_s = math.floor(math.sqrt((num - 2) / 2))
            check_flag = False
            for s in range(1, max_s + 1):
                if is_prime(num - 2 * s ** 2):
                    check_flag = True
                    break
            if not check_flag:
                print(num)

def run():
    goldbach_check(100000)

run()
