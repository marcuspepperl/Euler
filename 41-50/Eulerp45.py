import math

def is_pentagonal(num):
    return abs((math.sqrt(1 + 24 * num) % 6) - 5) < 10 ** -10

def is_triangular(num):
    return abs((math.sqrt(1 + 8 * num) % 2) - 1) < 10 ** -10


def tri_pent_hex_numbers(n):
    for root in range(1, n + 1):
        hex = root * (2 * root - 1)
        if is_triangular(hex) and is_pentagonal(hex):
            tri_root = (-1 + round(math.sqrt(1 + 8 * hex))) // 2
            print(tri_root, root, hex)


def tests():
    lst = [1, 3, 5, 6, 22]
    for entry in lst:
        print(is_triangular(entry), is_pentagonal(entry))

def run():
    tri_pent_hex_numbers(1000000)

run()
