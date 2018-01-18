import numpy as np
import unittest

import matrix_questions as matrix_q


class MatrixQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_rotate_matrix(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matrix_q.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

        dummy_matrix = np.random.rand(5, 6)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matrix_q.rotate_matrix(dummy_matrix)
        print('Rotated matrix by 90')
        print(rotated_matrix)

    def test_rotate_matrix_in_place(self):

        dummy_matrix = np.random.rand(5, 5)
        print('Original matrix')
        print(dummy_matrix)

        rotated_matrix = matrix_q.rotate_matrix_in_place(dummy_matrix, 5)
        print('Rotated matrix by 90')
        print(rotated_matrix)

    def test_map_matrix_island_color(self):

        country_map = np.array(([5, 4, 4],
                                [4, 3, 4],
                                [3, 2, 4],
                                [2, 2, 2],
                                [3, 3, 4],
                                [1, 4, 4]))

        num_of_countries = matrix_q.map_matrix_island_color(country_map)


if __name__ == '__main__':
    unittest.main()
