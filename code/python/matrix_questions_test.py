import numpy as np
import unittest

import matrix_questions as matrix_q


class MatrixQuestionsTest(unittest.TestCase):

    dump_output = False

    def test_3x3_matrix(self):
        matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        
        expected = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])

        matrix_q.rotate_matrix_90(matrix)
        np.testing.assert_array_equal(matrix, expected)

        matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        matrix_q.rotate_matrix_in_place(matrix)
        np.testing.assert_array_equal(matrix, expected)

    def test_4x4_matrix(self):
        matrix = np.array([
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])

        expected = np.array([
            [13,  9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])

        matrix_q.rotate_matrix_90(matrix)
        np.testing.assert_array_equal(matrix, expected)

        matrix = np.array([
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])

        matrix_q.rotate_matrix_in_place(matrix)
        np.testing.assert_array_equal(matrix, expected)

    def test_5x5_matrix(self):
        matrix = np.array([
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ])

        expected = np.array([
            [21, 16, 11,  6,  1],
            [22, 17, 12,  7,  2],
            [23, 18, 13,  8,  3],
            [24, 19, 14,  9,  4],
            [25, 20, 15, 10,  5]
        ])

        matrix_q.rotate_matrix_90(matrix)
        np.testing.assert_array_equal(matrix, expected)


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

        shortest_path = matrix_q.find_path_bin_maze_dfs(maze, [0, 0], [3, 4])

        self.assertEqual(shortest_path, 11)

        shortest_path = matrix_q.find_path_bin_maze_dfs(maze, [0, 0], [4, 3])
        # No path found
        self.assertEqual(shortest_path, -1)

    def test_shortest_path_maze_bfs(self):
        maze = [
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ]
        start = (0, 0)
        goal = (4, 4)
        path = matrix_q.shortest_path_maze_bfs(maze, start, goal)
        expected_path = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2),
            (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
        ]
        self.assertEqual(path, expected_path)


    def test_set_matrix_zeros(self):
        matrix = np.asarray([[1, 2, 3, 4, 5], [0, 4, 7, 6, 2], [3, 0, 3, 6, 2],
                             [1, 2, 3, 4, 1]])

        exp_matrix = np.asarray([[0, 0, 3, 4, 5], [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0], [0, 0, 3, 4, 1]])

        mat_out = matrix_q.set_matrix_row_col_all_zeros(matrix)
        np.testing.assert_array_equal(mat_out, exp_matrix)

    def test_set_matrix_zeros_vec(self):
        matrix = np.asarray([[1, 2, 3, 4, 5], [0, 4, 7, 6, 2], [3, 0, 3, 6, 2],
                             [1, 2, 3, 4, 1]])

        exp_matrix = np.asarray([[0, 0, 3, 4, 5], [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0], [0, 0, 3, 4, 1]])

        mat_out = matrix_q.set_matrix_row_col_all_zeros_vec(matrix)
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
        feature_map = matrix_q.convolve2d(matrix, kernel, padding, stride).astype(int)

        padding = (1,1)
        stride = 1
        dilation = 1
        feature_map = matrix_q.convolve2d_V2(matrix, kernel, padding, stride,
                                          dilation).astype(int)


if __name__ == '__main__':
    unittest.main()
