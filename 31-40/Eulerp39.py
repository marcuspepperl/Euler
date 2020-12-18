import math

def max_perimeter_solutions(max_perim):
    perim_solutions = {}
    for a in range(1, math.ceil(max_perim / 3)):
        for b in range(a + 1, math.ceil((max_perim - 1 - a) / 2) + 1):
            c = math.sqrt(a ** 2 + b ** 2)
            if not abs(int(c) - c) < 0.001:
                continue
            c = int(c)
            if a + b + c <= max_perim:
                p = a + b + c
                perim_solutions[p] = perim_solutions.get(p, 0) + 1

    max_solution = max(perim_solutions.values())
    max_perim = -1
    for perim in perim_solutions:
        if perim_solutions[perim] == max_solution:
            max_perim = perim
            break

    return perim_solutions, max_perim, max_solution

perim_solutions, max_perim, max_solution = max_perimeter_solutions(1000)
print('\nThe perimeter p =', max_perim, 'had', max_solution, 'distinct solutions\n')
