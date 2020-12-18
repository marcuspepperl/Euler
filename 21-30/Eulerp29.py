distinct_set = set()

for a in range(2, 101):
    for b in range(2, 101):
        distinct_set.add(a ** b)

print(len(distinct_set))
