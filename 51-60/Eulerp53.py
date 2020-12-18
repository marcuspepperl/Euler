import math

def combinations(n, r):
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))

def is_combination_greater_than(num, n, r):
    result = 1 / (math.factorial(n - r) * math.factorial(r))
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
        if result > num:
            return True
    return False


def combinations_greater_than(num, max_n):
    count = 0
    for n in range(1, max_n + 1):
        for r in range(1, n + 1):
            if is_combination_greater_than(num, n, r):
                count += 1
    return count



print(combinations_greater_than(10 ** 6, 100))
