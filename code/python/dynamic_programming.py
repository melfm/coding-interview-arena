import numpy as np


def get_min_steps_mem(n):
    """Minimum steps to minimize n as per given condition.
    If n is divisible by 2 then we may reduce n to n/2.
    If n is divisible by 3 then you may reduce n to n/3.
    Decrement n by 1.
    Technique: Memoization"""

    pass


def get_min_steps_dp(n):
    """Get minimum steps to reduce an int to 1.
    Technique: Dynamic programming."""

    dp = np.zeros([n])

    dp[1] = 0

    for i in range(n):
        dp[i] = 1 + dp[i-1]
        if i % 2:
            dp[i] = min(dp[i], 1 + dp[i/2])
        if i % 3:
            dp[i] = min(dp[i], 1 + dp[i/3])

    return dp[n]


def fibonacci_dp_recursive(n, fib_array, first_time):
    """Calculates fibonacci using DP recursively."""

    if first_time:
        # Hack because its doing n - 1 ??
        n += 1
        first_time = False

    if n < 0:
        print('Invalid input!')

    elif n <= len(fib_array):
        # print(fib_array)
        return fib_array[n - 1]

    else:
        tmp = fibonacci_dp_recursive((n - 1), fib_array, False) + \
              fibonacci_dp_recursive((n - 2), fib_array, False)
        fib_array.append(tmp)
        return tmp


def fibonacci_dp(n):
    """Calculates fibonacci using DP wiht a loop."""

    fib_array = [0, 1]

    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    return fib_array[-1]
