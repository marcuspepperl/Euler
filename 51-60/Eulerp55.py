def add_reverse(num):
    return num + int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_lychrel(n, max_iter):
    lychrel_count = 0
    num = 1
    while num < n:
        iter = 0
        iter_num = num
        is_lychrel = True
        while iter < max_iter:
            iter_num = add_reverse(iter_num)
            if is_palindrome(iter_num):
                is_lychrel = False
                break
            iter += 1
        if is_lychrel:
            lychrel_count += 1
        num += 1

    return lychrel_count

print(find_lychrel(10000, 50))
