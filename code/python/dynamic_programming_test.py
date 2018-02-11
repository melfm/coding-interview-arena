import unittest

import dynamic_programming as dp


class DynamicProgrammingQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_get_fib(self):

        n = 9
        res = dp.fibonacci_dp(n)
        self.assertEqual(res, 34)

        if self.dump_output:
            print('Fibonacci loop for value {} ->'.format
                  (n), res)

        fib_array = [0, 1]
        res = dp.fibonacci_dp_recursive(n, fib_array)
        self.assertEqual(res, 34)

        if self.dump_output:
            print('Fibonacci recursive for value {} ->'.format
                  (n), res)

    def test_get_min_steps_mem(self):

        n = 10
        db_res = dp.get_min_steps_mem(n)
        self.assertEqual(db_res, 3)
        if self.dump_output:
            print('Min steps to reduce {} --> '.format(n), db_res)


if __name__ == '__main__':
    unittest.main()
