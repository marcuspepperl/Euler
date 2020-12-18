def distinct_prime_factors(n):
    distinct_factors = set()
    while not n % 2:
        distinct_factors.add(2)
        n = n // 2
    min_div = 3
    while n != 1:
        for div in range(min_div, n + 1, 2):
            if not n % div:
                distinct_factors.add(div)
                n = n // div
                min_div = div
                break
    return distinct_factors


def consecutive_prime_factors(count, num_factors, max_check):
    consecutive_lst = []
    num = 2
    while num < max_check:

        if len(distinct_prime_factors(num)) == num_factors:
            consecutive_lst.append(num)
            if len(consecutive_lst) == count:
                return consecutive_lst
        else:
            if len(consecutive_lst) != 0:
                consecutive_lst.clear()
        num += 1

    return []

def run():
    # print(number_distinct_prime_factors(45))

    print(consecutive_prime_factors(2, 2, 20))
    print(consecutive_prime_factors(3, 3, 1000))
    
    numbers = consecutive_prime_factors(4, 4, 1000000)
    for number in numbers:
        print(number, distinct_prime_factors(number))

run()
