import numpy as np


n = 10
memo = np.full(n + 1, fill_value=-1)


def get_min_steps_mem(n):
    """Memoization"""

    if n == 1:
        return 0

    if memo[n] != -1:
        return memo[n]

    # x - 1 step
    # r will contain the optimal answer finally
    r = 1 + get_min_steps_mem(n - 1)
    if n % 2 == 0:
        # x/2 step
        r = min(r, 1 + get_min_steps_mem(n/2))
    if n % 3 == 0:
        r = min(r, 1 + get_min_steps_mem(n/3))

    # Save the result, this is the different step from
    # simple recursion
    memo[n] = r
    return r


def get_min_steps_dp(n):

    dp = np.zeros([n])

    dp[1] = 0

    for i in range(n):
        dp[i] = 1 + dp[i-1]
        if i % 2:
            dp[i] = min(dp[i], 1 + dp[i/2])
        if i % 3:
            dp[i] = min(dp[i], 1 + dp[i/3])

    return dp[n]


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    mem_res = get_min_steps_mem(10)
    print('mem_res ', mem_res)
    db_res = get_min_steps_dp(10)
