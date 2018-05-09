import numpy as np
import unittest

import misc_questions as misc


class MiscQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_isPowOf3(self):

        self.assertFalse(misc.isPowerOf3_loop(10))

        self.assertTrue(misc.isPowerOf3_int_limit(27))

        self.assertTrue(misc.isPowerOf3_recursive(27))
        self.assertFalse(misc.isPowerOf3_recursive(10))

    def test_two_sum(self):

        array = [1, 3, 7]
        sum_k = 8
        self.assertTrue(misc.two_sum(array, sum_k))

        sum_k = 6
        self.assertFalse(misc.two_sum(array, sum_k))

    def test_find_top_k_min_distance(self):

        top_k = 5
        array = np.asarray([[1, 0], [2, 0], [2, 1],
                            [3, 0], [3, 2], [3, 3],
                            [5, 1], [5, 4], [6, 2],
                            [4, 4], [3, 4], [3.5, 2]])

        location = [4, 2]

        exp_closes_points = np.asarray([[1.41, 3., 3.],
                                        [1.41, 5., 1.],
                                        [0.5, 3.5, 2.],
                                        [2.0, 4., 4.],
                                        [1.0, 3., 2.]])

        closest_points = misc.find_top_k_min_distance(array,
                                                      top_k,
                                                      location)

        np.testing.assert_array_almost_equal(closest_points,
                                             exp_closes_points,
                                             decimal=2)

        if self.dump_output:
            print('Closest points:')
            print(closest_points)

    def test_find_min_overlapping_ranges(self):

        ranges = [[0, 2], [3, 5], [0, 6], [2, 7]]
        exp_ranges = [[0, 7]]

        min_ranges = misc.find_min_overlapping_ranges(ranges)
        self.assertListEqual(min_ranges, exp_ranges)

        if self.dump_output:
            print('Original range-> ', ranges)
            print('New range-> ', min_ranges)

        ranges = [[0, 5], [6, 10], [2, 3]]
        exp_ranges = [[0, 5], [6, 10]]

        min_ranges = misc.find_min_overlapping_ranges(ranges)

        self.assertListEqual(min_ranges, exp_ranges)

        if self.dump_output:
            print('Original range-> ', ranges)
            print('New range-> ', min_ranges)

        ranges = [[1, 2], [6, 10], [0, 5], [4, 5], [10, 12]]
        exp_ranges = [[0, 5], [6, 12]]

        min_ranges = misc.find_min_overlapping_ranges(ranges)
        self.assertListEqual(min_ranges, exp_ranges)

        if self.dump_output:
            print('Original range-> ', ranges)
            print('New range-> ', min_ranges)

        ranges = [[0, 2], [0, 5], [3, 8], [6, 10], [10, 12]]
        exp_ranges = [[0, 12]]

        min_ranges = misc.find_min_overlapping_ranges(ranges)
        self.assertListEqual(min_ranges, exp_ranges)

        if self.dump_output:
            print('New range-> ', min_ranges)

        ranges = [[0, 2], [1, 3], [2, 4], [1, 5]]
        exp_ranges = [[0, 5]]

        min_ranges = misc.find_min_overlapping_ranges(ranges)

        self.assertListEqual(min_ranges, exp_ranges)

        if self.dump_output:
            print('Original range-> ', ranges)
            print('New range-> ', min_ranges)

    def test_chessboard_traveling(self):

        input_string = "(1 1)(2 2)"
        exp_route = 2
        possible_routes = misc.chessboard_traveling(input_string)

        self.assertEqual(possible_routes, exp_route)

        input_string = "(1 1)(3 3)"
        exp_route = 6
        possible_routes = misc.chessboard_traveling(input_string)

        self.assertEqual(possible_routes, exp_route)

        input_string = "(2 2)(4 3)"
        exp_route = 3
        possible_routes = misc.chessboard_traveling(input_string)

        self.assertEqual(possible_routes, exp_route)


if __name__ == '__main__':
    unittest.main()
