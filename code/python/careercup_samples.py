"""
Question:


This can be solved easily as below.
1. initialize smallest_range as MAX_INT
2. keep 3 pointers/index p1, p2 and p3 which points to the first elements of lists L1, L2 and L3 respectively.
3. find the max value and min value pointed/indexed by p1, p2 and p3
4. difference of max value and min value discovered in step 3 is the current range. compare it with smallest_range and update it, if found smaller.
5. increment the pointer/index of min value found in step 3.
6. repeat step 3 to 5 until the pointer/index of min value is in range.

constant space and O(n) time.
"""













"""

Maximum subarray problem
Given an array of integers. Find two disjoint contiguous sub-arrays such that the absolute difference between the sum of two sub-array is maximum.

The sub-arrays should not overlap and it can not be empty.

eg [2 -1 -2 1 -4 2 8]

ans (-1 -2 1 -4) (2 8)

diff = 16

Better than O(n2) solution was expected.

"""