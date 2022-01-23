#!/bin/python3
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

    while (True):
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
            rand_prob = np.random.random_sample((1, ))
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
    while (n / idx >= 1):
        count += math.floor(n / idx)
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

    mid_point = int(num_size / 2)

    def list_to_int(nums):
        return int(''.join(str(i) for i in nums))

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
        splitted = num_list[0:mid_point]
        mirrored = splitted + splitted[::-1]

        all_palindromes = []
        all_palindromes.append(mirrored)

        if splitted[-1] != 9:
            split_add_one = list(splitted)
            split_add_one[-1] += 1
            split_add_one = all_palindromes.append(split_add_one +
                                                   split_add_one[::-1])

        if splitted[-1] != 0:
            split_sub_one = list(splitted)
            split_sub_one[-1] -= 1
            split_sub_one = all_palindromes.append(split_sub_one +
                                                   split_sub_one[::-1])

    else:
        # Odd number
        splitted = num_list[0:mid_point]
        middle_num = num_list[mid_point]

        all_palindromes = []
        all_palindromes.append(splitted + [middle_num] + splitted[::-1])

        if middle_num != 9:
            all_palindromes.append(splitted + [middle_num + 1] +
                                   splitted[::-1])

        if middle_num != 0:
            all_palindromes.append(splitted + [middle_num - 1] +
                                   splitted[::-1])

    return check_palindromes(all_palindromes, number)


"""Orientation of 3 ordered points.
Orientation of an ordered triplet of points in the plane can be
    - counterclockwise
    - clockwise
    - collinear
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_coord(self):
        print('[', self.x, ',', self.y, ']')


def orientation3ps(p1, p2, p3):
    # Returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # This is done based on a formula comparing the slope
    # angles between points

    val = (float(p2.y - p1.y) * (p3.x - p2.x)) - \
           (float(p2.x - p1.x) * (p3.y - p2.y))

    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0


"""
Convex Hull Question.
Given a set of points in the plane, the convex hull of the
set is the smallest convex polygon that contains all the
points of it. Jarvis's Algorithm or Wrapping.

Step 1) Initialize p as leftmost point.
Step 2) The next point q is the point such that the triplet
    (p, q, r) is counterclockwise for any other point r.
    To find this initialize q as next point, traverse thru
    all the points. For any point i, if its more counterclockwise
    i.e. orientation(p, i, q) is counterclockwise then update
    q as i. Final value of q is going to be the most
    counterclockwise point.
"""


def left_index(points):
    min_p = 0

    for i in range(len(points)):
        point = points[i]
        if point.x < points[min_p].x:
            min_p = i
        elif point.x == points[min_p].x:
            # now check Y
            if point.y < points[min_p].y:
                min_p = i
    return min_p


def convex_hull(points, n):

    # Need at least 3 points
    if n < 3: return

    left_p = left_index(points)

    convex_hull_ps = []

    # Start from leftmost keep moving counterclockwise.
    p = left_p
    q = 0

    while (True):
        convex_hull_ps.append(p)
        # Keep track of last visited most counterclockwise
        # mod n stops it from going outside of bound of set
        q = (p + 1) % n

        for i in range(n):
            if (orientation3ps(points[p], points[i], points[q]) == 2):
                q = i

        # q is now the most counterclockwise, lets move on to the
        # next set of points
        p = q

        # Back to the first point
        if (p == left_p): break

    print('Convex hull points: ')
    for i in convex_hull_ps:
        print(points[i].x, points[i].y)


def look_and_say(n):
    """
    Implement a function that outputs the Look and Say sequence.
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    31131211131221
    13211311123113112211
    """

    # Base cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    prev_term = "11"

    for i in range(3, n + 1):
        # Add a dummy character to allow extra iteration
        # without this, your very first loop will exit
        prev_term += '$'
        seq_end = len(prev_term)

        count = 1
        seq_n = ''

        for j in range(1, seq_end):
            if (prev_term[j] != prev_term[j - 1]):
                seq_n += str(count)
                seq_n += prev_term[j - 1]
                count = 1
            else:
                count += 1

        print('\n LNS: ', seq_n)
        prev_term = seq_n

    print('\n')
    return prev_term


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def ice_cream_parlor(m, cost):

    cost_map = {}
    index_x = index_y = None

    for i in range(len(cost)):

        x = cost[i]
        y_sol = -x + m

        if y_sol in cost_map.values():
            index_x = i
            index_y = get_key_from_value(cost_map, y_sol)
            output = [index_x, index_y]
            return output
        else:
            # If the solution doesn't already exist
            # check for multiples of y
            for any_y in cost_map.values():
                if y_sol > 0 and y_sol % any_y == 0:
                    index_x = i
                    index_y = get_key_from_value(cost_map, any_y)
                    output = [index_x, index_y]
                    return output

        cost_map.update({i: x})

    # Solution not found
    output = [index_x, index_y]
    return output