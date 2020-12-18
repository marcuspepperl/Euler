def nesting(n):
    if n == 1:
        return 3, 2
    numerator = 1
    denominator = 2
    for _ in range(n - 1):
        numerator += denominator * 2
        numerator, denominator = denominator, numerator
    numerator += denominator

    return numerator, denominator


def run():
    count = 0
    for num in range(1, 1001):
        numer, denom = nesting(num)
        if len(str(numer)) > len(str(denom)):
            count += 1
    return count
    

# print(nesting(1))
# print(nesting(2))
# print(nesting(4))

print(run())
