def equivalent_permutation(str1, str2):
    # Strings are assumed to be the same length
    if len(str1) == 1:
        return str1 == str2
    else:
        if str1[0] in str2:
            loc = str2.find(str1[0])
            return equivalent_permutation(str1[1:], str2[:loc] + str2[loc+1:])
        return False


def permuted_multiples(n, mult_num):
    max_power = len(str(n))
    power = 0
    max_flag = False
    while power < max_power:
        max_num = int((10 ** (power + 1)) / mult_num)
        if n < max_num:
            max_num = n
            max_flag = True
        num = 10 ** power
        while num < max_num:
            candidate_num = True
            candidate_lst = [num]
            for factor in range(2, mult_num + 1):
                mult = num * factor
                if set(str(mult)) != set(str(num)):
                    candidate_num = False
                    break
                elif not equivalent_permutation(str(mult), str(num)):
                    candidate_num = False
                    break
                candidate_lst.append(mult)
            if candidate_num:
                print('Answer:', num)
                print(candidate_lst)
                return
            num += 1
        if max_flag:
            break
        power += 1
    return

def run():
    permuted_multiples(10 ** 7, 6)

run()
