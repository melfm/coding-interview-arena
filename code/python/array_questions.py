"""Array questions."""

import numpy as np
import sys

import string_manipulation as str_manip


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
        current_sum = array[-(i + 1)] + carry
        if current_sum == 10:
            carry = 1
        else:
            carry = 0
        result[-(i + 1)] = current_sum % 10

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

    return 1


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


def max_frequent_number(input_array):
    """Find maximum frequent numbers in an array.
    If there are more numbers with maximum frequency,
    they display all numbers in ascending order.
    Ascending order is important.
    """

    sorted_array = sorted(input_array)

    max_so_far = 1
    counter = 1
    max_nums = {}
    for i in range(len(sorted_array) - 1):

        p1 = sorted_array[i]
        p2 = sorted_array[i + 1]

        if p1 == p2:
            counter += 1
            if counter == max_so_far:
                max_nums[p1] = counter
            elif counter > max_so_far:

                max_so_far = counter
                max_nums = {}
                max_nums[p1] = counter

        else:
            counter = 1

    return max_nums


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

    deck_1 = input_array[0:mid_point]
    deck_2 = input_array[mid_point:]

    shuffled_array = []
    for i in range(len(deck_1)):
        shuffled_array.append(deck_2[i])
        shuffled_array.append(deck_1[i])
    if odd_size:
        # Append the missing last element
        shuffled_array.append(deck_2[-1])

    return shuffled_array


def smallest_odd_occurrence(input_array):
    """Given an array return the smallest number that has an odd
    number of occurrences.
        Input: [1, 1, 2, 2, 3, 4, 5, 6, 6, 5, 4]
        Output: 3
    """

    # Start the counter from 1 to include the current
    count = 1
    input_array = sorted(input_array)
    for i in range(len(input_array) - 1):
        if input_array[i] == input_array[i + 1]:
            count += 1
        else:
            if count % 2 != 0:
                return input_array[i]
            else:
                count = 1

    return -1


def combine_sum_pieces(array_p, array_s):
    """Given two arrays, one representing pieces and second possible
    sum of these pieces, return the number of pieces from array_s that
    is possible to sum using the available elements from array_p.
        Input: [6, 2, 9], [1, 4, 17, 3]
        Output: 2
    In the case above, we need 2 pieces (6 + 9) = 17 while the other
    combinations are not possible.
    Note: This implementation does not handle self element repeats,
    so for instance if 6 * 3 can also make a up sum or 6 + (9*2).
    The only edge case handled here is element * 2.
    """

    def combine_and_permute_order_free(input_array):

        def combinate(prefix, input_array, combos=[]):
            if input_array:
                if prefix:
                    new_combo = [prefix, input_array[0]]
                else:
                    new_combo = input_array[0]
                combos.append(new_combo)
                # This [1:] slicing is the magic here
                if prefix:
                    combinate([prefix, input_array[0]], input_array[1:],
                              combos)
                else:
                    combinate(input_array[0], input_array[1:], combos)
                combinate(prefix, input_array[1:], combos)

        combos = []
        combinate([], input_array, combos)
        # Mel: This line is not needed?
        # combos = [x for x in combos if x != []]
        return combos

    combinations = combine_and_permute_order_free(array_p)

    # print('Possible combinations ', combinations)

    all_combos = []
    for comb in combinations:
        if isinstance(comb, int):
            if (comb + comb) in array_s:
                all_combos.append([comb, comb])

        else:
            flattened = str_manip.flatten(comb)
            flat_list = []
            for el in flattened:
                flat_list.append(el)

            sum_comb = sum(flat_list)
            if sum_comb in array_s:
                all_combos.append(flat_list)

    return all_combos


def max_subarray_sum(array):
    """Find the sum of contiguous subarray within
    a one-dimensional array of numbers that has
    the largest sum.
    """
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0

    for i in range(len(array)):
        max_ending_here += array[i]

        if max_so_far < max_ending_here :
            max_so_far = max_ending_here

        if max_ending_here < 0:
            # Reset
            max_ending_here = 0

    return max_so_far


def find_two_disjoint_subarray_max(array):
    """Given an array of integers, find two disjoint
    contiguous sub-arrays such that the absolute diff
    between the sum of two sub-arrays is maximum.

    E.g. [2, -1, -2, 1, -2, 2, 8]
    Answer: [-1,-2,1,-4], [2,8] Diff=16

    Need to use the Kadane's Algorithm from max_subarray_sum()
    to find 4 subarrays.
    https://www.geeksforgeeks.org/maximum-absolute-difference-between-sum-of-two-contiguous-sub-arrays/
    """
    pass