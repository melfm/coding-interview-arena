"""Misc Questions."""


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
