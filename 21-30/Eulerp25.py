def first_fib_digit(num):
    n1, n2 = 1, 1
    count = 2
    while len(str(n2)) < num:
        temp = n2
        n2 = n1 + n2
        n1 = temp
        count = count + 1
    return count

print(first_fib_digit(1000))
