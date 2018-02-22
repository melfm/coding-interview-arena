"""Misc Questions."""
import math
import numpy as np


def isPowerOf3_loop(n):

    if n < 1:
        return False

    while(n % 3 == 0):
        n /= 3

    return n == 1


def isPowerOf3_int_limit(n):
    # Works for integers of limited size
    # The biggest power of 3 that fits into
    # signed 32 bits (3^19)
    return n > 0 and 1162261467 % n == 0


def isPowerOf3_recursive(n):

    if n < 1:
        return False

    if n == 1:
        return True

    return isPowerOf3_recursive(n/3)


def two_sum(array, sum_k):
    """Given an array of n integers and a number k,
    determine whether there is a pair of elements in
    the array that sums to k.
    Complexity O(n).
    """

    table = set()
    for i in range(len(array)):
        value = sum_k - array[i]
        # This works because a = b + c, therefore
        # c = a - b. So if we've already added c
        # which could've been a past solution, then
        # there is a potential pair.
        if value in table:
            return True
        table.add(array[i])

    return False


def find_top_k_min_distance(array, top_k, location):
    """Given an array of integers of 2D points and a location
    point, return the top_k closest points to the location.
    """

    # Store locations in the format [distance, x, y]
    top_k_list = np.full((top_k, 3), np.inf)

    def find_distance(point1, point2):
        x_diff = (point2[0] - point1[0]) ** 2
        y_diff = (point2[1] - point1[1]) ** 2

        return math.sqrt(x_diff + y_diff)

    for i in range(len(array)):
        current_point = array[i]

        distance = find_distance(current_point,
                                 location)

        if np.inf in top_k_list:
            # Check the distance indices only
            # and replace the first one
            inf_indx = np.where(top_k_list[:, 0] == np.inf)[0][0]
            top_k_list[inf_indx, 0] = distance
            top_k_list[inf_indx, 1] = current_point[0]
            top_k_list[inf_indx, 2] = current_point[1]

        else:
            # Update the existing indices
            # Compare the distance against the max of locations
            # found so far.
            current_max = np.max(top_k_list[:, 0])
            current_max_idx = np.argmax(top_k_list[:, 0])

            if distance < current_max:
                top_k_list[current_max_idx, 0] = distance
                top_k_list[current_max_idx, 1] = current_point[0]
                top_k_list[current_max_idx, 2] = current_point[1]

    return top_k_list


def find_min_overlapping_ranges(ranges):
    """Given a list of ranges, find a list of minimum number of
    'ranges' by combining the overlapping 'ranges'.
    """

    ranges = sorted(ranges)

    num_ranges = len(ranges)

    first_ptr = 0
    snd_ptr = 0

    while first_ptr != num_ranges:
        current_first_range = ranges[first_ptr]
        snd_ptr = first_ptr + 1

        while(snd_ptr != num_ranges):

            current_snd_range = ranges[snd_ptr]
            removed_ptr = False

            if not (current_first_range[0] < current_snd_range[0] and
                    current_first_range[1] < current_snd_range[1]):

                ranges.remove(current_snd_range)
                num_ranges -= 1
                removed_ptr = True

            elif current_first_range[1] == current_snd_range[0]:
                # Overlap, can combine the ranges
                new_range = [current_first_range[0],
                             current_snd_range[1]]

                ranges.remove(current_first_range)
                ranges.remove(current_snd_range)
                ranges.append(new_range)
                num_ranges -= 1
                removed_ptr = True

            # If an element was removed, don't incremenet the pointer
            if not removed_ptr:
                snd_ptr += 1

        first_ptr += 1

    return ranges
