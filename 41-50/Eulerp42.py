import math


fhandle = open('Eulerp42_words.txt')
file_str = ''
for line in fhandle:
    line = line.replace('"', '')
    file_str += line

words = file_str.split(',')
triangular_count = 0

for word in words:

    triangular_sum = 0
    for ch in word:
        triangular_sum += ord(ch) - 64

    root = math.floor(math.sqrt(2 * triangular_sum))
    if root * (root + 1) == 2 * triangular_sum:
        triangular_count += 1

print(triangular_count)
