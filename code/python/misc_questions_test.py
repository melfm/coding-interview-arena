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

if __name__ == '__main__':
    unittest.main()
