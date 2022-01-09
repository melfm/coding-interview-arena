"""Bit manipulation Questions."""

import math
import numpy as np
import sys
"""
You are given an integer array, where all numbers except for TWO numbers
appear even number of times. Find out the two numbers which appear odd number
of times. Ideal time complexity O(n), Space complexity O(1).

Binary manipulation solution below.
Simpler solution at the cost of space:

- Create a hash set
- Loop the integers
-- If the element is in the hash set, remove it
-- Otherwise, add it (since it's not already present)
- The answer is the contents of the hash set (which scales to any number of
  odd numbers)

Space Complexity: O(n) (due to an O(1) get/put hash set).
"""


def getBitAtPosition(x, position):
    return (x >> position) & 1


def findFirstBitWithSetBit(x):
    position = 0
    while ((x & 1) != 1):
        position += 1
        # bitwise right shift by 1
        x = x >> 1
    return position


def find_two_odds(list_a):
    xor = None
    for i in range(len(list_a)):
        if xor == None:
            xor = list_a[i]
        else:
            print("List val ", list_a[i], "binary ", "{0:b}".format(list_a[i]))
            print("XOR ", xor, "binary ", "{0:b}".format(xor))
            xor ^= list_a[i]

    # Find the first bit position in the result that is 1.
    position = findFirstBitWithSetBit(xor)

    xor0 = None
    xor1 = None
    # XOR the elements that have 1 at x bit position and
    # XOR the elements that have 0 at x bit position.
    for i in range(len(list_a)):
        if (getBitAtPosition(list_a[i], position) == 0):
            if xor0 == None:
                xor0 = list_a[i]
            else:
                xor0 ^= list_a[i]

        else:
            if xor1 == None:
                xor1 = list_a[i]
            else:
                xor1 ^= list_a[i]

    print('XOR0: ', xor0)
    print('XOR1: ', xor1)