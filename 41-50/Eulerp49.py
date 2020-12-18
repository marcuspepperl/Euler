import itertools
import math

def is_prime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    for div in range(3, 1 + math.floor(math.sqrt(n)), 2):
        if not n % div:
            return False
    return True




def lst_to_num(num_lst):
    num_str = ''
    for digit in num_lst:
        num_str += str(digit)
    return int(num_str)

def prime_permutations():
    winners = []
    for num in range(1000, 10000):
        if not is_prime(num):
            continue
        num_lst = [int(ch) for ch in str(num)]
        perm_lst = [lst_to_num(list(other_lst)) for other_lst in itertools.permutations(num_lst) if list(other_lst) > num_lst]
        perm_lst = list(filter(is_prime, perm_lst))
        for perm1 in perm_lst:
            if (2 * perm1 - num) in perm_lst:
                if not tuple([num, perm1, 2 * perm1 - num]) in winners:
                    winners.append(tuple([num, perm1, 2 * perm1 - num]))

    return winners


def run():
    winners = prime_permutations()
    result = ''
    for prime in winners[1]:
        print(prime)
        result += str(prime)
    print("Answer:", int(result))

run()
