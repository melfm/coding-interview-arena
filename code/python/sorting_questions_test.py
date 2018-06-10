import unittest
import numpy as np

import sorting_questions as sorting


class SortingTest(unittest.TestCase):

    dump_output = True

    def test_merge_and_sort(self):

        array1 = [1, 3, 5]
        array2 = [2, 5, 6, 7, 20]

        sorted_arr = sorting.merge_and_sort(array1, array2)
        if self.dump_output:
            print("sorted ", sorted_arr)

    def test_insertion_sort(self):

        array = [12, 11, 13, 5, 6]

        sorted_arr = sorting.insertion_sort(array)
        print(sorted_arr)

        string = 'sheep'
        string_list = list(string)

        sorted_string = sorting.insertion_sort(string_list)
        print(sorted_string)

    def test_heap_sort(self):

        array = [12, 11, 13, 5, 6, 7]
        exp_array = [5, 6, 7, 11, 12, 13]
        sorted_array = sorting.heap_sort(array)

        if self.dump_output:
            print("Heap Sort ->", sorted_array)

        np.testing.assert_array_equal(sorted_array,
                                      exp_array)

    def test_sort_in_lexicographic_order(self):

        input_string = ['a1 b2', 'a0 z6', 'x5 rt', 's2 r1']
        exp_sorted = ['a0 z6', 'a1 b2', 's2 r1', 'x5 rt']

        sorted_str = sorting.sort_in_lexicographic_order(input_string)
        self.assertEqual(sorted_str, exp_sorted)

        input_string = ['t1 ao2', 'mi1 mi2', 'm1 mi2',
                        'mxz4 5 4', 'xi xi2', 'x4 45 34 3',
                        'w1 has uni gry', 'b4 3 3',
                        'x2 45 34 3', 'x2 22 34 3']

        exp_sorted = ['b4 3 3', 'm1 mi2', 'mi1 mi2',
                      'mxz4 5 4', 't1 ao2', 'w1 has uni gry',
                      'x2 22 34 3', 'x2 45 34 3', 'x4 45 34 3',
                      'xi xi2']

        sorted_str = sorting.sort_in_lexicographic_order(input_string)

        self.assertEqual(sorted_str, exp_sorted)


if __name__ == '__main__':
    unittest.main()
