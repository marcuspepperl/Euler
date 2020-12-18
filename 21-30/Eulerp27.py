import math


def is_prime(num):

    if num < 0:
        num = abs(num)

    is_prime = True

    if num % 2 == 0:
        is_prime = False

    if is_prime:
        for factor in range(3, math.ceil(math.sqrt(num)) + 1, 2):
            if num % factor == 0:
                is_prime = False
                break

    return is_prime



def prime_factors(num):

    if num < 0:
        num = abs(num)
    primes = set()

    while num % 2 == 0:
        primes.add(2)
        num = num // 2

    while num != 1:

        smallest_factor_remaining = 3
        for factor in range(smallest_factor_remaining, num + 1, 2):
            if num % factor == 0:
                num = num // factor
                primes.add(factor)
                smallest_factor_remaining = factor
                break

    return primes





def prime_factors_below(num):

    primes = set([2])

    for n in range(2, num + 1):
        is_prime = True
        if n % 2 == 0:
            continue


        for factor in range(3, math.ceil(math.sqrt(n)) + 1, 2):
            if n % factor == 0:
                is_prime = False
                break

        if is_prime:
            primes.add(n)

    return primes




def generate_possible_b(b_bounds, least_primes):

    all_prime_factors = prime_factors_below(least_primes)

    possible_b = []

    pos_range = list(range(b_bounds[0], -1 * least_primes)) + list(range(least_primes + 1, b_bounds[1] + 1))

    for b in pos_range:
        if len(prime_factors(b) & all_prime_factors) == 0:
            possible_b.append(b)


    return possible_b







def quadratic_most_primes(a_bounds, b_bounds, least_primes, upper_bound):

    possible_b = generate_possible_b(b_bounds, least_primes)
    most_primes = 0
    best_a = None
    best_b = None
    for b in possible_b:
        for a in range(a_bounds[0], a_bounds[1] + 1):
            primes = 0
            for n in range(upper_bound):
                if not is_prime(n ** 2 + a * n + b):
                    if primes > most_primes:
                        most_primes = primes
                        best_a = a
                        best_b = b
                    break
                primes += 1


    return best_a, best_b, most_primes


def accuracy_test(best_a, best_b, most_primes):
    for n in range(most_primes):
        val = n ** 2 + best_a * n + best_b
        print(val, is_prime(val))


    return



def run():

    a_bounds_1 = tuple([-1000, 1000])
    b_bounds_1 = tuple([-1000, 1000])
    least_primes = 40
    upper_bound = 100

    solution_a, solution_b, performance = quadratic_most_primes(a_bounds_1, b_bounds_1, least_primes, upper_bound)
    # accuracy_test(solution_a, solution_b, performance)
    print('A:', solution_a, 'B:', solution_b, 'C:', performance)
    # print(solution_a * solution_b)
    # print(prime_factors_below(7))
    # print(prime_factors(34672))
    # print(generate_possible_b(b_bounds_1, least_primes))

run()
