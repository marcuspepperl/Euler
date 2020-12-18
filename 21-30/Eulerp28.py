def corner_sum(box_size):


    return 4 * box_size ** 2 - 6 * (box_size - 1)



def entire_sum_diagonals(dim):

    entire_sum = 1

    for box_size in range(3, dim + 1, 2):

        entire_sum += corner_sum(box_size)

    return entire_sum


print(entire_sum_diagonals(1001))
