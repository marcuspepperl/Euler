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



def list_all_primes_below(n):
    if n < 2:
        return []
    prime_lst = [2]
    for pos_prime in range(3, n + 1, 2):
        if is_prime(pos_prime):
            prime_lst.append(pos_prime)
    return prime_lst


def partial_sums(lst):
    partial_sums = [0]
    total = 0
    for elem in lst:
        total += elem
        partial_sums.append(total)

    return partial_sums

def consecutive_sum(ind1, ind2, partial_sums_lst):
    return partial_sums_lst[ind2 + 1] - partial_sums_lst[ind1]


def greatest_prime_chain_below(n, min_string_length, min_prime_search):

    prime_set = set_all_primes_below(n)
    full_addend_lst = list_all_primes_below(int(n ** (2/3)))
    sum_addend_lst = partial_sums(full_addend_lst)
    string_length = min_string_length
    num_primes = len(full_addend_lst)


    while string_length - 1 < num_primes:

        if string_length % 2 == 0:

            ind1 = 0
            ind2 = ind1 + string_length - 1
            consecutive_total = consecutive_sum(ind1, ind2, sum_addend_lst)
            if consecutive_total > n:
                print('Exhausted')
                break
            if consecutive_total in prime_set:
                print('Length:', string_length, 'First:', full_addend_lst[ind1], 'Last:', full_addend_lst[ind2], 'Sum:', consecutive_total)


        else:
            ind1 = 1
            ind2 = ind1 + string_length - 1
            consecutive_total = 0
            while ind2 < num_primes and consecutive_total < n:

                consecutive_total = consecutive_sum(ind1, ind2, sum_addend_lst)
                if consecutive_total in prime_set:
                    print('Length:', string_length, 'First:', full_addend_lst[ind1], 'Last:', full_addend_lst[ind2], 'Sum:', consecutive_total)
                    if consecutive_total < min_prime_search:
                        break
                ind1 += 1
                ind2 += 1

        string_length += 1



greatest_prime_chain_below(1000000, 10, 100000)
