import math


def retreive_digits(index_lst):
    max_index = max(index_lst)
    digit_starting_index = []
    digit_starting_index[0 : 3] = [0, 1, 10]
    range_max = max(4, math.floor(math.log(max_index)))

    for digit in range(3, range_max + 1):
        digit_starting_index.append(digit_starting_index[digit - 1] + 9 * 10 ** (digit - 2) * (digit - 1))
    print(digit_starting_index)

    retreive_lst = []
    for index in index_lst:
        digit_number = -1
        for digit in range(len(digit_starting_index)):
            if index < digit_starting_index[digit]:
                digit_number = digit - 1
                index_in_field = index - digit_starting_index[digit_number]
                break
        number_in_field = index_in_field // digit_number + 10 ** (digit_number - 1)
        character_in_number = index_in_field % digit_number
        character = int(str(number_in_field)[character_in_number])
        print(number_in_field, character_in_number, character)
        retreive_lst.append(character)

    return retreive_lst



index_lst_1 = [10 ** i for i in range(7)]

retreived_digits_1 = retreive_digits(index_lst_1)
product = 1
for digit in retreived_digits_1:
    product *= digit
print('The product is:', product)
