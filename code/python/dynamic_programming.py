import numpy as np


def get_min_steps_mem(n):
    """Minimum steps to minimize n as per given condition.
    - If n is divisible by 2 then we may reduce n to n/2.
    - If n is divisible by 3 then you may reduce n to n/3.
    - Else decrement n by 1.
    Technique: Memoization"""

    steps = np.full(n + 1, -1)
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
        res = min(res, get_min_steps(int(n / 2), steps))

    if n % 3 == 0:
        res = min(res, get_min_steps(int(n / 3), steps))

    # Increment the step
    steps[n] = 1 + res

    return steps[n]


def fibonacci_dp_recursive(n, fib_array):
    """Calculates fibonacci using DP recursively."""

    if n < 0:
        print('Invalid input!')

    elif (n + 1) <= len(fib_array):
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
    count_table = [0] * (n + 1)
    # Given our def, we can only use two digits to represent an alphabet
    # so lets set the first two counters to 1
    count_table[0] = 1
    count_table[1] = 1

    # Lets continue our iteration from 3rd position
    for i in range(2, n + 1):
        count_table[i] = 0
        # If our neighbouring digit to the left is greater than 0
        # we can form a valid digit so we will set our current
        # counter to that
        if (digits[i - 1] > '0'):
            # Think of this as copying over what we have seen so far
            count_table[i] = count_table[i - 1]

        # Previously we took into account for single digits
        # Lets use some prior knowledge, we can only form a digit starting
        # with 1, or 2 something, but something must be less than 7!
        # We are gonna look back two steps before to see if there was a two
        # digit possibility.
        if (digits[i - 2] == '1'
                or (digits[i - 2] == '2' and digits[i - 1] < '7')):
            # Now we accumulate
            # This is a bit confusing, maybe you can just accumulate +=1
            # but this is more intuitive in the recursive version where you
            # start from the end and recur for n-2 while accummulating.
            # Another way to think about this, is that we accumulate the count
            # of the digit to the left, which would be 1 or 2, and not the
            # count of the outer digit which may not form another valid digit.
            count_table[i] += count_table[i - 2]

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
    if digits[n - 1] > '0':
        count = decode_ways_rec(digits, n - 1)

    if (digits[n - 2] == '1'
            or (digits[n - 2] == '2' and digits[n - 1] < '7')):
        count += decode_ways_rec(digits, n - 2)

    return count


def alive_probs_check(x, y, n, step, map):

    if (step == 0):
        return 1.0

    key = str(x) + "," + str(y) + "," + str(step)
    if key in map.keys():
        return map[key]

    probability = 0.0

    if (x >= 0):
        probability += 0.25 * alive_probs_check(x - 1, y, n, step - 1, map)
    if x < (n - 1):
        probability += 0.25 * alive_probs_check(x + 1, y, n, step - 1, map)
    if (y >= 0):
        probability += 0.25 * alive_probs_check(x, y - 1, n, step - 1, map)
    if y < (n - 1):
        probability += 0.25 * alive_probs_check(x, y + 1, n, step - 1, map)

    map[key] = probability

    # print('Current map : ', len(map))
    # for item in map:
    #     print(item)

    return probability


def alive_probability(x, y, N):
    """
    There is an island represented by square matrix NxN.
    A person is standing at a given location (x,y).
    He can move one step up/down/left/right with equal
    probability. If he steps outside of the grid he dies.
    What's the probability that he is alive after n steps?

    Probability of locations of a 4x4 matrix, after 1 step:

        -------------------------------------
        |        |        |        |        |
        |  0.50  |  0.75  |  0.75  |  0.50  |
        |        |        |        |        |
        -------------------------------------
        |        |        |        |        |
        |  0.75  |  1.00  |  1.00  |  0.75  |
        |        |        |        |        |
        -------------------------------------
        |        |        |        |        |
        |  0.75  |  1.00  |  1.00  |  0.75  |
        |        |        |        |        |
        -------------------------------------
        |        |        |        |        |
        |  0.50  |  0.75  |  0.75  |  0.50  |
        |        |        |        |        |
        -------------------------------------
    """

    if (x < 0 or x > (N - 1) or y < 0 or y > (N - 1) or N < 1):
        return 0.0
    return alive_probs_check(x, y, N, N, {})


def unique_paths_with_obstacles(grid):
    """
    You are designing an autonomous vehicle's path-planning algorithm.
    The vehicle must navigate from the top-left corner of a m x n grid to
    the bottom-right corner while avoiding obstacles.

    The grid consists of:
        0 (open cell): The vehicle can move to this cell.
        1 (obstacle): The vehicle cannot move through this cell.
    The vehicle can only move right or down at each step.
    Return the number of unique paths from the top-left to the bottom-right.
    """
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    # Fill DP table
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0  # No path through obstacles
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # Paths from top
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # Paths from left

    return dp[m-1][n-1]

def unique_paths_with_obstacles_op2(grid):
    # Instead of maintaining a full 2D DP table,
    # we reuse a single row (1D array) to store intermediate results.
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n  # Only storing one row
    dp[0] = 1  # Start position

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0  # Obstacle blocks the path
            elif j > 0:
                dp[j] += dp[j - 1]  # Accumulate paths from the left

    return dp[-1]