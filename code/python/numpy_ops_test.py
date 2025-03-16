
import numpy as np
import numpy_ops as npop
import unittest


class NumpyOpsTest(unittest.TestCase):

    dump_output = False

    def test_subsample_traj(self):

        # ---------------------------
        # Example input/output:
        # Trajectory: (0, 1, 2) (1, 2, 3) (2, 3, 4) (4, 5, 6) (5, 6, 7)
        # Output with stride 1 -> (1, 1, 1) (1, 1, 1) (2, 2, 2)
        # This means the difference from going from i to i+s
        # Output with stride 2, offset 0 -> (2, 2, 2) (3, 3, 3)
        # ---------------------------
        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v1(trajectory, stride=1, offset=0)
        expected = [(1, 1, 1), (1, 1, 1), (2, 2, 2), (1, 1, 1)]
        self.assertEqual(diff, expected)

        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v1(trajectory, stride=2, offset=0)
        expected = [(2, 2, 2), (3, 3, 3)]
        self.assertEqual(diff, expected)

        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v1(trajectory, stride=3, offset=0)
        expected = [(4, 4, 4)]
        self.assertEqual(diff, expected)


        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v2(trajectory, stride=1, offset=0)
        expected = [(1, 1, 1), (1, 1, 1), (2, 2, 2), (1, 1, 1)]
        self.assertEqual(diff, expected)

        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v2(trajectory, stride=2, offset=0)
        expected = [(2, 2, 2), (3, 3, 3)]
        self.assertEqual(diff, expected)

        trajectory = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6), (5, 6, 7)]
        diff = npop.subsample_trajectory_v2(trajectory, stride=3, offset=0)
        expected = [(4, 4, 4)]
        self.assertEqual(diff, expected)



    def test_function_along_axis(self):
        # Shape (2,3,2)
        arr = np.array([
            [[1, 2], [3, 4], [5, 6]],
            [[7, 8], [9, 10], [11, 12]]
        ])

        # Function to apply (sum along each slice)
        def sum_func(x):
            return np.sum(x, axis=0)

        # Using NumPy's apply_along_axis for verification
        numpy_result = np.apply_along_axis(sum_func, axis=1, arr=arr)
        custom_result = npop.function_along_axis(sum_func, axis=1, arr=arr)
        np.array_equal(numpy_result, custom_result)



if __name__ == '__main__':
    unittest.main()