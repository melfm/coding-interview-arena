import numpy as np
import unittest

import matrix_questions as matric_q


class MatrixQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_rotate_matrix(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matric_q.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

        dummy_matrix = np.random.rand(5, 6)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matric_q.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

    def test_rotate_matrix_in_place(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matric_q.rotate_matrix_in_place(dummy_matrix, 5)
        print('Rotated matrix by 90')
        print(rotated_matrix)


if __name__ == '__main__':
    unittest.main()
