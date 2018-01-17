import numpy as np


def merge_and_sort(array1, array2):
    """Merges two sorted arrays
    Args:
        array1: A sorted array of integers
        array2: A sorted array of integers
    """

    p1 = len(array1) - 1
    p2 = len(array2) - 1

    array1 = np.asarray(array1)
    array2 = np.asarray(array2)
    # Append zeros to the first array
    # this will have the new sorted values
    array1 = np.append(array1, np.zeros(len(array2)))

    last = len(array1) - 1

    while p1 >= 0 and p2 >= 0:

        if array1[p1] >= array2[p2]:
            array1[last] = array1[p1]
            p1 -= 1
            last -= 1

        if array1[p1] <= array2[p2]:
            array1[last] = array2[p2]
            last -= 1
            p2 -= 1

    # This is needed in case array1 is larger than array2
    while (p2 >= 0):
        array1[last] = array2[p2]
        p2 -= 1

    return array1
