import numpy as np


def get_min_steps_mem(n):
    """Minimum steps to minimize n as per given condition.
    - If n is divisible by 2 then we may reduce n to n/2.
    - If n is divisible by 3 then you may reduce n to n/3.
    - Else decrement n by 1.
    Technique: Memoization"""

    steps = np.full(n+1, -1)
    return get_min_steps(n, steps)


def get_min_steps(n, steps):
    """
    Try all possibilities to find the minimum.
    f(n) = 1 + f(n-1)
    f(n) = 1 + f(n/2) // if n is divisible by 2
    f(n) = 1 + f(n/3) // if n is divisible by 3
    """

    if n == 1:
        return 0

    if steps[n] != -1:
        return steps[n]

    res = get_min_steps(n - 1, steps)

    if n % 2 == 0:
        res = min(res, get_min_steps(int(n/2), steps))

    if n % 3 == 0:
        res = min(res, get_min_steps(int(n/3), steps))

    # Increment the step
    steps[n] = 1 + res

    return steps[n]


def fibonacci_dp_recursive(n, fib_array):
    """Calculates fibonacci using DP recursively."""

    if n < 0:
        print('Invalid input!')

    elif (n+1) <= len(fib_array):
        print(fib_array)
        return fib_array[n]

    else:
        current = fibonacci_dp_recursive((n - 1), fib_array) + \
              fibonacci_dp_recursive((n - 2), fib_array)
        fib_array.append(current)
        return current


def fibonacci_dp(n):
    """Calculates fibonacci using DP with a loop."""

    fib_array = [0, 1]

    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    return fib_array[-1]


def decode_ways(digits, n):
    """A message containing letters from A-Z is being encoded to numbers
    using the following mapping:
        A -> 1
        B -> 2
        .
        .
        Z -> 26
    Given a non-empty string containing only digits, determine the total
    number of ways to decode it.
    Input: "226"
    Output: 3
    Explanation: "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    This is recursive and be divided to sub-problems.We keep a table for
    our book- keeping of our counts, incrementally we will add the counter.

    This idea can be implemented either via dynamic programming or recursively.

    Complexity : O(n)
    """

    # n+1 because we will store the final counter in the end once we have
    # seen all the digits
    count_table = [0] * (n+1)
    # Given our def, we can only use two digits to represent an alphabet
    # so lets set the first two counters to 1
    count_table[0] = 1
    count_table[1] = 1

    # Lets continue our iteration from 3rd position
    for i in range(2, n+1):
        count_table[i] = 0
        # If our neighbouring digit to the left is greater than 0
        # we can form a valid digit so we will set our current
        # counter to that
        if (digits[i-1] > '0'):
            # Think of this as copying over what we have seen so far
            count_table[i] = count_table[i-1]

        # Previously we took into account for single digits
        # Lets use some prior knowledge, we can only form a digit starting
        # with 1, or 2 something, but something must be less than 7!
        # We are gonna look back two steps before to see if there was a two
        # digit possibility.
        if (digits[i-2] == '1' or (digits[i-2] == '2' and digits[i-1] < '7')):
            # Now we accumulate
            # This is a bit confusing, maybe you can just accumulate +=1
            # but this is more intuitive in the recursive version where you
            # start from the end and recur for n-2 while accummulating.
            # Another way to think about this, is that we accumulate the count
            # of the digit to the left, which would be 1 or 2, and not the
            # count of the outer digit which may not form another valid digit.
            count_table[i] += count_table[i-2]

    return count_table[n]


def decode_ways_rec(digits, n):
    """The main idea is to start from the outer side of the digit to decide
    whether it should be counted as a valid digit.
    1) If the last digit is non-zero, recur for remaining (n-1) digits
    and add the result to total count.
    2) If the last two digits form a valid character (or smaller than 27),
    recur for remaining (n-2) digits and ADD the result to total count.

    Complexity : exponential
    If you are not sure why, think of Fibonacci numbers and how the recursive
    steps does repeated work!
    """

    if (n == 0 or n == 1):
        return 1

    count = 0
    if digits[n-1] > '0':
        count = decode_ways_rec(digits, n-1)

    if (digits[n-2] == '1' or (digits[n-2] == '2' and digits[n-1] < '7')):
        count += decode_ways_rec(digits, n-2)

    return count
