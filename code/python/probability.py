"""
Probability, coin tossing questions.
"""
import numpy as np


def prob_more_heads_than_tails(probs, N):
    """Given an array probs of odd length N where
    probs[i] denotes the probability of getting a
    head on the ith coin. As the coins are biased,
    the probability of getting a head is not always
    equal to 0.5. The task is to find the probability
    of getting heads more number of times than tails.
    Input: p[] = {0.3, 0.4, 0.7} 
    Output: 0.442 

    P({head, head, tail}) = 0.3 x 0.4 x (1 - 0.7) = 0.036 
    P({tail, head, head}) = (1 - 0.3) x 0.4 x 0.7 = 0.196 
    P({head, tail, head}) = 0.3 x (1 - 0.4) x 0.7= 0.126 
    P({head, head, head}) = 0.3 x 0.4 x 0.7 = 0.084 
    Adding the above probabilities 
    0.036 + 0.196 + 0.126 + 0.084 = 0.442

    Input: p[] = {0.3, 0.5, 0.2, 0.6, 0.9} 
    Output: 0.495


    The naive way would be to just generate all the permutations.
    The DP version is slightly confusing though.
    To get j heads at the i position, there are two possibilities:  

    1) If number of heads till (i - 1) coins is equal to j
        then a tail comes at i.
    2) If number of heads till (i - 1) coins is equal to (j - 1)
        then a head comes at i.

    Mel: Frankly this is confusing as f***!
    """

    dp = np.zeros((N, N))

    # Base case
    dp[0][0] = 1.0

    for i in range(1, N):
        for j in range(i + 1):
            # If the number of heads is 0
            if j == 0:
                # Just consider the probability of tail
                dp[i][j] = dp[i - 1][j] * (1.0 - probs[i])
            else:
                dp[i][j] = (dp[i - 1][j] * (1.0 - probs[i]) +
                            dp[i - 1][j - 1] * probs[i])

    head_prob = 0

    # When the number of heads is greater than (n+1)/2
    # it means that heads are greater than tails as
    # N of tails + N of heads is equal to N for
    # any permutation of heads and tails
    for i in range(N // 2, N):
        head_prob += dp[N - 1][i]

    return head_prob