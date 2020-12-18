url1 = 'Eulerp54.txt'


face_cards = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}


def is_straight(sorted_vals):

    straight = True
    for ind in range(len(sorted_vals) - 1):
        if sorted_vals[ind + 1] - sorted_vals[ind] != 1:
            straight = False
    if not straight and face_cards['A'] in sorted_vals:
        new_sorted_vals = [1]
        new_sorted_vals.extend(sorted_vals[:-1])
        straight = True
        for ind in range(len(new_sorted_vals) - 1):
            if new_sorted_vals[ind + 1] - new_sorted_vals[ind] != 1:
                straight = False
                break

    return straight


def is_flush(suits):

    flush = True
    first_suit = suits[0]
    for ind in range(1, len(suits)):
        if suits[ind] != first_suit:
            flush = False
            break
    return flush


def freq_dict(sorted_vals):
    val_dict = {}
    for val in sorted_vals:
        val_dict[val] = val_dict.get(val, 0) + 1
    return val_dict


def corresponding_key(val_dict, val, all = False):
    key_lst = []

    for key, value in val_dict.items():
        if value == val:
            key_lst.append(key)
            if not all:
                break
    return key_lst


def remove_all(lst, nums):
    return [entry for entry in lst if lst not in nums]

def rating(hand):

    # first slot: straight flush
    # second slot: four of a kind
    # third slot/fourth slot: full house
    # fifth slot: flush
    # sixth slot: straight
    # seventh slot: three of a kind
    # eighth slot/ninth slot: two pairs
    # tenth slot: one pair
    # eleventh slot and onwards: high cards

    rating_lst = [0] * 10
    vals = [card[0] for card in hand]
    num_vals = []
    for val in vals:
        if val in face_cards:
            num_vals.append(face_cards[val])
        else:
            num_vals.append(int(val))
    num_vals.sort()
    reversed_vals = reversed(num_vals)
    suits = [card[1] for card in hand]

    #boolean values
    straight = is_straight(num_vals)
    flush = is_flush(suits)

    val_dict = freq_dict(num_vals)
    frequencies = sorted(val_dict.values(), reverse = True)


    if straight:
        if flush:
            # straight flush
            rating_lst[0] = 1
            rating_lst.extend(reversed_vals)
        else:
            # simple straight
            rating_lst[5] = 1
            rating_lst.extend(reversed_vals)
    elif flush:
        # simple flush
        rating_lst[4] = 1
        rating_lst.extend(reversed_vals)
    elif frequencies[0] == 4:
        # four of a kind
        special_num = corresponding_key(val_dict, 4)[0]
        rating_lst[1] = special_num
        rating_lst.extend(remove_all(reversed_vals, [special_num]))
    elif frequencies[0] == 3:
        if frequencies[1] == 2:
            # full house
            rating_lst[2] = corresponding_key(val_dict, 3)[0]
            rating_lst[3] = corresponding_key(val_dict, 2)[0]
        else:
            # simple three of a kind
            special_num = corresponding_key(val_dict, 3)[0]
            rating_lst[6] = special_num
            rating_lst.extend(remove_all(reversed_vals, [special_num]))
    elif frequencies[0] == 2:
        if frequencies[1] == 2:
            # two pairs
            special_nums = corresponding_key(val_dict, 2, all = True)
            special_nums.sort(reverse = True)
            rating_lst[7] = special_nums[0]
            rating_lst[8] = special_nums[1]
            rating_lst.extend(remove_all(reversed_vals, special_nums))

        else:
            # single pair
            special_num = corresponding_key(val_dict, 2)[0]
            rating_lst[9] = special_num
            rating_lst.extend(remove_all(reversed_vals, [special_num]))
    else:
        # high card
        rating_lst.extend(reversed_vals)


    return rating_lst



def rating_tests():
    # print(rating(['5C', '5D', '6C', '6D', '6H']))
    print(rating(['8D', '3S', '5D', '5C', 'AH']))
    print(is_straight([3, 5, 5, 8, 14]))
    # print(is_straight([5, 5, 6, 7, 13]))

# rating_tests()



def run(url):
    fhandle = open(url)
    count = 0
    one_better = 0
    for line in fhandle:

        line = line[:-2]
        cards = line.split()
        hand1 = cards[:5]
        hand2 = cards[5:]

        if rating(hand1) > rating(hand2):
            one_better += 1
        count += 1

    return one_better, count

answer = run(url1)
print('Player One Wins:', answer[0], 'times of', answer[1])
