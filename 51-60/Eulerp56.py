def sum_of_digits(num):
    return sum([int(ch) for ch in str(num)])

def greatest_digit_sum(max_a, max_b):
    max_digits = 0
    max_vals = tuple()
    for a in range(1, max_a + 1):
        for b in range(1, max_b + 1):
            if sum_of_digits(a ** b) > max_digits:
                max_digits = sum_of_digits(a ** b)
                max_vals = tuple([a, b])
    print('For a <', max_a, 'and b <', max_b)
    print('a =', max_vals[0], 'and b =', max_vals[1], 'acheived the max digit sum of', max_digits)
    return

greatest_digit_sum(100, 100)
