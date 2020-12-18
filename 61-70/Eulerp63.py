def length_num(n):
    return len(str(n))

def all_ndigit_npowers():
    count = 0
    power = 1
    while power == length_num(9 ** power):
        power += 1
    max_power = power

    for base in range(1, 10):
        for power in range(1, max_power):
            if power == length_num(base ** power):
                count += 1
    print(count)

all_ndigit_npowers()
