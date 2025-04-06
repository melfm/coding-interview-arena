import numpy as np
import time
import unittest
from collections import Counter

import array_questions as array_qs


class ArraysTest(unittest.TestCase):

    dump_output = False
    test_runtime = False

    def test_find_largest_sub_input_array_sum(self):

        input_array = [-1, 3, -4, 6, 7, 8]
        exp_sum = 21

        max_sum = array_qs.find_largest_sub_array_sum(input_array)
        self.assertEqual(max_sum, exp_sum)
        if self.dump_output:
            print("Max so far ", max_sum)

        input_array = [-1, 6, 7, 8, -3, -4, 2, 4]
        exp_sum = 21

        max_sum = array_qs.find_largest_sub_array_sum(input_array)
        self.assertEqual(max_sum, exp_sum)
        if self.dump_output:
            print("Max so far ", max_sum)

        input_array = [-1, 6, -7, 8, -3, -4, 2]
        exp_sum = 8

        max_sum = array_qs.find_largest_sub_array_sum(input_array)
        self.assertEqual(max_sum, exp_sum)
        if self.dump_output:
            print("Max so far ", max_sum)

    def test_find_largest_sum_sub_array(self):

        input_array = [-1, 6, -7, 8, -3, -4, 2]
        exp_sum = 8
        exp_start = 3
        exp_end = 3

        max_sum, start, end = array_qs.find_largest_sum_sub_array(input_array)
        self.assertEqual(max_sum, exp_sum)
        self.assertEqual(start, exp_start)
        self.assertEqual(end, exp_end)

        if self.dump_output:

            print("Max so far {} with indices {},{} ".format(
                max_sum, start, end))

        input_array = [-1, 6, -7, 8, 3, -4, 2]
        exp_sum = 11
        exp_start = 3
        exp_end = 4

        max_sum, start, end = array_qs.find_largest_sum_sub_array(input_array)
        self.assertEqual(max_sum, exp_sum)
        self.assertEqual(start, exp_start)
        self.assertEqual(end, exp_end)

        if self.dump_output:

            print("Max so far {} with indices {},{} ".format(
                max_sum, start, end))

        input_array = [-1, 6, 7, 8, 3, -4, 2]
        exp_sum = 24
        exp_start = 1
        exp_end = 4

        max_sum, start, end = array_qs.find_largest_sum_sub_array(input_array)
        self.assertEqual(max_sum, exp_sum)
        self.assertEqual(start, exp_start)
        self.assertEqual(end, exp_end)

        if self.dump_output:
            print("Max so far {} with indices {},{} ".format(
                max_sum, start, end))

    def test_add_one(self):

        array = [1, 2, 3, 4]
        exp_ans = [1, 2, 3, 5]

        answer = array_qs.add_one(array)
        np.testing.assert_array_equal(answer, exp_ans)

        array = [1, 9, 9]
        exp_ans = [2, 0, 0]

        answer = array_qs.add_one(array)
        np.testing.assert_array_equal(answer, exp_ans)

        array = [9, 9, 9]
        exp_ans = [1, 0, 0, 0]

        answer = array_qs.add_one(array)
        np.testing.assert_array_equal(answer, exp_ans)

    def test_find_smallest_pos(self):

        array = [0, 1, 3, 6, 4, 1, 2]
        small_pos = array_qs.find_smallest_pos(array)
        self.assertEqual(small_pos, 5)

        array = [1, 2, 3]
        small_pos = array_qs.find_smallest_pos(array)
        self.assertEqual(small_pos, 4)

        array = [-1, -3]
        small_pos = array_qs.find_smallest_pos(array)
        self.assertEqual(small_pos, 1)

        array = [0, 1, 3, 6, 4, 1, 2]
        small_pos = array_qs.find_smallest_pos_v2(array)
        self.assertEqual(small_pos, 5)

        if self.test_runtime:
            print('Running runtime test ....')
            array = np.random.randint(0, 100000, size=1000000)
            start = time.time()
            small_pos = array_qs.find_smallest_pos(array)
            print('find_smallest_pos took ', time.time() - start)
            start = time.time()
            small_pos = array_qs.find_smallest_pos_v2(array)
            print('find_smallest_pos_v2 took ', time.time() - start)

    def test_max_frequent_number(self):

        input_array = [1, 1, 2, 2, 3, 3, 3]
        exp_output = {3: 3}

        max_nums = array_qs.max_frequent_number(input_array)
        self.assertDictEqual(max_nums, exp_output)

        input_array = [1, 1, 2, 2, 3, 4]
        exp_output = {1: 2, 2: 2}

        max_nums = array_qs.max_frequent_number(input_array)
        self.assertDictEqual(max_nums, exp_output)

        input_array = [11, 9, 8, 5, 5, 6, 5]
        exp_output = {5: 3}

        max_nums = array_qs.max_frequent_number(input_array)
        self.assertDictEqual(max_nums, exp_output)

    def test_shuffle_cards(self):

        input_array = [1, 2, 3, 4, 5, 6]
        exp_shuffled = [4, 1, 5, 2, 6, 3]
        shuffled = array_qs.shuffle_cards(input_array)
        self.assertEqual(shuffled, exp_shuffled)

        input_array = [1, 2, 3, 4, 5]
        exp_shuffled = [3, 1, 4, 2, 5]
        shuffled = array_qs.shuffle_cards(input_array)
        self.assertEqual(shuffled, exp_shuffled)

    def test_smallest_odd_occurrence(self):

        input_array = [1, 1, 2, 2, 3, 4, 5, 6, 6, 5, 4]
        small_odd_occur = array_qs.smallest_odd_occurrence(input_array)
        self.assertEqual(small_odd_occur, 3)

        input_array = [2, 3, 2, 2, -4, -4]
        small_odd_occur = array_qs.smallest_odd_occurrence(input_array)
        self.assertEqual(small_odd_occur, 2)

        input_array = [20, -10, -10, 30, 10]
        small_odd_occur = array_qs.smallest_odd_occurrence(input_array)
        self.assertEqual(small_odd_occur, 10)

    def test_combine_sum_pieces(self):

        input_array = [6, 2, 9]
        sum_array = [1, 4, 17, 3]
        exp_combos = [[6, 2, 9], [2, 2]]
        combinations = array_qs.combine_sum_pieces(input_array, sum_array)
        self.assertEqual(combinations, exp_combos)

        input_array = [4, 5, 6, 1, 3]
        sum_array = [9, 15, 12, 8]
        exp_combos = [[4, 4], [4, 5], [4, 5, 6], [4, 5, 3], [4, 1,
                                                             3], [5, 6, 1],
                      [5, 6, 1, 3], [5, 1, 3], [5, 3], [6, 6], [6, 3]]
        combinations = array_qs.combine_sum_pieces(input_array, sum_array)
        self.assertEqual(combinations, exp_combos)

    def test_max_subarray_sum(self):
        array = [-2, -3, 4, -1, -2, 1, 5, -3]
        max_sum = array_qs.max_subarray_sum(array)
        self.assertEqual(max_sum, 7)

    def test_find_two_disjoint_subarray_max(self):
        arr = [2, -1, -2, 1, -4, 2, 8]
        max_subarray_sum = array_qs.find_two_disjoint_subarray_max(arr)
        # For the example above, we'd expect the following 4 arrays.
        # max_left  = [2, 2, 2, 2, 2, 2, 10]
        # min_right = [-6, -6, -5, -4, -4, 2, 8]

        # min_left  = [2, -1, -3, -3, -6, -6, -6]
        # max_right = [10, 10, 10, 10, 10, 10, 8]
        self.assertEqual(max_subarray_sum, 16)


    def test_pick_random_max(self):
        arr = [5, 1, 5, 3, 5]
        max_indices = [0, 2, 4]
        max_value = 5
        num_trials = 10_000
        counts = Counter()

        for _ in range(num_trials):
            result_indx = array_qs.pick_random_max(arr)
            result = arr[result_indx]
            self.assertEqual(result, max_value)
            # Count how often each index is picked
            for idx in max_indices:
                if idx == result_indx:
                    counts[idx] += 1
                    break

        # Check approximate uniformity — within 5% margin
        expected = num_trials / len(max_indices)
        for idx in max_indices:
            picked = counts[idx]
            ratio_diff = abs(picked - expected) / expected
            self.assertTrue(
                ratio_diff < 0.05,
                f"Index {idx} was picked {picked} times, expected ~{expected}"
            )


if __name__ == '__main__':
    unittest.main()
