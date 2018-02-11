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
