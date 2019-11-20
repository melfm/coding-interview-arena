"""Maths & Probability Questions."""

import math
import numpy as np
import sys


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
            # Generate a random num between 0 - 1
            # i.e. flip a coin.
            rand_prob = np.random.random_sample((1,))
            if rand_prob <= [intervals[i]]:
                new_numbers.append(numbers[i])
                counter += 1

    return new_numbers


def factorial_trailing_zero(n):
    """Given an integer n, return the number of trailing zeroes in n!.
    A simple method is to first calculate factorial of n, then count
    trailing 0s in the result. But this can cause overflow for a big
    numbers as the factorial becomes large.
    Instead consider prime factors, a trailing zero is produced by 2
    and 5. It turns out the number of 2s in prime factors is always
    more than or equal to the number of 5s, so we just need to count 5s.
    Finally, we also need to consider numbers like 25, 125 etc that have
    more than one 5 (consider 28!). To handle this, we start by dividing
    by 5, and then multiples of 5, like 25 and so on.
    The formula becomes: floor(n/5) + floor(n/25) + floor(n/125) ....
    """

    count = 0
    idx = 5
    while(n/idx >= 1):
        count += math.floor(n/idx)
        idx *= 5

    return count


def closest_palindrome_number(number):
    """Given a number, find the closest Palindrome number whose absolute
    difference with given number is minimum and absolute difference must
    be greater than 0.
        Input: 121
        Output: [131, 111]

        Input: 1234
        Outpyt: 1221
    The trick here to mirror the first half of the digit onto the second half.
    Turns out this will always give you the shortest distane you need to the
    number, and obviously we would not want to mirror the second half for this
    reason. Once we mirror, say 121 stays 121, then out next options are adding
    and subtracting one from this middle number to get 111 and 131. We can
    then check for min distance.
    """

    def check_all_9(number):

        for n in number:
            if n != 9:
                return False
        return True

    num_list = [int(i) for i in str(number)]

    num_size = len(num_list)

    if check_all_9(num_list):
        return number + 2

    mid_point = int(num_size/2)

    def list_to_int(nums): return int(''.join(str(i) for i in nums))

    def check_palindromes(all_palindromes, number):
        min_found = sys.maxsize
        pal_found = 0
        multiple_pals = []

        for i in all_palindromes:
            pal = list_to_int(i)
            distance = abs(number - pal)
            if distance <= min_found and distance != 0:
                if distance == min_found:
                    multiple_pals.append(i)
                else:
                    multiple_pals = []
                    min_found = distance
                    pal_found = i
                    multiple_pals.append(i)

        if len(multiple_pals) == 1:
            return list_to_int(pal_found)
        else:
            numbers = []
            for i in multiple_pals:
                number = list_to_int(i)
                numbers.append(number)
            return numbers

    if num_size % 2 == 0:

        # Even number
        splitted = num_list[0: mid_point]
        mirrored = splitted + splitted[::-1]

        all_palindromes = []
        all_palindromes.append(mirrored)

        if splitted[-1] != 9:
            split_add_one = list(splitted)
            split_add_one[-1] += 1
            split_add_one = all_palindromes.append(
                split_add_one + split_add_one[::-1])

        if splitted[-1] != 0:
            split_sub_one = list(splitted)
            split_sub_one[-1] -= 1
            split_sub_one = all_palindromes.append(
                split_sub_one + split_sub_one[::-1])

    else:
        # Odd number
        splitted = num_list[0: mid_point]
        middle_num = num_list[mid_point]

        all_palindromes = []
        all_palindromes.append(
            splitted + [middle_num] + splitted[::-1])

        if middle_num != 9:
            all_palindromes.append(
                splitted + [middle_num + 1] + splitted[::-1])

        if middle_num != 0:
            all_palindromes.append(
                splitted + [middle_num - 1] + splitted[::-1])

    return check_palindromes(all_palindromes, number)
