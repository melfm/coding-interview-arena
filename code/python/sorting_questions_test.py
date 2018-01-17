import unittest

import sorting_questions as sorting


class SortingTest(unittest.TestCase):

    dump_output = True

    def test_merge_and_sort(self):

        array1 = [1, 3, 5]
        array2 = [2, 5, 6, 7, 20]

        sorted_arr = sorting.merge_and_sort(array2, array1)
        print("sorted ", sorted_arr)


if __name__ == '__main__':
    unittest.main()
