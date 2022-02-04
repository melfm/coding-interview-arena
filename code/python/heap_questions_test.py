import numpy as np
import unittest

import heap_questions as heap_qs


class HeapQuestionsTest(unittest.TestCase):

    def test_find_smallest_range_k_lists(self):
        list1 = [4, 10, 15, 24, 26]
        list2 = [0, 9, 12, 20]
        list3 = [5, 18, 22, 30]

        min_range = heap_qs.find_smallest_range_k_lists(list1, list2, list3)


if __name__ == '__main__':
    unittest.main()