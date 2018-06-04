"""Array questions."""

import numpy as np


def find_largest_sub_array_sum(array):
    """Returns the largest sum of subset array.
    """

    max_sum_so_far = 0
    current_sum = 0

    for i in range(0, len(array)):
        current_sum = current_sum + array[i]
        if (max_sum_so_far < current_sum):
            max_sum_so_far = current_sum

        if current_sum < 0:
            current_sum = 0
    return max_sum_so_far


def find_largest_sum_sub_array(array):
    """Returns the subset array with the largest sum.
    """
    # pointers to the beginning and end of array subset
    start = 0
    end = 0
    set_start = True
    set_end = True

    max_sum_so_far = 0
    current_sum = 0

    for i in range(0, len(array)):
        current_sum = current_sum + array[i]
        if (max_sum_so_far < current_sum):
            max_sum_so_far = current_sum
            if set_start:
                start = i
                set_start = False
                if set_end:
                    end = start
                    set_end = False
            else:
                end = i

        if current_sum < 0:
            current_sum = 0
            set_start = True
            set_end = True

    return max_sum_so_far, start, end


def add_one(array):
    """Given an array representing an integer, add one and return
    the new number represented as an array.
    e.g. -> [1, 2, 3, 4] -> [1, 2, 3, 5]
         -> [1, 9, 9] -> [2, 0, 0]
         -> [9, 9, 9] -> [1, 0, 0, 0]
    """
    carry = 1
    result = np.zeros_like(array)

    for i in range(len(array)):
        # Iterate the array backwards
        current_sum = array[-(i+1)] + carry
        if current_sum == 10:
            carry = 1
        else:
            carry = 0
        result[-(i+1)] = current_sum % 10

    if carry == 1:
        result = np.insert(result, 0, 1)

    return result


def find_smallest_pos(input_array):
    """Given an array input_array of N integers, return the
    smallest positive integer (greater than 0)
    that does not occur in input_array.
    """

    possible_sol = np.arange(1, abs(max(input_array)) + 2)

    for i in possible_sol:
        if i not in input_array:
            return i

    return -1


def find_smallest_pos_v2(input_array):
    """This version avoids creating a separate array.
    """

    missing = 1
    for elem in sorted(input_array):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing


def shuffle_cards(input_array):
    """Given an array of cards, shuffle them according to the following:
        Input: [1, 2, 3, 4, 5, 6]
        Output: [4, 1, 5, 2, 6, 3]

    Shuffling works by splitting the deck of cards into two and taking cards
    from each deck one at a time starting with second deck.
    """

    input_size = len(input_array)

    # Takes care of input with an odd size
    odd_size = False
    if input_size % 2 != 0:
        odd_size = True

    mid_point = int(len(input_array) / 2)

    deck_1 = input_array[0: mid_point]
    deck_2 = input_array[mid_point:]

    shuffled_array = []
    for i in range(len(deck_1)):
        shuffled_array.append(deck_2[i])
        shuffled_array.append(deck_1[i])
    if odd_size:
        # Append the missing last element
        shuffled_array.append(deck_2[-1])

    return shuffled_array
