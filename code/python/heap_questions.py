""" Heap Questions.
"""
import heapq

def find_smallest_range_k_lists(list1, list2, list3):
    """ You have k lists of sorted integers.
    Find the smallest range that includes at least
    one number from each of the k lists.

    E.g.
    List1: [4, 10, 15, 24, 26]
    List2: [0, 9, 12, 20]
    List3: [5, 18, 22, 30]

    SL: [20, 24] contains 24 from L2, 20 from L2 and
        22 from L3.

    This is efficient solving with a heap data structure.
    1. initialize smallest_range as MAX_INT
    2. keep 3 pointers/index p1, p2 and p3 which points
        to the first elements of lists L1, L2 and L3
        respectively.
    3. find the max value and min value pointed/indexed
        by p1, p2 and p3
    4. difference of max value and min value discovered
        in step 3 is the current range. Compare it with
        smallest_range and update it, if found smaller.
    5. increment the pointer/index of min value found
        in step 3.
    6. repeat step 3 to 5 until the pointer/index of min
        value is in range.

    constant space and O(n) time.
    """
    # init_dict= {0: list1[0], 1: list2[0], 2: list3[0]}
    init_dict= {list1[0] : 0, list2[0]: 1, list3[0]: 2}
    min_heap = list(init_dict.items())
    heapq.heapify(min_heap)

    dist_list1 = len(list1)
    dist_list2 = len(list2)
    dist_list3 = len(list3)

    top_node = min_heap[1][1]
    big_node = min_heap[2][1]
    current_range = big_node - top_node

    min_heap[1] = (list2[1], 1)
    # TODO: Need to check if this heap lib allows storing
    # dict type values since we want to decide how to replace
    # each node value from a particular list.
    heapq.heapify(min_heap)
