import time
import unittest
import numpy as np

import optimization_questions as opt_q


class OptimizationQTest(unittest.TestCase):

    dump_output = True

    def test_sum_set_of_k(self):

        k = 9
        exp_set = [[2, 3, 4], [4, 5]]
        sum_set = opt_q.sum_set_of_k_v1(k)
        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))

        k = 10
        exp_set = [[1, 2, 3, 4]]
        sum_set = opt_q.sum_set_of_k_v1(k)
        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))

        k = 50
        exp_set = [[8, 9, 10, 11, 12], [11, 12, 13, 14]]
        sum_set = opt_q.sum_set_of_k_v1(k)
        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))

        k = 50
        sum_set = opt_q.sum_set_of_k_v2(k)
        exp_set = [[11, 12, 13, 14], [8, 9, 10, 11, 12]]
        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))

        # Test run-time speed
        k = 100000
        start = time.time()
        sum_set_v1 = opt_q.sum_set_of_k_v1(k)
        v1_runtime = time.time() - start
        if self.dump_output:
            print('sum_set_of_k_v1 Runtime -> ', v1_runtime)

        start = time.time()
        sum_set_v2 = opt_q.sum_set_of_k_v2(k)
        v2_runtime = time.time() - start
        if self.dump_output:
            print('sum_set_of_k_v2 Runtime -> ', v2_runtime)

        self.assertGreater(v1_runtime, v2_runtime)
        # Make sure both methods give the same answer
        np.testing.assert_array_equal(np.asarray(sum_set_v1),
                                      np.asarray(sum_set_v2[::-1]))


if __name__ == '__main__':
    unittest.main()
