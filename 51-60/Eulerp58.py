import math

def is_prime(n):
    if n == 2:
        return 1
    if not n % 2:
        return 0
    max_div = math.sqrt(n)
    div = 3
    while div <= math.sqrt(n):
        if not n % div:
            return 0

        div += 2
    return 1






def spirals(prop = .10):
    prime_count = 3
    num_count = 5
    prime_prop = 3 / 5
    square_size = 3

    while prime_prop >= prop:

        square_size += 2
        square_num = square_size ** 2
        first_num = square_num - (square_size) + 1
        second_num = first_num - (square_size) + 1
        third_num = second_num - (square_size) + 1
        candidates = [first_num, second_num, third_num]

        prime_count += sum(map(is_prime, candidates))
        num_count += 4
        prime_prop = prime_count / num_count

    return square_size


print(spirals())
