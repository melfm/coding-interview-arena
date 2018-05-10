"""Maths & Probability Questions."""

import numpy as np


def divisible_by_r(m, n):
    """Q: Given two numbers m and n, write a method to return the first
    number r that is divisible by both - > Least common multiple
    """
    def gcd(m, n):
        if n == 0:
            return m
        else:
            return gcd(n, m % n)

    return m * n / gcd(m, n)


def generate_rand_7():
    """Write a method to generate a random number between 1 and 7, given a
    method that generates a random number between 1 and 5 (i.e., implement
    rand7() using rand5()).

    Solution based on accept-reject algorithm.
    """

    while(True):
        # This generates a random number uniformly distributed between 1 and 24.
        # The first term is 5 times a rand num between 1 - 4, yielding {5, 10,
        # 15, 20}. The second is a rand num between 1 - 4.
        # Since the two numbers are *independent*, adding them gives a rand num
        # uniformly distributed between 1 - 24.
        # The test then rejects any number that is 21 or above. This is then
        # divided into 7 numbers between 1 - 7 using % 7. Since there are 21
        # numbers in the interval [1, 21] and 21 is divisble by 7, the numbers
        # between 1 and 7 will occur with equal probability.
        num = 5 * (np.random.uniform(1, 5, 1) - 1) +\
            (np.random.uniform(1, 5, 1) - 1)
        if num[0] < 21:
            return int(num[0] % 7 + 1)


def sample_distribution(numbers, probabilities, num_samples):
    """Given a list of numbers and corresponding probabilities, sample
    'num_samples' numbers. Note that the probabilities sum to 1.
    """

    # Generate a random num between 0 - 1
    rand_prob = np.random.random_sample((1,))
    intervals = []
    intervals.append(probabilities[0])
    new_interval = probabilities[0]

    for i in range(1, len(probabilities)):
        new_interval += probabilities[i]
        intervals.append(new_interval)

    counter = 0
    new_numbers = []
    while counter <= num_samples:
        for i in range(len(intervals)):
            if rand_prob <= [intervals[i]]:
                new_numbers.append(numbers[i])
                counter += 1

    return new_numbers
