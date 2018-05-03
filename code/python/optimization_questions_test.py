import unittest
import numpy as np

import optimization_questions as opt_q


class OptimizationQTest(unittest.TestCase):

    dump_output = True

    def test_sum_set_of_k(self):

        k = 9
        exp_set = [[2, 3, 4], [4, 5]]

        sum_set = opt_q.sum_set_of_k_v1(k)

        print('Sum set ', sum_set)

        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))

        k = 10
        exp_set = [[1,2,3,4]]

        sum_set = opt_q.sum_set_of_k_v1(k)

        print('Sum set ', sum_set)

        np.testing.assert_array_equal(np.asarray(sum_set),
                                      np.asarray(exp_set))



        """
        k = 100
        sum_set = opt_q.sum_set_of_k_v1(k)
        print('Sum set ', sum_set)


        k = 100
        sum_set = opt_q.sum_set_of_k_v2(k)
        print('Sum set ', sum_set)
        """






if __name__ == '__main__':
    unittest.main()
