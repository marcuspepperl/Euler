import math

def is_pentagonal(num):
    return abs((math.sqrt(1 + 24 * num) % 6) - 5) < 0.001

def two_pentagonals():
    is_found = False
    min_val = float("inf")
    min_pair = tuple()
    upper_limit = float("inf")
    n1 = 2
    while n1 < upper_limit or not is_found:

        pent1 = (3 * n1 ** 2 - n1) // 2
        n2 = 1
        while n2 < n1:

            pent2 = (3 * n2 ** 2 - n2) // 2
            difference = pent1 - pent2
            added = pent1 + pent2

            if is_pentagonal(difference) and is_pentagonal(added):
                if abs(difference) < min_val:
                    if not is_found:
                        is_found = True
                    min_pair = (n1, n2)
                    min_val = difference
                    print(min_pair, min_val)
                    upper_limit = math.floor((difference - 1) / 3)

            n2 += 1
        n1 += 1
    return min_pair, min_val



min_pair, min_val = two_pentagonals()
print(min_pair)
print(min_val)
