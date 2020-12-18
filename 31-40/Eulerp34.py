import math

def sum_factorial_digits(num):

    return sum([math.factorial(int(digit)) for digit in list(str(num))])



def sum_cool_numbers(n):
    total = 0
    # Not including 1 or 2
    for num in range(3, n + 1):
        if num == sum_factorial_digits(num):
            total += num
            print(num)

    return total


print(sum_cool_numbers(math.factorial(10)))
