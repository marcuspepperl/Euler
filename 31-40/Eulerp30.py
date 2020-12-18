def strip_and_power(num, power):

    power_sum = 0
    for ch in str(num):
        val = int(ch) ** power
        power_sum += val

    return power_sum

def power_of_digits(n, power):
    numb_lst = []
    for num in range(2, n + 1):
        if num == strip_and_power(num, power):
            numb_lst.append(num)

    return numb_lst

lst1 = power_of_digits(2000000, 5)
print(lst1)
print(sum(lst1))
