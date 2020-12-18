def num_size(n):
    return len(str(n))


def self_powers(n):
    last_ten_digits = 0
    for num in range(1, n + 1):
        product = 1
        for power in range(num):
            product *= num
            if product >= 10 ** 10:
                product = product % (10 ** 10)
        last_ten_digits = (last_ten_digits + product) % (10 ** 10)
        print(num, last_ten_digits)
    return last_ten_digits

print(self_powers(1000))
