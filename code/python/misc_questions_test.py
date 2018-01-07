import numpy as np
import unittest

import misc_questions as misc


class StringManipulationTest(unittest.TestCase):

    dump_output = True

    def test_isPowOf3(self):

        self.assertFalse(misc.isPowerOf3_loop(10))

        self.assertTrue(misc.isPowerOf3_int_limit(27))

        self.assertTrue(misc.isPowerOf3_recursive(27))
        self.assertFalse(misc.isPowerOf3_recursive(10))

    def test_rotate_matrix(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = misc.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

        dummy_matrix = np.random.rand(5, 6)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = misc.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

    def test_rotate_matrix_in_place(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = misc.rotate_matrix_in_place(dummy_matrix, 5)
        print('Rotated matrix by 90')
        print(rotated_matrix)


if __name__ == '__main__':
    unittest.main()
