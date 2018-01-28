import unittest

import array_questions as array_qs


class ArraysTest(unittest.TestCase):

    dump_output = True

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


if __name__ == '__main__':
    unittest.main()
