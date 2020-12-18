import math

def list_to_number(lst1):
    str1 = ''
    for elem in lst1:
        str1 += str(elem)

    return int(str1)




def lexicographic_permutation(permutation_number, ordered_characters):

    permutation_number -= 1
    permutation = []
    remaining_characters = ordered_characters.copy()
    character_count = len(remaining_characters)
    total_permutations = math.factorial(character_count)

    while total_permutations != 1:

        permutations_per_category = total_permutations / character_count

        character_range = math.floor(permutation_number / permutations_per_category)

        permutation.append(remaining_characters[character_range])

        permutation_number -= character_range * permutations_per_category
        remaining_characters.pop(character_range)

        total_permutations = total_permutations / character_count
        character_count = len(remaining_characters)


    permutation.append(remaining_characters[0])

    return permutation

def all_lexicographic_permutations(ordered_characters):
    for num in range(1, math.factorial(len(ordered_characters)) + 1):
        print(lexicographic_permutation(num, ordered_characters))






ordered_characters_1 = [1, 2, 3, 4, 5]
ordered_characters_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# all_lexicographic_permutations(ordered_characters_1)
print(list_to_number(lexicographic_permutation(1000000, ordered_characters_2)))
