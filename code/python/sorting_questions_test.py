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


if __name__ == '__main__':
    unittest.main()
