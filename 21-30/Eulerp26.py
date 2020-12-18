
import math
import decimal


decimal.getcontext().prec = 10000



def largest_repeating_substring(num_str, start):

    max_cycle = ''
    num_str = num_str[start :]
    for ind1 in range(len(num_str) // 2 + 1):

        pos_cycle = num_str[: ind1 + 1]

        if max_cycle in pos_cycle and max_cycle != '':
            continue

        is_cycle = True

        ind2 = -1

        for ind2 in range(ind1 + 1, len(num_str) - ind1 - 2, ind1 + 1):

            if pos_cycle != num_str[ind2 : ind2 + ind1 + 1]:
                is_cycle = False
                break

        if ind2 != - 1 and is_cycle:
            max_cycle = pos_cycle

    return len(max_cycle)



def length_longest_cycle(d):
    num = decimal.Decimal(1) / decimal.Decimal(d)
    places_out = math.ceil(math.log10(d)) - 1
    num_str = str(num)
    num_str = num_str[num_str.find('.') + 1 :]
    max_length = None

    for iter in range(places_out + 1):
        length = largest_repeating_substring(num_str, iter)
        if max_length == None or length > max_length:
            max_length = length

    return max_length


def longest_cycle_below(n):

    max_length = None
    max_divisor = None
    for num in range(1, n):
        length = length_longest_cycle(num)
        print(num, length)
        if max_length == None or length > max_length:
            max_length = length
            max_divisor = num


    return max_divisor, max_length


print(length_longest_cycle(7))
print(longest_cycle_below(1000))
