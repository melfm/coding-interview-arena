import numpy as np
import unittest

import matrix_questions as matrix_q


class MatrixQuestionsTest(unittest.TestCase):

    dump_output = False

    def test_rotate_matrix(self):

        if self.dump_output:

            dummy_matrix = np.round(np.random.rand(5, 5), 2)
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

        if self.dump_output:

            dummy_matrix = np.round(np.random.rand(5, 5), 2)
            print('Original matrix')
            print(dummy_matrix)

            rotated_matrix = matrix_q.rotate_matrix_in_place(dummy_matrix, 5)
            print('Rotated matrix by 90')
            print(rotated_matrix)

    def test_map_matrix_island_color(self):

        country_map = np.array(
            ([5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4]))

        exp_num_countries = 9
        num_countries = \
            matrix_q.map_matrix_island_color_recursive(country_map)

        self.assertEqual(num_countries, exp_num_countries)

        country_map = np.array(
            ([5, 4, 4], [4, 3, 4], [4, 2, 4], [4, 4, 4], [3, 3, 4], [1, 4, 4]))
        exp_num_countries = 6

        num_countries = \
            matrix_q.map_matrix_island_color_recursive(country_map)

        self.assertEqual(num_countries, exp_num_countries)

    def test_shorted_path_bin_maze(self):

        maze = np.asarray([[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

        shortest_path = matrix_q.shorted_path_bin_maze(maze, [0, 0], [3, 4])

        self.assertEqual(shortest_path, 11)

        shortest_path = matrix_q.shorted_path_bin_maze(maze, [0, 0], [4, 3])
        # No path found
        self.assertEqual(shortest_path, -1)

    def test_set_matrix_zeros(self):
        matrix = np.asarray([[1, 2, 3, 4, 5], [0, 4, 7, 6, 2], [3, 0, 3, 6, 2],
                             [1, 2, 3, 4, 1]])

        exp_matrix = np.asarray([[0, 0, 3, 4, 5], [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0], [0, 0, 3, 4, 1]])

        mat_out = matrix_q.set_matrix_row_col_all_zeros(matrix)
        np.testing.assert_array_equal(mat_out, exp_matrix)

    def test_map_matrix_island_string_version(self):

        connected_xs = matrix_q.map_matrix_island_string_version(
            6, 4, '.....xx..x........x.....')
        self.assertEqual(connected_xs, 2)

        input_string = '........' \
                       '..x...x.' \
                       '.xxx..x.' \
                       '.....xx.' \
                       '.x..xx..' \
                       '...xx...' \
                       '.xxx..x.' \
                       '........'
        connected_xs = matrix_q.map_matrix_island_string_version(
            8, 8, input_string)
        self.assertEqual(connected_xs, 4)

        connected_xs = matrix_q.map_matrix_island_string_version(
            3, 3, '.........')
        self.assertEqual(connected_xs, 0)

    def test_spiral(self):

        out_mat = matrix_q.spiral(4)
        if self.dump_output:
            print('Spiral Matrix \n', out_mat)

    def test_convolve2d(self):
        matrix = np.array([[1, 4, 4, 2], [0, 2, 0, 2], [3, 3, 1, 1]])
        kernel = np.array([[0, 1], [1, 3]])

        exp_matrix = np.array([[10, 6, 8], [14, 6, 6]])

        feature_map = matrix_q.convolve2d_vanilla(matrix, kernel).astype(int)
        np.testing.assert_array_equal(feature_map, exp_matrix)

        padding = (1,1)
        stride = 1
        dilation = 0
        feature_map = matrix_q.convolve2d(matrix, kernel, padding, stride,
                                          dilation).astype(int)

        # padding = (1,1)
        # stride = 1
        # dilation = 1
        # feature_map = matrix_q.convolve2d(matrix, kernel, padding, stride,
        #                                   dilation).astype(int)


if __name__ == '__main__':
    unittest.main()
