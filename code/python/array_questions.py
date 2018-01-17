"""Array questions."""

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
